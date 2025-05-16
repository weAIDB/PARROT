# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: pre_byte
# @Author: Wei Zhou
# @Time: 2025/5/11 14:11

import json
import sqlglot

from tqdm import tqdm


def merge_sql():
    # holo_load = "/data/wei/index/SQLBench/Commercial/sql_translator_benchmark/ddl/holo_create_tables.sql"
    holo_load = "/data/wei/index/SQLBench/Commercial/sql_translator_benchmark/dql/holo_343_value.sql"
    with open(holo_load, "r") as rf:
        holo_data = rf.readlines()
    # holo_data = "".join(holo_data).split(";")

    # ck_load = "/data/wei/index/SQLBench/Commercial/sql_translator_benchmark/ddl/clickhouse_create_tables.sql"
    ck_load = "/data/wei/index/SQLBench/Commercial/sql_translator_benchmark/dql/clickhouse_343_value.sql"
    with open(ck_load, "r") as rf:
        ck_data = rf.readlines()
    # ck_data = "".join(ck_data).split(";")

    data_save = "/data/wei/index/SQLBench/Commercial/sql_translator_benchmark/Byte_DQL_merged.json"

    total_data = list()
    for holo, ck in tqdm(zip(holo_data, ck_data)):
        sqlglot.parse_one(holo, read="postgres")
        sqlglot.parse_one(ck, read="clickhouse")

        # parsed = sqlglot.parse_one(holo, read="postgres")
        # token_count = sum(1 for _ in parsed.walk())

        total_data.append({"hologres": holo,
                           "clickhouse": ck})

    with open(data_save, "w") as wf:
        json.dump(total_data, wf, indent=2)


if __name__ == "__main__":
    merge_sql()
