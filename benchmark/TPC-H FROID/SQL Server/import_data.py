import pymssql
import pandas as pd
import os

# 宏定义
DBGEN_PATH = "path-to-dbgen"
SQL_SERVER_HOST = '127.0.0.1:1433'
SQL_SERVER_USER = 'your username'
SQL_SERVER_PASSWORD = 'your password'


def load_data(path):
    """
    加载文件数据
    :param path: 文件所在路径
    :return: 返回数据
    """
    data = {}
    columns = {"PART": ["P_PARTKEY", "P_NAME", "P_MFGR", "P_BRAND", "P_TYPE", "P_SIZE", "P_CONTAINER", "P_RETAILPRICE",
                        "P_COMMENT"],
               "SUPPLIER": ["S_SUPPKEY", "S_NAME", "S_ADDRESS", "S_NATIONKEY", "S_PHONE", "S_ACCTBAL", "S_COMMENT"],
               "PARTSUPP": ["PS_PARTKEY", "PS_SUPPKEY", "PS_AVAILQTY", "PS_SUPPLYCOST", "PS_COMMENT"],
               "REGION": ["R_REGIONKEY", "R_NAME", "R_COMMENT"],
               "NATION": ["N_NATIONKEY", "N_NAME", "N_REGIONKEY", "N_COMMENT"],
               "CUSTOMER": ["C_CUSTKEY", "C_NAME", "C_ADDRESS", "C_NATIONKEY", "C_PHONE", "C_ACCTBAL", "C_MKTSEGMENT",
                            "C_COMMENT"],
               "ORDERS": ["O_ORDERKEY", "O_CUSTKEY", "O_ORDERSTATUS", "O_TOTALPRICE", "O_ORDERDATE", "O_ORDERPRIORITY",
                          "O_CLERK", "O_SHIPPRIORITY", "O_COMMENT"],
               "LINEITEM": ["L_ORDERKEY", "L_PARTKEY", "L_SUPPKEY", "L_LINENUMBER", "L_QUANTITY", "L_EXTENDEDPRICE",
                            "L_DISCOUNT", "L_TAX"
                   , "L_RETURNFLAG", "L_LINESTATUS", "L_SHIPDATE", "L_COMMITDATE", "L_RECEIPTDATE", "L_SHIPINSTRUCT",
                            "L_SHIPMODE", "L_COMMENT"]}
    for file in os.listdir(path):
        if file.endswith(".tbl"):
            name = file.split('.')[0].upper()
            d = pd.read_csv(path + "\\" + file, sep='|', header=None)
            d.drop(columns=d.shape[1] - 1, inplace=True)
            d.columns = columns[name]
            data.update({name: d})
    return data


def connect_sql_server(host, username, password):
    """
    连接 Sql Server 数据库
    :param host: ip和端口
    :param username: 登录账号
    :param password: 登录密码
    :return: 返回数据库连接
    """
    connect = pymssql.connect(host=host, user=username, password=password, database='TPCH')
    if connect:
        print("connect success.")
        return connect
    else:
        print("connect fail.")
        return None


def insert(data, cursor):
    """
    将数据导入 Sql Server
    :param data: 待导入数据
    :param cursor: Sql Server 游标
    """
    sqls = {}
    # 执行顺序，要先执行被引用的表
    order = ["REGION", "NATION", "CUSTOMER", "ORDERS", "PART", "SUPPLIER", "PARTSUPP", "LINEITEM"]
    with open("sql.txt", 'w') as f:
        for key in data:
            sql = []
            for t in [tuple(i) for i in data[key].values]:
                s = "insert into " + key + str(tuple(data[key].columns)).replace('\'', '') + " values" + str(t) + ";"
                sql.append(s)
                # 将 Sql 语句保存至文件中
                f.write(s + "\n")
            f.write("\n\n")
            sqls.update({key: sql})
    for key in order:
        le = len(sqls[key])
        for s in range(le):
            try:
                cursor.execute(sqls[key][s])
            except:
                pass
            if s % 100 == 0:
                print('\'' + key + '\'' + " 进度:" + str(s / le * 100))
        print(key + " has done.")


if __name__ == "__main__":
    # 使用宏定义的路径
    data = load_data(DBGEN_PATH)
    # 使用宏定义的IP端口，账号，密码
    connect = connect_sql_server(SQL_SERVER_HOST, SQL_SERVER_USER, SQL_SERVER_PASSWORD)
    if connect:
        # 获得 Sql Server 游标
        cursor = connect.cursor()
        # 执行插入
        insert(data, cursor)
        # 提交事务
        connect.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        connect.close()
