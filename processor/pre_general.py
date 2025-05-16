# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: pre_general
# @Author: Wei Zhou
# @Time: 2025/5/11 10:13

import os
import json

import sqlglot
from tqdm import tqdm

from processor.utils import format_sql

dialect_list = [
    "athena",  # Amazon Athena (基于Presto的SQL查询服务)
    "bigquery",  # Google BigQuery (关系型数据仓库)
    "clickhouse",  # ClickHouse (关系型列式数据库)
    "doris",  # Apache Doris (关系型MPP数据库)
    "drill",
    "druid",
    "duckdb",
    "databricks",
    "hive",
    "mysql",  # MySQL (关系型数据库)
    "oracle",  # Oracle Database (关系型数据库)
    "postgres",  # PostgreSQL (关系型数据库)
    "presto",  # Presto (分布式SQL查询引擎，支持关系数据源)
    "redshift",  # Amazon Redshift (关系型数据仓库)
    "risingwave",  # RisingWave (关系型流数据库)
    "snowflake",  # Snowflake (关系型云数据仓库)
    "spark",  # Apache Spark SQL (关系型数据处理)
    "sqlite",  # SQLite (嵌入式关系型数据库)
    "starrocks",  # StarRocks (关系型分析数据库)
    "teradata",  # Teradata (关系型数据仓库)
    "trino",  # Trino (原PrestoSQL，关系型查询引擎)
    "tsql"  # T-SQL (Microsoft SQL Server的SQL方言)
]

data_ids = ["ATIS", "GeoQuery", "Restaurants", "Academic", "IMDb",
            "Yelp", "Scholar", "WikiSQL", "Advising", "Spider",
            "SParC", "CoSQL", "CSpider", "MIMICSQL", "SQUALL",
            "FIBEN", "ViText2SQL", "DuSQL", "PortugueseSpider", "CHASE",
            "Spider-Syn", "Spider-DK", "Spider-Realistic", "KaggleDBQA", "SEDE",
            "MT-TEQL", "PAUQ", "knowSQL", "Dr.Spider", "BIRD",
            "AmbiQT", "ScienceBenchmark", "BULL", "BookSQL", "Archer",
            "Spider 2.0", "BIRD Mini-Dev", "BIRD Critic"]

data_loads = {
    "Scholar": "/data/wei/index/SQLBench/benchmark/Scholar/scholar.json",
    "WikiSQL": [
        "/data/wei/index/SQLBench/benchmark/WikiSQL/train.jsonl",
        "/data/wei/index/SQLBench/benchmark/WikiSQL/dev.jsonl",
        "/data/wei/index/SQLBench/benchmark/WikiSQL/test.jsonl"
    ],
    "Advising": ["/data/wei/index/SQLBench/benchmark/Advising/advising.json"],

}


def load_sql(data_id):
    sql_list = list()

    # 1. ATIS
    if data_id == "ATIS":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/ATIS/atis.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 2. GeoQuery
    if data_id == "GeoQuery":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/GeoQuery/geography.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 3. Restaurants
    if data_id == "Restaurants":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/Restaurants/restaurants.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 4. Academic
    if data_id == "Academic":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/Academic/academic.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 5. IMDb
    if data_id == "IMDb":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/IMDb/imdb.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 6. Yelp
    if data_id == "Yelp":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/Yelp/yelp.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 7. Scholar
    if data_id == "Scholar":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/Scholar/scholar.json"
        data_save = data_load.replace(".json", "_merged.json")

        with open(data_load, "r") as rf:
            sql_data = json.load(rf)

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 8. WikiSQL

    # 9. Advising
    if data_id == "Advising":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/Advising/advising.json"
        data_save = data_load.replace(".json", "_merged.json")

        sql_data = list()
        with open(data_load, "r") as rf:
            sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 10. Spider
    if data_id == "Spider":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/Spider/train_gold.sql",
            "/data/wei/index/SQLBench/benchmark/Spider/dev_gold.sql",
            "/data/wei/index/SQLBench/benchmark/Spider/test_gold.sql"
        ]
        data_save = data_loads[0].replace(".sql", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(rf.readlines())

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item.split("\t")[0])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 11. SParC
    if data_id == "SParC":
        src_dialect = "sqlite"
        data_loads = ["/data/wei/index/SQLBench/benchmark/SParC/train.json",
                      "/data/wei/index/SQLBench/benchmark/SParC/dev.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["final"]["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 12. CoSQL
    if data_id == "CoSQL":
        src_dialect = "sqlite"
        data_loads = ["/data/wei/index/SQLBench/benchmark/SParC/cosql_train.json",
                      "/data/wei/index/SQLBench/benchmark/SParC/cosql_dev.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["final"]["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 13. CSpider
    if data_id == "CSpider":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/CSpider/train.json",
            "/data/wei/index/SQLBench/benchmark/CSpider/dev.json",
            "/data/wei/index/SQLBench/benchmark/CSpider/test.json"
        ]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 14. MIMICSQL
    if data_id == "MIMICSQL":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/MINICSQL/train.json",
            "/data/wei/index/SQLBench/benchmark/MINICSQL/dev.json",
            "/data/wei/index/SQLBench/benchmark/MINICSQL/test.json"
        ]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            item = json.loads(item)
            sql_list_temp.extend(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 15. SQUALL
    if data_id == "SQUALL":
        src_dialect = "sqlite"
        data_load = "/data/wei/index/SQLBench/benchmark/SQUALL/squall.json"
        data_save = data_load.replace(".json", "_merged.json")

        sql_data = list()
        with open(data_load, "r") as rf:
            sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            item = json.loads(item)
            sql_list_temp.append(" ".join([token[1] for token in item["sql"]]))

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 16. FIBEN
    if data_id == "FIBEN":
        src_dialect = "postgres"
        data_load = "/data/wei/index/SQLBench/benchmark/FIBEN/FIBEN_Queries.json"
        data_save = data_load.replace(".json", "_merged.json")

        sql_data = list()
        with open(data_load, "r") as rf:
            sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["SQL"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 17. ViText2SQL

    # 18. DuSQL

    # 19. PortugueseSpider

    # 20. CHASE
    if data_id == "CHASE":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/CHASE/chase_train.json",
            "/data/wei/index/SQLBench/benchmark/CHASE/chase_dev.json"
        ]
        data_save = data_load.replace(".json", "_merged.json")

        sql_data = list()
        with open(data_load, "r") as rf:
            sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["final"]["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 21. Spider-Syn
    if data_id == "Spider-Syn":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/Spider-Syn/train_spider.json",
            "/data/wei/index/SQLBench/benchmark/Spider-Syn/dev.json"
        ]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 22. Spider-DK
    if data_id == "Spider-DK":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/Spider-DK/Spider-DK.json"
        ]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 23. Spider-Realistic
    if data_id == "Spider-Realistic":
        src_dialect = "sqlite"
        data_loads = [
            "/data/wei/index/SQLBench/benchmark/Spider-Realistic/spider-realistic.json"
        ]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 24. KaggleDBQA
    if data_id == "KaggleDBQA":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/KaggleDBQA/examples"
        data_loads = [os.path.join(file_dir, file) for file in os.listdir(file_dir)]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 25. SEDE
    if data_id == "SEDE":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/SEDE"
        data_loads = [os.path.join(file_dir, file) for file in os.listdir(file_dir)]
        data_save = data_loads[0].replace(".jsonl", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend([json.loads(line) for line in rf.readlines()])

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["QueryBody"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 26. MT-TEQL

    # 27. PAUQ
    if data_id == "PAUQ":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/PAUQ"
        data_loads = [os.path.join(file_dir, file) for file in os.listdir(file_dir)]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"]["en"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 28. knowSQL
    if data_id == "knowSQL":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/knowSQL"
        data_loads = [os.path.join(file_dir, file) for file in os.listdir(file_dir)]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["answer"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 29. Dr.Spider
    if data_id == "Dr.Spider":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/Dr.Spider"
        data_loads = ([os.path.join(file_dir, file, "gold_pre_perturbation.sql") for file in os.listdir(file_dir)] +
                      [os.path.join(file_dir, file, "gold_post_perturbation.sql") for file in os.listdir(file_dir)])
        data_save = data_loads[0].replace(".sql", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(rf.readlines())

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 30. BIRD
    if data_id == "BIRD":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/BIRD"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BIRD/train_gold.sql",
                      "/data/wei/index/SQLBench/benchmark/BIRD/dev.sql"]
        data_save = data_loads[0].replace(".sql", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(rf.readlines())

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item.split("\t")[0])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 31. AmbiQT
    if data_id == "AmbiQT":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/AmbiQT"
        data_loads = ([os.path.join(file_dir, file, "train.json") for file in os.listdir(file_dir)] +
                      [os.path.join(file_dir, file, "validation.json") for file in os.listdir(file_dir)])
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["orig_query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 32. ScienceBenchmark
    if data_id == "ScienceBenchmark":
        src_dialect = "sqlite"
        file_dir = "/data/wei/index/SQLBench/benchmark/ScienceBenchmark"
        data_loads = ([os.path.join(file_dir, file, "synth.json") for file in os.listdir(file_dir)] +
                      [os.path.join(file_dir, file, "seed.json") for file in os.listdir(file_dir)] +
                      [os.path.join(file_dir, file, "dev.json") for file in os.listdir(file_dir)])
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["orig_query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 33. BULL
    if data_id == "BULL":
        src_dialect = "sqlite"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BULL/BULL-en/train.json",
                      "/data/wei/index/SQLBench/benchmark/BULL/BULL-en/dev_en.json",
                      "/data/wei/index/SQLBench/benchmark/BULL/BULL-en/dev.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["sql_query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 34. BookSQL
    if data_id == "BookSQL":
        src_dialect = "sqlite"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BookSQL/train.json",
                      "/data/wei/index/SQLBench/benchmark/BookSQL/val.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["SQL"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 35. Archer
    if data_id == "Archer":
        src_dialect = "sqlite"
        data_loads = ["/data/wei/index/SQLBench/benchmark/Archer/en_data/train.json",
                      "/data/wei/index/SQLBench/benchmark/Archer/en_data/dev.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.append(item["query"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    # 36. Spider 2.0

    # 37. BIRD Mini-Dev

    # 38. BIRD Critic
    if data_id == "BIRD Critic (PostgreSQL)":
        src_dialect = "postgres"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BIRD Critic/BIRD-Critic_postgresql.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sol_sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    if data_id == "BIRD Critic (MySQL)":
        src_dialect = "mysql"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BIRD Critic/BIRD-Critic_mysql.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sol_sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    if data_id == "BIRD Critic (SQLServer)":
        src_dialect = "tsql"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BIRD Critic/BIRD-Critic_sqlserver.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sol_sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    if data_id == "BIRD Critic (Oracle)":
        src_dialect = "oracle"
        data_loads = ["/data/wei/index/SQLBench/benchmark/BIRD Critic/BIRD-Critic_oracle.json"]
        data_save = data_loads[0].replace(".json", "_merged.json")

        sql_data = list()
        for data_load in data_loads:
            with open(data_load, "r") as rf:
                sql_data.extend(json.load(rf))

        sql_list_temp = list()
        for no, item in tqdm(enumerate(sql_data)):
            sql_list_temp.extend(item["sol_sql"])

        for no, sql in tqdm(enumerate(sql_list_temp)):
            try:
                sql = format_sql(sql)
                parsed_tree = sqlglot.parse_one(sql, read=src_dialect)
                sql_list.append(sql)
            except Exception as e:
                print(data_id, sql)
                print(e)

        print(data_id)

    return sql_list, src_dialect, data_save


def translate_sql(sql_list, src_dialect):
    total_list = list()
    for sql in tqdm(sql_list):
        sql = sql.split("\t")[0]
        res_dict = {src_dialect: sql}
        try:
            for tgt_dialect in dialect_list:
                if src_dialect == tgt_dialect:
                    continue

                translated_sql = sqlglot.transpile(sql, read=src_dialect,
                                                   write=tgt_dialect)[0]
                res_dict[tgt_dialect] = translated_sql

                # 4. filter
                parsed_tree = sqlglot.parse_one(translated_sql, read=tgt_dialect)

            total_list.append(res_dict)
        except Exception as e:
            print(tgt_dialect)
            print(str(e))

    return total_list


def merge_sql():
    data_id = data_ids[8]

    # 1. load
    sql_list, src_dialect, data_save = load_sql(data_id)

    # 2. deduplicate
    sql_list = set(sql_list)

    # 3. translate
    total_list = translate_sql(sql_list, src_dialect)

    with open(data_save, "w") as wf:
        json.dump(total_list, wf, indent=2)


if __name__ == "__main__":
    merge_sql()
