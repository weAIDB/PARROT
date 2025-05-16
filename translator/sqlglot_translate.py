# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: sqlglot_translate
# @Author: Wei Zhou
# @Time: 2025/5/10 9:52

import json
import sqlglot

dialect_list = []


def translate(dialect):
    data_load = ""
    with open(data_load, "r") as rf:
        sql_list = json.load(rf)

    total_list = list()
    for sql in sql_list:
        res_dict = {dialect: sql}
        for target in dialect_list:
            translated_sql = sqlglot.transpile(sql, read=dialect, write=target)[0]
            res_dict[target] = translated_sql
        total_list.append(translated_sql)

    data_save = ""
    with open(data_save, "w") as wf:
        json.dump(total_list, wf, indent=2)


if __name__ == "__main__":
    dialect = ""
    translate(dialect)
