import traceback
import tqdm
import json
import coverage
from .clickhouse_parser.ClickHouseLexer import ClickHouseLexer
from .clickhouse_parser.ClickHouseParser import ClickHouseParser
from .pg_parser.PostgreSQLLexer import PostgreSQLLexer
from .pg_parser.PostgreSQLParser import PostgreSQLParser
from .pg_parser.PostgreSQLParserListener import PostgreSQLParserListener
from antlr4 import *

def parse_clickhouse_sql(sql):
    input_stream = InputStream(sql)
    lexer = ClickHouseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ClickHouseParser(stream)
    tree = parser.queryStmt()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise Exception("SQL syntax error")
    return tree

def parse_postgresql_sql(sql):
    input_stream = InputStream(sql)
    lexer = PostgreSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PostgreSQLParser(stream)
    tree = parser.stmtblock()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise Exception("SQL syntax error")
    return tree

if __name__ == "__main__":
    sqls = []
    with open(r"", "r", encoding="utf-8") as file:
        sqls = json.load(file)
    sqls = [sql["hologres"] for sql in sqls]
    cov = coverage.Coverage(branch=True, cover_pylib=True)
    cov.start()
    for sql in tqdm.tqdm(sqls, desc="Parsing SQLs"):
        try:
            parse_postgresql_sql(sql)
        except Exception as e:
            print(sql)
            input("Press Enter to continue...")
    cov.stop()
    cov.save()
    cov.html_report(directory="cov_html")