# -*- coding: utf-8 -*-
# @Project: index_test
# @Module: utils
# @Author: Wei Zhou
# @Time: 2025/5/11 18:49

import re

import sqlglot
from sqlglot import exp


def format_sql(sql):
    # remove starting comment, redundant signs
    sql = sql.split("*/", maxsplit=1)[-1]
    sql = sql.replace("--comment line", " ").replace("\n", " ").replace("\t", " ")
    sql = sql.strip(" ").strip(";").strip(" ")
    sql = re.sub(r"\s+", " ", sql.strip())

    return sql


def norm_sql(sql, dialect):
    parsed = sqlglot.parse_one(sql, read=dialect)
    for node in parsed.find_all(exp.Identifier):
        node.args["this"] = "identifier"

    # for node in parsed.find_all(exp.Table):
    #     node.args["this"] = "table"
    #
    # for node in parsed.find_all(exp.Column):
    #     node.args["this"] = "column"

    for node in parsed.find_all(exp.Literal):
        node.args["this"] = "'value'"

    sql = parsed.sql()
    sql = re.sub(r"(identifier,\s*)+identifier", "identifier", sql)
    sql = sql.replace("identifier.identifier", "identifier")

    return sql
