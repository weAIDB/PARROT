import logging
import sys

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from validator.pg_parser.PostgreSQLParser import PostgreSQLParser
from validator.pg_parser.PostgreSQLLexer import PostgreSQLLexer

from validator.mysql_parser.MySqlParser import MySqlParser
from validator.mysql_parser.MySqlLexer import MySqlLexer

from validator.oracle_parser.PlSqlParser import PlSqlParser
from validator.oracle_parser.PlSqlLexer import PlSqlLexer


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SelfParseError(line, column, msg)


def parse_tree(src_sql: str, dialect: str) -> (str, int, int, str):
    if dialect == 'pg':
        return parse_pg_tree(src_sql)
    elif dialect == 'mysql':
        return parse_mysql_tree(src_sql)
    elif dialect == 'oracle':
        return parse_oracle_tree(src_sql)


def parse_pg_tree(src_sql: str) -> (str, int, int, str):
    try:
        input_stream = InputStream(src_sql)
        lexer = PostgreSQLLexer(input_stream)
        lexer.addErrorListener(CustomErrorListener())
        stream = CommonTokenStream(lexer)
        parser = PostgreSQLParser(stream)
        parser.addErrorListener(CustomErrorListener())
        tree = parser.root()
        return tree, None, None, None
    except SelfParseError as e:
        return None, e.line, e.column, e.msg
    except Exception as e:
        logging.error(f"An error occurred: {e}", file=sys.stderr)
        raise e


def parse_mysql_tree(src_sql: str):
    try:
        input_stream = InputStream(src_sql)
        lexer = MySqlLexer(input_stream)
        lexer.addErrorListener(CustomErrorListener())
        stream = CommonTokenStream(lexer)
        parser = MySqlParser(stream)
        parser.addErrorListener(CustomErrorListener())
        tree = parser.root()
        return tree, None, None, None
    except SelfParseError as e:
        return None, e.line, e.column, e.msg
    except Exception as e:
        logging.error(f"An error occurred: {e}", file=sys.stderr)
        raise e


def parse_oracle_tree(src_sql: str):
    try:
        input_stream = InputStream(src_sql)
        lexer = PlSqlLexer(input_stream)
        lexer.addErrorListener(CustomErrorListener())
        stream = CommonTokenStream(lexer)
        parser = PlSqlParser(stream)
        parser.addErrorListener(CustomErrorListener())
        tree = parser.sql_script()
        return tree, None, None, None
    except SelfParseError as e:
        return None, e.line, e.column, e.msg
    except Exception as e:
        logging.error(f"An error occurred: {e}", file=sys.stderr)
        return None, -1, -1, ''


def get_parser(dialect: str):
    input_stream = InputStream('')
    if dialect == 'pg':
        lexer = PostgreSQLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        return PostgreSQLParser(stream)
    elif dialect == 'mysql':
        lexer = MySqlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        return MySqlParser(stream)
    elif dialect == 'oracle':
        lexer = PlSqlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        return PlSqlParser(stream)


class SelfParseError(Exception):
    def __init__(self, line, column, msg):
        super().__init__(f"Syntax error at line {line} , column {column} : {msg}")
        self.line = line
        self.column = column
        self.msg = msg


if __name__ == "__main__":
    src_sql = "SELECT * FROM table;"
    tree, _, _, _ = parse_oracle_tree(src_sql)

    print(tree)
