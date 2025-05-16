# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: db_conn
# @Author: Wei Zhou
# @Time: 2024/7/19 23:32
import re
import time
import logging
import paramiko
import traceback

import pyodbc
import pymysql
import psycopg2 as pg

import sqlite3
import cx_Oracle

from func_timeout import func_set_timeout


# https://docs.oracle.com/en/database/oracle/oracle-database/23/lacli/install-instant-client-using-zip.html#GUID-D3DCB4FB-D3CA-4C25-BE48-3A1FB5A22E84


@func_set_timeout(60)
def read_output(shell, prompt, timeout=3 * 60):
    start_time = time.time()

    output = str()
    while True:
        # if shell.recv_ready():
        output += shell.recv(1024).decode('utf-8')

        # Check for the shell prompt to know when the command has finished
        if re.search(prompt, output):
            break

        # Check for timeout
        if time.time() - start_time > timeout:
            break

        time.sleep(0.1)  # Small delay to avoid busy waiting

    return output


class DatabaseConnector:
    def __init__(self, db_system, config, autocommit=False, by_shell=False):
        self.db_system = db_system

        self.config = config
        self.autocommit = autocommit

        self._connection = None
        self.shell = None

        if not by_shell:
            self.create_connection()
        else:
            self.create_shell()

        # This does not reflect the number of unique simulated indexes
        # but the number of simulate_index calls
        self.simulated_indexes = 0
        self.cost_estimations = 0
        self.cost_estimation_duration = 0
        self.index_simulation_duration = 0

    def create_connection(self):
        if self._connection:
            self.close()

        if self.db_system == "postgresql" or self.db_system == "openGauss":
            # self._connection = pg.connect(database=self.config["database"],
            #                               user=self.config["user"],
            #                               password=self.config["password"],
            #                               host=self.config["host"],
            #                               port=self.config["port"])
            self._connection = pg.connect(database=self.config["database"],
                                          user=self.config["user"],
                                          # password=self.config["password"],
                                          host=self.config["host"],
                                          port=self.config["port"])

        elif self.db_system == "mysql":
            self._connection = pymysql.connect(host=self.config["host"],
                                               user=self.config["user"],
                                               password=self.config["password"],
                                               database=self.config["database"],
                                               port=int(self.config["port"]))

        elif self.db_system == "mssql":
            self._connection = pyodbc.connect(r'Driver=' + self.config["driver"] +
                                              ';Server=' + self.config["host"] +
                                              ';Database=' + self.config["database"] +
                                              ';UID=' + self.config["user"] +
                                              ';PWD=' + self.config["password"] + ';')
            # self._connection = pyodbc.connect(r'Driver=' + self.config["driver"] +
            #                                   ';Server=' + self.config["host"] +
            #                                   ';Database=' + self.config["database"] +
            #                                   ';Trusted_Connection=yes;')

        elif self.db_system == "sqlite":
            self._connection = sqlite3.connect(self.config["database"])

        elif self.db_system == "oracle":
            dsn = cx_Oracle.makedsn(self.config["host"], self.config["port"],
                                    service_name=self.config["service_name"])
            # self._connection = cx_Oracle.connect(self.config["user"], self.config["password"],
            #                                      dsn, mode=cx_Oracle.SYSDBA)
            self._connection = cx_Oracle.connect(self.config["user"], self.config["password"], dsn)

        if self.db_system != "sqlite":
            self._connection.autocommit = self.autocommit

        self._cursor = self._connection.cursor()
        # logging.debug("Database connector created: {} on {}".format(self.db_system,
        #                                                             self.config["database"]))

    def create_shell(self):
        if self.db_system == "oracle":
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.config["host"], username='zhouwei', password='7G6dKXva')

            self.shell = ssh.invoke_shell()
            self.shell.send(f'sqlplus {self.config["user"]}/{self.config["password"]}'
                            f'@//{self.config["host"]}:{self.config["port"]}/'
                            f'{self.config["service_name"]}\n')

            time.sleep(3)
            read_output(self.shell, prompt="SQL>")

    @func_set_timeout(60)
    def exec_only(self, statement):
        self._cursor.execute(statement)

    @func_set_timeout(60)
    def exec_fetch(self, statement, one=True):
        self._cursor.execute(statement)
        # try:
        #     self._cursor.execute(statement)
        # except:
        #     print(statement)
        #     raise AssertionError
        if one:
            return self._cursor.fetchone()
        return self._cursor.fetchall()

    @func_set_timeout(30)
    def shell_exec(self, statement):
        self.shell.send(f"{statement.strip(';')};\n")

        output = read_output(self.shell, "SQL>")
        output = output.replace(f"{statement.strip(';')};\r\n", "").replace("\r\n\r\n\r\nSQL>", "")
        return output

    def enable_simulation(self):
        raise NotImplementedError

    def commit(self):
        self._connection.commit()

    def close(self):
        self._connection.close()
        logging.debug("Database connector closed: {}".format(self.config["database"]))

    def ssh_close(self):
        self.ssh.close()

    def rollback(self):
        self._connection.rollback()

    def drop_index(self, index):
        statement = f"drop index {index.index_idx()}"
        self.exec_only(statement)

    def _prepare_query(self, query):
        if hasattr(query, "text"):
            query = query.text

        if "create view" in query:
            for query_statement in query.split(";"):
                if "create view" in query_statement:
                    try:
                        self.exec_only(query_statement)
                    except Exception as e:
                        logging.error(e)
                        logging.error(traceback.format_exc())
                elif "select" in query_statement or "SELECT" in query_statement:
                    return query_statement
                    # queries.append(query_statement)
        else:
            return query

    def _cleanup_query(self, query):
        """
        Drop view created in the query
        :param query:
        :return:
        """
        if hasattr(query, "text"):
            query = query.text

        for query_statement in query.split(";"):
            if "drop view" in query_statement:
                self.exec_only(query_statement)
                self.commit()

    def simulate_index(self, index):
        self.simulated_indexes += 1

        start_time = time.time()
        result = self._simulate_index(index)
        end_time = time.time()
        self.index_simulation_duration += end_time - start_time

        return result

    def drop_simulated_index(self, identifier):
        start_time = time.time()
        self._drop_simulated_index(identifier)
        end_time = time.time()
        self.index_simulation_duration += end_time - start_time

    def get_cost(self, query):
        self.cost_estimations += 1

        start_time = time.time()
        cost = self._get_cost(query)
        end_time = time.time()
        self.cost_estimation_duration += end_time - start_time

        return cost

    # This is very similar to get_cost() above. Some algorithms need to directly access
    # get_plan. To not exclude it from costing, we add the instrumentation here.
    def get_plan(self, query):
        self.cost_estimations += 1

        start_time = time.time()
        plan = self._get_plan(query)
        end_time = time.time()
        self.cost_estimation_duration += end_time - start_time

        return plan

    def table_exists(self, table_name):
        raise NotImplementedError

    def database_exists(self, database_name):
        raise NotImplementedError

    def drop_database(self, database_name):
        raise NotImplementedError

    def create_statistics(self):
        raise NotImplementedError

    def set_random_seed(self, value):
        raise NotImplementedError

    def _get_cost(self, query):
        query_plan = self._get_plan(query)
        total_cost = query_plan["Total Cost"]

        return total_cost

    def _get_plan(self, query):
        # create view and return the next sql.
        query_text = self._prepare_query(query)
        statement = f"explain {query_text}"
        # query_plan = self.exec_fetch(statement)[0][0]["Plan"]
        query_plan = self.exec_fetch(statement)

        # drop view
        self._cleanup_query(query)

        return query_plan

    def _simulate_index(self, index):
        raise NotImplementedError

    def _drop_simulated_index(self, identifier):
        raise NotImplementedError
