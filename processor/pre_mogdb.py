# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: pre_mogdb
# @Author: Wei Zhou
# @Time: 2025/5/11 14:46

import re
import json
import pandas as pd

from tqdm import tqdm
from itertools import combinations
from collections import defaultdict

import sqlglot
from sqlglot import exp

import sys
sys.path.append("/data/wei/index/SQLBench")

from processor.utils import norm_sql


def merge_sql():
    data_load = "/data/wei/index/SQLBench/Commercial/sql_normalized.csv"
    sql_data = pd.read_csv(data_load)

    data_save = "/data/wei/index/SQLBench/Commercial/MogDB_merged.json"

    error = 0
    total_data = list()
    to_drop = list()
    for no, item in tqdm(sql_data.iterrows()):
        try:
            if bool(re.search(r"[\u4e00-\u9fff]", item["source_sql"])) or \
                    bool(re.search(r"[\u4e00-\u9fff]", item["target_sql"])):
                continue

            item["source_sql"] = item["source_sql"].split("*/", maxsplit=1)[-1]
            item["source_sql"] = item["source_sql"].replace("--comment line", " ").replace("\n", " ").replace("\t", " ")
            item["source_sql"] = re.sub(r"\s+", " ", item["source_sql"].strip())

            item["target_sql"] = item["target_sql"].split("*/", maxsplit=1)[-1]
            item["target_sql"] = item["target_sql"].replace("--comment line", " ").replace("\n", " ").replace("\t", " ")
            item["target_sql"] = re.sub(r"\s+", " ", item["target_sql"].strip())

            oracle_sql, mogdb_sql = item["source_sql"], item["target_sql"]
            for sign in [" ", "'", '"', '`', "\n"]:
                oracle_sql = oracle_sql.strip(sign)
                oracle_sql = oracle_sql.replace(sign, "")

                mogdb_sql = mogdb_sql.strip(sign)
                mogdb_sql = mogdb_sql.replace(sign, "")

            if oracle_sql.lower() == mogdb_sql.lower():
                to_drop.append(no)
                continue

            sqlglot.parse_one(item["source_sql"], read="oracle")

            # parsed = sqlglot.parse_one(holo, read="postgres")
            # token_count = sum(1 for _ in parsed.walk())

            total_data.append({"oracle": item["source_sql"],
                               "mogdb": item["target_sql"]})
        except Exception as e:
            to_drop.append(no)
            error += 1
            print(e)

    print(error)

    with open(data_save, "w") as wf:
        json.dump(total_data, wf, indent=2)

    sql_data_filtered = sql_data.drop(to_drop)

    sql_data_filtered.to_csv(data_load.replace(".csv", "_filtered.csv"), index=False)


def pre_sql():
    data_load = "/data/wei/index/SQLBench/Commercial/MogDB_merged.json"
    with open(data_load, "r") as rf:
        sql_data = json.load(rf)

    dialect = "oracle"
    prefix_length = 50
    groups = defaultdict(list)

    for sql in sql_data:
        prefix = norm_sql(sql[dialect], dialect)[:prefix_length]
        groups[prefix].append(sql)

    data_save = data_load.replace(".json", f"_grouped_{prefix_length}.json")
    with open(data_save, "w") as wf:
        json.dump(groups, wf, indent=2)


if __name__ == "__main__":
    # merge_sql()
    pre_sql()
