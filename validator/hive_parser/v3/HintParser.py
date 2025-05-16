# Generated from sql/hive/v3/HintParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,375,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,1,2,1,2,1,
        2,3,2,29,8,2,1,3,1,3,1,4,1,4,1,4,5,4,36,8,4,10,4,12,4,39,9,4,1,5,
        1,5,1,5,0,0,6,0,2,4,6,8,10,0,2,2,0,167,168,213,213,2,0,4,4,367,368,
        39,0,12,1,0,0,0,2,15,1,0,0,0,4,23,1,0,0,0,6,30,1,0,0,0,8,32,1,0,
        0,0,10,40,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,20,
        3,4,2,0,16,17,5,334,0,0,17,19,3,4,2,0,18,16,1,0,0,0,19,22,1,0,0,
        0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,20,1,0,0,0,23,28,3,
        6,3,0,24,25,5,336,0,0,25,26,3,8,4,0,26,27,5,337,0,0,27,29,1,0,0,
        0,28,24,1,0,0,0,28,29,1,0,0,0,29,5,1,0,0,0,30,31,7,0,0,0,31,7,1,
        0,0,0,32,37,3,10,5,0,33,34,5,334,0,0,34,36,3,10,5,0,35,33,1,0,0,
        0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,9,1,0,0,0,39,37,1,
        0,0,0,40,41,7,1,0,0,41,11,1,0,0,0,3,20,28,37
    ]

class HintParser ( Parser ):

    grammarFileName = "HintParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TRUE'", "'FALSE'", "'ALL'", "'NONE'", 
                     "'AND'", "'OR'", "<INVALID>", "'LIKE'", "'ANY'", "'IF'", 
                     "'EXISTS'", "'ASC'", "'DESC'", "'NULLS'", "'LAST'", 
                     "'ORDER'", "'GROUP'", "'BY'", "'HAVING'", "'WHERE'", 
                     "'FROM'", "'AS'", "'SELECT'", "'DISTINCT'", "'INSERT'", 
                     "'OVERWRITE'", "'OUTER'", "'UNIQUEJOIN'", "'PRESERVE'", 
                     "'JOIN'", "'LEFT'", "'RIGHT'", "'FULL'", "'ON'", "'PARTITION'", 
                     "'PARTITIONS'", "'TABLE'", "'TABLES'", "'COLUMNS'", 
                     "'INDEX'", "'INDEXES'", "'REBUILD'", "'FUNCTIONS'", 
                     "'SHOW'", "'MSCK'", "'REPAIR'", "'DIRECTORY'", "'LOCAL'", 
                     "'TRANSFORM'", "'USING'", "'CLUSTER'", "'DISTRIBUTE'", 
                     "'SORT'", "'UNION'", "'EXCEPT'", "'LOAD'", "'EXPORT'", 
                     "'IMPORT'", "'REPLICATION'", "'METADATA'", "'DATA'", 
                     "'INPATH'", "'IS'", "'NULL'", "'CREATE'", "'EXTERNAL'", 
                     "'ALTER'", "'CHANGE'", "'COLUMN'", "'FIRST'", "'AFTER'", 
                     "'DESCRIBE'", "'DROP'", "'RENAME'", "'TO'", "'COMMENT'", 
                     "'BOOLEAN'", "'TINYINT'", "'SMALLINT'", "<INVALID>", 
                     "'BIGINT'", "'FLOAT'", "'DOUBLE'", "'PRECISION'", "'DATE'", 
                     "'DATETIME'", "'TIMESTAMP'", "'TIMESTAMPLOCALTZ'", 
                     "'TIME'", "'ZONE'", "'INTERVAL'", "<INVALID>", "'STRING'", 
                     "'CHAR'", "'VARCHAR'", "'ARRAY'", "'STRUCT'", "'MAP'", 
                     "'UNIONTYPE'", "'REDUCE'", "'PARTITIONED'", "'CLUSTERED'", 
                     "'SORTED'", "'INTO'", "'BUCKETS'", "'ROW'", "'ROWS'", 
                     "'FORMAT'", "'DELIMITED'", "'FIELDS'", "'TERMINATED'", 
                     "'ESCAPED'", "'COLLECTION'", "'ITEMS'", "'KEYS'", "'$KEY$'", 
                     "'KILL'", "'LINES'", "'STORED'", "'FILEFORMAT'", "'INPUTFORMAT'", 
                     "'OUTPUTFORMAT'", "'INPUTDRIVER'", "'OUTPUTDRIVER'", 
                     "'ENABLE'", "'DISABLE'", "'LOCATION'", "'TABLESAMPLE'", 
                     "'BUCKET'", "'OUT'", "'OF'", "'PERCENT'", "'CAST'", 
                     "'ADD'", "'REPLACE'", "'RLIKE'", "'REGEXP'", "'TEMPORARY'", 
                     "'FUNCTION'", "'MACRO'", "'FILE'", "'JAR'", "'EXPLAIN'", 
                     "'EXTENDED'", "'FORMATTED'", "'DEPENDENCY'", "'LOGICAL'", 
                     "'SERDE'", "'WITH'", "'DEFERRED'", "'SERDEPROPERTIES'", 
                     "'DBPROPERTIES'", "'LIMIT'", "'OFFSET'", "'SET'", "'UNSET'", 
                     "'TBLPROPERTIES'", "'IDXPROPERTIES'", "'$VALUE$'", 
                     "'$ELEM$'", "'DEFINED'", "'CASE'", "'WHEN'", "'THEN'", 
                     "'ELSE'", "'END'", "'MAPJOIN'", "'STREAMTABLE'", "'CLUSTERSTATUS'", 
                     "'UTC'", "'UTC_TMESTAMP'", "'LONG'", "'DELETE'", "'PLUS'", 
                     "'MINUS'", "'FETCH'", "'INTERSECT'", "'VIEW'", "'VIEWS'", 
                     "'IN'", "'DATABASE'", "'DATABASES'", "'MATERIALIZED'", 
                     "'SCHEMA'", "'SCHEMAS'", "'GRANT'", "'REVOKE'", "'SSL'", 
                     "'UNDO'", "'LOCK'", "'LOCKS'", "'UNLOCK'", "'SHARED'", 
                     "'EXCLUSIVE'", "'PROCEDURE'", "'UNSIGNED'", "'WHILE'", 
                     "'READ'", "'READS'", "'PURGE'", "'RANGE'", "'ANALYZE'", 
                     "'BEFORE'", "'BETWEEN'", "'BOTH'", "'BINARY'", "'CROSS'", 
                     "'CONTINUE'", "'CURSOR'", "'TRIGGER'", "'RECORDREADER'", 
                     "'RECORDWRITER'", "'SEMI'", "'LATERAL'", "'TOUCH'", 
                     "'ARCHIVE'", "'UNARCHIVE'", "'COMPUTE'", "'STATISTICS'", 
                     "'USE'", "'OPTION'", "'CONCATENATE'", "'SHOW_DATABASE'", 
                     "'UPDATE'", "'RESTRICT'", "'CASCADE'", "'SKEWED'", 
                     "'ROLLUP'", "'CUBE'", "'DIRECTORIES'", "'FOR'", "'WINDOW'", 
                     "'UNBOUNDED'", "'PRECEDING'", "'FOLLOWING'", "'CURRENT'", 
                     "'CURRENT_DATE'", "'CURRENT_TIMESTAMP'", "'LESS'", 
                     "'MORE'", "'OVER'", "'GROUPING'", "'SETS'", "'TRUNCATE'", 
                     "'NOSCAN'", "'USER'", "'ROLE'", "'ROLES'", "'INNER'", 
                     "'EXCHANGE'", "'URI'", "'SERVER'", "'ADMIN'", "'OWNER'", 
                     "'PRINCIPALS'", "'COMPACT'", "'COMPACTIONS'", "'TRANSACTIONS'", 
                     "'REWRITE'", "'AUTHORIZATION'", "'REOPTIMIZATION'", 
                     "'CONF'", "'VALUES'", "'RELOAD'", "<INVALID>", "'QUERY'", 
                     "'QUARTER'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'DAYOFWEEK'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'START'", "'TRANSACTION'", "'COMMIT'", "'ROLLBACK'", 
                     "'WORK'", "'ONLY'", "'WRITE'", "'ISOLATION'", "'LEVEL'", 
                     "'SNAPSHOT'", "'AUTOCOMMIT'", "'CACHE'", "'PRIMARY'", 
                     "'FOREIGN'", "'REFERENCES'", "'CONSTRAINT'", "'ENFORCED'", 
                     "'VALIDATE'", "'NOVALIDATE'", "'RELY'", "'NORELY'", 
                     "'UNIQUE'", "'KEY'", "'ABORT'", "'EXTRACT'", "'FLOOR'", 
                     "'MERGE'", "'MATCHED'", "'REPL'", "'DUMP'", "'STATUS'", 
                     "'VECTORIZATION'", "'SUMMARY'", "'OPERATOR'", "'EXPRESSION'", 
                     "'DETAIL'", "'WAIT'", "'RESOURCE'", "'PLAN'", "'QUERY_PARALLELISM'", 
                     "'PLANS'", "'ACTIVATE'", "'DEFAULT'", "'CHECK'", "'POOL'", 
                     "'MOVE'", "'DO'", "'ALLOC_FRACTION'", "'SCHEDULING_POLICY'", 
                     "'PATH'", "'MAPPING'", "'WORKLOAD'", "'MANAGEMENT'", 
                     "'ACTIVE'", "'UNMANAGED'", "'APPLICATION'", "'SYNC'", 
                     "'.'", "':'", "','", "';'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "<INVALID>", "'<=>'", "<INVALID>", "'<='", 
                     "'<'", "'>='", "'>'", "'/'", "'+'", "'-'", "'*'", "'%'", 
                     "'DIV'", "'&'", "'~'", "'|'", "'||'", "'^'", "'?'", 
                     "'$'" ]

    symbolicNames = [ "<INVALID>", "KW_TRUE", "KW_FALSE", "KW_ALL", "KW_NONE", 
                      "KW_AND", "KW_OR", "KW_NOT", "KW_LIKE", "KW_ANY", 
                      "KW_IF", "KW_EXISTS", "KW_ASC", "KW_DESC", "KW_NULLS", 
                      "KW_LAST", "KW_ORDER", "KW_GROUP", "KW_BY", "KW_HAVING", 
                      "KW_WHERE", "KW_FROM", "KW_AS", "KW_SELECT", "KW_DISTINCT", 
                      "KW_INSERT", "KW_OVERWRITE", "KW_OUTER", "KW_UNIQUEJOIN", 
                      "KW_PRESERVE", "KW_JOIN", "KW_LEFT", "KW_RIGHT", "KW_FULL", 
                      "KW_ON", "KW_PARTITION", "KW_PARTITIONS", "KW_TABLE", 
                      "KW_TABLES", "KW_COLUMNS", "KW_INDEX", "KW_INDEXES", 
                      "KW_REBUILD", "KW_FUNCTIONS", "KW_SHOW", "KW_MSCK", 
                      "KW_REPAIR", "KW_DIRECTORY", "KW_LOCAL", "KW_TRANSFORM", 
                      "KW_USING", "KW_CLUSTER", "KW_DISTRIBUTE", "KW_SORT", 
                      "KW_UNION", "KW_EXCEPT", "KW_LOAD", "KW_EXPORT", "KW_IMPORT", 
                      "KW_REPLICATION", "KW_METADATA", "KW_DATA", "KW_INPATH", 
                      "KW_IS", "KW_NULL", "KW_CREATE", "KW_EXTERNAL", "KW_ALTER", 
                      "KW_CHANGE", "KW_COLUMN", "KW_FIRST", "KW_AFTER", 
                      "KW_DESCRIBE", "KW_DROP", "KW_RENAME", "KW_TO", "KW_COMMENT", 
                      "KW_BOOLEAN", "KW_TINYINT", "KW_SMALLINT", "KW_INT", 
                      "KW_BIGINT", "KW_FLOAT", "KW_DOUBLE", "KW_PRECISION", 
                      "KW_DATE", "KW_DATETIME", "KW_TIMESTAMP", "KW_TIMESTAMPLOCALTZ", 
                      "KW_TIME", "KW_ZONE", "KW_INTERVAL", "KW_DECIMAL", 
                      "KW_STRING", "KW_CHAR", "KW_VARCHAR", "KW_ARRAY", 
                      "KW_STRUCT", "KW_MAP", "KW_UNIONTYPE", "KW_REDUCE", 
                      "KW_PARTITIONED", "KW_CLUSTERED", "KW_SORTED", "KW_INTO", 
                      "KW_BUCKETS", "KW_ROW", "KW_ROWS", "KW_FORMAT", "KW_DELIMITED", 
                      "KW_FIELDS", "KW_TERMINATED", "KW_ESCAPED", "KW_COLLECTION", 
                      "KW_ITEMS", "KW_KEYS", "KW_KEY_TYPE", "KW_KILL", "KW_LINES", 
                      "KW_STORED", "KW_FILEFORMAT", "KW_INPUTFORMAT", "KW_OUTPUTFORMAT", 
                      "KW_INPUTDRIVER", "KW_OUTPUTDRIVER", "KW_ENABLE", 
                      "KW_DISABLE", "KW_LOCATION", "KW_TABLESAMPLE", "KW_BUCKET", 
                      "KW_OUT", "KW_OF", "KW_PERCENT", "KW_CAST", "KW_ADD", 
                      "KW_REPLACE", "KW_RLIKE", "KW_REGEXP", "KW_TEMPORARY", 
                      "KW_FUNCTION", "KW_MACRO", "KW_FILE", "KW_JAR", "KW_EXPLAIN", 
                      "KW_EXTENDED", "KW_FORMATTED", "KW_DEPENDENCY", "KW_LOGICAL", 
                      "KW_SERDE", "KW_WITH", "KW_DEFERRED", "KW_SERDEPROPERTIES", 
                      "KW_DBPROPERTIES", "KW_LIMIT", "KW_OFFSET", "KW_SET", 
                      "KW_UNSET", "KW_TBLPROPERTIES", "KW_IDXPROPERTIES", 
                      "KW_VALUE_TYPE", "KW_ELEM_TYPE", "KW_DEFINED", "KW_CASE", 
                      "KW_WHEN", "KW_THEN", "KW_ELSE", "KW_END", "KW_MAPJOIN", 
                      "KW_STREAMTABLE", "KW_CLUSTERSTATUS", "KW_UTC", "KW_UTCTIMESTAMP", 
                      "KW_LONG", "KW_DELETE", "KW_PLUS", "KW_MINUS", "KW_FETCH", 
                      "KW_INTERSECT", "KW_VIEW", "KW_VIEWS", "KW_IN", "KW_DATABASE", 
                      "KW_DATABASES", "KW_MATERIALIZED", "KW_SCHEMA", "KW_SCHEMAS", 
                      "KW_GRANT", "KW_REVOKE", "KW_SSL", "KW_UNDO", "KW_LOCK", 
                      "KW_LOCKS", "KW_UNLOCK", "KW_SHARED", "KW_EXCLUSIVE", 
                      "KW_PROCEDURE", "KW_UNSIGNED", "KW_WHILE", "KW_READ", 
                      "KW_READS", "KW_PURGE", "KW_RANGE", "KW_ANALYZE", 
                      "KW_BEFORE", "KW_BETWEEN", "KW_BOTH", "KW_BINARY", 
                      "KW_CROSS", "KW_CONTINUE", "KW_CURSOR", "KW_TRIGGER", 
                      "KW_RECORDREADER", "KW_RECORDWRITER", "KW_SEMI", "KW_LATERAL", 
                      "KW_TOUCH", "KW_ARCHIVE", "KW_UNARCHIVE", "KW_COMPUTE", 
                      "KW_STATISTICS", "KW_USE", "KW_OPTION", "KW_CONCATENATE", 
                      "KW_SHOW_DATABASE", "KW_UPDATE", "KW_RESTRICT", "KW_CASCADE", 
                      "KW_SKEWED", "KW_ROLLUP", "KW_CUBE", "KW_DIRECTORIES", 
                      "KW_FOR", "KW_WINDOW", "KW_UNBOUNDED", "KW_PRECEDING", 
                      "KW_FOLLOWING", "KW_CURRENT", "KW_CURRENT_DATE", "KW_CURRENT_TIMESTAMP", 
                      "KW_LESS", "KW_MORE", "KW_OVER", "KW_GROUPING", "KW_SETS", 
                      "KW_TRUNCATE", "KW_NOSCAN", "KW_USER", "KW_ROLE", 
                      "KW_ROLES", "KW_INNER", "KW_EXCHANGE", "KW_URI", "KW_SERVER", 
                      "KW_ADMIN", "KW_OWNER", "KW_PRINCIPALS", "KW_COMPACT", 
                      "KW_COMPACTIONS", "KW_TRANSACTIONS", "KW_REWRITE", 
                      "KW_AUTHORIZATION", "KW_REOPTIMIZATION", "KW_CONF", 
                      "KW_VALUES", "KW_RELOAD", "KW_YEAR", "KW_QUERY", "KW_QUARTER", 
                      "KW_MONTH", "KW_WEEK", "KW_DAY", "KW_DOW", "KW_HOUR", 
                      "KW_MINUTE", "KW_SECOND", "KW_START", "KW_TRANSACTION", 
                      "KW_COMMIT", "KW_ROLLBACK", "KW_WORK", "KW_ONLY", 
                      "KW_WRITE", "KW_ISOLATION", "KW_LEVEL", "KW_SNAPSHOT", 
                      "KW_AUTOCOMMIT", "KW_CACHE", "KW_PRIMARY", "KW_FOREIGN", 
                      "KW_REFERENCES", "KW_CONSTRAINT", "KW_ENFORCED", "KW_VALIDATE", 
                      "KW_NOVALIDATE", "KW_RELY", "KW_NORELY", "KW_UNIQUE", 
                      "KW_KEY", "KW_ABORT", "KW_EXTRACT", "KW_FLOOR", "KW_MERGE", 
                      "KW_MATCHED", "KW_REPL", "KW_DUMP", "KW_STATUS", "KW_VECTORIZATION", 
                      "KW_SUMMARY", "KW_OPERATOR", "KW_EXPRESSION", "KW_DETAIL", 
                      "KW_WAIT", "KW_RESOURCE", "KW_PLAN", "KW_QUERY_PARALLELISM", 
                      "KW_PLANS", "KW_ACTIVATE", "KW_DEFAULT", "KW_CHECK", 
                      "KW_POOL", "KW_MOVE", "KW_DO", "KW_ALLOC_FRACTION", 
                      "KW_SCHEDULING_POLICY", "KW_PATH", "KW_MAPPING", "KW_WORKLOAD", 
                      "KW_MANAGEMENT", "KW_ACTIVE", "KW_UNMANAGED", "KW_APPLICATION", 
                      "KW_SYNC", "DOT", "COLON", "COMMA", "SEMICOLON", "LPAREN", 
                      "RPAREN", "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", 
                      "EQUAL", "EQUAL_NS", "NOTEQUAL", "LESSTHANOREQUALTO", 
                      "LESSTHAN", "GREATERTHANOREQUALTO", "GREATERTHAN", 
                      "DIVIDE", "PLUS", "MINUS", "STAR", "MOD", "DIV", "AMPERSAND", 
                      "TILDE", "BITWISEOR", "CONCATENATE", "BITWISEXOR", 
                      "QUESTION", "DOLLAR", "StringLiteral", "CharSetLiteral", 
                      "IntegralLiteral", "NumberLiteral", "ByteLengthLiteral", 
                      "Number", "Identifier", "QuotedIdentifier", "CharSetName", 
                      "WS", "LINE_COMMENT", "QUERY_HINT", "SHOW_HINT", "HIDDEN_HINT" ]

    RULE_hint = 0
    RULE_hintList = 1
    RULE_hintItem = 2
    RULE_hintName = 3
    RULE_hintArgs = 4
    RULE_hintArgName = 5

    ruleNames =  [ "hint", "hintList", "hintItem", "hintName", "hintArgs", 
                   "hintArgName" ]

    EOF = Token.EOF
    KW_TRUE=1
    KW_FALSE=2
    KW_ALL=3
    KW_NONE=4
    KW_AND=5
    KW_OR=6
    KW_NOT=7
    KW_LIKE=8
    KW_ANY=9
    KW_IF=10
    KW_EXISTS=11
    KW_ASC=12
    KW_DESC=13
    KW_NULLS=14
    KW_LAST=15
    KW_ORDER=16
    KW_GROUP=17
    KW_BY=18
    KW_HAVING=19
    KW_WHERE=20
    KW_FROM=21
    KW_AS=22
    KW_SELECT=23
    KW_DISTINCT=24
    KW_INSERT=25
    KW_OVERWRITE=26
    KW_OUTER=27
    KW_UNIQUEJOIN=28
    KW_PRESERVE=29
    KW_JOIN=30
    KW_LEFT=31
    KW_RIGHT=32
    KW_FULL=33
    KW_ON=34
    KW_PARTITION=35
    KW_PARTITIONS=36
    KW_TABLE=37
    KW_TABLES=38
    KW_COLUMNS=39
    KW_INDEX=40
    KW_INDEXES=41
    KW_REBUILD=42
    KW_FUNCTIONS=43
    KW_SHOW=44
    KW_MSCK=45
    KW_REPAIR=46
    KW_DIRECTORY=47
    KW_LOCAL=48
    KW_TRANSFORM=49
    KW_USING=50
    KW_CLUSTER=51
    KW_DISTRIBUTE=52
    KW_SORT=53
    KW_UNION=54
    KW_EXCEPT=55
    KW_LOAD=56
    KW_EXPORT=57
    KW_IMPORT=58
    KW_REPLICATION=59
    KW_METADATA=60
    KW_DATA=61
    KW_INPATH=62
    KW_IS=63
    KW_NULL=64
    KW_CREATE=65
    KW_EXTERNAL=66
    KW_ALTER=67
    KW_CHANGE=68
    KW_COLUMN=69
    KW_FIRST=70
    KW_AFTER=71
    KW_DESCRIBE=72
    KW_DROP=73
    KW_RENAME=74
    KW_TO=75
    KW_COMMENT=76
    KW_BOOLEAN=77
    KW_TINYINT=78
    KW_SMALLINT=79
    KW_INT=80
    KW_BIGINT=81
    KW_FLOAT=82
    KW_DOUBLE=83
    KW_PRECISION=84
    KW_DATE=85
    KW_DATETIME=86
    KW_TIMESTAMP=87
    KW_TIMESTAMPLOCALTZ=88
    KW_TIME=89
    KW_ZONE=90
    KW_INTERVAL=91
    KW_DECIMAL=92
    KW_STRING=93
    KW_CHAR=94
    KW_VARCHAR=95
    KW_ARRAY=96
    KW_STRUCT=97
    KW_MAP=98
    KW_UNIONTYPE=99
    KW_REDUCE=100
    KW_PARTITIONED=101
    KW_CLUSTERED=102
    KW_SORTED=103
    KW_INTO=104
    KW_BUCKETS=105
    KW_ROW=106
    KW_ROWS=107
    KW_FORMAT=108
    KW_DELIMITED=109
    KW_FIELDS=110
    KW_TERMINATED=111
    KW_ESCAPED=112
    KW_COLLECTION=113
    KW_ITEMS=114
    KW_KEYS=115
    KW_KEY_TYPE=116
    KW_KILL=117
    KW_LINES=118
    KW_STORED=119
    KW_FILEFORMAT=120
    KW_INPUTFORMAT=121
    KW_OUTPUTFORMAT=122
    KW_INPUTDRIVER=123
    KW_OUTPUTDRIVER=124
    KW_ENABLE=125
    KW_DISABLE=126
    KW_LOCATION=127
    KW_TABLESAMPLE=128
    KW_BUCKET=129
    KW_OUT=130
    KW_OF=131
    KW_PERCENT=132
    KW_CAST=133
    KW_ADD=134
    KW_REPLACE=135
    KW_RLIKE=136
    KW_REGEXP=137
    KW_TEMPORARY=138
    KW_FUNCTION=139
    KW_MACRO=140
    KW_FILE=141
    KW_JAR=142
    KW_EXPLAIN=143
    KW_EXTENDED=144
    KW_FORMATTED=145
    KW_DEPENDENCY=146
    KW_LOGICAL=147
    KW_SERDE=148
    KW_WITH=149
    KW_DEFERRED=150
    KW_SERDEPROPERTIES=151
    KW_DBPROPERTIES=152
    KW_LIMIT=153
    KW_OFFSET=154
    KW_SET=155
    KW_UNSET=156
    KW_TBLPROPERTIES=157
    KW_IDXPROPERTIES=158
    KW_VALUE_TYPE=159
    KW_ELEM_TYPE=160
    KW_DEFINED=161
    KW_CASE=162
    KW_WHEN=163
    KW_THEN=164
    KW_ELSE=165
    KW_END=166
    KW_MAPJOIN=167
    KW_STREAMTABLE=168
    KW_CLUSTERSTATUS=169
    KW_UTC=170
    KW_UTCTIMESTAMP=171
    KW_LONG=172
    KW_DELETE=173
    KW_PLUS=174
    KW_MINUS=175
    KW_FETCH=176
    KW_INTERSECT=177
    KW_VIEW=178
    KW_VIEWS=179
    KW_IN=180
    KW_DATABASE=181
    KW_DATABASES=182
    KW_MATERIALIZED=183
    KW_SCHEMA=184
    KW_SCHEMAS=185
    KW_GRANT=186
    KW_REVOKE=187
    KW_SSL=188
    KW_UNDO=189
    KW_LOCK=190
    KW_LOCKS=191
    KW_UNLOCK=192
    KW_SHARED=193
    KW_EXCLUSIVE=194
    KW_PROCEDURE=195
    KW_UNSIGNED=196
    KW_WHILE=197
    KW_READ=198
    KW_READS=199
    KW_PURGE=200
    KW_RANGE=201
    KW_ANALYZE=202
    KW_BEFORE=203
    KW_BETWEEN=204
    KW_BOTH=205
    KW_BINARY=206
    KW_CROSS=207
    KW_CONTINUE=208
    KW_CURSOR=209
    KW_TRIGGER=210
    KW_RECORDREADER=211
    KW_RECORDWRITER=212
    KW_SEMI=213
    KW_LATERAL=214
    KW_TOUCH=215
    KW_ARCHIVE=216
    KW_UNARCHIVE=217
    KW_COMPUTE=218
    KW_STATISTICS=219
    KW_USE=220
    KW_OPTION=221
    KW_CONCATENATE=222
    KW_SHOW_DATABASE=223
    KW_UPDATE=224
    KW_RESTRICT=225
    KW_CASCADE=226
    KW_SKEWED=227
    KW_ROLLUP=228
    KW_CUBE=229
    KW_DIRECTORIES=230
    KW_FOR=231
    KW_WINDOW=232
    KW_UNBOUNDED=233
    KW_PRECEDING=234
    KW_FOLLOWING=235
    KW_CURRENT=236
    KW_CURRENT_DATE=237
    KW_CURRENT_TIMESTAMP=238
    KW_LESS=239
    KW_MORE=240
    KW_OVER=241
    KW_GROUPING=242
    KW_SETS=243
    KW_TRUNCATE=244
    KW_NOSCAN=245
    KW_USER=246
    KW_ROLE=247
    KW_ROLES=248
    KW_INNER=249
    KW_EXCHANGE=250
    KW_URI=251
    KW_SERVER=252
    KW_ADMIN=253
    KW_OWNER=254
    KW_PRINCIPALS=255
    KW_COMPACT=256
    KW_COMPACTIONS=257
    KW_TRANSACTIONS=258
    KW_REWRITE=259
    KW_AUTHORIZATION=260
    KW_REOPTIMIZATION=261
    KW_CONF=262
    KW_VALUES=263
    KW_RELOAD=264
    KW_YEAR=265
    KW_QUERY=266
    KW_QUARTER=267
    KW_MONTH=268
    KW_WEEK=269
    KW_DAY=270
    KW_DOW=271
    KW_HOUR=272
    KW_MINUTE=273
    KW_SECOND=274
    KW_START=275
    KW_TRANSACTION=276
    KW_COMMIT=277
    KW_ROLLBACK=278
    KW_WORK=279
    KW_ONLY=280
    KW_WRITE=281
    KW_ISOLATION=282
    KW_LEVEL=283
    KW_SNAPSHOT=284
    KW_AUTOCOMMIT=285
    KW_CACHE=286
    KW_PRIMARY=287
    KW_FOREIGN=288
    KW_REFERENCES=289
    KW_CONSTRAINT=290
    KW_ENFORCED=291
    KW_VALIDATE=292
    KW_NOVALIDATE=293
    KW_RELY=294
    KW_NORELY=295
    KW_UNIQUE=296
    KW_KEY=297
    KW_ABORT=298
    KW_EXTRACT=299
    KW_FLOOR=300
    KW_MERGE=301
    KW_MATCHED=302
    KW_REPL=303
    KW_DUMP=304
    KW_STATUS=305
    KW_VECTORIZATION=306
    KW_SUMMARY=307
    KW_OPERATOR=308
    KW_EXPRESSION=309
    KW_DETAIL=310
    KW_WAIT=311
    KW_RESOURCE=312
    KW_PLAN=313
    KW_QUERY_PARALLELISM=314
    KW_PLANS=315
    KW_ACTIVATE=316
    KW_DEFAULT=317
    KW_CHECK=318
    KW_POOL=319
    KW_MOVE=320
    KW_DO=321
    KW_ALLOC_FRACTION=322
    KW_SCHEDULING_POLICY=323
    KW_PATH=324
    KW_MAPPING=325
    KW_WORKLOAD=326
    KW_MANAGEMENT=327
    KW_ACTIVE=328
    KW_UNMANAGED=329
    KW_APPLICATION=330
    KW_SYNC=331
    DOT=332
    COLON=333
    COMMA=334
    SEMICOLON=335
    LPAREN=336
    RPAREN=337
    LSQUARE=338
    RSQUARE=339
    LCURLY=340
    RCURLY=341
    EQUAL=342
    EQUAL_NS=343
    NOTEQUAL=344
    LESSTHANOREQUALTO=345
    LESSTHAN=346
    GREATERTHANOREQUALTO=347
    GREATERTHAN=348
    DIVIDE=349
    PLUS=350
    MINUS=351
    STAR=352
    MOD=353
    DIV=354
    AMPERSAND=355
    TILDE=356
    BITWISEOR=357
    CONCATENATE=358
    BITWISEXOR=359
    QUESTION=360
    DOLLAR=361
    StringLiteral=362
    CharSetLiteral=363
    IntegralLiteral=364
    NumberLiteral=365
    ByteLengthLiteral=366
    Number=367
    Identifier=368
    QuotedIdentifier=369
    CharSetName=370
    WS=371
    LINE_COMMENT=372
    QUERY_HINT=373
    SHOW_HINT=374
    HIDDEN_HINT=375

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hintList(self):
            return self.getTypedRuleContext(HintParser.HintListContext,0)


        def EOF(self):
            return self.getToken(HintParser.EOF, 0)

        def getRuleIndex(self):
            return HintParser.RULE_hint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHint" ):
                listener.enterHint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHint" ):
                listener.exitHint(self)




    def hint(self):

        localctx = HintParser.HintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_hint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.hintList()
            self.state = 13
            self.match(HintParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hintItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HintParser.HintItemContext)
            else:
                return self.getTypedRuleContext(HintParser.HintItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HintParser.COMMA)
            else:
                return self.getToken(HintParser.COMMA, i)

        def getRuleIndex(self):
            return HintParser.RULE_hintList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHintList" ):
                listener.enterHintList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHintList" ):
                listener.exitHintList(self)




    def hintList(self):

        localctx = HintParser.HintListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hintList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.hintItem()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==334:
                self.state = 16
                self.match(HintParser.COMMA)
                self.state = 17
                self.hintItem()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hintName(self):
            return self.getTypedRuleContext(HintParser.HintNameContext,0)


        def LPAREN(self):
            return self.getToken(HintParser.LPAREN, 0)

        def hintArgs(self):
            return self.getTypedRuleContext(HintParser.HintArgsContext,0)


        def RPAREN(self):
            return self.getToken(HintParser.RPAREN, 0)

        def getRuleIndex(self):
            return HintParser.RULE_hintItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHintItem" ):
                listener.enterHintItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHintItem" ):
                listener.exitHintItem(self)




    def hintItem(self):

        localctx = HintParser.HintItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_hintItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.hintName()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==336:
                self.state = 24
                self.match(HintParser.LPAREN)
                self.state = 25
                self.hintArgs()
                self.state = 26
                self.match(HintParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_MAPJOIN(self):
            return self.getToken(HintParser.KW_MAPJOIN, 0)

        def KW_SEMI(self):
            return self.getToken(HintParser.KW_SEMI, 0)

        def KW_STREAMTABLE(self):
            return self.getToken(HintParser.KW_STREAMTABLE, 0)

        def getRuleIndex(self):
            return HintParser.RULE_hintName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHintName" ):
                listener.enterHintName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHintName" ):
                listener.exitHintName(self)




    def hintName(self):

        localctx = HintParser.HintNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_hintName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(((((_la - 167)) & ~0x3f) == 0 and ((1 << (_la - 167)) & 70368744177667) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hintArgName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HintParser.HintArgNameContext)
            else:
                return self.getTypedRuleContext(HintParser.HintArgNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HintParser.COMMA)
            else:
                return self.getToken(HintParser.COMMA, i)

        def getRuleIndex(self):
            return HintParser.RULE_hintArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHintArgs" ):
                listener.enterHintArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHintArgs" ):
                listener.exitHintArgs(self)




    def hintArgs(self):

        localctx = HintParser.HintArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hintArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.hintArgName()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==334:
                self.state = 33
                self.match(HintParser.COMMA)
                self.state = 34
                self.hintArgName()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintArgNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(HintParser.Identifier, 0)

        def Number(self):
            return self.getToken(HintParser.Number, 0)

        def KW_NONE(self):
            return self.getToken(HintParser.KW_NONE, 0)

        def getRuleIndex(self):
            return HintParser.RULE_hintArgName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHintArgName" ):
                listener.enterHintArgName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHintArgName" ):
                listener.exitHintArgName(self)




    def hintArgName(self):

        localctx = HintParser.HintArgNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hintArgName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==4 or _la==367 or _la==368):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





