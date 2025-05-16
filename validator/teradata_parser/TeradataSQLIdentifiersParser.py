# Generated from sql/teradata/TeradataSQLIdentifiersParser.g4 by ANTLR 4.13.2
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
        4,1,1233,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,62,8,0,1,1,1,1,1,1,1,1,3,1,68,8,
        1,1,2,1,2,3,2,72,8,2,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,3,3,81,8,3,1,
        4,1,4,1,4,3,4,86,8,4,1,4,1,4,3,4,90,8,4,1,5,1,5,1,5,3,5,95,8,5,1,
        5,1,5,3,5,99,8,5,1,6,1,6,1,6,3,6,104,8,6,1,6,1,6,3,6,108,8,6,1,7,
        1,7,1,7,3,7,113,8,7,1,7,1,7,3,7,117,8,7,1,8,1,8,3,8,121,8,8,1,9,
        1,9,3,9,125,8,9,1,10,1,10,1,10,3,10,130,8,10,1,11,1,11,3,11,134,
        8,11,1,12,1,12,3,12,138,8,12,1,13,1,13,3,13,142,8,13,1,14,1,14,3,
        14,146,8,14,1,15,1,15,3,15,150,8,15,1,16,1,16,3,16,154,8,16,1,17,
        1,17,3,17,158,8,17,1,18,1,18,3,18,162,8,18,1,19,1,19,3,19,166,8,
        19,1,20,1,20,3,20,170,8,20,1,21,1,21,3,21,174,8,21,1,22,1,22,3,22,
        178,8,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,2,12,0,106,106,506,
        509,678,678,774,774,778,779,863,864,904,904,949,949,985,985,1009,
        1009,1026,1028,1061,1062,1,0,488,1192,190,0,61,1,0,0,0,2,67,1,0,
        0,0,4,71,1,0,0,0,6,76,1,0,0,0,8,85,1,0,0,0,10,94,1,0,0,0,12,103,
        1,0,0,0,14,112,1,0,0,0,16,120,1,0,0,0,18,124,1,0,0,0,20,129,1,0,
        0,0,22,133,1,0,0,0,24,137,1,0,0,0,26,141,1,0,0,0,28,145,1,0,0,0,
        30,149,1,0,0,0,32,153,1,0,0,0,34,157,1,0,0,0,36,161,1,0,0,0,38,165,
        1,0,0,0,40,169,1,0,0,0,42,173,1,0,0,0,44,177,1,0,0,0,46,179,1,0,
        0,0,48,181,1,0,0,0,50,51,3,16,8,0,51,52,5,1209,0,0,52,53,3,4,2,0,
        53,54,5,1209,0,0,54,55,3,2,1,0,55,62,1,0,0,0,56,57,3,4,2,0,57,58,
        5,1209,0,0,58,59,3,2,1,0,59,62,1,0,0,0,60,62,3,2,1,0,61,50,1,0,0,
        0,61,56,1,0,0,0,61,60,1,0,0,0,62,1,1,0,0,0,63,68,5,1193,0,0,64,68,
        3,48,24,0,65,68,5,366,0,0,66,68,5,363,0,0,67,63,1,0,0,0,67,64,1,
        0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,72,5,1193,0,0,
        70,72,3,48,24,0,71,69,1,0,0,0,71,70,1,0,0,0,72,5,1,0,0,0,73,74,3,
        16,8,0,74,75,5,1209,0,0,75,77,1,0,0,0,76,73,1,0,0,0,76,77,1,0,0,
        0,77,80,1,0,0,0,78,81,5,1193,0,0,79,81,3,48,24,0,80,78,1,0,0,0,80,
        79,1,0,0,0,81,7,1,0,0,0,82,83,3,16,8,0,83,84,5,1209,0,0,84,86,1,
        0,0,0,85,82,1,0,0,0,85,86,1,0,0,0,86,89,1,0,0,0,87,90,5,1193,0,0,
        88,90,3,48,24,0,89,87,1,0,0,0,89,88,1,0,0,0,90,9,1,0,0,0,91,92,3,
        16,8,0,92,93,5,1209,0,0,93,95,1,0,0,0,94,91,1,0,0,0,94,95,1,0,0,
        0,95,98,1,0,0,0,96,99,5,1193,0,0,97,99,3,48,24,0,98,96,1,0,0,0,98,
        97,1,0,0,0,99,11,1,0,0,0,100,101,3,16,8,0,101,102,5,1209,0,0,102,
        104,1,0,0,0,103,100,1,0,0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,
        108,5,1193,0,0,106,108,3,48,24,0,107,105,1,0,0,0,107,106,1,0,0,0,
        108,13,1,0,0,0,109,110,3,16,8,0,110,111,5,1209,0,0,111,113,1,0,0,
        0,112,109,1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,117,5,1193,
        0,0,115,117,3,48,24,0,116,114,1,0,0,0,116,115,1,0,0,0,117,15,1,0,
        0,0,118,121,5,1193,0,0,119,121,3,48,24,0,120,118,1,0,0,0,120,119,
        1,0,0,0,121,17,1,0,0,0,122,125,5,1193,0,0,123,125,3,48,24,0,124,
        122,1,0,0,0,124,123,1,0,0,0,125,19,1,0,0,0,126,130,5,1193,0,0,127,
        130,5,10,0,0,128,130,3,48,24,0,129,126,1,0,0,0,129,127,1,0,0,0,129,
        128,1,0,0,0,130,21,1,0,0,0,131,134,5,1193,0,0,132,134,3,48,24,0,
        133,131,1,0,0,0,133,132,1,0,0,0,134,23,1,0,0,0,135,138,5,1193,0,
        0,136,138,3,48,24,0,137,135,1,0,0,0,137,136,1,0,0,0,138,25,1,0,0,
        0,139,142,5,1193,0,0,140,142,3,48,24,0,141,139,1,0,0,0,141,140,1,
        0,0,0,142,27,1,0,0,0,143,146,5,1193,0,0,144,146,3,48,24,0,145,143,
        1,0,0,0,145,144,1,0,0,0,146,29,1,0,0,0,147,150,5,1193,0,0,148,150,
        3,48,24,0,149,147,1,0,0,0,149,148,1,0,0,0,150,31,1,0,0,0,151,154,
        5,1193,0,0,152,154,3,48,24,0,153,151,1,0,0,0,153,152,1,0,0,0,154,
        33,1,0,0,0,155,158,5,1193,0,0,156,158,3,48,24,0,157,155,1,0,0,0,
        157,156,1,0,0,0,158,35,1,0,0,0,159,162,5,1193,0,0,160,162,3,48,24,
        0,161,159,1,0,0,0,161,160,1,0,0,0,162,37,1,0,0,0,163,166,5,1193,
        0,0,164,166,3,48,24,0,165,163,1,0,0,0,165,164,1,0,0,0,166,39,1,0,
        0,0,167,170,5,1193,0,0,168,170,3,48,24,0,169,167,1,0,0,0,169,168,
        1,0,0,0,170,41,1,0,0,0,171,174,5,1193,0,0,172,174,3,48,24,0,173,
        171,1,0,0,0,173,172,1,0,0,0,174,43,1,0,0,0,175,178,5,1193,0,0,176,
        178,3,48,24,0,177,175,1,0,0,0,177,176,1,0,0,0,178,45,1,0,0,0,179,
        180,7,0,0,0,180,47,1,0,0,0,181,182,7,1,0,0,182,49,1,0,0,0,28,61,
        67,71,76,80,85,89,94,98,103,107,112,116,120,124,129,133,137,141,
        145,149,153,157,161,165,169,173,177
    ]

class TeradataSQLIdentifiersParser ( Parser ):

    grammarFileName = "TeradataSQLIdentifiersParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ABORT'", "'ABORTSESSION'", "'ABS'", 
                     "'ACCESS_LOCK'", "'ACCOUNT'", "'ACOS'", "'ACOSH'", 
                     "'ADD'", "'ADD_MONTHS'", "'ADMIN'", "'AFTER'", "'AGGREGATE'", 
                     "'ALL'", "'ALTER'", "'AMP'", "'AND'", "'ANSIDATE'", 
                     "'ANY'", "'ARGLPAREN'", "'AS'", "'ASC'", "'ASIN'", 
                     "'ASINH'", "'AT'", "'ATAN'", "'ATAN2'", "'ATANH'", 
                     "'ATOMIC'", "'AUTHORIZATION'", "'AVE'", "'AVERAGE'", 
                     "'AVG'", "'BEFORE'", "'BEGIN'", "'BETWEEN'", "'BIGINT'", 
                     "'BINARY'", "'BLOB'", "'BOTH'", "'BT'", "'BUT'", "'BY'", 
                     "'BYTE'", "'BYTEINT'", "'BYTES'", "'CALL'", "'CASE'", 
                     "'CASE_N'", "'CASESPECIFIC'", "'CAST'", "'CD'", "'CHAR'", 
                     "'CHAR_LENGTH'", "'CHAR2HEXINT'", "'CHARACTER'", "'CHARACTER_LENGTH'", 
                     "'CHARACTERS'", "'CHARS'", "'CHECK'", "'CHECKPOINT'", 
                     "'CLASS'", "'CLOB'", "'CLOSE'", "'CLUSTER'", "'CM'", 
                     "'COALESCE'", "'COLLATION'", "'COLLECT'", "'COLUMN'", 
                     "'COMMENT'", "'COMMIT'", "'COMPRESS'", "'CONNECT'", 
                     "'CONSTRAINT'", "'CONSTRUCTOR'", "'CONSUME'", "'CONTAINS'", 
                     "'CONTINUE'", "'CONVERT_TABLE_HEADER'", "'CORR'", "'COS'", 
                     "'COSH'", "'COUNT'", "'COVAR_POP'", "'COVAR_SAMP'", 
                     "'CREATE'", "'CROSS'", "'CS'", "'CSUM'", "'CT'", "'CTCONTROL'", 
                     "'CUBE'", "'CURRENT'", "'CURRENT_DATE'", "'CURRENT_ROLE'", 
                     "'CURRENT_TIME'", "'CURRENT_TIMESTAMP'", "'CURRENT_USER'", 
                     "'CURSOR'", "'CV'", "'CYCLE'", "'DATABASE'", "'DATABLOCKSIZE'", 
                     "'DATE'", "'DATEFORM'", "'DAY'", "'DEALLOCATE'", "'DEC'", 
                     "'DECIMAL'", "'DECLARE'", "'DEFAULT'", "'DEFERRED'", 
                     "'DEGREES'", "'DEL'", "'DELETE'", "'DESC'", "'DETERMINISTIC'", 
                     "'DIAGNOSTIC'", "'DICTIONARY'", "'DISABLED'", "'DISTINCT'", 
                     "'DO'", "'DOMAIN'", "'DOUBLE'", "'DROP'", "'DUAL'", 
                     "'DUMP'", "'DYNAMIC'", "'EACH'", "'ECHO'", "'ELSE'", 
                     "'ELSEIF'", "'ENABLED'", "'END'", "'EQ'", "'EQUALS'", 
                     "'ERROR'", "'ERRORFILES'", "'ERRORTABLES'", "'ESCAPE'", 
                     "'ET'", "'EXCEPT'", "'EXEC'", "'EXECUTE'", "'EXISTS'", 
                     "'EXIT'", "'EXP'", "'EXPAND'", "'EXPANDING'", "'EXPLAIN'", 
                     "'EXTERNAL'", "'EXTRACT'", "'FALLBACK'", "'FASTEXPORT'", 
                     "'FETCH'", "'FIRST'", "'FLOAT'", "'FLUSH'", "'FOR'", 
                     "'FOREIGN'", "'FORMAT'", "'FOUND'", "'FREESPACE'", 
                     "'FROM'", "'FULL'", "'FUNCTION'", "'FUNCTIONDESCRIPTOR'", 
                     "'GE'", "'GENERATED'", "'GET'", "'GIVE'", "'GRANT'", 
                     "'GRAPHIC'", "'GROUP'", "'GROUPING'", "'GT'", "'HANDLER'", 
                     "'HASH'", "'HASHAMP'", "'HASHBAKAMP'", "'HASHBUCKET'", 
                     "'HASHROW'", "'HAVING'", "'HELP'", "'HOUR'", "'ID2BIGINT'", 
                     "'IDENTITY'", "'IF'", "'IMMEDIATE'", "'IN'", "'INCONSISTENT'", 
                     "'INDEX'", "'INITIATE'", "'INNER'", "'INOUT'", "'INPUT'", 
                     "'INS'", "'INSERT'", "'INSTANCE'", "'INSTEAD'", "'INT'", 
                     "'INTEGER'", "'INTEGERDATE'", "'INTERSECT'", "'INTERVAL'", 
                     "'INTO'", "'IS'", "'ITERATE'", "'JAR'", "'JOIN'", "'JOURNAL'", 
                     "'KEY'", "'KURTOSIS'", "'LANGUAGE'", "'LARGE'", "'LE'", 
                     "'LEADING'", "'LEAVE'", "'LEFT'", "'LIKE'", "'LIMIT'", 
                     "'LN'", "'LOADING'", "'LOCAL'", "'LOCATOR'", "'LOCK'", 
                     "'LOCKING'", "'LOG'", "'LOGGING'", "'LOGON'", "'LONG'", 
                     "'LOOP'", "'LOWER'", "'LT'", "'MACRO'", "'MAP'", "'MAVG'", 
                     "'MAX'", "'MAXIMUM'", "'MCHARACTERS'", "'MDIFF'", "'MERGE'", 
                     "'METHOD'", "'MIN'", "'MINDEX'", "'MINIMUM'", "'MINUS'", 
                     "'MINUTE'", "'MLINREG'", "'MLOAD'", "'MOD'", "'MODE'", 
                     "'MODIFIES'", "'MODIFY'", "'MONITOR'", "'MONRESOURCE'", 
                     "'MONSESSION'", "'MONTH'", "'MSUBSTR'", "'MSUM'", "'MULTISET'", 
                     "'NAMED'", "'NATURAL'", "'NE'", "'NEW'", "'NEW_TABLE'", 
                     "'NEXT'", "'NO'", "'NONE'", "'NONTEMPORAL'", "'NORMALIZE'", 
                     "'NOT'", "'NOWAIT'", "'NULL'", "'NULLIF'", "'NULLIFZERO'", 
                     "'NUMBER'", "'NUMERIC'", "'OBJECT'", "'OBJECTS'", "'OCTET_LENGTH'", 
                     "'OF'", "'OFF'", "'OLD'", "'OLD_TABLE'", "'ON'", "'ONLY'", 
                     "'OPEN'", "'OPTION'", "'OR'", "'ORDER'", "'ORDERING'", 
                     "'OUT'", "'OUTER'", "'OVER'", "'OVERLAPS'", "'OVERRIDE'", 
                     "'PARAMETER'", "'PASSWORD'", "'PERCENT'", "'PERCENT_RANK'", 
                     "'PERM'", "'PERMANENT'", "'POSITION'", "'PRECISION'", 
                     "'PREPARE'", "'PRESERVE'", "'PRIMARY'", "'PRIVILEGES'", 
                     "'PROCEDURE'", "'PROFILE'", "'PROTECTION'", "'PUBLIC'", 
                     "'QUALIFIED'", "'QUALIFY'", "'QUANTILE'", "'QUEUE'", 
                     "'RADIANS'", "'RANDOM'", "'RANGE_N'", "'RANK'", "'READS'", 
                     "'REAL'", "'RECURSIVE'", "'REFERENCES'", "'REFERENCING'", 
                     "'REGR_AVGX'", "'REGR_AVGY'", "'REGR_COUNT'", "'REGR_INTERCEPT'", 
                     "'REGR_R2'", "'REGR_SLOPE'", "'REGR_SXX'", "'REGR_SXY'", 
                     "'REGR_SYY'", "'RELATIVE'", "'RELEASE'", "'RENAME'", 
                     "'REPEAT'", "'REPLACE'", "'REPLCONTROL'", "'REPLICATION'", 
                     "'REQUEST'", "'RESIGNAL'", "'RESTART'", "'RESTORE'", 
                     "'RESULT'", "'RESUME'", "'RET'", "'RETRIEVE'", "'RETURN'", 
                     "'RETURNS'", "'REVALIDATE'", "'REVOKE'", "'RIGHT'", 
                     "'RIGHTS'", "'ROLE'", "'ROLLBACK'", "'ROLLFORWARD'", 
                     "'ROLLUP'", "'ROW'", "'ROW_NUMBER'", "'ROWID'", "'ROWS'", 
                     "'SAMPLE'", "'SAMPLEID'", "'SCROLL'", "'SECOND'", "'SEL'", 
                     "'SELECT'", "'SESSION'", "'SET'", "'SETRESRATE'", "'SETS'", 
                     "'SETSESSRATE'", "'SHOW'", "'SIGNAL'", "'SIN'", "'SINH'", 
                     "'SKEW'", "'SMALLINT'", "'SOME'", "'SOUNDEX'", "'SPECIFIC'", 
                     "'SPOOL'", "'SQL'", "'SQLEXCEPTION'", "'SQLTEXT'", 
                     "'SQLWARNING'", "'SQRT'", "'SS'", "'START'", "'STARTUP'", 
                     "'STATEMENT'", "'STATISTICS'", "'STDDEV_POP'", "'STDDEV_SAMP'", 
                     "'STEPINFO'", "'STRING_CS'", "'SUBSCRIBER'", "'SUBSTR'", 
                     "'SUBSTRING'", "'SUM'", "'SUMMARY'", "'SUSPEND'", "'TABLE'", 
                     "'TAN'", "'TANH'", "'TBL_CS'", "'TD_ANYTYPE'", "'TD_AUTHID'", 
                     "'TD_HOST'", "'TD_ROWLOADID'", "'TD_ROWREVISION'", 
                     "'TD_ROWSIZE'", "'TD_VALIST'", "'TEMPORARY'", "'TERMINATE'", 
                     "'THEN'", "'THRESHOLD'", "'TIME'", "'TIMESTAMP'", "'TIMEZONE_HOUR'", 
                     "'TIMEZONE_MINUTE'", "'TITLE'", "'TO'", "'TOP'", "'TRACE'", 
                     "'TRAILING'", "'TRANSACTION'", "'TRANSACTIONTIME'", 
                     "'TRANSFORM'", "'TRANSLATE'", "'TRANSLATE_CHK'", "'TRIGGER'", 
                     "'TRIM'", "'TYPE'", "'UC'", "'UDTCASTAS'", "'UDTCASTLPAREN'", 
                     "'UDTMETHOD'", "'UDTTYPE'", "'UDTUSAGE'", "'UESCAPE'", 
                     "'UNDEFINED'", "'UNDO'", "'UNION'", "'UNIQUE'", "'UNTIL'", 
                     "'UNTIL_CHANGED'", "'UNTIL_CLOSED'", "'UPD'", "'UPDATE'", 
                     "'UPPER'", "'UPPERCASE'", "'USER'", "'USING'", "'VALIDTIME'", 
                     "'VALUE'", "'VALUES'", "'VAR_POP'", "'VAR_SAMP'", "'VARBYTE'", 
                     "'VARCHAR'", "'VARGRAPHIC'", "'VARIANT_TYPE'", "'VARYING'", 
                     "'VIEW'", "'VOLATILE'", "'WHEN'", "'WHERE'", "'WHILE'", 
                     "'WIDTH_BUCKET'", "'WITH'", "'WITHOUT'", "'WORK'", 
                     "'XMLPLAN'", "'YEAR'", "'ZEROIFNULL'", "'ZONE'", "'ALIAS'", 
                     "'DESCRIPTOR'", "'GO'", "'GOTO'", "'INDICATOR'", "'PRIVATE'", 
                     "'WAIT'", "'AbortSessions'", "'ABSENT'", "'ACCESS'", 
                     "'ACCORDING'", "'ACCUMULATE'", "'AG'", "'AggGeomIntersection'", 
                     "'AggGeomUnion'", "'ALLDBQL'", "'ALLOCATE'", "'ALLOCATION'", 
                     "'ALLOW'", "'ALLPARAMS'", "'ALLTDWM'", "'ALWAYS'", 
                     "'AMPCOUNT'", "'ANALYSIS'", "'ANCHOR'", "'ANCHOR_HOUR'", 
                     "'ANCHOR_MILLISECOND'", "'ANCHOR_MINUTE'", "'ANCHOR_SECOND'", 
                     "'APPLNAME'", "'ARCHIVE'", "'ARRAY'", "'ARRAY_ADD'", 
                     "'ARRAY_AGG'", "'ARRAY_AVG'", "'ARRAY_COMPARE'", "'ARRAY_CONCAT'", 
                     "'ARRAY_COUNT_DISTINCT'", "'ARRAY_DIV'", "'ARRAY_EQ'", 
                     "'ARRAY_GE'", "'ARRAY_GET'", "'ARRAY_GT'", "'ARRAY_LE'", 
                     "'ARRAY_LT'", "'ARRAY_MAX'", "'ARRAY_MIN'", "'ARRAY_MOD'", 
                     "'ARRAY_MUL'", "'ARRAY_NE'", "'ARRAY_SUB'", "'ARRAY_SUM'", 
                     "'ARRAY_UPDATE'", "'ARRAY_UPDATE_STRIDE'", "'ASCII'", 
                     "'ASSIGNMENT'", "'ATTR'", "'ATTRIBUTE'", "'ATTRIBUTES'", 
                     "'ATTRIBUTION'", "'ATTRS'", "'AUTH'", "'AUTO'", "'AUTOTEMP'", 
                     "'AVRO'", "'BIT_LENGTH'", "'BITAND'", "'BITNOT'", "'BITOR'", 
                     "'BITXOR'", "'BLOCKCOMPRESSION'", "'BLOCKCOMPRESSIONALGORITHM'", 
                     "'BLOCKCOMPRESSIONLEVEL'", "'BOM'", "'BOTTOM'", "'BSON'", 
                     "'C'", "'CALENDAR'", "'CALLED'", "'CALLER'", "'camset'", 
                     "'camset_l'", "'CAPTURE'", "'CARDINALITY'", "'CEIL'", 
                     "'CEILING'", "'CHANGERATE'", "'CHARACTERISTICS'", "'CHARSET'", 
                     "'CHARSET_COLL'", "'CHECKSUM'", "'CHR'", "'CLASS_ORIGIN'", 
                     "'CLICKLAG'", "'CLIENT'", "'CNT'", "'COLOCATE'", "'COLUMNMETA'", 
                     "'COLUMNS'", "'COLUMNSPERINDEX'", "'COLUMNSPERJOININDEX'", 
                     "'COMMAND_FUNCTION'", "'COMMAND_FUNCTION_CODE'", "'COMPARISON'", 
                     "'COMPILE'", "'CONCAT'", "'CONCURRENT'", "'CONDITION'", 
                     "'CONDITION_IDENTIFIER'", "'CONDITION_NUMBER'", "'CONTAINED'", 
                     "'CONTAINEDTOKEN'", "'CONTENT'", "'CONTIGUOUS'", "'COST'", 
                     "'COSTS'", "'COUNTSET'", "'CPP'", "'CPUTIME'", "'CPUTIMENORM'", 
                     "'CREATEDATASET'", "'CREATOR'", "'CUME_DIST'", "'CURDATE'", 
                     "'CURTIME'", "'DATA'", "'DATASET'", "'day_of_calendar'", 
                     "'day_of_month'", "'day_of_week'", "'day_of_year'", 
                     "'DayNumber_Of_Calendar'", "'DayNumber_Of_Month'", 
                     "'DayNumber_Of_Week'", "'DayNumber_Of_Year'", "'DayOccurrence_Of_Month'", 
                     "'DBA'", "'DBC'", "'DEBUG'", "'decamset'", "'decamset_l'", 
                     "'DECODE'", "'DECOMPRESS'", "'DEFINER'", "'DELIMITER'", 
                     "'DELTA_T'", "'DEMOGRAPHICS'", "'DENIALS'", "'DENSE'", 
                     "'DENSE_RANK'", "'DESCRIBE'", "'DETAILED'", "'DIAGNOSTICS'", 
                     "'DIGITS'", "'DIMENSION'", "'DOCUMENT'", "'DOT'", "'DOWN'", 
                     "'DR'", "'DUPCOUNT'", "'DUPCOUNTCUM'", "'EBCDIC'", 
                     "'EDITDISTANCE'", "'ELAPSEDSEC'", "'ELAPSEDTIME'", 
                     "'ELEMENT'", "'ELZS_H'", "'EMITNULL'", "'EMPTY'", "'EMPTY_BLOB'", 
                     "'EMPTY_CLOB'", "'ENCODE'", "'ENCODING'", "'ENCRYPT'", 
                     "'ERRORS'", "'ERRORTBL'", "'EVENTCOLUMN'", "'EXCEPTION'", 
                     "'EXCL'", "'EXCLUDE'", "'EXCLUDING'", "'EXCLUSIVE'", 
                     "'EXPIRE'", "'EXPORT'", "'EXPORTWIDTH'", "'FALSE'", 
                     "'FEATUREINFO'", "'FILE'", "'FILL'", "'FILTER'", "'FINAL'", 
                     "'FIRST_NOTNULL'", "'FIRST_VALUE'", "'FLOOR'", "'FOLLOWING'", 
                     "'FOREIGNFUNCTION'", "'FORTOKEN'", "'FRIDAY'", "'FROM_BYTES'", 
                     "'FUNCTIONPARAMETER'", "'G'", "'GETBIT'", "'GetPSFVersion'", 
                     "'GetQueryBand'", "'GetQueryBandValue'", "'GetTimeZoneDisplacement'", 
                     "'GLOBAL'", "'GLOP'", "'Greatest'", "'HIGH'", "'HOST'", 
                     "'IdentifyDatabase'", "'IdentifySession'", "'IdentifyTable'", 
                     "'IdentifyUser'", "'IFP'", "'IGNORE'", "'IMMEDIATELY'", 
                     "'IMPORT'", "'INCLUDE'", "'INCLUDING'", "'INCREMENT'", 
                     "'INCREMENTAL'", "'INDENT'", "'INDEXESPERTABLE'", "'INDEXMAINTMODE'", 
                     "'INIT'", "'INITCAP'", "'INLINE'", "'INSTANTIABLE'", 
                     "'INSTR'", "'INTERNAL'", "'INVOKER'", "'IOCOUNT'", 
                     "'IPARTITION'", "'ISOLATED'", "'ISOLATION'", "'JAVA'", 
                     "'JIS_COLL'", "'JSON'", "'JSON_AGG'", "'JSON_COMPOSE'", 
                     "'K'", "'KANJI1'", "'KANJISJIS'", "'KBYTE'", "'KBYTES'", 
                     "'KEEP'", "'KILOBYTES'", "'LAG'", "'LAST'", "'Last_Day'", 
                     "'LAST_NOTNULL'", "'LAST_VALUE'", "'LATIN'", "'LDIFF'", 
                     "'LEAD'", "'Least'", "'LENGTH'", "'LEVEL'", "'LIST'", 
                     "'LOAD'", "'LOCATE'", "'LOCKEDUSEREXPIRE'", "'LOW'", 
                     "'LPAD'", "'LTRIM'", "'lzcomp'", "'lzcomp_L'", "'lzdecomp'", 
                     "'lzdecomp_L'", "'M'", "'MAD'", "'MANUAL'", "'MAPPING'", 
                     "'MATCHED'", "'MAX_CHOOSE'", "'MAXCHAR'", "'MAXINTERVALS'", 
                     "'MAXLOGONATTEMPTS'", "'MAXVALUE'", "'MAXVALUELENGTH'", 
                     "'MEDIAN'", "'MEDIUM'", "'MEETS'", "'MEMBER'", "'MERGEBLOCKRATIO'", 
                     "'MESSAGE_LENGTH'", "'MESSAGE_TEXT'", "'MIN_CHOOSE'", 
                     "'MINCHAR'", "'MINVALUE'", "'MODIFIED'", "'MONDAY'", 
                     "'MonitorQueryBand'", "'MonitorSessionRate'", "'MonitorVersion'", 
                     "'MONTH_BEGIN'", "'MONTH_END'", "'month_of_calendar'", 
                     "'month_of_quarter'", "'month_of_year'", "'MonthNumber_Of_Calendar'", 
                     "'MonthNumber_Of_Quarter'", "'MonthNumber_Of_Year'", 
                     "'Months_Between'", "'MORE'", "'MULTINATIONAL'", "'NAME'", 
                     "'NAMESPACE'", "'NEVER'", "'NEXT_DAY'", "'NGRAM'", 
                     "'NIL'", "'NODDLTEXT'", "'NODE'", "'NONOPTCOST'", "'NONOPTINIT'", 
                     "'NONSEQUENCED'", "'NORIGHT'", "'NOSEXTRACTVARFROMPATH'", 
                     "'NOTATION'", "'NOW'", "'NPATH'", "'NTH'", "'NULLS'", 
                     "'NUMFPFNS'", "'NUMTODSINTERVAL'", "'NUMTOYMINTERVAL'", 
                     "'nvl'", "'nvl2'", "'NVP'", "'OA'", "'OAdd_Months'", 
                     "'OCOUNT'", "'ODELETE'", "'OEXISTS'", "'OEXTEND'", 
                     "'OFIRST'", "'OLAST'", "'OLD_NEW_TABLE'", "'OLIMIT'", 
                     "'ONEXT'", "'ONLINE'", "'OPRIOR'", "'OPTIONS'", "'ORDERBYVALUES'", 
                     "'ORDERED_ANALYTIC'", "'ORDINALITY'", "'OREPLACE'", 
                     "'OTRANSLATE'", "'OTRIM'", "'OVERLAYS'", "'OWNER'", 
                     "'P_INTERSECT'", "'P_NORMALIZE'", "'PARAMID'", "'PARAMINFO'", 
                     "'PARENT'", "'PARTITION'", "<INVALID>", "'PARTITIONED'", 
                     "'PARTITIONNAMES'", "'PASS'", "'PASSING'", "'PATH_GENERATOR'", 
                     "'PATH_START'", "'PATH_SUMMARIZER'", "'PATTERN'", "'PERCENTILE'", 
                     "'PERCENTILE_CONT'", "'PERCENTILE_DISC'", "'PERIOD'", 
                     "'PIVOT'", "'PORTION'", "'POWER'", "'PRECEDES'", "'PRECEDING'", 
                     "'PREFIX'", "'PRINT'", "'PRIOR'", "'PROTECTED'", "'QUARTER_BEGIN'", 
                     "'QUARTER_END'", "'quarter_of_calendar'", "'quarter_of_year'", 
                     "'QuarterNumber_Of_Calendar'", "'QuarterNumber_Of_Year'", 
                     "'QUERY'", "'QUERY_BAND'", "'QUOTECHAR'", "'RANDOMIZED'", 
                     "'RANGE'", "<INVALID>", "'RAPIDFIRE'", "'RDIFF'", "'READ'", 
                     "'RECALC'", "'regexp_instr'", "'regexp_replace'", "'regexp_similar'", 
                     "'regexp_substr'", "'REPLACEMENT'", "'RESET'", "'RESPECT'", 
                     "'RESTRICTWORDS'", "'RETAIN'", "'RETURNED_SQLSTATE'", 
                     "'RETURNING'", "'REUSE'", "'ROOT'", "'ROTATELEFT'", 
                     "'ROTATERIGHT'", "'Round'", "'ROW_COUNT'", "'ROWIDGEN'", 
                     "'ROWIDGEN2'", "'RPAD'", "'RTRIM'", "'RU'", "'RULES'", 
                     "'RULESET'", "'SAMPLES'", "'SATURDAY'", "'SCHEMA'", 
                     "'SCRIPT'", "'SCRIPT_COMMAND'", "'SEARCHSPACE'", "'SEARCHUIFDBPATH'", 
                     "'SECURITY'", "'SEED'", "'SELF'", "'SEQ'", "'SEQUENCE'", 
                     "'SEQUENCED'", "'SERIALIZABLE'", "'SERVER'", "'SESSIONIZE'", 
                     "'SETBIT'", "'SetResourceRate'", "'SetSessionAccount'", 
                     "'SetSessionRate'", "'SHARE'", "'SHIFTLEFT'", "'SHIFTRIGHT'", 
                     "'SIGN'", "'SIZE'", "'SNAPPY_COMPRESS'", "'SNAPPY_DECOMPRESS'", 
                     "'SOURCE'", "'SPARSE'", "'SPECCHAR'", "'SPL'", "'SQLSTATE'", 
                     "'SR'", "'ST_GEOMETRY'", "'STAT'", "'STATIC'", "'STATS'", 
                     "'STATSUSAGE'", "'STORAGE'", "'STRIP'", "'STRTOK'", 
                     "'STYLE'", "'SUBBITSTR'", "'SUBCLASS_ORIGIN'", "'SUCCEEDS'", 
                     "'SUMMARYONLY'", "'SUNDAY'", "'SYMBOLS'", "'SYSTEM'", 
                     "'SYSTEM_TIME'", "'SYSTEMTEST'", "'TARGET'", "'TD_ARRAY2P'", 
                     "'TD_DATASET'", "'td_day_of_calendar'", "'td_day_of_month'", 
                     "'td_day_of_week'", "'td_day_of_year'", "'TD_GENERAL'", 
                     "'TD_GETTIMEBUCKET'", "'TD_INTERNAL'", "'TD_LZ_COMPRESS'", 
                     "'TD_LZ_DECOMPRESS'", "'td_month_of_calendar'", "'td_month_of_quarter'", 
                     "'td_month_of_year'", "'td_quarter_of_calendar'", "'td_quarter_of_year'", 
                     "'TD_TIME_BUCKET_NUMBER'", "'td_week_of_calendar'", 
                     "'td_week_of_month'", "'td_week_of_year'", "'td_weekday_of_month'", 
                     "'td_year_of_calendar'", "'TDWMEVENT'", "'TDWMEXCEPTION'", 
                     "'TDWMHISTORY'", "'TEMPORAL_DATE'", "'TEMPORAL_TIMESTAMP'", 
                     "'TEXT'", "'THRESHOLDPERCENT'", "'THROUGH'", "'THURSDAY'", 
                     "'TIES'", "'TIMECODE'", "'TIMECOLUMN'", "'TIMEOUT'", 
                     "'TIMESTAMPCOLUMN'", "'TO_BYTE'", "'TO_BYTES'", "'TO_CHAR'", 
                     "'TO_DATE'", "'TO_DSINTERVAL'", "'TO_NUMBER'", "'TO_TIMESTAMP'", 
                     "'TO_TIMESTAMP_TZ'", "'TO_YMINTERVAL'", "'TOTOKEN'", 
                     "'TPA'", "'TRANSACTION_ACTIVE'", "'TransUnicodeToUTF8'", 
                     "'TransUTF8ToUnicode'", "'TRUE'", "'Trunc'", "'TRUST_ONLY'", 
                     "'TTGRANULARITY'", "'TUESDAY'", "'UBJSON'", "'UCASE'", 
                     "'UDFSEARCHPATH'", "'UNBOUNDED'", "'UNCOMMITTED'", 
                     "'UNICODE'", "'UNKNOWN'", "'UNPIVOT'", "'USE'", "'USECOUNT'", 
                     "'UTILITYINFO'", "'VARRAY'", "'VERBOSE'", "'VERSION'", 
                     "'VERSIONING'", "'WARNING'", "'WEDNESDAY'", "'WEEK_BEGIN'", 
                     "'WEEK_END'", "'week_of_calendar'", "'week_of_month'", 
                     "'week_of_year'", "'weekday_of_month'", "'WeekNumber_Of_Calendar'", 
                     "'WeekNumber_Of_Month'", "'WeekNumber_Of_Quarter'", 
                     "'WeekNumber_Of_Year'", "'WHITESPACE'", "'WINDOWSIZE'", 
                     "'WITHIN'", "'WORKLOAD'", "'WRITE'", "'XML'", "'XMLAGG'", 
                     "'XMLATTRIBUTES'", "'XMLCOMMENT'", "'XMLCONCAT'", "'XMLDECLARATION'", 
                     "'XMLDOCUMENT'", "'XMLELEMENT'", "'XMLFOREST'", "'XMLNAMESPACES'", 
                     "'XMLPARSE'", "'XMLPI'", "'XMLQUERY'", "'XMLSCHEMA'", 
                     "'XMLSERIALIZE'", "'XMLTABLE'", "'XMLTEXT'", "'XMLTYPE'", 
                     "'XMLVALIDATE'", "'YEAR_BEGIN'", "'YEAR_END'", "'year_of_calendar'", 
                     "'YearNumber_Of_Calendar'", "'ZLIB'", "'BUCKET'", "'COMMITTED'", 
                     "'CREATEXML'", "'_LATIN'", "'_UNICODE'", "'_KANJISJIS'", 
                     "'_GRAPHIC'", "'CSV'", "'CSVLD'", "'DATASIZE'", "'DAYOFMONTH'", 
                     "'DAYS'", "'DEFINITION'", "'DELETED'", "'FAST'", "'LISTAGG'", 
                     "'PATH'", "'REGEXP_SPLIT_TO_TABLE'", "'REVERSE'", "'SAS'", 
                     "'SQLTABLE'", "'STRTOK_SPLIT_TO_TABLE'", "'SYSLIB'", 
                     "'SYSUDTLIB'", "'TD_SERVER_DB'", "'TD_SYSFNLIB'", "'TD_SYSXML'", 
                     "'TIMEDATEWZCONTROL'", "'TRUST'", "'TRYCAST'", "'UDT'", 
                     "'USAGE'", "'VARIANT'", "'WEEK'", "'WIDTH'", "'XMLPUBLISH'", 
                     "'XMLPUBLISH_STREAM'", "'XMLSPLIT'", "'LATIN_TO_UNICODE'", 
                     "'UNICODE_TO_LATIN'", "'LOCALE_TO_UNICODE'", "'UNICODE_TO_LOCALE'", 
                     "'ASBSON'", "'ASBSONTEXT'", "'COMBINE'", "'EXISTVALUE'", 
                     "'JSONEXTRACT'", "'JSONEXTRACTVALUE'", "'JSONEXTRACTLARGEVALUE'", 
                     "'KEYCOUNT'", "'METADATA'", "'STORAGE_SIZE'", "'CREATESCHEMABASEDXML'", 
                     "'CREATENONSCHEMABASEDXML'", "'EXISTSNODE'", "'ISCONTENT'", 
                     "'ISDOCUMENT'", "'ISSCHEMAVALID'", "'ISSCHEMAVALIDATED'", 
                     "'XMLEXTRACT'", "'XMLTRANSFORM'", "'PROC_ID'", "'LOCATION'", 
                     "'PAYLOAD'", "'TRUSTED'", "'PATHPATTERN'", "'MANIFEST'", 
                     "'ROWFORMAT'", "'STOREDAS'", "'HEADER'", "'STRIP_EXTERIOR_SPACES'", 
                     "'STRIP_ENCLOSING_CHAR'", "'RLS'", "'SINGLE'", "'MULTIPLE'", 
                     "'JSON_COMPRESS'", "'JSON_DECOMPRESS'", "'TS_COMPRESS'", 
                     "'TS_DECOMPRESS'", "'CONTIGUOUSMAPAMPS'", "'SPARSEMAPAMPS'", 
                     "'SPARSETABLEAMPS'", "'UNNEST'", "'CALCMATRIX'", "'PHRASE'", 
                     "'CALCTYPE'", "'OUTPUT'", "'NULL_HANDLING'", "'READ_NOS'", 
                     "'BUFFERSIZE'", "'RETURNTYPE'", "'SAMPLE_PERC'", "'FULLSCAN'", 
                     "'TD_UNPIVOT'", "'VALUE_COLUMNS'", "'UNPIVOT_COLUMN'", 
                     "'COLUMN_LIST'", "'COLUMN_ALIAS_LIST'", "'INCLUDE_NULLS'", 
                     "'WRITE_NOS'", "'NAMING'", "'MANIFESTFILE'", "'MANIFESTONLY'", 
                     "'OVERWRITE'", "'INCLUDE_ORDERING'", "'INCLUDE_HASHBY'", 
                     "'MAXOBJECTSIZE'", "'COMPRESSION'", "'ARRAY_TO_JSON'", 
                     "'BSON_CHECK'", "'GEOJSONFROMGEOM'", "'GEOMFROMGEOJSON'", 
                     "'JSON_CHECK'", "'JSONGETVALUE'", "'JSONMETADATA'", 
                     "'NVP2JSON'", "'TD_JSONSHRED'", "'JSON_KEYS'", "'JSON_TABLE'", 
                     "'DEPTH'", "'QUOTES'", "'ROWEXPR'", "'COLEXPR'", "'RETURNTYPES'", 
                     "'NOCASE'", "'TRUNCATE'", "'LINK'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "':'", 
                     "','", "'.'", "'@'", "'^'", "'?'", "'('", "')'", "'['", 
                     "']'", "'||'", "'\\u00A6\\u00A6'", "'*'", "'/'", "'+'", 
                     "'-'", "'**'", "'='", "'<>'", "'^='", "'<'", "'<='", 
                     "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "ABORT", "ABORTSESSION", "ABS", "ACCESS_LOCK", 
                      "ACCOUNT", "ACOS", "ACOSH", "ADD", "ADD_MONTHS", "ADMIN", 
                      "AFTER", "AGGREGATE", "ALL", "ALTER", "AMP", "AND", 
                      "ANSIDATE", "ANY", "ARGLPAREN", "AS", "ASC", "ASIN", 
                      "ASINH", "AT", "ATAN", "ATAN2", "ATANH", "ATOMIC", 
                      "AUTHORIZATION", "AVE", "AVERAGE", "AVG", "BEFORE", 
                      "BEGIN", "BETWEEN", "BIGINT", "BINARY", "BLOB", "BOTH", 
                      "BT", "BUT", "BY", "BYTE", "BYTEINT", "BYTES", "CALL", 
                      "CASE", "CASE_N", "CASESPECIFIC", "CAST", "CD", "CHAR", 
                      "CHAR_LENGTH", "CHAR2HEXINT", "CHARACTER", "CHARACTER_LENGTH", 
                      "CHARACTERS", "CHARS", "CHECK", "CHECKPOINT", "CLASS", 
                      "CLOB", "CLOSE", "CLUSTER", "CM", "COALESCE", "COLLATION", 
                      "COLLECT", "COLUMN", "COMMENT", "COMMIT", "COMPRESS", 
                      "CONNECT", "CONSTRAINT", "CONSTRUCTOR", "CONSUME", 
                      "CONTAINS", "CONTINUE", "CONVERT_TABLE_HEADER", "CORR", 
                      "COS", "COSH", "COUNT", "COVAR_POP", "COVAR_SAMP", 
                      "CREATE", "CROSS", "CS", "CSUM", "CT", "CTCONTROL", 
                      "CUBE", "CURRENT", "CURRENT_DATE", "CURRENT_ROLE", 
                      "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", 
                      "CURSOR", "CV", "CYCLE", "DATABASE", "DATABLOCKSIZE", 
                      "DATE", "DATEFORM", "DAY", "DEALLOCATE", "DEC", "DECIMAL", 
                      "DECLARE", "DEFAULT", "DEFERRED", "DEGREES", "DEL", 
                      "DELETE", "DESC", "DETERMINISTIC", "DIAGNOSTIC", "DICTIONARY", 
                      "DISABLED", "DISTINCT", "DO", "DOMAIN", "DOUBLE", 
                      "DROP", "DUAL", "DUMP", "DYNAMIC", "EACH", "ECHO", 
                      "ELSE", "ELSEIF", "ENABLED", "END", "EQ", "EQUALS", 
                      "ERROR", "ERRORFILES", "ERRORTABLES", "ESCAPE", "ET", 
                      "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", "EXP", 
                      "EXPAND", "EXPANDING", "EXPLAIN", "EXTERNAL", "EXTRACT", 
                      "FALLBACK", "FASTEXPORT", "FETCH", "FIRST", "FLOAT", 
                      "FLUSH", "FOR", "FOREIGN", "FORMAT", "FOUND", "FREESPACE", 
                      "FROM", "FULL", "FUNCTION", "FUNCTIONDESCRIPTOR", 
                      "GE", "GENERATED", "GET", "GIVE", "GRANT", "GRAPHIC", 
                      "GROUP", "GROUPING", "GT", "HANDLER", "HASH", "HASHAMP", 
                      "HASHBAKAMP", "HASHBUCKET", "HASHROW", "HAVING", "HELP", 
                      "HOUR", "ID2BIGINT", "IDENTITY", "IF", "IMMEDIATE", 
                      "IN", "INCONSISTENT", "INDEX", "INITIATE", "INNER", 
                      "INOUT", "INPUT", "INS", "INSERT", "INSTANCE", "INSTEAD", 
                      "INT", "INTEGER", "INTEGERDATE", "INTERSECT", "INTERVAL", 
                      "INTO", "IS", "ITERATE", "JAR", "JOIN", "JOURNAL", 
                      "KEY", "KURTOSIS", "LANGUAGE", "LARGE", "LE", "LEADING", 
                      "LEAVE", "LEFT", "LIKE", "LIMIT", "LN", "LOADING", 
                      "LOCAL", "LOCATOR", "LOCK", "LOCKING", "LOG", "LOGGING", 
                      "LOGON", "LONG", "LOOP", "LOWER", "LT", "MACRO", "MAP", 
                      "MAVG", "MAX", "MAXIMUM", "MCHARACTERS", "MDIFF", 
                      "MERGE", "METHOD", "MIN", "MINDEX", "MINIMUM", "MINUS", 
                      "MINUTE", "MLINREG", "MLOAD", "MOD", "MODE", "MODIFIES", 
                      "MODIFY", "MONITOR", "MONRESOURCE", "MONSESSION", 
                      "MONTH", "MSUBSTR", "MSUM", "MULTISET", "NAMED", "NATURAL", 
                      "NE", "NEW", "NEW_TABLE", "NEXT", "NO", "NONE", "NONTEMPORAL", 
                      "NORMALIZE", "NOT", "NOWAIT", "NULL", "NULLIF", "NULLIFZERO", 
                      "NUMBER", "NUMERIC", "OBJECT", "OBJECTS", "OCTET_LENGTH", 
                      "OF", "OFF", "OLD", "OLD_TABLE", "ON", "ONLY", "OPEN", 
                      "OPTION", "OR", "ORDER", "ORDERING", "OUT", "OUTER", 
                      "OVER", "OVERLAPS", "OVERRIDE", "PARAMETER", "PASSWORD", 
                      "PERCENT", "PERCENT_RANK", "PERM", "PERMANENT", "POSITION", 
                      "PRECISION", "PREPARE", "PRESERVE", "PRIMARY", "PRIVILEGES", 
                      "PROCEDURE", "PROFILE", "PROTECTION", "PUBLIC", "QUALIFIED", 
                      "QUALIFY", "QUANTILE", "QUEUE", "RADIANS", "RANDOM", 
                      "RANGE_N", "RANK", "READS", "REAL", "RECURSIVE", "REFERENCES", 
                      "REFERENCING", "REGR_AVGX", "REGR_AVGY", "REGR_COUNT", 
                      "REGR_INTERCEPT", "REGR_R2", "REGR_SLOPE", "REGR_SXX", 
                      "REGR_SXY", "REGR_SYY", "RELATIVE", "RELEASE", "RENAME", 
                      "REPEAT", "REPLACE", "REPLCONTROL", "REPLICATION", 
                      "REQUEST", "RESIGNAL", "RESTART", "RESTORE", "RESULT", 
                      "RESUME", "RET", "RETRIEVE", "RETURN", "RETURNS", 
                      "REVALIDATE", "REVOKE", "RIGHT", "RIGHTS", "ROLE", 
                      "ROLLBACK", "ROLLFORWARD", "ROLLUP", "ROW", "ROW_NUMBER", 
                      "ROWID", "ROWS", "SAMPLE", "SAMPLEID", "SCROLL", "SECOND", 
                      "SEL", "SELECT", "SESSION", "SET", "SETRESRATE", "SETS", 
                      "SETSESSRATE", "SHOW", "SIGNAL", "SIN", "SINH", "SKEW", 
                      "SMALLINT", "SOME", "SOUNDEX", "SPECIFIC", "SPOOL", 
                      "SQL", "SQLEXCEPTION", "SQLTEXT", "SQLWARNING", "SQRT", 
                      "SS", "START", "STARTUP", "STATEMENT", "STATISTICS", 
                      "STDDEV_POP", "STDDEV_SAMP", "STEPINFO", "STRING_CS", 
                      "SUBSCRIBER", "SUBSTR", "SUBSTRING", "SUM", "SUMMARY", 
                      "SUSPEND", "TABLE", "TAN", "TANH", "TBL_CS", "TD_ANYTYPE", 
                      "TD_AUTHID", "TD_HOST", "TD_ROWLOADID", "TD_ROWREVISION", 
                      "TD_ROWSIZE", "TD_VALIST", "TEMPORARY", "TERMINATE", 
                      "THEN", "THRESHOLD", "TIME", "TIMESTAMP", "TIMEZONE_HOUR", 
                      "TIMEZONE_MINUTE", "TITLE", "TO", "TOP", "TRACE", 
                      "TRAILING", "TRANSACTION", "TRANSACTIONTIME", "TRANSFORM", 
                      "TRANSLATE", "TRANSLATE_CHK", "TRIGGER", "TRIM", "TYPE", 
                      "UC", "UDTCASTAS", "UDTCASTLPAREN", "UDTMETHOD", "UDTTYPE", 
                      "UDTUSAGE", "UESCAPE", "UNDEFINED", "UNDO", "UNION", 
                      "UNIQUE", "UNTIL", "UNTIL_CHANGED", "UNTIL_CLOSED", 
                      "UPD", "UPDATE", "UPPER", "UPPERCASE", "USER", "USING", 
                      "VALIDTIME", "VALUE", "VALUES", "VAR_POP", "VAR_SAMP", 
                      "VARBYTE", "VARCHAR", "VARGRAPHIC", "VARIANT_TYPE", 
                      "VARYING", "VIEW", "VOLATILE", "WHEN", "WHERE", "WHILE", 
                      "WIDTH_BUCKET", "WITH", "WITHOUT", "WORK", "XMLPLAN", 
                      "YEAR", "ZEROIFNULL", "ZONE", "ALIAS", "DESCRIPTOR", 
                      "GO", "GOTO", "INDICATOR", "PRIVATE", "WAIT", "ABORTSESSIONS", 
                      "ABSENT", "ACCESS", "ACCORDING", "ACCUMULATE", "AG", 
                      "AGGGEOMINTERSECTION", "AGGGEOMUNION", "ALLDBQL", 
                      "ALLOCATE", "ALLOCATION", "ALLOW", "ALLPARAMS", "ALLTDWM", 
                      "ALWAYS", "AMPCOUNT", "ANALYSIS", "ANCHOR", "ANCHOR_HOUR", 
                      "ANCHOR_MILLISECOND", "ANCHOR_MINUTE", "ANCHOR_SECOND", 
                      "APPLNAME", "ARCHIVE", "ARRAY", "ARRAY_ADD", "ARRAY_AGG", 
                      "ARRAY_AVG", "ARRAY_COMPARE", "ARRAY_CONCAT", "ARRAY_COUNT_DISTINCT", 
                      "ARRAY_DIV", "ARRAY_EQ", "ARRAY_GE", "ARRAY_GET", 
                      "ARRAY_GT", "ARRAY_LE", "ARRAY_LT", "ARRAY_MAX", "ARRAY_MIN", 
                      "ARRAY_MOD", "ARRAY_MUL", "ARRAY_NE", "ARRAY_SUB", 
                      "ARRAY_SUM", "ARRAY_UPDATE", "ARRAY_UPDATE_STRIDE", 
                      "ASCII", "ASSIGNMENT", "ATTR", "ATTRIBUTE", "ATTRIBUTES", 
                      "ATTRIBUTION", "ATTRS", "AUTH", "AUTO", "AUTOTEMP", 
                      "AVRO", "BIT_LENGTH", "BITAND", "BITNOT", "BITOR", 
                      "BITXOR", "BLOCKCOMPRESSION", "BLOCKCOMPRESSIONALGORITHM", 
                      "BLOCKCOMPRESSIONLEVEL", "BOM", "BOTTOM", "BSON", 
                      "C", "CALENDAR", "CALLED", "CALLER", "CAMSET", "CAMSET_L", 
                      "CAPTURE", "CARDINALITY", "CEIL", "CEILING", "CHANGERATE", 
                      "CHARACTERISTICS", "CHARSET", "CHARSET_COLL", "CHECKSUM", 
                      "CHR", "CLASS_ORIGIN", "CLICKLAG", "CLIENT", "CNT", 
                      "COLOCATE", "COLUMNMETA", "COLUMNS", "COLUMNSPERINDEX", 
                      "COLUMNSPERJOININDEX", "COMMAND_FUNCTION", "COMMAND_FUNCTION_CODE", 
                      "COMPARISON", "COMPILE", "CONCAT", "CONCURRENT", "CONDITION", 
                      "CONDITION_IDENTIFIER", "CONDITION_NUMBER", "CONTAINED", 
                      "CONTAINEDTOKEN", "CONTENT", "CONTIGUOUS", "COST", 
                      "COSTS", "COUNTSET", "CPP", "CPUTIME", "CPUTIMENORM", 
                      "CREATEDATASET", "CREATOR", "CUME_DIST", "CURDATE", 
                      "CURTIME", "DATA", "DATASET", "DAY_OF_CALENDAR", "DAY_OF_MONTH", 
                      "DAY_OF_WEEK", "DAY_OF_YEAR", "DAYNUMBER_OF_CALENDAR", 
                      "DAYNUMBER_OF_MONTH", "DAYNUMBER_OF_WEEK", "DAYNUMBER_OF_YEAR", 
                      "DAYOCCURRENCE_OF_MONTH", "DBA", "DBC", "DEBUG", "DECAMSET", 
                      "DECAMSET_L", "DECODE", "DECOMPRESS", "DEFINER", "DELIMITER", 
                      "DELTA_T", "DEMOGRAPHICS", "DENIALS", "DENSE", "DENSE_RANK", 
                      "DESCRIBE", "DETAILED", "DIAGNOSTICS", "DIGITS", "DIMENSION", 
                      "DOCUMENT", "DOT", "DOWN", "DR", "DUPCOUNT", "DUPCOUNTCUM", 
                      "EBCDIC", "EDITDISTANCE", "ELAPSEDSEC", "ELAPSEDTIME", 
                      "ELEMENT", "ELZS_H", "EMITNULL", "EMPTY", "EMPTY_BLOB", 
                      "EMPTY_CLOB", "ENCODE", "ENCODING", "ENCRYPT", "ERRORS", 
                      "ERRORTBL", "EVENTCOLUMN", "EXCEPTION", "EXCL", "EXCLUDE", 
                      "EXCLUDING", "EXCLUSIVE", "EXPIRE", "EXPORT", "EXPORTWIDTH", 
                      "FALSE", "FEATUREINFO", "FILE", "FILL", "FILTER", 
                      "FINAL", "FIRST_NOTNULL", "FIRST_VALUE", "FLOOR", 
                      "FOLLOWING", "FOREIGNFUNCTION", "FORTOKEN", "FRIDAY", 
                      "FROM_BYTES", "FUNCTIONPARAMETER", "G", "GETBIT", 
                      "GETPSFVERSION", "GETQUERYBAND", "GETQUERYBANDVALUE", 
                      "GETTIMEZONEDISPLACEMENT", "GLOBAL", "GLOP", "GREATEST", 
                      "HIGH", "HOST", "IDENTIFYDATABASE", "IDENTIFYSESSION", 
                      "IDENTIFYTABLE", "IDENTIFYUSER", "IFP", "IGNORE", 
                      "IMMEDIATELY", "IMPORT", "INCLUDE", "INCLUDING", "INCREMENT", 
                      "INCREMENTAL", "INDENT", "INDEXESPERTABLE", "INDEXMAINTMODE", 
                      "INIT", "INITCAP", "INLINE", "INSTANTIABLE", "INSTR", 
                      "INTERNAL", "INVOKER", "IOCOUNT", "IPARTITION", "ISOLATED", 
                      "ISOLATION", "JAVA", "JIS_COLL", "JSON", "JSON_AGG", 
                      "JSON_COMPOSE", "K", "KANJI1", "KANJISJIS", "KBYTE", 
                      "KBYTES", "KEEP", "KILOBYTES", "LAG", "LAST", "LAST_DAY", 
                      "LAST_NOTNULL", "LAST_VALUE", "LATIN", "LDIFF", "LEAD", 
                      "LEAST", "LENGTH", "LEVEL", "LIST", "LOAD", "LOCATE", 
                      "LOCKEDUSEREXPIRE", "LOW", "LPAD", "LTRIM", "LZCOMP", 
                      "LZCOMP_L", "LZDECOMP", "LZDECOMP_L", "M", "MAD", 
                      "MANUAL", "MAPPING", "MATCHED", "MAX_CHOOSE", "MAXCHAR", 
                      "MAXINTERVALS", "MAXLOGONATTEMPTS", "MAXVALUE", "MAXVALUELENGTH", 
                      "MEDIAN", "MEDIUM", "MEETS", "MEMBER", "MERGEBLOCKRATIO", 
                      "MESSAGE_LENGTH", "MESSAGE_TEXT", "MIN_CHOOSE", "MINCHAR", 
                      "MINVALUE", "MODIFIED", "MONDAY", "MONITORQUERYBAND", 
                      "MONITORSESSIONRATE", "MONITORVERSION", "MONTH_BEGIN", 
                      "MONTH_END", "MONTH_OF_CALENDAR", "MONTH_OF_QUARTER", 
                      "MONTH_OF_YEAR", "MONTHNUMBER_OF_CALENDAR", "MONTHNUMBER_OF_QUARTER", 
                      "MONTHNUMBER_OF_YEAR", "MONTHS_BETWEEN", "MORE_", 
                      "MULTINATIONAL", "NAME", "NAMESPACE", "NEVER", "NEXT_DAY", 
                      "NGRAM", "NIL", "NODDLTEXT", "NODE", "NONOPTCOST", 
                      "NONOPTINIT", "NONSEQUENCED", "NORIGHT", "NOSEXTRACTVARFROMPATH", 
                      "NOTATION", "NOW", "NPATH", "NTH", "NULLS", "NUMFPFNS", 
                      "NUMTODSINTERVAL", "NUMTOYMINTERVAL", "NVL", "NVL2", 
                      "NVP", "OA", "OADD_MONTHS", "OCOUNT", "ODELETE", "OEXISTS", 
                      "OEXTEND", "OFIRST", "OLAST", "OLD_NEW_TABLE", "OLIMIT", 
                      "ONEXT", "ONLINE", "OPRIOR", "OPTIONS", "ORDERBYVALUES", 
                      "ORDERED_ANALYTIC", "ORDINALITY", "OREPLACE", "OTRANSLATE", 
                      "OTRIM", "OVERLAYS", "OWNER", "P_INTERSECT", "P_NORMALIZE", 
                      "PARAMID", "PARAMINFO", "PARENT", "PARTITION", "PARTITION_L", 
                      "PARTITIONED", "PARTITIONNAMES", "PASS", "PASSING", 
                      "PATH_GENERATOR", "PATH_START", "PATH_SUMMARIZER", 
                      "PATTERN", "PERCENTILE", "PERCENTILE_CONT", "PERCENTILE_DISC", 
                      "PERIOD", "PIVOT", "PORTION", "POWER", "PRECEDES", 
                      "PRECEDING", "PREFIX", "PRINT", "PRIOR", "PROTECTED", 
                      "QUARTER_BEGIN", "QUARTER_END", "QUARTER_OF_CALENDAR", 
                      "QUARTER_OF_YEAR", "QUARTERNUMBER_OF_CALENDAR", "QUARTERNUMBER_OF_YEAR", 
                      "QUERY", "QUERY_BAND", "QUOTECHAR", "RANDOMIZED", 
                      "RANGE", "RANGE_L", "RAPIDFIRE", "RDIFF", "READ", 
                      "RECALC", "REGEXP_INSTR", "REGEXP_REPLACE", "REGEXP_SIMILAR", 
                      "REGEXP_SUBSTR", "REPLACEMENT", "RESET", "RESPECT", 
                      "RESTRICTWORDS", "RETAIN", "RETURNED_SQLSTATE", "RETURNING", 
                      "REUSE", "ROOT", "ROTATELEFT", "ROTATERIGHT", "ROUND", 
                      "ROW_COUNT", "ROWIDGEN", "ROWIDGEN2", "RPAD", "RTRIM", 
                      "RU", "RULES", "RULESET", "SAMPLES", "SATURDAY", "SCHEMA", 
                      "SCRIPT", "SCRIPT_COMMAND", "SEARCHSPACE", "SEARCHUIFDBPATH", 
                      "SECURITY", "SEED", "SELF", "SEQ", "SEQUENCE", "SEQUENCED", 
                      "SERIALIZABLE", "SERVER", "SESSIONIZE", "SETBIT", 
                      "SETRESOURCERATE", "SETSESSIONACCOUNT", "SETSESSIONRATE", 
                      "SHARE", "SHIFTLEFT", "SHIFTRIGHT", "SIGN", "SIZE", 
                      "SNAPPY_COMPRESS", "SNAPPY_DECOMPRESS", "SOURCE", 
                      "SPARSE", "SPECCHAR", "SPL", "SQLSTATE", "SR", "ST_GEOMETRY", 
                      "STAT", "STATIC", "STATS", "STATSUSAGE", "STORAGE", 
                      "STRIP", "STRTOK", "STYLE", "SUBBITSTR", "SUBCLASS_ORIGIN", 
                      "SUCCEEDS", "SUMMARYONLY", "SUNDAY", "SYMBOLS", "SYSTEM", 
                      "SYSTEM_TIME", "SYSTEMTEST", "TARGET", "TD_ARRAY2P", 
                      "TD_DATASET", "TD_DAY_OF_CALENDAR", "TD_DAY_OF_MONTH", 
                      "TD_DAY_OF_WEEK", "TD_DAY_OF_YEAR", "TD_GENERAL", 
                      "TD_GETTIMEBUCKET", "TD_INTERNAL", "TD_LZ_COMPRESS", 
                      "TD_LZ_DECOMPRESS", "TD_MONTH_OF_CALENDAR", "TD_MONTH_OF_QUARTER", 
                      "TD_MONTH_OF_YEAR", "TD_QUARTER_OF_CALENDAR", "TD_QUARTER_OF_YEAR", 
                      "TD_TIME_BUCKET_NUMBER", "TD_WEEK_OF_CALENDAR", "TD_WEEK_OF_MONTH", 
                      "TD_WEEK_OF_YEAR", "TD_WEEKDAY_OF_MONTH", "TD_YEAR_OF_CALENDAR", 
                      "TDWMEVENT", "TDWMEXCEPTION", "TDWMHISTORY", "TEMPORAL_DATE", 
                      "TEMPORAL_TIMESTAMP", "TEXT", "THRESHOLDPERCENT", 
                      "THROUGH", "THURSDAY", "TIES", "TIMECODE", "TIMECOLUMN", 
                      "TIMEOUT", "TIMESTAMPCOLUMN", "TO_BYTE", "TO_BYTES", 
                      "TO_CHAR", "TO_DATE", "TO_DSINTERVAL", "TO_NUMBER", 
                      "TO_TIMESTAMP", "TO_TIMESTAMP_TZ", "TO_YMINTERVAL", 
                      "TOTOKEN", "TPA", "TRANSACTION_ACTIVE", "TRANSUNICODETOUTF8", 
                      "TRANSUTF8TOUNICODE", "TRUE", "TRUNC", "TRUST_ONLY", 
                      "TTGRANULARITY", "TUESDAY", "UBJSON", "UCASE", "UDFSEARCHPATH", 
                      "UNBOUNDED", "UNCOMMITTED", "UNICODE", "UNKNOWN", 
                      "UNPIVOT", "USE", "USECOUNT", "UTILITYINFO", "VARRAY", 
                      "VERBOSE", "VERSION", "VERSIONING", "WARNING", "WEDNESDAY", 
                      "WEEK_BEGIN", "WEEK_END", "WEEK_OF_CALENDAR", "WEEK_OF_MONTH", 
                      "WEEK_OF_YEAR", "WEEKDAY_OF_MONTH", "WEEKNUMBER_OF_CALENDAR", 
                      "WEEKNUMBER_OF_MONTH", "WEEKNUMBER_OF_QUARTER", "WEEKNUMBER_OF_YEAR", 
                      "WHITESPACE", "WINDOWSIZE", "WITHIN", "WORKLOAD", 
                      "WRITE", "XML", "XMLAGG", "XMLATTRIBUTES", "XMLCOMMENT", 
                      "XMLCONCAT", "XMLDECLARATION", "XMLDOCUMENT", "XMLELEMENT", 
                      "XMLFOREST", "XMLNAMESPACES", "XMLPARSE", "XMLPI", 
                      "XMLQUERY", "XMLSCHEMA", "XMLSERIALIZE", "XMLTABLE", 
                      "XMLTEXT", "XMLTYPE", "XMLVALIDATE", "YEAR_BEGIN", 
                      "YEAR_END", "YEAR_OF_CALENDAR", "YEARNUMBER_OF_CALENDAR", 
                      "ZLIB", "BUCKET", "COMMITTED", "CREATEXML", "CS_LATIN", 
                      "CS_UNICODE", "CS_KANJISJIS", "CS_GRAPHIC", "CSV", 
                      "CSVLD", "DATASIZE", "DAYOFMONTH", "DAYS", "DEFINITION", 
                      "DELETED", "FAST", "LISTAGG", "PATH", "REGEXP_SPLIT_TO_TABLE", 
                      "REVERSE", "SAS", "SQLTABLE", "STRTOK_SPLIT_TO_TABLE", 
                      "SYSLIB", "SYSUDTLIB", "TD_SERVER_DB", "TD_SYSFNLIB", 
                      "TD_SYSXML", "TIMEDATEWZCONTROL", "TRUST", "TRYCAST", 
                      "UDT", "USAGE", "VARIANT", "WEEK", "WIDTH", "XMLPUBLISH", 
                      "XMLPUBLISH_STREAM", "XMLSPLIT", "LATIN_TO_UNICODE", 
                      "UNICODE_TO_LATIN", "LOCALE_TO_UNICODE", "UNICODE_TO_LOCALE", 
                      "ASBSON", "ASBSONTEXT", "COMBINE", "EXISTVALUE", "JSONEXTRACT", 
                      "JSONEXTRACTVALUE", "JSONEXTRACTLARGEVALUE", "KEYCOUNT", 
                      "METADATA", "STORAGE_SIZE", "CREATESCHEMABASEDXML", 
                      "CREATENONSCHEMABASEDXML", "EXISTSNODE", "ISCONTENT", 
                      "ISDOCUMENT", "ISSCHEMAVALID", "ISSCHEMAVALIDATED", 
                      "XMLEXTRACT", "XMLTRANSFORM", "PROC_ID", "LOCATION", 
                      "PAYLOAD", "TRUSTED", "PATHPATTERN", "MANIFEST", "ROWFORMAT", 
                      "STOREDAS", "HEADER", "STRIP_EXTERIOR_SPACES", "STRIP_ENCLOSING_CHAR", 
                      "RLS", "SINGLE", "MULTIPLE", "JSON_COMPRESS", "JSON_DECOMPRESS", 
                      "TS_COMPRESS", "TS_DECOMPRESS", "CONTIGUOUSMAPAMPS", 
                      "SPARSEMAPAMPS", "SPARSETABLEAMPS", "UNNEST", "CALCMATRIX", 
                      "PHRASE", "CALCTYPE", "OUTPUT", "NULL_HANDLING", "READ_NOS", 
                      "BUFFERSIZE", "RETURNTYPE", "SAMPLE_PERC", "FULLSCAN", 
                      "TD_UNPIVOT", "VALUE_COLUMNS", "UNPIVOT_COLUMN", "COLUMN_LIST", 
                      "COLUMN_ALIAS_LIST", "INCLUDE_NULLS", "WRITE_NOS", 
                      "NAMING", "MANIFESTFILE", "MANIFESTONLY", "OVERWRITE", 
                      "INCLUDE_ORDERING", "INCLUDE_HASHBY", "MAXOBJECTSIZE", 
                      "COMPRESSION", "ARRAY_TO_JSON", "BSON_CHECK", "GEOJSONFROMGEOM", 
                      "GEOMFROMGEOJSON", "JSON_CHECK", "JSONGETVALUE", "JSONMETADATA", 
                      "NVP2JSON", "TD_JSONSHRED", "JSON_KEYS", "JSON_TABLE", 
                      "DEPTH", "QUOTES", "ROWEXPR", "COLEXPR", "RETURNTYPES", 
                      "NOCASE", "TRUNCATE", "LINK", "OBJECT_NAME", "UNSIGNED_INTEGER", 
                      "HEX_BYTE_LITERAL", "HEX_INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "DATE_STRING", "TIME_STRING", "TIMESTAMP_STRING", 
                      "PERIOD_STRING", "UNICODE_STRING_LEADING", "CHAR_STRING", 
                      "HEX_STRING", "PASSWORD_STRING", "SEMICOLON", "COLON", 
                      "COMMA", "DOT_", "AT_SIGN", "CARET", "QUESTION_MARK", 
                      "OPEN_PAR", "CLOSE_PAR", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", 
                      "CONCATENATE", "BROKEN_CONCATENATE", "MUL_SIGN", "DIV_SIGN", 
                      "PLUS_SIGN", "MINUS_SIGN", "EXPONENTIATION", "EQUALS_SIGN", 
                      "NOT_EQUALS_SIGN", "NOT_EQUALS_SIGN_TD", "LT_SIGN", 
                      "LE_SIGN", "GT_SIGN", "GE_SIGN", "SINGLE_LINE_COMMENT", 
                      "MULTI_LINE_COMMENT", "WS" ]

    RULE_column_name = 0
    RULE_unqualified_column_name = 1
    RULE_unqualified_name = 2
    RULE_object_name = 3
    RULE_table_name = 4
    RULE_procedure_name = 5
    RULE_function_name = 6
    RULE_macro_name = 7
    RULE_database_name = 8
    RULE_user_name = 9
    RULE_role_name = 10
    RULE_profile_name = 11
    RULE_alias_name = 12
    RULE_variable_name = 13
    RULE_parameter_name = 14
    RULE_label_name = 15
    RULE_condition_name = 16
    RULE_cursor_name = 17
    RULE_statement_name = 18
    RULE_statistics_name = 19
    RULE_udt_name = 20
    RULE_attribute_name = 21
    RULE_method_name = 22
    RULE_anchor_name = 23
    RULE_nonreserved_word = 24

    ruleNames =  [ "column_name", "unqualified_column_name", "unqualified_name", 
                   "object_name", "table_name", "procedure_name", "function_name", 
                   "macro_name", "database_name", "user_name", "role_name", 
                   "profile_name", "alias_name", "variable_name", "parameter_name", 
                   "label_name", "condition_name", "cursor_name", "statement_name", 
                   "statistics_name", "udt_name", "attribute_name", "method_name", 
                   "anchor_name", "nonreserved_word" ]

    EOF = Token.EOF
    ABORT=1
    ABORTSESSION=2
    ABS=3
    ACCESS_LOCK=4
    ACCOUNT=5
    ACOS=6
    ACOSH=7
    ADD=8
    ADD_MONTHS=9
    ADMIN=10
    AFTER=11
    AGGREGATE=12
    ALL=13
    ALTER=14
    AMP=15
    AND=16
    ANSIDATE=17
    ANY=18
    ARGLPAREN=19
    AS=20
    ASC=21
    ASIN=22
    ASINH=23
    AT=24
    ATAN=25
    ATAN2=26
    ATANH=27
    ATOMIC=28
    AUTHORIZATION=29
    AVE=30
    AVERAGE=31
    AVG=32
    BEFORE=33
    BEGIN=34
    BETWEEN=35
    BIGINT=36
    BINARY=37
    BLOB=38
    BOTH=39
    BT=40
    BUT=41
    BY=42
    BYTE=43
    BYTEINT=44
    BYTES=45
    CALL=46
    CASE=47
    CASE_N=48
    CASESPECIFIC=49
    CAST=50
    CD=51
    CHAR=52
    CHAR_LENGTH=53
    CHAR2HEXINT=54
    CHARACTER=55
    CHARACTER_LENGTH=56
    CHARACTERS=57
    CHARS=58
    CHECK=59
    CHECKPOINT=60
    CLASS=61
    CLOB=62
    CLOSE=63
    CLUSTER=64
    CM=65
    COALESCE=66
    COLLATION=67
    COLLECT=68
    COLUMN=69
    COMMENT=70
    COMMIT=71
    COMPRESS=72
    CONNECT=73
    CONSTRAINT=74
    CONSTRUCTOR=75
    CONSUME=76
    CONTAINS=77
    CONTINUE=78
    CONVERT_TABLE_HEADER=79
    CORR=80
    COS=81
    COSH=82
    COUNT=83
    COVAR_POP=84
    COVAR_SAMP=85
    CREATE=86
    CROSS=87
    CS=88
    CSUM=89
    CT=90
    CTCONTROL=91
    CUBE=92
    CURRENT=93
    CURRENT_DATE=94
    CURRENT_ROLE=95
    CURRENT_TIME=96
    CURRENT_TIMESTAMP=97
    CURRENT_USER=98
    CURSOR=99
    CV=100
    CYCLE=101
    DATABASE=102
    DATABLOCKSIZE=103
    DATE=104
    DATEFORM=105
    DAY=106
    DEALLOCATE=107
    DEC=108
    DECIMAL=109
    DECLARE=110
    DEFAULT=111
    DEFERRED=112
    DEGREES=113
    DEL=114
    DELETE=115
    DESC=116
    DETERMINISTIC=117
    DIAGNOSTIC=118
    DICTIONARY=119
    DISABLED=120
    DISTINCT=121
    DO=122
    DOMAIN=123
    DOUBLE=124
    DROP=125
    DUAL=126
    DUMP=127
    DYNAMIC=128
    EACH=129
    ECHO=130
    ELSE=131
    ELSEIF=132
    ENABLED=133
    END=134
    EQ=135
    EQUALS=136
    ERROR=137
    ERRORFILES=138
    ERRORTABLES=139
    ESCAPE=140
    ET=141
    EXCEPT=142
    EXEC=143
    EXECUTE=144
    EXISTS=145
    EXIT=146
    EXP=147
    EXPAND=148
    EXPANDING=149
    EXPLAIN=150
    EXTERNAL=151
    EXTRACT=152
    FALLBACK=153
    FASTEXPORT=154
    FETCH=155
    FIRST=156
    FLOAT=157
    FLUSH=158
    FOR=159
    FOREIGN=160
    FORMAT=161
    FOUND=162
    FREESPACE=163
    FROM=164
    FULL=165
    FUNCTION=166
    FUNCTIONDESCRIPTOR=167
    GE=168
    GENERATED=169
    GET=170
    GIVE=171
    GRANT=172
    GRAPHIC=173
    GROUP=174
    GROUPING=175
    GT=176
    HANDLER=177
    HASH=178
    HASHAMP=179
    HASHBAKAMP=180
    HASHBUCKET=181
    HASHROW=182
    HAVING=183
    HELP=184
    HOUR=185
    ID2BIGINT=186
    IDENTITY=187
    IF=188
    IMMEDIATE=189
    IN=190
    INCONSISTENT=191
    INDEX=192
    INITIATE=193
    INNER=194
    INOUT=195
    INPUT=196
    INS=197
    INSERT=198
    INSTANCE=199
    INSTEAD=200
    INT=201
    INTEGER=202
    INTEGERDATE=203
    INTERSECT=204
    INTERVAL=205
    INTO=206
    IS=207
    ITERATE=208
    JAR=209
    JOIN=210
    JOURNAL=211
    KEY=212
    KURTOSIS=213
    LANGUAGE=214
    LARGE=215
    LE=216
    LEADING=217
    LEAVE=218
    LEFT=219
    LIKE=220
    LIMIT=221
    LN=222
    LOADING=223
    LOCAL=224
    LOCATOR=225
    LOCK=226
    LOCKING=227
    LOG=228
    LOGGING=229
    LOGON=230
    LONG=231
    LOOP=232
    LOWER=233
    LT=234
    MACRO=235
    MAP=236
    MAVG=237
    MAX=238
    MAXIMUM=239
    MCHARACTERS=240
    MDIFF=241
    MERGE=242
    METHOD=243
    MIN=244
    MINDEX=245
    MINIMUM=246
    MINUS=247
    MINUTE=248
    MLINREG=249
    MLOAD=250
    MOD=251
    MODE=252
    MODIFIES=253
    MODIFY=254
    MONITOR=255
    MONRESOURCE=256
    MONSESSION=257
    MONTH=258
    MSUBSTR=259
    MSUM=260
    MULTISET=261
    NAMED=262
    NATURAL=263
    NE=264
    NEW=265
    NEW_TABLE=266
    NEXT=267
    NO=268
    NONE=269
    NONTEMPORAL=270
    NORMALIZE=271
    NOT=272
    NOWAIT=273
    NULL=274
    NULLIF=275
    NULLIFZERO=276
    NUMBER=277
    NUMERIC=278
    OBJECT=279
    OBJECTS=280
    OCTET_LENGTH=281
    OF=282
    OFF=283
    OLD=284
    OLD_TABLE=285
    ON=286
    ONLY=287
    OPEN=288
    OPTION=289
    OR=290
    ORDER=291
    ORDERING=292
    OUT=293
    OUTER=294
    OVER=295
    OVERLAPS=296
    OVERRIDE=297
    PARAMETER=298
    PASSWORD=299
    PERCENT=300
    PERCENT_RANK=301
    PERM=302
    PERMANENT=303
    POSITION=304
    PRECISION=305
    PREPARE=306
    PRESERVE=307
    PRIMARY=308
    PRIVILEGES=309
    PROCEDURE=310
    PROFILE=311
    PROTECTION=312
    PUBLIC=313
    QUALIFIED=314
    QUALIFY=315
    QUANTILE=316
    QUEUE=317
    RADIANS=318
    RANDOM=319
    RANGE_N=320
    RANK=321
    READS=322
    REAL=323
    RECURSIVE=324
    REFERENCES=325
    REFERENCING=326
    REGR_AVGX=327
    REGR_AVGY=328
    REGR_COUNT=329
    REGR_INTERCEPT=330
    REGR_R2=331
    REGR_SLOPE=332
    REGR_SXX=333
    REGR_SXY=334
    REGR_SYY=335
    RELATIVE=336
    RELEASE=337
    RENAME=338
    REPEAT=339
    REPLACE=340
    REPLCONTROL=341
    REPLICATION=342
    REQUEST=343
    RESIGNAL=344
    RESTART=345
    RESTORE=346
    RESULT=347
    RESUME=348
    RET=349
    RETRIEVE=350
    RETURN=351
    RETURNS=352
    REVALIDATE=353
    REVOKE=354
    RIGHT=355
    RIGHTS=356
    ROLE=357
    ROLLBACK=358
    ROLLFORWARD=359
    ROLLUP=360
    ROW=361
    ROW_NUMBER=362
    ROWID=363
    ROWS=364
    SAMPLE=365
    SAMPLEID=366
    SCROLL=367
    SECOND=368
    SEL=369
    SELECT=370
    SESSION=371
    SET=372
    SETRESRATE=373
    SETS=374
    SETSESSRATE=375
    SHOW=376
    SIGNAL=377
    SIN=378
    SINH=379
    SKEW=380
    SMALLINT=381
    SOME=382
    SOUNDEX=383
    SPECIFIC=384
    SPOOL=385
    SQL=386
    SQLEXCEPTION=387
    SQLTEXT=388
    SQLWARNING=389
    SQRT=390
    SS=391
    START=392
    STARTUP=393
    STATEMENT=394
    STATISTICS=395
    STDDEV_POP=396
    STDDEV_SAMP=397
    STEPINFO=398
    STRING_CS=399
    SUBSCRIBER=400
    SUBSTR=401
    SUBSTRING=402
    SUM=403
    SUMMARY=404
    SUSPEND=405
    TABLE=406
    TAN=407
    TANH=408
    TBL_CS=409
    TD_ANYTYPE=410
    TD_AUTHID=411
    TD_HOST=412
    TD_ROWLOADID=413
    TD_ROWREVISION=414
    TD_ROWSIZE=415
    TD_VALIST=416
    TEMPORARY=417
    TERMINATE=418
    THEN=419
    THRESHOLD=420
    TIME=421
    TIMESTAMP=422
    TIMEZONE_HOUR=423
    TIMEZONE_MINUTE=424
    TITLE=425
    TO=426
    TOP=427
    TRACE=428
    TRAILING=429
    TRANSACTION=430
    TRANSACTIONTIME=431
    TRANSFORM=432
    TRANSLATE=433
    TRANSLATE_CHK=434
    TRIGGER=435
    TRIM=436
    TYPE=437
    UC=438
    UDTCASTAS=439
    UDTCASTLPAREN=440
    UDTMETHOD=441
    UDTTYPE=442
    UDTUSAGE=443
    UESCAPE=444
    UNDEFINED=445
    UNDO=446
    UNION=447
    UNIQUE=448
    UNTIL=449
    UNTIL_CHANGED=450
    UNTIL_CLOSED=451
    UPD=452
    UPDATE=453
    UPPER=454
    UPPERCASE=455
    USER=456
    USING=457
    VALIDTIME=458
    VALUE=459
    VALUES=460
    VAR_POP=461
    VAR_SAMP=462
    VARBYTE=463
    VARCHAR=464
    VARGRAPHIC=465
    VARIANT_TYPE=466
    VARYING=467
    VIEW=468
    VOLATILE=469
    WHEN=470
    WHERE=471
    WHILE=472
    WIDTH_BUCKET=473
    WITH=474
    WITHOUT=475
    WORK=476
    XMLPLAN=477
    YEAR=478
    ZEROIFNULL=479
    ZONE=480
    ALIAS=481
    DESCRIPTOR=482
    GO=483
    GOTO=484
    INDICATOR=485
    PRIVATE=486
    WAIT=487
    ABORTSESSIONS=488
    ABSENT=489
    ACCESS=490
    ACCORDING=491
    ACCUMULATE=492
    AG=493
    AGGGEOMINTERSECTION=494
    AGGGEOMUNION=495
    ALLDBQL=496
    ALLOCATE=497
    ALLOCATION=498
    ALLOW=499
    ALLPARAMS=500
    ALLTDWM=501
    ALWAYS=502
    AMPCOUNT=503
    ANALYSIS=504
    ANCHOR=505
    ANCHOR_HOUR=506
    ANCHOR_MILLISECOND=507
    ANCHOR_MINUTE=508
    ANCHOR_SECOND=509
    APPLNAME=510
    ARCHIVE=511
    ARRAY=512
    ARRAY_ADD=513
    ARRAY_AGG=514
    ARRAY_AVG=515
    ARRAY_COMPARE=516
    ARRAY_CONCAT=517
    ARRAY_COUNT_DISTINCT=518
    ARRAY_DIV=519
    ARRAY_EQ=520
    ARRAY_GE=521
    ARRAY_GET=522
    ARRAY_GT=523
    ARRAY_LE=524
    ARRAY_LT=525
    ARRAY_MAX=526
    ARRAY_MIN=527
    ARRAY_MOD=528
    ARRAY_MUL=529
    ARRAY_NE=530
    ARRAY_SUB=531
    ARRAY_SUM=532
    ARRAY_UPDATE=533
    ARRAY_UPDATE_STRIDE=534
    ASCII=535
    ASSIGNMENT=536
    ATTR=537
    ATTRIBUTE=538
    ATTRIBUTES=539
    ATTRIBUTION=540
    ATTRS=541
    AUTH=542
    AUTO=543
    AUTOTEMP=544
    AVRO=545
    BIT_LENGTH=546
    BITAND=547
    BITNOT=548
    BITOR=549
    BITXOR=550
    BLOCKCOMPRESSION=551
    BLOCKCOMPRESSIONALGORITHM=552
    BLOCKCOMPRESSIONLEVEL=553
    BOM=554
    BOTTOM=555
    BSON=556
    C=557
    CALENDAR=558
    CALLED=559
    CALLER=560
    CAMSET=561
    CAMSET_L=562
    CAPTURE=563
    CARDINALITY=564
    CEIL=565
    CEILING=566
    CHANGERATE=567
    CHARACTERISTICS=568
    CHARSET=569
    CHARSET_COLL=570
    CHECKSUM=571
    CHR=572
    CLASS_ORIGIN=573
    CLICKLAG=574
    CLIENT=575
    CNT=576
    COLOCATE=577
    COLUMNMETA=578
    COLUMNS=579
    COLUMNSPERINDEX=580
    COLUMNSPERJOININDEX=581
    COMMAND_FUNCTION=582
    COMMAND_FUNCTION_CODE=583
    COMPARISON=584
    COMPILE=585
    CONCAT=586
    CONCURRENT=587
    CONDITION=588
    CONDITION_IDENTIFIER=589
    CONDITION_NUMBER=590
    CONTAINED=591
    CONTAINEDTOKEN=592
    CONTENT=593
    CONTIGUOUS=594
    COST=595
    COSTS=596
    COUNTSET=597
    CPP=598
    CPUTIME=599
    CPUTIMENORM=600
    CREATEDATASET=601
    CREATOR=602
    CUME_DIST=603
    CURDATE=604
    CURTIME=605
    DATA=606
    DATASET=607
    DAY_OF_CALENDAR=608
    DAY_OF_MONTH=609
    DAY_OF_WEEK=610
    DAY_OF_YEAR=611
    DAYNUMBER_OF_CALENDAR=612
    DAYNUMBER_OF_MONTH=613
    DAYNUMBER_OF_WEEK=614
    DAYNUMBER_OF_YEAR=615
    DAYOCCURRENCE_OF_MONTH=616
    DBA=617
    DBC=618
    DEBUG=619
    DECAMSET=620
    DECAMSET_L=621
    DECODE=622
    DECOMPRESS=623
    DEFINER=624
    DELIMITER=625
    DELTA_T=626
    DEMOGRAPHICS=627
    DENIALS=628
    DENSE=629
    DENSE_RANK=630
    DESCRIBE=631
    DETAILED=632
    DIAGNOSTICS=633
    DIGITS=634
    DIMENSION=635
    DOCUMENT=636
    DOT=637
    DOWN=638
    DR=639
    DUPCOUNT=640
    DUPCOUNTCUM=641
    EBCDIC=642
    EDITDISTANCE=643
    ELAPSEDSEC=644
    ELAPSEDTIME=645
    ELEMENT=646
    ELZS_H=647
    EMITNULL=648
    EMPTY=649
    EMPTY_BLOB=650
    EMPTY_CLOB=651
    ENCODE=652
    ENCODING=653
    ENCRYPT=654
    ERRORS=655
    ERRORTBL=656
    EVENTCOLUMN=657
    EXCEPTION=658
    EXCL=659
    EXCLUDE=660
    EXCLUDING=661
    EXCLUSIVE=662
    EXPIRE=663
    EXPORT=664
    EXPORTWIDTH=665
    FALSE=666
    FEATUREINFO=667
    FILE=668
    FILL=669
    FILTER=670
    FINAL=671
    FIRST_NOTNULL=672
    FIRST_VALUE=673
    FLOOR=674
    FOLLOWING=675
    FOREIGNFUNCTION=676
    FORTOKEN=677
    FRIDAY=678
    FROM_BYTES=679
    FUNCTIONPARAMETER=680
    G=681
    GETBIT=682
    GETPSFVERSION=683
    GETQUERYBAND=684
    GETQUERYBANDVALUE=685
    GETTIMEZONEDISPLACEMENT=686
    GLOBAL=687
    GLOP=688
    GREATEST=689
    HIGH=690
    HOST=691
    IDENTIFYDATABASE=692
    IDENTIFYSESSION=693
    IDENTIFYTABLE=694
    IDENTIFYUSER=695
    IFP=696
    IGNORE=697
    IMMEDIATELY=698
    IMPORT=699
    INCLUDE=700
    INCLUDING=701
    INCREMENT=702
    INCREMENTAL=703
    INDENT=704
    INDEXESPERTABLE=705
    INDEXMAINTMODE=706
    INIT=707
    INITCAP=708
    INLINE=709
    INSTANTIABLE=710
    INSTR=711
    INTERNAL=712
    INVOKER=713
    IOCOUNT=714
    IPARTITION=715
    ISOLATED=716
    ISOLATION=717
    JAVA=718
    JIS_COLL=719
    JSON=720
    JSON_AGG=721
    JSON_COMPOSE=722
    K=723
    KANJI1=724
    KANJISJIS=725
    KBYTE=726
    KBYTES=727
    KEEP=728
    KILOBYTES=729
    LAG=730
    LAST=731
    LAST_DAY=732
    LAST_NOTNULL=733
    LAST_VALUE=734
    LATIN=735
    LDIFF=736
    LEAD=737
    LEAST=738
    LENGTH=739
    LEVEL=740
    LIST=741
    LOAD=742
    LOCATE=743
    LOCKEDUSEREXPIRE=744
    LOW=745
    LPAD=746
    LTRIM=747
    LZCOMP=748
    LZCOMP_L=749
    LZDECOMP=750
    LZDECOMP_L=751
    M=752
    MAD=753
    MANUAL=754
    MAPPING=755
    MATCHED=756
    MAX_CHOOSE=757
    MAXCHAR=758
    MAXINTERVALS=759
    MAXLOGONATTEMPTS=760
    MAXVALUE=761
    MAXVALUELENGTH=762
    MEDIAN=763
    MEDIUM=764
    MEETS=765
    MEMBER=766
    MERGEBLOCKRATIO=767
    MESSAGE_LENGTH=768
    MESSAGE_TEXT=769
    MIN_CHOOSE=770
    MINCHAR=771
    MINVALUE=772
    MODIFIED=773
    MONDAY=774
    MONITORQUERYBAND=775
    MONITORSESSIONRATE=776
    MONITORVERSION=777
    MONTH_BEGIN=778
    MONTH_END=779
    MONTH_OF_CALENDAR=780
    MONTH_OF_QUARTER=781
    MONTH_OF_YEAR=782
    MONTHNUMBER_OF_CALENDAR=783
    MONTHNUMBER_OF_QUARTER=784
    MONTHNUMBER_OF_YEAR=785
    MONTHS_BETWEEN=786
    MORE_=787
    MULTINATIONAL=788
    NAME=789
    NAMESPACE=790
    NEVER=791
    NEXT_DAY=792
    NGRAM=793
    NIL=794
    NODDLTEXT=795
    NODE=796
    NONOPTCOST=797
    NONOPTINIT=798
    NONSEQUENCED=799
    NORIGHT=800
    NOSEXTRACTVARFROMPATH=801
    NOTATION=802
    NOW=803
    NPATH=804
    NTH=805
    NULLS=806
    NUMFPFNS=807
    NUMTODSINTERVAL=808
    NUMTOYMINTERVAL=809
    NVL=810
    NVL2=811
    NVP=812
    OA=813
    OADD_MONTHS=814
    OCOUNT=815
    ODELETE=816
    OEXISTS=817
    OEXTEND=818
    OFIRST=819
    OLAST=820
    OLD_NEW_TABLE=821
    OLIMIT=822
    ONEXT=823
    ONLINE=824
    OPRIOR=825
    OPTIONS=826
    ORDERBYVALUES=827
    ORDERED_ANALYTIC=828
    ORDINALITY=829
    OREPLACE=830
    OTRANSLATE=831
    OTRIM=832
    OVERLAYS=833
    OWNER=834
    P_INTERSECT=835
    P_NORMALIZE=836
    PARAMID=837
    PARAMINFO=838
    PARENT=839
    PARTITION=840
    PARTITION_L=841
    PARTITIONED=842
    PARTITIONNAMES=843
    PASS=844
    PASSING=845
    PATH_GENERATOR=846
    PATH_START=847
    PATH_SUMMARIZER=848
    PATTERN=849
    PERCENTILE=850
    PERCENTILE_CONT=851
    PERCENTILE_DISC=852
    PERIOD=853
    PIVOT=854
    PORTION=855
    POWER=856
    PRECEDES=857
    PRECEDING=858
    PREFIX=859
    PRINT=860
    PRIOR=861
    PROTECTED=862
    QUARTER_BEGIN=863
    QUARTER_END=864
    QUARTER_OF_CALENDAR=865
    QUARTER_OF_YEAR=866
    QUARTERNUMBER_OF_CALENDAR=867
    QUARTERNUMBER_OF_YEAR=868
    QUERY=869
    QUERY_BAND=870
    QUOTECHAR=871
    RANDOMIZED=872
    RANGE=873
    RANGE_L=874
    RAPIDFIRE=875
    RDIFF=876
    READ=877
    RECALC=878
    REGEXP_INSTR=879
    REGEXP_REPLACE=880
    REGEXP_SIMILAR=881
    REGEXP_SUBSTR=882
    REPLACEMENT=883
    RESET=884
    RESPECT=885
    RESTRICTWORDS=886
    RETAIN=887
    RETURNED_SQLSTATE=888
    RETURNING=889
    REUSE=890
    ROOT=891
    ROTATELEFT=892
    ROTATERIGHT=893
    ROUND=894
    ROW_COUNT=895
    ROWIDGEN=896
    ROWIDGEN2=897
    RPAD=898
    RTRIM=899
    RU=900
    RULES=901
    RULESET=902
    SAMPLES=903
    SATURDAY=904
    SCHEMA=905
    SCRIPT=906
    SCRIPT_COMMAND=907
    SEARCHSPACE=908
    SEARCHUIFDBPATH=909
    SECURITY=910
    SEED=911
    SELF=912
    SEQ=913
    SEQUENCE=914
    SEQUENCED=915
    SERIALIZABLE=916
    SERVER=917
    SESSIONIZE=918
    SETBIT=919
    SETRESOURCERATE=920
    SETSESSIONACCOUNT=921
    SETSESSIONRATE=922
    SHARE=923
    SHIFTLEFT=924
    SHIFTRIGHT=925
    SIGN=926
    SIZE=927
    SNAPPY_COMPRESS=928
    SNAPPY_DECOMPRESS=929
    SOURCE=930
    SPARSE=931
    SPECCHAR=932
    SPL=933
    SQLSTATE=934
    SR=935
    ST_GEOMETRY=936
    STAT=937
    STATIC=938
    STATS=939
    STATSUSAGE=940
    STORAGE=941
    STRIP=942
    STRTOK=943
    STYLE=944
    SUBBITSTR=945
    SUBCLASS_ORIGIN=946
    SUCCEEDS=947
    SUMMARYONLY=948
    SUNDAY=949
    SYMBOLS=950
    SYSTEM=951
    SYSTEM_TIME=952
    SYSTEMTEST=953
    TARGET=954
    TD_ARRAY2P=955
    TD_DATASET=956
    TD_DAY_OF_CALENDAR=957
    TD_DAY_OF_MONTH=958
    TD_DAY_OF_WEEK=959
    TD_DAY_OF_YEAR=960
    TD_GENERAL=961
    TD_GETTIMEBUCKET=962
    TD_INTERNAL=963
    TD_LZ_COMPRESS=964
    TD_LZ_DECOMPRESS=965
    TD_MONTH_OF_CALENDAR=966
    TD_MONTH_OF_QUARTER=967
    TD_MONTH_OF_YEAR=968
    TD_QUARTER_OF_CALENDAR=969
    TD_QUARTER_OF_YEAR=970
    TD_TIME_BUCKET_NUMBER=971
    TD_WEEK_OF_CALENDAR=972
    TD_WEEK_OF_MONTH=973
    TD_WEEK_OF_YEAR=974
    TD_WEEKDAY_OF_MONTH=975
    TD_YEAR_OF_CALENDAR=976
    TDWMEVENT=977
    TDWMEXCEPTION=978
    TDWMHISTORY=979
    TEMPORAL_DATE=980
    TEMPORAL_TIMESTAMP=981
    TEXT=982
    THRESHOLDPERCENT=983
    THROUGH=984
    THURSDAY=985
    TIES=986
    TIMECODE=987
    TIMECOLUMN=988
    TIMEOUT=989
    TIMESTAMPCOLUMN=990
    TO_BYTE=991
    TO_BYTES=992
    TO_CHAR=993
    TO_DATE=994
    TO_DSINTERVAL=995
    TO_NUMBER=996
    TO_TIMESTAMP=997
    TO_TIMESTAMP_TZ=998
    TO_YMINTERVAL=999
    TOTOKEN=1000
    TPA=1001
    TRANSACTION_ACTIVE=1002
    TRANSUNICODETOUTF8=1003
    TRANSUTF8TOUNICODE=1004
    TRUE=1005
    TRUNC=1006
    TRUST_ONLY=1007
    TTGRANULARITY=1008
    TUESDAY=1009
    UBJSON=1010
    UCASE=1011
    UDFSEARCHPATH=1012
    UNBOUNDED=1013
    UNCOMMITTED=1014
    UNICODE=1015
    UNKNOWN=1016
    UNPIVOT=1017
    USE=1018
    USECOUNT=1019
    UTILITYINFO=1020
    VARRAY=1021
    VERBOSE=1022
    VERSION=1023
    VERSIONING=1024
    WARNING=1025
    WEDNESDAY=1026
    WEEK_BEGIN=1027
    WEEK_END=1028
    WEEK_OF_CALENDAR=1029
    WEEK_OF_MONTH=1030
    WEEK_OF_YEAR=1031
    WEEKDAY_OF_MONTH=1032
    WEEKNUMBER_OF_CALENDAR=1033
    WEEKNUMBER_OF_MONTH=1034
    WEEKNUMBER_OF_QUARTER=1035
    WEEKNUMBER_OF_YEAR=1036
    WHITESPACE=1037
    WINDOWSIZE=1038
    WITHIN=1039
    WORKLOAD=1040
    WRITE=1041
    XML=1042
    XMLAGG=1043
    XMLATTRIBUTES=1044
    XMLCOMMENT=1045
    XMLCONCAT=1046
    XMLDECLARATION=1047
    XMLDOCUMENT=1048
    XMLELEMENT=1049
    XMLFOREST=1050
    XMLNAMESPACES=1051
    XMLPARSE=1052
    XMLPI=1053
    XMLQUERY=1054
    XMLSCHEMA=1055
    XMLSERIALIZE=1056
    XMLTABLE=1057
    XMLTEXT=1058
    XMLTYPE=1059
    XMLVALIDATE=1060
    YEAR_BEGIN=1061
    YEAR_END=1062
    YEAR_OF_CALENDAR=1063
    YEARNUMBER_OF_CALENDAR=1064
    ZLIB=1065
    BUCKET=1066
    COMMITTED=1067
    CREATEXML=1068
    CS_LATIN=1069
    CS_UNICODE=1070
    CS_KANJISJIS=1071
    CS_GRAPHIC=1072
    CSV=1073
    CSVLD=1074
    DATASIZE=1075
    DAYOFMONTH=1076
    DAYS=1077
    DEFINITION=1078
    DELETED=1079
    FAST=1080
    LISTAGG=1081
    PATH=1082
    REGEXP_SPLIT_TO_TABLE=1083
    REVERSE=1084
    SAS=1085
    SQLTABLE=1086
    STRTOK_SPLIT_TO_TABLE=1087
    SYSLIB=1088
    SYSUDTLIB=1089
    TD_SERVER_DB=1090
    TD_SYSFNLIB=1091
    TD_SYSXML=1092
    TIMEDATEWZCONTROL=1093
    TRUST=1094
    TRYCAST=1095
    UDT=1096
    USAGE=1097
    VARIANT=1098
    WEEK=1099
    WIDTH=1100
    XMLPUBLISH=1101
    XMLPUBLISH_STREAM=1102
    XMLSPLIT=1103
    LATIN_TO_UNICODE=1104
    UNICODE_TO_LATIN=1105
    LOCALE_TO_UNICODE=1106
    UNICODE_TO_LOCALE=1107
    ASBSON=1108
    ASBSONTEXT=1109
    COMBINE=1110
    EXISTVALUE=1111
    JSONEXTRACT=1112
    JSONEXTRACTVALUE=1113
    JSONEXTRACTLARGEVALUE=1114
    KEYCOUNT=1115
    METADATA=1116
    STORAGE_SIZE=1117
    CREATESCHEMABASEDXML=1118
    CREATENONSCHEMABASEDXML=1119
    EXISTSNODE=1120
    ISCONTENT=1121
    ISDOCUMENT=1122
    ISSCHEMAVALID=1123
    ISSCHEMAVALIDATED=1124
    XMLEXTRACT=1125
    XMLTRANSFORM=1126
    PROC_ID=1127
    LOCATION=1128
    PAYLOAD=1129
    TRUSTED=1130
    PATHPATTERN=1131
    MANIFEST=1132
    ROWFORMAT=1133
    STOREDAS=1134
    HEADER=1135
    STRIP_EXTERIOR_SPACES=1136
    STRIP_ENCLOSING_CHAR=1137
    RLS=1138
    SINGLE=1139
    MULTIPLE=1140
    JSON_COMPRESS=1141
    JSON_DECOMPRESS=1142
    TS_COMPRESS=1143
    TS_DECOMPRESS=1144
    CONTIGUOUSMAPAMPS=1145
    SPARSEMAPAMPS=1146
    SPARSETABLEAMPS=1147
    UNNEST=1148
    CALCMATRIX=1149
    PHRASE=1150
    CALCTYPE=1151
    OUTPUT=1152
    NULL_HANDLING=1153
    READ_NOS=1154
    BUFFERSIZE=1155
    RETURNTYPE=1156
    SAMPLE_PERC=1157
    FULLSCAN=1158
    TD_UNPIVOT=1159
    VALUE_COLUMNS=1160
    UNPIVOT_COLUMN=1161
    COLUMN_LIST=1162
    COLUMN_ALIAS_LIST=1163
    INCLUDE_NULLS=1164
    WRITE_NOS=1165
    NAMING=1166
    MANIFESTFILE=1167
    MANIFESTONLY=1168
    OVERWRITE=1169
    INCLUDE_ORDERING=1170
    INCLUDE_HASHBY=1171
    MAXOBJECTSIZE=1172
    COMPRESSION=1173
    ARRAY_TO_JSON=1174
    BSON_CHECK=1175
    GEOJSONFROMGEOM=1176
    GEOMFROMGEOJSON=1177
    JSON_CHECK=1178
    JSONGETVALUE=1179
    JSONMETADATA=1180
    NVP2JSON=1181
    TD_JSONSHRED=1182
    JSON_KEYS=1183
    JSON_TABLE=1184
    DEPTH=1185
    QUOTES=1186
    ROWEXPR=1187
    COLEXPR=1188
    RETURNTYPES=1189
    NOCASE=1190
    TRUNCATE=1191
    LINK=1192
    OBJECT_NAME=1193
    UNSIGNED_INTEGER=1194
    HEX_BYTE_LITERAL=1195
    HEX_INTEGER_LITERAL=1196
    FLOAT_LITERAL=1197
    DATE_STRING=1198
    TIME_STRING=1199
    TIMESTAMP_STRING=1200
    PERIOD_STRING=1201
    UNICODE_STRING_LEADING=1202
    CHAR_STRING=1203
    HEX_STRING=1204
    PASSWORD_STRING=1205
    SEMICOLON=1206
    COLON=1207
    COMMA=1208
    DOT_=1209
    AT_SIGN=1210
    CARET=1211
    QUESTION_MARK=1212
    OPEN_PAR=1213
    CLOSE_PAR=1214
    OPEN_SQ_BRACKET=1215
    CLOSE_SQ_BRACKET=1216
    CONCATENATE=1217
    BROKEN_CONCATENATE=1218
    MUL_SIGN=1219
    DIV_SIGN=1220
    PLUS_SIGN=1221
    MINUS_SIGN=1222
    EXPONENTIATION=1223
    EQUALS_SIGN=1224
    NOT_EQUALS_SIGN=1225
    NOT_EQUALS_SIGN_TD=1226
    LT_SIGN=1227
    LE_SIGN=1228
    GT_SIGN=1229
    GE_SIGN=1230
    SINGLE_LINE_COMMENT=1231
    MULTI_LINE_COMMENT=1232
    WS=1233

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Column_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.unqualified_table_name = None # Unqualified_nameContext

        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self, i:int=None):
            if i is None:
                return self.getTokens(TeradataSQLIdentifiersParser.DOT_)
            else:
                return self.getToken(TeradataSQLIdentifiersParser.DOT_, i)

        def unqualified_column_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Unqualified_column_nameContext,0)


        def unqualified_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Unqualified_nameContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_column_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_name" ):
                listener.enterColumn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_name" ):
                listener.exitColumn_name(self)




    def column_name(self):

        localctx = TeradataSQLIdentifiersParser.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_column_name)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.database_name()
                self.state = 51
                self.match(TeradataSQLIdentifiersParser.DOT_)
                self.state = 52
                localctx.unqualified_table_name = self.unqualified_name()
                self.state = 53
                self.match(TeradataSQLIdentifiersParser.DOT_)
                self.state = 54
                self.unqualified_column_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                localctx.unqualified_table_name = self.unqualified_name()
                self.state = 57
                self.match(TeradataSQLIdentifiersParser.DOT_)
                self.state = 58
                self.unqualified_column_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.unqualified_column_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unqualified_column_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def SAMPLEID(self):
            return self.getToken(TeradataSQLIdentifiersParser.SAMPLEID, 0)

        def ROWID(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROWID, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_unqualified_column_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualified_column_name" ):
                listener.enterUnqualified_column_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualified_column_name" ):
                listener.exitUnqualified_column_name(self)




    def unqualified_column_name(self):

        localctx = TeradataSQLIdentifiersParser.Unqualified_column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unqualified_column_name)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.nonreserved_word()
                pass
            elif token in [366]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(TeradataSQLIdentifiersParser.SAMPLEID)
                pass
            elif token in [363]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(TeradataSQLIdentifiersParser.ROWID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unqualified_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_unqualified_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualified_name" ):
                listener.enterUnqualified_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualified_name" ):
                listener.exitUnqualified_name(self)




    def unqualified_name(self):

        localctx = TeradataSQLIdentifiersParser.Unqualified_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unqualified_name)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT_, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_object_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_name" ):
                listener.enterObject_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_name" ):
                listener.exitObject_name(self)




    def object_name(self):

        localctx = TeradataSQLIdentifiersParser.Object_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_object_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 73
                self.database_name()
                self.state = 74
                self.match(TeradataSQLIdentifiersParser.DOT_)


            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.state = 78
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.state = 79
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT_, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)




    def table_name(self):

        localctx = TeradataSQLIdentifiersParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 82
                self.database_name()
                self.state = 83
                self.match(TeradataSQLIdentifiersParser.DOT_)


            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.state = 87
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.state = 88
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT_, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_procedure_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure_name" ):
                listener.enterProcedure_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure_name" ):
                listener.exitProcedure_name(self)




    def procedure_name(self):

        localctx = TeradataSQLIdentifiersParser.Procedure_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_procedure_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 91
                self.database_name()
                self.state = 92
                self.match(TeradataSQLIdentifiersParser.DOT_)


            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.state = 96
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.state = 97
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT_, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)




    def function_name(self):

        localctx = TeradataSQLIdentifiersParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 100
                self.database_name()
                self.state = 101
                self.match(TeradataSQLIdentifiersParser.DOT_)


            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.state = 105
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.state = 106
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def database_name(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Database_nameContext,0)


        def DOT_(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT_, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_macro_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_name" ):
                listener.enterMacro_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_name" ):
                listener.exitMacro_name(self)




    def macro_name(self):

        localctx = TeradataSQLIdentifiersParser.Macro_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_macro_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 109
                self.database_name()
                self.state = 110
                self.match(TeradataSQLIdentifiersParser.DOT_)


            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.state = 114
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.state = 115
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Database_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_database_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatabase_name" ):
                listener.enterDatabase_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatabase_name" ):
                listener.exitDatabase_name(self)




    def database_name(self):

        localctx = TeradataSQLIdentifiersParser.Database_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_database_name)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class User_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_user_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUser_name" ):
                listener.enterUser_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUser_name" ):
                listener.exitUser_name(self)




    def user_name(self):

        localctx = TeradataSQLIdentifiersParser.User_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_user_name)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Role_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def ADMIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.ADMIN, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_role_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole_name" ):
                listener.enterRole_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole_name" ):
                listener.exitRole_name(self)




    def role_name(self):

        localctx = TeradataSQLIdentifiersParser.Role_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_role_name)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(TeradataSQLIdentifiersParser.ADMIN)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Profile_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_profile_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProfile_name" ):
                listener.enterProfile_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProfile_name" ):
                listener.exitProfile_name(self)




    def profile_name(self):

        localctx = TeradataSQLIdentifiersParser.Profile_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_profile_name)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alias_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_alias_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlias_name" ):
                listener.enterAlias_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlias_name" ):
                listener.exitAlias_name(self)




    def alias_name(self):

        localctx = TeradataSQLIdentifiersParser.Alias_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_alias_name)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_name" ):
                listener.enterVariable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_name" ):
                listener.exitVariable_name(self)




    def variable_name(self):

        localctx = TeradataSQLIdentifiersParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable_name)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_parameter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_name" ):
                listener.enterParameter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_name" ):
                listener.exitParameter_name(self)




    def parameter_name(self):

        localctx = TeradataSQLIdentifiersParser.Parameter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter_name)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Label_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_label_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_name" ):
                listener.enterLabel_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_name" ):
                listener.exitLabel_name(self)




    def label_name(self):

        localctx = TeradataSQLIdentifiersParser.Label_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_label_name)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_condition_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_name" ):
                listener.enterCondition_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_name" ):
                listener.exitCondition_name(self)




    def condition_name(self):

        localctx = TeradataSQLIdentifiersParser.Condition_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_name)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cursor_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_cursor_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCursor_name" ):
                listener.enterCursor_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCursor_name" ):
                listener.exitCursor_name(self)




    def cursor_name(self):

        localctx = TeradataSQLIdentifiersParser.Cursor_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cursor_name)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_statement_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_name" ):
                listener.enterStatement_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_name" ):
                listener.exitStatement_name(self)




    def statement_name(self):

        localctx = TeradataSQLIdentifiersParser.Statement_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement_name)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statistics_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_statistics_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatistics_name" ):
                listener.enterStatistics_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatistics_name" ):
                listener.exitStatistics_name(self)




    def statistics_name(self):

        localctx = TeradataSQLIdentifiersParser.Statistics_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statistics_name)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Udt_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_udt_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUdt_name" ):
                listener.enterUdt_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUdt_name" ):
                listener.exitUdt_name(self)




    def udt_name(self):

        localctx = TeradataSQLIdentifiersParser.Udt_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_udt_name)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_attribute_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_name" ):
                listener.enterAttribute_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_name" ):
                listener.exitAttribute_name(self)




    def attribute_name(self):

        localctx = TeradataSQLIdentifiersParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_attribute_name)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.OBJECT_NAME, 0)

        def nonreserved_word(self):
            return self.getTypedRuleContext(TeradataSQLIdentifiersParser.Nonreserved_wordContext,0)


        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_method_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_name" ):
                listener.enterMethod_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_name" ):
                listener.exitMethod_name(self)




    def method_name(self):

        localctx = TeradataSQLIdentifiersParser.Method_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_name)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1193]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(TeradataSQLIdentifiersParser.OBJECT_NAME)
                pass
            elif token in [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.nonreserved_word()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anchor_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANCHOR_MILLISECOND(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_MILLISECOND, 0)

        def ANCHOR_SECOND(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_SECOND, 0)

        def ANCHOR_MINUTE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_MINUTE, 0)

        def ANCHOR_HOUR(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_HOUR, 0)

        def DAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAY, 0)

        def WEEK_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_BEGIN, 0)

        def WEEK_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_END, 0)

        def MONTH_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_BEGIN, 0)

        def MONTH_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_END, 0)

        def QUARTER_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_BEGIN, 0)

        def QUARTER_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_END, 0)

        def YEAR_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEAR_BEGIN, 0)

        def YEAR_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEAR_END, 0)

        def MONDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONDAY, 0)

        def TUESDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.TUESDAY, 0)

        def WEDNESDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEDNESDAY, 0)

        def THURSDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.THURSDAY, 0)

        def FRIDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.FRIDAY, 0)

        def SATURDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SATURDAY, 0)

        def SUNDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUNDAY, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_anchor_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnchor_name" ):
                listener.enterAnchor_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnchor_name" ):
                listener.exitAnchor_name(self)




    def anchor_name(self):

        localctx = TeradataSQLIdentifiersParser.Anchor_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_anchor_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==106 or ((((_la - 506)) & ~0x3f) == 0 and ((1 << (_la - 506)) & 15) != 0) or _la==678 or ((((_la - 774)) & ~0x3f) == 0 and ((1 << (_la - 774)) & 49) != 0) or ((((_la - 863)) & ~0x3f) == 0 and ((1 << (_la - 863)) & 2199023255555) != 0) or ((((_la - 949)) & ~0x3f) == 0 and ((1 << (_la - 949)) & 1152921573326323713) != 0) or ((((_la - 1026)) & ~0x3f) == 0 and ((1 << (_la - 1026)) & 103079215111) != 0)):
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


    class Nonreserved_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABORTSESSIONS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ABORTSESSIONS, 0)

        def ABSENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ABSENT, 0)

        def ACCESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ACCESS, 0)

        def ACCORDING(self):
            return self.getToken(TeradataSQLIdentifiersParser.ACCORDING, 0)

        def ACCUMULATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ACCUMULATE, 0)

        def AG(self):
            return self.getToken(TeradataSQLIdentifiersParser.AG, 0)

        def AGGGEOMINTERSECTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.AGGGEOMINTERSECTION, 0)

        def AGGGEOMUNION(self):
            return self.getToken(TeradataSQLIdentifiersParser.AGGGEOMUNION, 0)

        def ALLDBQL(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLDBQL, 0)

        def ALLOCATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLOCATE, 0)

        def ALLOCATION(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLOCATION, 0)

        def ALLOW(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLOW, 0)

        def ALLPARAMS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLPARAMS, 0)

        def ALLTDWM(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALLTDWM, 0)

        def ALWAYS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ALWAYS, 0)

        def AMPCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.AMPCOUNT, 0)

        def ANALYSIS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANALYSIS, 0)

        def ANCHOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR, 0)

        def ANCHOR_HOUR(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_HOUR, 0)

        def ANCHOR_MILLISECOND(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_MILLISECOND, 0)

        def ANCHOR_MINUTE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_MINUTE, 0)

        def ANCHOR_SECOND(self):
            return self.getToken(TeradataSQLIdentifiersParser.ANCHOR_SECOND, 0)

        def APPLNAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.APPLNAME, 0)

        def ARCHIVE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARCHIVE, 0)

        def ARRAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY, 0)

        def ARRAY_ADD(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_ADD, 0)

        def ARRAY_AGG(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_AGG, 0)

        def ARRAY_AVG(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_AVG, 0)

        def ARRAY_COMPARE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_COMPARE, 0)

        def ARRAY_CONCAT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_CONCAT, 0)

        def ARRAY_COUNT_DISTINCT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_COUNT_DISTINCT, 0)

        def ARRAY_DIV(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_DIV, 0)

        def ARRAY_EQ(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_EQ, 0)

        def ARRAY_GE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_GE, 0)

        def ARRAY_GET(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_GET, 0)

        def ARRAY_GT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_GT, 0)

        def ARRAY_LE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_LE, 0)

        def ARRAY_LT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_LT, 0)

        def ARRAY_MAX(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_MAX, 0)

        def ARRAY_MIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_MIN, 0)

        def ARRAY_MOD(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_MOD, 0)

        def ARRAY_MUL(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_MUL, 0)

        def ARRAY_NE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_NE, 0)

        def ARRAY_SUB(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_SUB, 0)

        def ARRAY_SUM(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_SUM, 0)

        def ARRAY_UPDATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_UPDATE, 0)

        def ARRAY_UPDATE_STRIDE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_UPDATE_STRIDE, 0)

        def ASCII(self):
            return self.getToken(TeradataSQLIdentifiersParser.ASCII, 0)

        def ASSIGNMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ASSIGNMENT, 0)

        def ATTR(self):
            return self.getToken(TeradataSQLIdentifiersParser.ATTR, 0)

        def ATTRIBUTE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ATTRIBUTE, 0)

        def ATTRIBUTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.ATTRIBUTES, 0)

        def ATTRIBUTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.ATTRIBUTION, 0)

        def ATTRS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ATTRS, 0)

        def AUTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.AUTH, 0)

        def AUTO(self):
            return self.getToken(TeradataSQLIdentifiersParser.AUTO, 0)

        def AUTOTEMP(self):
            return self.getToken(TeradataSQLIdentifiersParser.AUTOTEMP, 0)

        def AVRO(self):
            return self.getToken(TeradataSQLIdentifiersParser.AVRO, 0)

        def BIT_LENGTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.BIT_LENGTH, 0)

        def BITAND(self):
            return self.getToken(TeradataSQLIdentifiersParser.BITAND, 0)

        def BITNOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.BITNOT, 0)

        def BITOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.BITOR, 0)

        def BITXOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.BITXOR, 0)

        def BLOCKCOMPRESSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.BLOCKCOMPRESSION, 0)

        def BLOCKCOMPRESSIONALGORITHM(self):
            return self.getToken(TeradataSQLIdentifiersParser.BLOCKCOMPRESSIONALGORITHM, 0)

        def BLOCKCOMPRESSIONLEVEL(self):
            return self.getToken(TeradataSQLIdentifiersParser.BLOCKCOMPRESSIONLEVEL, 0)

        def BOM(self):
            return self.getToken(TeradataSQLIdentifiersParser.BOM, 0)

        def BOTTOM(self):
            return self.getToken(TeradataSQLIdentifiersParser.BOTTOM, 0)

        def BSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.BSON, 0)

        def C(self):
            return self.getToken(TeradataSQLIdentifiersParser.C, 0)

        def CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.CALENDAR, 0)

        def CALLED(self):
            return self.getToken(TeradataSQLIdentifiersParser.CALLED, 0)

        def CALLER(self):
            return self.getToken(TeradataSQLIdentifiersParser.CALLER, 0)

        def CAMSET(self):
            return self.getToken(TeradataSQLIdentifiersParser.CAMSET, 0)

        def CAMSET_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.CAMSET_L, 0)

        def CAPTURE(self):
            return self.getToken(TeradataSQLIdentifiersParser.CAPTURE, 0)

        def CARDINALITY(self):
            return self.getToken(TeradataSQLIdentifiersParser.CARDINALITY, 0)

        def CEIL(self):
            return self.getToken(TeradataSQLIdentifiersParser.CEIL, 0)

        def CEILING(self):
            return self.getToken(TeradataSQLIdentifiersParser.CEILING, 0)

        def CHANGERATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHANGERATE, 0)

        def CHARACTERISTICS(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHARACTERISTICS, 0)

        def CHARSET(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHARSET, 0)

        def CHARSET_COLL(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHARSET_COLL, 0)

        def CHECKSUM(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHECKSUM, 0)

        def CHR(self):
            return self.getToken(TeradataSQLIdentifiersParser.CHR, 0)

        def CLASS_ORIGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.CLASS_ORIGIN, 0)

        def CLICKLAG(self):
            return self.getToken(TeradataSQLIdentifiersParser.CLICKLAG, 0)

        def CLIENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.CLIENT, 0)

        def CNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.CNT, 0)

        def COLOCATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLOCATE, 0)

        def COLUMNMETA(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMNMETA, 0)

        def COLUMNS(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMNS, 0)

        def COLUMNSPERINDEX(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMNSPERINDEX, 0)

        def COLUMNSPERJOININDEX(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMNSPERJOININDEX, 0)

        def COMMAND_FUNCTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMMAND_FUNCTION, 0)

        def COMMAND_FUNCTION_CODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMMAND_FUNCTION_CODE, 0)

        def COMPARISON(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMPARISON, 0)

        def COMPILE(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMPILE, 0)

        def CONCAT(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONCAT, 0)

        def CONCURRENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONCURRENT, 0)

        def CONDITION(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONDITION, 0)

        def CONDITION_IDENTIFIER(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONDITION_IDENTIFIER, 0)

        def CONDITION_NUMBER(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONDITION_NUMBER, 0)

        def CONTAINED(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONTAINED, 0)

        def CONTAINEDTOKEN(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONTAINEDTOKEN, 0)

        def CONTENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONTENT, 0)

        def CONTIGUOUS(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONTIGUOUS, 0)

        def COST(self):
            return self.getToken(TeradataSQLIdentifiersParser.COST, 0)

        def COSTS(self):
            return self.getToken(TeradataSQLIdentifiersParser.COSTS, 0)

        def COUNTSET(self):
            return self.getToken(TeradataSQLIdentifiersParser.COUNTSET, 0)

        def CPP(self):
            return self.getToken(TeradataSQLIdentifiersParser.CPP, 0)

        def CPUTIME(self):
            return self.getToken(TeradataSQLIdentifiersParser.CPUTIME, 0)

        def CPUTIMENORM(self):
            return self.getToken(TeradataSQLIdentifiersParser.CPUTIMENORM, 0)

        def CREATEDATASET(self):
            return self.getToken(TeradataSQLIdentifiersParser.CREATEDATASET, 0)

        def CREATOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.CREATOR, 0)

        def CUME_DIST(self):
            return self.getToken(TeradataSQLIdentifiersParser.CUME_DIST, 0)

        def CURDATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.CURDATE, 0)

        def CURTIME(self):
            return self.getToken(TeradataSQLIdentifiersParser.CURTIME, 0)

        def DATA(self):
            return self.getToken(TeradataSQLIdentifiersParser.DATA, 0)

        def DATASET(self):
            return self.getToken(TeradataSQLIdentifiersParser.DATASET, 0)

        def DAY_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAY_OF_CALENDAR, 0)

        def DAY_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAY_OF_MONTH, 0)

        def DAY_OF_WEEK(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAY_OF_WEEK, 0)

        def DAY_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAY_OF_YEAR, 0)

        def DAYNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYNUMBER_OF_CALENDAR, 0)

        def DAYNUMBER_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYNUMBER_OF_MONTH, 0)

        def DAYNUMBER_OF_WEEK(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYNUMBER_OF_WEEK, 0)

        def DAYNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYNUMBER_OF_YEAR, 0)

        def DAYOCCURRENCE_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYOCCURRENCE_OF_MONTH, 0)

        def DBA(self):
            return self.getToken(TeradataSQLIdentifiersParser.DBA, 0)

        def DBC(self):
            return self.getToken(TeradataSQLIdentifiersParser.DBC, 0)

        def DEBUG(self):
            return self.getToken(TeradataSQLIdentifiersParser.DEBUG, 0)

        def DECAMSET(self):
            return self.getToken(TeradataSQLIdentifiersParser.DECAMSET, 0)

        def DECAMSET_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.DECAMSET_L, 0)

        def DECODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.DECODE, 0)

        def DECOMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DECOMPRESS, 0)

        def DEFINER(self):
            return self.getToken(TeradataSQLIdentifiersParser.DEFINER, 0)

        def DELIMITER(self):
            return self.getToken(TeradataSQLIdentifiersParser.DELIMITER, 0)

        def DELTA_T(self):
            return self.getToken(TeradataSQLIdentifiersParser.DELTA_T, 0)

        def DEMOGRAPHICS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DEMOGRAPHICS, 0)

        def DENIALS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DENIALS, 0)

        def DENSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.DENSE, 0)

        def DENSE_RANK(self):
            return self.getToken(TeradataSQLIdentifiersParser.DENSE_RANK, 0)

        def DESCRIBE(self):
            return self.getToken(TeradataSQLIdentifiersParser.DESCRIBE, 0)

        def DETAILED(self):
            return self.getToken(TeradataSQLIdentifiersParser.DETAILED, 0)

        def DIAGNOSTICS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DIAGNOSTICS, 0)

        def DIGITS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DIGITS, 0)

        def DIMENSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.DIMENSION, 0)

        def DOCUMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOCUMENT, 0)

        def DOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOT, 0)

        def DOWN(self):
            return self.getToken(TeradataSQLIdentifiersParser.DOWN, 0)

        def DR(self):
            return self.getToken(TeradataSQLIdentifiersParser.DR, 0)

        def DUPCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.DUPCOUNT, 0)

        def DUPCOUNTCUM(self):
            return self.getToken(TeradataSQLIdentifiersParser.DUPCOUNTCUM, 0)

        def EBCDIC(self):
            return self.getToken(TeradataSQLIdentifiersParser.EBCDIC, 0)

        def EDITDISTANCE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EDITDISTANCE, 0)

        def ELAPSEDSEC(self):
            return self.getToken(TeradataSQLIdentifiersParser.ELAPSEDSEC, 0)

        def ELAPSEDTIME(self):
            return self.getToken(TeradataSQLIdentifiersParser.ELAPSEDTIME, 0)

        def ELEMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ELEMENT, 0)

        def ELZS_H(self):
            return self.getToken(TeradataSQLIdentifiersParser.ELZS_H, 0)

        def EMITNULL(self):
            return self.getToken(TeradataSQLIdentifiersParser.EMITNULL, 0)

        def EMPTY(self):
            return self.getToken(TeradataSQLIdentifiersParser.EMPTY, 0)

        def EMPTY_BLOB(self):
            return self.getToken(TeradataSQLIdentifiersParser.EMPTY_BLOB, 0)

        def EMPTY_CLOB(self):
            return self.getToken(TeradataSQLIdentifiersParser.EMPTY_CLOB, 0)

        def ENCODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ENCODE, 0)

        def ENCODING(self):
            return self.getToken(TeradataSQLIdentifiersParser.ENCODING, 0)

        def ENCRYPT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ENCRYPT, 0)

        def ERRORS(self):
            return self.getToken(TeradataSQLIdentifiersParser.ERRORS, 0)

        def ERRORTBL(self):
            return self.getToken(TeradataSQLIdentifiersParser.ERRORTBL, 0)

        def EVENTCOLUMN(self):
            return self.getToken(TeradataSQLIdentifiersParser.EVENTCOLUMN, 0)

        def EXCEPTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXCEPTION, 0)

        def EXCL(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXCL, 0)

        def EXCLUDE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXCLUDE, 0)

        def EXCLUDING(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXCLUDING, 0)

        def EXCLUSIVE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXCLUSIVE, 0)

        def EXPIRE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXPIRE, 0)

        def EXPORT(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXPORT, 0)

        def EXPORTWIDTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXPORTWIDTH, 0)

        def FALSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.FALSE, 0)

        def FEATUREINFO(self):
            return self.getToken(TeradataSQLIdentifiersParser.FEATUREINFO, 0)

        def FILE(self):
            return self.getToken(TeradataSQLIdentifiersParser.FILE, 0)

        def FILL(self):
            return self.getToken(TeradataSQLIdentifiersParser.FILL, 0)

        def FILTER(self):
            return self.getToken(TeradataSQLIdentifiersParser.FILTER, 0)

        def FINAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.FINAL, 0)

        def FIRST_NOTNULL(self):
            return self.getToken(TeradataSQLIdentifiersParser.FIRST_NOTNULL, 0)

        def FIRST_VALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.FIRST_VALUE, 0)

        def FLOOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.FLOOR, 0)

        def FOLLOWING(self):
            return self.getToken(TeradataSQLIdentifiersParser.FOLLOWING, 0)

        def FOREIGNFUNCTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.FOREIGNFUNCTION, 0)

        def FORTOKEN(self):
            return self.getToken(TeradataSQLIdentifiersParser.FORTOKEN, 0)

        def FRIDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.FRIDAY, 0)

        def FROM_BYTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.FROM_BYTES, 0)

        def FUNCTIONPARAMETER(self):
            return self.getToken(TeradataSQLIdentifiersParser.FUNCTIONPARAMETER, 0)

        def G(self):
            return self.getToken(TeradataSQLIdentifiersParser.G, 0)

        def GETBIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.GETBIT, 0)

        def GETPSFVERSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.GETPSFVERSION, 0)

        def GETQUERYBAND(self):
            return self.getToken(TeradataSQLIdentifiersParser.GETQUERYBAND, 0)

        def GETQUERYBANDVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.GETQUERYBANDVALUE, 0)

        def GETTIMEZONEDISPLACEMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.GETTIMEZONEDISPLACEMENT, 0)

        def GLOBAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.GLOBAL, 0)

        def GLOP(self):
            return self.getToken(TeradataSQLIdentifiersParser.GLOP, 0)

        def GREATEST(self):
            return self.getToken(TeradataSQLIdentifiersParser.GREATEST, 0)

        def HIGH(self):
            return self.getToken(TeradataSQLIdentifiersParser.HIGH, 0)

        def HOST(self):
            return self.getToken(TeradataSQLIdentifiersParser.HOST, 0)

        def IDENTIFYDATABASE(self):
            return self.getToken(TeradataSQLIdentifiersParser.IDENTIFYDATABASE, 0)

        def IDENTIFYSESSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.IDENTIFYSESSION, 0)

        def IDENTIFYTABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.IDENTIFYTABLE, 0)

        def IDENTIFYUSER(self):
            return self.getToken(TeradataSQLIdentifiersParser.IDENTIFYUSER, 0)

        def IFP(self):
            return self.getToken(TeradataSQLIdentifiersParser.IFP, 0)

        def IGNORE(self):
            return self.getToken(TeradataSQLIdentifiersParser.IGNORE, 0)

        def IMMEDIATELY(self):
            return self.getToken(TeradataSQLIdentifiersParser.IMMEDIATELY, 0)

        def IMPORT(self):
            return self.getToken(TeradataSQLIdentifiersParser.IMPORT, 0)

        def INCLUDE(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCLUDE, 0)

        def INCLUDING(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCLUDING, 0)

        def INCREMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCREMENT, 0)

        def INCREMENTAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCREMENTAL, 0)

        def INDENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.INDENT, 0)

        def INDEXESPERTABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.INDEXESPERTABLE, 0)

        def INDEXMAINTMODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.INDEXMAINTMODE, 0)

        def INIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.INIT, 0)

        def INITCAP(self):
            return self.getToken(TeradataSQLIdentifiersParser.INITCAP, 0)

        def INLINE(self):
            return self.getToken(TeradataSQLIdentifiersParser.INLINE, 0)

        def INSTANTIABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.INSTANTIABLE, 0)

        def INSTR(self):
            return self.getToken(TeradataSQLIdentifiersParser.INSTR, 0)

        def INTERNAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.INTERNAL, 0)

        def INVOKER(self):
            return self.getToken(TeradataSQLIdentifiersParser.INVOKER, 0)

        def IOCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.IOCOUNT, 0)

        def IPARTITION(self):
            return self.getToken(TeradataSQLIdentifiersParser.IPARTITION, 0)

        def ISOLATED(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISOLATED, 0)

        def ISOLATION(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISOLATION, 0)

        def JAVA(self):
            return self.getToken(TeradataSQLIdentifiersParser.JAVA, 0)

        def JIS_COLL(self):
            return self.getToken(TeradataSQLIdentifiersParser.JIS_COLL, 0)

        def JSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON, 0)

        def JSON_AGG(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_AGG, 0)

        def JSON_COMPOSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_COMPOSE, 0)

        def K(self):
            return self.getToken(TeradataSQLIdentifiersParser.K, 0)

        def KANJI1(self):
            return self.getToken(TeradataSQLIdentifiersParser.KANJI1, 0)

        def KANJISJIS(self):
            return self.getToken(TeradataSQLIdentifiersParser.KANJISJIS, 0)

        def KBYTE(self):
            return self.getToken(TeradataSQLIdentifiersParser.KBYTE, 0)

        def KBYTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.KBYTES, 0)

        def KEEP(self):
            return self.getToken(TeradataSQLIdentifiersParser.KEEP, 0)

        def KILOBYTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.KILOBYTES, 0)

        def LAG(self):
            return self.getToken(TeradataSQLIdentifiersParser.LAG, 0)

        def LAST(self):
            return self.getToken(TeradataSQLIdentifiersParser.LAST, 0)

        def LAST_DAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.LAST_DAY, 0)

        def LAST_NOTNULL(self):
            return self.getToken(TeradataSQLIdentifiersParser.LAST_NOTNULL, 0)

        def LAST_VALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.LAST_VALUE, 0)

        def LATIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.LATIN, 0)

        def LDIFF(self):
            return self.getToken(TeradataSQLIdentifiersParser.LDIFF, 0)

        def LEAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.LEAD, 0)

        def LEAST(self):
            return self.getToken(TeradataSQLIdentifiersParser.LEAST, 0)

        def LENGTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.LENGTH, 0)

        def LEVEL(self):
            return self.getToken(TeradataSQLIdentifiersParser.LEVEL, 0)

        def LIST(self):
            return self.getToken(TeradataSQLIdentifiersParser.LIST, 0)

        def LOAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOAD, 0)

        def LOCATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOCATE, 0)

        def LOCKEDUSEREXPIRE(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOCKEDUSEREXPIRE, 0)

        def LOW(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOW, 0)

        def LPAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.LPAD, 0)

        def LTRIM(self):
            return self.getToken(TeradataSQLIdentifiersParser.LTRIM, 0)

        def LZCOMP(self):
            return self.getToken(TeradataSQLIdentifiersParser.LZCOMP, 0)

        def LZCOMP_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.LZCOMP_L, 0)

        def LZDECOMP(self):
            return self.getToken(TeradataSQLIdentifiersParser.LZDECOMP, 0)

        def LZDECOMP_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.LZDECOMP_L, 0)

        def M(self):
            return self.getToken(TeradataSQLIdentifiersParser.M, 0)

        def MAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAD, 0)

        def MANUAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.MANUAL, 0)

        def MAPPING(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAPPING, 0)

        def MATCHED(self):
            return self.getToken(TeradataSQLIdentifiersParser.MATCHED, 0)

        def MAX_CHOOSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAX_CHOOSE, 0)

        def MAXCHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXCHAR, 0)

        def MAXINTERVALS(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXINTERVALS, 0)

        def MAXLOGONATTEMPTS(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXLOGONATTEMPTS, 0)

        def MAXVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXVALUE, 0)

        def MAXVALUELENGTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXVALUELENGTH, 0)

        def MEDIAN(self):
            return self.getToken(TeradataSQLIdentifiersParser.MEDIAN, 0)

        def MEDIUM(self):
            return self.getToken(TeradataSQLIdentifiersParser.MEDIUM, 0)

        def MEETS(self):
            return self.getToken(TeradataSQLIdentifiersParser.MEETS, 0)

        def MEMBER(self):
            return self.getToken(TeradataSQLIdentifiersParser.MEMBER, 0)

        def MERGEBLOCKRATIO(self):
            return self.getToken(TeradataSQLIdentifiersParser.MERGEBLOCKRATIO, 0)

        def MESSAGE_LENGTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.MESSAGE_LENGTH, 0)

        def MESSAGE_TEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.MESSAGE_TEXT, 0)

        def MIN_CHOOSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MIN_CHOOSE, 0)

        def MINCHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MINCHAR, 0)

        def MINVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MINVALUE, 0)

        def MODIFIED(self):
            return self.getToken(TeradataSQLIdentifiersParser.MODIFIED, 0)

        def MONDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONDAY, 0)

        def MONITORQUERYBAND(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONITORQUERYBAND, 0)

        def MONITORSESSIONRATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONITORSESSIONRATE, 0)

        def MONITORVERSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONITORVERSION, 0)

        def MONTH_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_BEGIN, 0)

        def MONTH_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_END, 0)

        def MONTH_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_OF_CALENDAR, 0)

        def MONTH_OF_QUARTER(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_OF_QUARTER, 0)

        def MONTH_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTH_OF_YEAR, 0)

        def MONTHNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTHNUMBER_OF_CALENDAR, 0)

        def MONTHNUMBER_OF_QUARTER(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTHNUMBER_OF_QUARTER, 0)

        def MONTHNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTHNUMBER_OF_YEAR, 0)

        def MONTHS_BETWEEN(self):
            return self.getToken(TeradataSQLIdentifiersParser.MONTHS_BETWEEN, 0)

        def MORE_(self):
            return self.getToken(TeradataSQLIdentifiersParser.MORE_, 0)

        def MULTINATIONAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.MULTINATIONAL, 0)

        def NAME(self):
            return self.getToken(TeradataSQLIdentifiersParser.NAME, 0)

        def NAMESPACE(self):
            return self.getToken(TeradataSQLIdentifiersParser.NAMESPACE, 0)

        def NEVER(self):
            return self.getToken(TeradataSQLIdentifiersParser.NEVER, 0)

        def NEXT_DAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.NEXT_DAY, 0)

        def NGRAM(self):
            return self.getToken(TeradataSQLIdentifiersParser.NGRAM, 0)

        def NIL(self):
            return self.getToken(TeradataSQLIdentifiersParser.NIL, 0)

        def NODDLTEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.NODDLTEXT, 0)

        def NODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.NODE, 0)

        def NONOPTCOST(self):
            return self.getToken(TeradataSQLIdentifiersParser.NONOPTCOST, 0)

        def NONOPTINIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.NONOPTINIT, 0)

        def NONSEQUENCED(self):
            return self.getToken(TeradataSQLIdentifiersParser.NONSEQUENCED, 0)

        def NORIGHT(self):
            return self.getToken(TeradataSQLIdentifiersParser.NORIGHT, 0)

        def NOSEXTRACTVARFROMPATH(self):
            return self.getToken(TeradataSQLIdentifiersParser.NOSEXTRACTVARFROMPATH, 0)

        def NOTATION(self):
            return self.getToken(TeradataSQLIdentifiersParser.NOTATION, 0)

        def NOW(self):
            return self.getToken(TeradataSQLIdentifiersParser.NOW, 0)

        def NPATH(self):
            return self.getToken(TeradataSQLIdentifiersParser.NPATH, 0)

        def NTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.NTH, 0)

        def NULLS(self):
            return self.getToken(TeradataSQLIdentifiersParser.NULLS, 0)

        def NUMFPFNS(self):
            return self.getToken(TeradataSQLIdentifiersParser.NUMFPFNS, 0)

        def NUMTODSINTERVAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.NUMTODSINTERVAL, 0)

        def NUMTOYMINTERVAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.NUMTOYMINTERVAL, 0)

        def NVL(self):
            return self.getToken(TeradataSQLIdentifiersParser.NVL, 0)

        def NVL2(self):
            return self.getToken(TeradataSQLIdentifiersParser.NVL2, 0)

        def NVP(self):
            return self.getToken(TeradataSQLIdentifiersParser.NVP, 0)

        def OA(self):
            return self.getToken(TeradataSQLIdentifiersParser.OA, 0)

        def OADD_MONTHS(self):
            return self.getToken(TeradataSQLIdentifiersParser.OADD_MONTHS, 0)

        def OCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.OCOUNT, 0)

        def ODELETE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ODELETE, 0)

        def OEXISTS(self):
            return self.getToken(TeradataSQLIdentifiersParser.OEXISTS, 0)

        def OEXTEND(self):
            return self.getToken(TeradataSQLIdentifiersParser.OEXTEND, 0)

        def OFIRST(self):
            return self.getToken(TeradataSQLIdentifiersParser.OFIRST, 0)

        def OLAST(self):
            return self.getToken(TeradataSQLIdentifiersParser.OLAST, 0)

        def OLD_NEW_TABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.OLD_NEW_TABLE, 0)

        def OLIMIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.OLIMIT, 0)

        def ONEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ONEXT, 0)

        def ONLINE(self):
            return self.getToken(TeradataSQLIdentifiersParser.ONLINE, 0)

        def OPRIOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.OPRIOR, 0)

        def OPTIONS(self):
            return self.getToken(TeradataSQLIdentifiersParser.OPTIONS, 0)

        def ORDERBYVALUES(self):
            return self.getToken(TeradataSQLIdentifiersParser.ORDERBYVALUES, 0)

        def ORDERED_ANALYTIC(self):
            return self.getToken(TeradataSQLIdentifiersParser.ORDERED_ANALYTIC, 0)

        def ORDINALITY(self):
            return self.getToken(TeradataSQLIdentifiersParser.ORDINALITY, 0)

        def OREPLACE(self):
            return self.getToken(TeradataSQLIdentifiersParser.OREPLACE, 0)

        def OTRANSLATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.OTRANSLATE, 0)

        def OTRIM(self):
            return self.getToken(TeradataSQLIdentifiersParser.OTRIM, 0)

        def OVERLAYS(self):
            return self.getToken(TeradataSQLIdentifiersParser.OVERLAYS, 0)

        def OWNER(self):
            return self.getToken(TeradataSQLIdentifiersParser.OWNER, 0)

        def P_INTERSECT(self):
            return self.getToken(TeradataSQLIdentifiersParser.P_INTERSECT, 0)

        def P_NORMALIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.P_NORMALIZE, 0)

        def PARAMID(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARAMID, 0)

        def PARAMINFO(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARAMINFO, 0)

        def PARENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARENT, 0)

        def PARTITION(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARTITION, 0)

        def PARTITION_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARTITION_L, 0)

        def PARTITIONED(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARTITIONED, 0)

        def PARTITIONNAMES(self):
            return self.getToken(TeradataSQLIdentifiersParser.PARTITIONNAMES, 0)

        def PASS(self):
            return self.getToken(TeradataSQLIdentifiersParser.PASS, 0)

        def PASSING(self):
            return self.getToken(TeradataSQLIdentifiersParser.PASSING, 0)

        def PATH_GENERATOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATH_GENERATOR, 0)

        def PATH_START(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATH_START, 0)

        def PATH_SUMMARIZER(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATH_SUMMARIZER, 0)

        def PATTERN(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATTERN, 0)

        def PERCENTILE(self):
            return self.getToken(TeradataSQLIdentifiersParser.PERCENTILE, 0)

        def PERCENTILE_CONT(self):
            return self.getToken(TeradataSQLIdentifiersParser.PERCENTILE_CONT, 0)

        def PERCENTILE_DISC(self):
            return self.getToken(TeradataSQLIdentifiersParser.PERCENTILE_DISC, 0)

        def PERIOD(self):
            return self.getToken(TeradataSQLIdentifiersParser.PERIOD, 0)

        def PIVOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.PIVOT, 0)

        def PORTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.PORTION, 0)

        def POWER(self):
            return self.getToken(TeradataSQLIdentifiersParser.POWER, 0)

        def PRECEDES(self):
            return self.getToken(TeradataSQLIdentifiersParser.PRECEDES, 0)

        def PRECEDING(self):
            return self.getToken(TeradataSQLIdentifiersParser.PRECEDING, 0)

        def PREFIX(self):
            return self.getToken(TeradataSQLIdentifiersParser.PREFIX, 0)

        def PRINT(self):
            return self.getToken(TeradataSQLIdentifiersParser.PRINT, 0)

        def PRIOR(self):
            return self.getToken(TeradataSQLIdentifiersParser.PRIOR, 0)

        def PROTECTED(self):
            return self.getToken(TeradataSQLIdentifiersParser.PROTECTED, 0)

        def QUARTER_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_BEGIN, 0)

        def QUARTER_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_END, 0)

        def QUARTER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_OF_CALENDAR, 0)

        def QUARTER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTER_OF_YEAR, 0)

        def QUARTERNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTERNUMBER_OF_CALENDAR, 0)

        def QUARTERNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUARTERNUMBER_OF_YEAR, 0)

        def QUERY(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUERY, 0)

        def QUERY_BAND(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUERY_BAND, 0)

        def QUOTECHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUOTECHAR, 0)

        def RANDOMIZED(self):
            return self.getToken(TeradataSQLIdentifiersParser.RANDOMIZED, 0)

        def RANGE(self):
            return self.getToken(TeradataSQLIdentifiersParser.RANGE, 0)

        def RANGE_L(self):
            return self.getToken(TeradataSQLIdentifiersParser.RANGE_L, 0)

        def RAPIDFIRE(self):
            return self.getToken(TeradataSQLIdentifiersParser.RAPIDFIRE, 0)

        def RDIFF(self):
            return self.getToken(TeradataSQLIdentifiersParser.RDIFF, 0)

        def READ(self):
            return self.getToken(TeradataSQLIdentifiersParser.READ, 0)

        def RECALC(self):
            return self.getToken(TeradataSQLIdentifiersParser.RECALC, 0)

        def REGEXP_INSTR(self):
            return self.getToken(TeradataSQLIdentifiersParser.REGEXP_INSTR, 0)

        def REGEXP_REPLACE(self):
            return self.getToken(TeradataSQLIdentifiersParser.REGEXP_REPLACE, 0)

        def REGEXP_SIMILAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.REGEXP_SIMILAR, 0)

        def REGEXP_SUBSTR(self):
            return self.getToken(TeradataSQLIdentifiersParser.REGEXP_SUBSTR, 0)

        def REPLACEMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.REPLACEMENT, 0)

        def RESET(self):
            return self.getToken(TeradataSQLIdentifiersParser.RESET, 0)

        def RESPECT(self):
            return self.getToken(TeradataSQLIdentifiersParser.RESPECT, 0)

        def RESTRICTWORDS(self):
            return self.getToken(TeradataSQLIdentifiersParser.RESTRICTWORDS, 0)

        def RETAIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.RETAIN, 0)

        def RETURNED_SQLSTATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.RETURNED_SQLSTATE, 0)

        def RETURNING(self):
            return self.getToken(TeradataSQLIdentifiersParser.RETURNING, 0)

        def REUSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.REUSE, 0)

        def ROOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROOT, 0)

        def ROTATELEFT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROTATELEFT, 0)

        def ROTATERIGHT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROTATERIGHT, 0)

        def ROUND(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROUND, 0)

        def ROW_COUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROW_COUNT, 0)

        def ROWIDGEN(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROWIDGEN, 0)

        def ROWIDGEN2(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROWIDGEN2, 0)

        def RPAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.RPAD, 0)

        def RTRIM(self):
            return self.getToken(TeradataSQLIdentifiersParser.RTRIM, 0)

        def RU(self):
            return self.getToken(TeradataSQLIdentifiersParser.RU, 0)

        def RULES(self):
            return self.getToken(TeradataSQLIdentifiersParser.RULES, 0)

        def RULESET(self):
            return self.getToken(TeradataSQLIdentifiersParser.RULESET, 0)

        def SAMPLES(self):
            return self.getToken(TeradataSQLIdentifiersParser.SAMPLES, 0)

        def SATURDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SATURDAY, 0)

        def SCHEMA(self):
            return self.getToken(TeradataSQLIdentifiersParser.SCHEMA, 0)

        def SCRIPT(self):
            return self.getToken(TeradataSQLIdentifiersParser.SCRIPT, 0)

        def SCRIPT_COMMAND(self):
            return self.getToken(TeradataSQLIdentifiersParser.SCRIPT_COMMAND, 0)

        def SEARCHSPACE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEARCHSPACE, 0)

        def SEARCHUIFDBPATH(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEARCHUIFDBPATH, 0)

        def SECURITY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SECURITY, 0)

        def SEED(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEED, 0)

        def SELF(self):
            return self.getToken(TeradataSQLIdentifiersParser.SELF, 0)

        def SEQ(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEQ, 0)

        def SEQUENCE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEQUENCE, 0)

        def SEQUENCED(self):
            return self.getToken(TeradataSQLIdentifiersParser.SEQUENCED, 0)

        def SERIALIZABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SERIALIZABLE, 0)

        def SERVER(self):
            return self.getToken(TeradataSQLIdentifiersParser.SERVER, 0)

        def SESSIONIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SESSIONIZE, 0)

        def SETBIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.SETBIT, 0)

        def SETRESOURCERATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SETRESOURCERATE, 0)

        def SETSESSIONACCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.SETSESSIONACCOUNT, 0)

        def SETSESSIONRATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SETSESSIONRATE, 0)

        def SHARE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SHARE, 0)

        def SHIFTLEFT(self):
            return self.getToken(TeradataSQLIdentifiersParser.SHIFTLEFT, 0)

        def SHIFTRIGHT(self):
            return self.getToken(TeradataSQLIdentifiersParser.SHIFTRIGHT, 0)

        def SIGN(self):
            return self.getToken(TeradataSQLIdentifiersParser.SIGN, 0)

        def SIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SIZE, 0)

        def SNAPPY_COMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SNAPPY_COMPRESS, 0)

        def SNAPPY_DECOMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SNAPPY_DECOMPRESS, 0)

        def SOURCE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SOURCE, 0)

        def SPARSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SPARSE, 0)

        def SPECCHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.SPECCHAR, 0)

        def SPL(self):
            return self.getToken(TeradataSQLIdentifiersParser.SPL, 0)

        def SQLSTATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SQLSTATE, 0)

        def SR(self):
            return self.getToken(TeradataSQLIdentifiersParser.SR, 0)

        def ST_GEOMETRY(self):
            return self.getToken(TeradataSQLIdentifiersParser.ST_GEOMETRY, 0)

        def STAT(self):
            return self.getToken(TeradataSQLIdentifiersParser.STAT, 0)

        def STATIC(self):
            return self.getToken(TeradataSQLIdentifiersParser.STATIC, 0)

        def STATS(self):
            return self.getToken(TeradataSQLIdentifiersParser.STATS, 0)

        def STATSUSAGE(self):
            return self.getToken(TeradataSQLIdentifiersParser.STATSUSAGE, 0)

        def STORAGE(self):
            return self.getToken(TeradataSQLIdentifiersParser.STORAGE, 0)

        def STRIP(self):
            return self.getToken(TeradataSQLIdentifiersParser.STRIP, 0)

        def STRTOK(self):
            return self.getToken(TeradataSQLIdentifiersParser.STRTOK, 0)

        def STYLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.STYLE, 0)

        def SUBBITSTR(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUBBITSTR, 0)

        def SUBCLASS_ORIGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUBCLASS_ORIGIN, 0)

        def SUCCEEDS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUCCEEDS, 0)

        def SUMMARYONLY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUMMARYONLY, 0)

        def SUNDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.SUNDAY, 0)

        def SYMBOLS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYMBOLS, 0)

        def SYSTEM(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYSTEM, 0)

        def SYSTEM_TIME(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYSTEM_TIME, 0)

        def SYSTEMTEST(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYSTEMTEST, 0)

        def TARGET(self):
            return self.getToken(TeradataSQLIdentifiersParser.TARGET, 0)

        def TD_ARRAY2P(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_ARRAY2P, 0)

        def TD_DATASET(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_DATASET, 0)

        def TD_DAY_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_DAY_OF_CALENDAR, 0)

        def TD_DAY_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_DAY_OF_MONTH, 0)

        def TD_DAY_OF_WEEK(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_DAY_OF_WEEK, 0)

        def TD_DAY_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_DAY_OF_YEAR, 0)

        def TD_GENERAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_GENERAL, 0)

        def TD_GETTIMEBUCKET(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_GETTIMEBUCKET, 0)

        def TD_INTERNAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_INTERNAL, 0)

        def TD_LZ_COMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_LZ_COMPRESS, 0)

        def TD_LZ_DECOMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_LZ_DECOMPRESS, 0)

        def TD_MONTH_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_MONTH_OF_CALENDAR, 0)

        def TD_MONTH_OF_QUARTER(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_MONTH_OF_QUARTER, 0)

        def TD_MONTH_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_MONTH_OF_YEAR, 0)

        def TD_QUARTER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_QUARTER_OF_CALENDAR, 0)

        def TD_QUARTER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_QUARTER_OF_YEAR, 0)

        def TD_TIME_BUCKET_NUMBER(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_TIME_BUCKET_NUMBER, 0)

        def TD_WEEK_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_WEEK_OF_CALENDAR, 0)

        def TD_WEEK_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_WEEK_OF_MONTH, 0)

        def TD_WEEK_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_WEEK_OF_YEAR, 0)

        def TD_WEEKDAY_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_WEEKDAY_OF_MONTH, 0)

        def TD_YEAR_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_YEAR_OF_CALENDAR, 0)

        def TDWMEVENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.TDWMEVENT, 0)

        def TDWMEXCEPTION(self):
            return self.getToken(TeradataSQLIdentifiersParser.TDWMEXCEPTION, 0)

        def TDWMHISTORY(self):
            return self.getToken(TeradataSQLIdentifiersParser.TDWMHISTORY, 0)

        def TEMPORAL_DATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TEMPORAL_DATE, 0)

        def TEMPORAL_TIMESTAMP(self):
            return self.getToken(TeradataSQLIdentifiersParser.TEMPORAL_TIMESTAMP, 0)

        def TEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.TEXT, 0)

        def THRESHOLDPERCENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.THRESHOLDPERCENT, 0)

        def THROUGH(self):
            return self.getToken(TeradataSQLIdentifiersParser.THROUGH, 0)

        def THURSDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.THURSDAY, 0)

        def TIES(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIES, 0)

        def TIMECODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIMECODE, 0)

        def TIMECOLUMN(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIMECOLUMN, 0)

        def TIMEOUT(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIMEOUT, 0)

        def TIMESTAMPCOLUMN(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIMESTAMPCOLUMN, 0)

        def TO_BYTE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_BYTE, 0)

        def TO_BYTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_BYTES, 0)

        def TO_CHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_CHAR, 0)

        def TO_DATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_DATE, 0)

        def TO_DSINTERVAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_DSINTERVAL, 0)

        def TO_NUMBER(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_NUMBER, 0)

        def TO_TIMESTAMP(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_TIMESTAMP, 0)

        def TO_TIMESTAMP_TZ(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_TIMESTAMP_TZ, 0)

        def TO_YMINTERVAL(self):
            return self.getToken(TeradataSQLIdentifiersParser.TO_YMINTERVAL, 0)

        def TOTOKEN(self):
            return self.getToken(TeradataSQLIdentifiersParser.TOTOKEN, 0)

        def TPA(self):
            return self.getToken(TeradataSQLIdentifiersParser.TPA, 0)

        def TRANSACTION_ACTIVE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRANSACTION_ACTIVE, 0)

        def TRANSUNICODETOUTF8(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRANSUNICODETOUTF8, 0)

        def TRANSUTF8TOUNICODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRANSUTF8TOUNICODE, 0)

        def TRUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUE, 0)

        def TRUNC(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUNC, 0)

        def TRUST_ONLY(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUST_ONLY, 0)

        def TTGRANULARITY(self):
            return self.getToken(TeradataSQLIdentifiersParser.TTGRANULARITY, 0)

        def TUESDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.TUESDAY, 0)

        def UBJSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.UBJSON, 0)

        def UCASE(self):
            return self.getToken(TeradataSQLIdentifiersParser.UCASE, 0)

        def UDFSEARCHPATH(self):
            return self.getToken(TeradataSQLIdentifiersParser.UDFSEARCHPATH, 0)

        def UNBOUNDED(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNBOUNDED, 0)

        def UNCOMMITTED(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNCOMMITTED, 0)

        def UNICODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNICODE, 0)

        def UNKNOWN(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNKNOWN, 0)

        def UNPIVOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNPIVOT, 0)

        def USE(self):
            return self.getToken(TeradataSQLIdentifiersParser.USE, 0)

        def USECOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.USECOUNT, 0)

        def UTILITYINFO(self):
            return self.getToken(TeradataSQLIdentifiersParser.UTILITYINFO, 0)

        def VARRAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.VARRAY, 0)

        def VERBOSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.VERBOSE, 0)

        def VERSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.VERSION, 0)

        def VERSIONING(self):
            return self.getToken(TeradataSQLIdentifiersParser.VERSIONING, 0)

        def WARNING(self):
            return self.getToken(TeradataSQLIdentifiersParser.WARNING, 0)

        def WEDNESDAY(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEDNESDAY, 0)

        def WEEK_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_BEGIN, 0)

        def WEEK_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_END, 0)

        def WEEK_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_OF_CALENDAR, 0)

        def WEEK_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_OF_MONTH, 0)

        def WEEK_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK_OF_YEAR, 0)

        def WEEKDAY_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEKDAY_OF_MONTH, 0)

        def WEEKNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEKNUMBER_OF_CALENDAR, 0)

        def WEEKNUMBER_OF_MONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEKNUMBER_OF_MONTH, 0)

        def WEEKNUMBER_OF_QUARTER(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEKNUMBER_OF_QUARTER, 0)

        def WEEKNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEKNUMBER_OF_YEAR, 0)

        def WHITESPACE(self):
            return self.getToken(TeradataSQLIdentifiersParser.WHITESPACE, 0)

        def WINDOWSIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.WINDOWSIZE, 0)

        def WITHIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.WITHIN, 0)

        def WORKLOAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.WORKLOAD, 0)

        def WRITE(self):
            return self.getToken(TeradataSQLIdentifiersParser.WRITE, 0)

        def XML(self):
            return self.getToken(TeradataSQLIdentifiersParser.XML, 0)

        def XMLAGG(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLAGG, 0)

        def XMLATTRIBUTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLATTRIBUTES, 0)

        def XMLCOMMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLCOMMENT, 0)

        def XMLCONCAT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLCONCAT, 0)

        def XMLDECLARATION(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLDECLARATION, 0)

        def XMLDOCUMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLDOCUMENT, 0)

        def XMLELEMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLELEMENT, 0)

        def XMLFOREST(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLFOREST, 0)

        def XMLNAMESPACES(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLNAMESPACES, 0)

        def XMLPARSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLPARSE, 0)

        def XMLPI(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLPI, 0)

        def XMLQUERY(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLQUERY, 0)

        def XMLSCHEMA(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLSCHEMA, 0)

        def XMLSERIALIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLSERIALIZE, 0)

        def XMLTABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLTABLE, 0)

        def XMLTEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLTEXT, 0)

        def XMLTYPE(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLTYPE, 0)

        def XMLVALIDATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLVALIDATE, 0)

        def YEAR_BEGIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEAR_BEGIN, 0)

        def YEAR_END(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEAR_END, 0)

        def YEAR_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEAR_OF_CALENDAR, 0)

        def YEARNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.YEARNUMBER_OF_CALENDAR, 0)

        def ZLIB(self):
            return self.getToken(TeradataSQLIdentifiersParser.ZLIB, 0)

        def BUCKET(self):
            return self.getToken(TeradataSQLIdentifiersParser.BUCKET, 0)

        def COMMITTED(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMMITTED, 0)

        def CREATEXML(self):
            return self.getToken(TeradataSQLIdentifiersParser.CREATEXML, 0)

        def CS_LATIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.CS_LATIN, 0)

        def CS_UNICODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.CS_UNICODE, 0)

        def CS_KANJISJIS(self):
            return self.getToken(TeradataSQLIdentifiersParser.CS_KANJISJIS, 0)

        def CS_GRAPHIC(self):
            return self.getToken(TeradataSQLIdentifiersParser.CS_GRAPHIC, 0)

        def CSV(self):
            return self.getToken(TeradataSQLIdentifiersParser.CSV, 0)

        def CSVLD(self):
            return self.getToken(TeradataSQLIdentifiersParser.CSVLD, 0)

        def DATASIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.DATASIZE, 0)

        def DAYOFMONTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYOFMONTH, 0)

        def DAYS(self):
            return self.getToken(TeradataSQLIdentifiersParser.DAYS, 0)

        def DEFINITION(self):
            return self.getToken(TeradataSQLIdentifiersParser.DEFINITION, 0)

        def DELETED(self):
            return self.getToken(TeradataSQLIdentifiersParser.DELETED, 0)

        def FAST(self):
            return self.getToken(TeradataSQLIdentifiersParser.FAST, 0)

        def LISTAGG(self):
            return self.getToken(TeradataSQLIdentifiersParser.LISTAGG, 0)

        def PATH(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATH, 0)

        def REGEXP_SPLIT_TO_TABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.REGEXP_SPLIT_TO_TABLE, 0)

        def REVERSE(self):
            return self.getToken(TeradataSQLIdentifiersParser.REVERSE, 0)

        def SAS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SAS, 0)

        def SQLTABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SQLTABLE, 0)

        def STRTOK_SPLIT_TO_TABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.STRTOK_SPLIT_TO_TABLE, 0)

        def SYSLIB(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYSLIB, 0)

        def SYSUDTLIB(self):
            return self.getToken(TeradataSQLIdentifiersParser.SYSUDTLIB, 0)

        def TD_SERVER_DB(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_SERVER_DB, 0)

        def TD_SYSFNLIB(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_SYSFNLIB, 0)

        def TD_SYSXML(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_SYSXML, 0)

        def TIMEDATEWZCONTROL(self):
            return self.getToken(TeradataSQLIdentifiersParser.TIMEDATEWZCONTROL, 0)

        def TRUST(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUST, 0)

        def TRYCAST(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRYCAST, 0)

        def UDT(self):
            return self.getToken(TeradataSQLIdentifiersParser.UDT, 0)

        def USAGE(self):
            return self.getToken(TeradataSQLIdentifiersParser.USAGE, 0)

        def VARIANT(self):
            return self.getToken(TeradataSQLIdentifiersParser.VARIANT, 0)

        def WEEK(self):
            return self.getToken(TeradataSQLIdentifiersParser.WEEK, 0)

        def WIDTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.WIDTH, 0)

        def XMLPUBLISH(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLPUBLISH, 0)

        def XMLPUBLISH_STREAM(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLPUBLISH_STREAM, 0)

        def XMLSPLIT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLSPLIT, 0)

        def LATIN_TO_UNICODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.LATIN_TO_UNICODE, 0)

        def UNICODE_TO_LATIN(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNICODE_TO_LATIN, 0)

        def LOCALE_TO_UNICODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOCALE_TO_UNICODE, 0)

        def UNICODE_TO_LOCALE(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNICODE_TO_LOCALE, 0)

        def ASBSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.ASBSON, 0)

        def ASBSONTEXT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ASBSONTEXT, 0)

        def COMBINE(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMBINE, 0)

        def EXISTVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXISTVALUE, 0)

        def JSONEXTRACT(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSONEXTRACT, 0)

        def JSONEXTRACTVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSONEXTRACTVALUE, 0)

        def JSONEXTRACTLARGEVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSONEXTRACTLARGEVALUE, 0)

        def KEYCOUNT(self):
            return self.getToken(TeradataSQLIdentifiersParser.KEYCOUNT, 0)

        def METADATA(self):
            return self.getToken(TeradataSQLIdentifiersParser.METADATA, 0)

        def STORAGE_SIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.STORAGE_SIZE, 0)

        def CREATESCHEMABASEDXML(self):
            return self.getToken(TeradataSQLIdentifiersParser.CREATESCHEMABASEDXML, 0)

        def CREATENONSCHEMABASEDXML(self):
            return self.getToken(TeradataSQLIdentifiersParser.CREATENONSCHEMABASEDXML, 0)

        def EXISTSNODE(self):
            return self.getToken(TeradataSQLIdentifiersParser.EXISTSNODE, 0)

        def ISCONTENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISCONTENT, 0)

        def ISDOCUMENT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISDOCUMENT, 0)

        def ISSCHEMAVALID(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISSCHEMAVALID, 0)

        def ISSCHEMAVALIDATED(self):
            return self.getToken(TeradataSQLIdentifiersParser.ISSCHEMAVALIDATED, 0)

        def XMLEXTRACT(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLEXTRACT, 0)

        def XMLTRANSFORM(self):
            return self.getToken(TeradataSQLIdentifiersParser.XMLTRANSFORM, 0)

        def PROC_ID(self):
            return self.getToken(TeradataSQLIdentifiersParser.PROC_ID, 0)

        def LOCATION(self):
            return self.getToken(TeradataSQLIdentifiersParser.LOCATION, 0)

        def PAYLOAD(self):
            return self.getToken(TeradataSQLIdentifiersParser.PAYLOAD, 0)

        def TRUSTED(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUSTED, 0)

        def PATHPATTERN(self):
            return self.getToken(TeradataSQLIdentifiersParser.PATHPATTERN, 0)

        def MANIFEST(self):
            return self.getToken(TeradataSQLIdentifiersParser.MANIFEST, 0)

        def ROWFORMAT(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROWFORMAT, 0)

        def STOREDAS(self):
            return self.getToken(TeradataSQLIdentifiersParser.STOREDAS, 0)

        def HEADER(self):
            return self.getToken(TeradataSQLIdentifiersParser.HEADER, 0)

        def STRIP_EXTERIOR_SPACES(self):
            return self.getToken(TeradataSQLIdentifiersParser.STRIP_EXTERIOR_SPACES, 0)

        def STRIP_ENCLOSING_CHAR(self):
            return self.getToken(TeradataSQLIdentifiersParser.STRIP_ENCLOSING_CHAR, 0)

        def RLS(self):
            return self.getToken(TeradataSQLIdentifiersParser.RLS, 0)

        def SINGLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.SINGLE, 0)

        def MULTIPLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MULTIPLE, 0)

        def JSON_COMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_COMPRESS, 0)

        def JSON_DECOMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_DECOMPRESS, 0)

        def TS_COMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.TS_COMPRESS, 0)

        def TS_DECOMPRESS(self):
            return self.getToken(TeradataSQLIdentifiersParser.TS_DECOMPRESS, 0)

        def CONTIGUOUSMAPAMPS(self):
            return self.getToken(TeradataSQLIdentifiersParser.CONTIGUOUSMAPAMPS, 0)

        def SPARSEMAPAMPS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SPARSEMAPAMPS, 0)

        def SPARSETABLEAMPS(self):
            return self.getToken(TeradataSQLIdentifiersParser.SPARSETABLEAMPS, 0)

        def UNNEST(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNNEST, 0)

        def CALCMATRIX(self):
            return self.getToken(TeradataSQLIdentifiersParser.CALCMATRIX, 0)

        def PHRASE(self):
            return self.getToken(TeradataSQLIdentifiersParser.PHRASE, 0)

        def CALCTYPE(self):
            return self.getToken(TeradataSQLIdentifiersParser.CALCTYPE, 0)

        def OUTPUT(self):
            return self.getToken(TeradataSQLIdentifiersParser.OUTPUT, 0)

        def NULL_HANDLING(self):
            return self.getToken(TeradataSQLIdentifiersParser.NULL_HANDLING, 0)

        def READ_NOS(self):
            return self.getToken(TeradataSQLIdentifiersParser.READ_NOS, 0)

        def BUFFERSIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.BUFFERSIZE, 0)

        def RETURNTYPE(self):
            return self.getToken(TeradataSQLIdentifiersParser.RETURNTYPE, 0)

        def SAMPLE_PERC(self):
            return self.getToken(TeradataSQLIdentifiersParser.SAMPLE_PERC, 0)

        def FULLSCAN(self):
            return self.getToken(TeradataSQLIdentifiersParser.FULLSCAN, 0)

        def TD_UNPIVOT(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_UNPIVOT, 0)

        def VALUE_COLUMNS(self):
            return self.getToken(TeradataSQLIdentifiersParser.VALUE_COLUMNS, 0)

        def UNPIVOT_COLUMN(self):
            return self.getToken(TeradataSQLIdentifiersParser.UNPIVOT_COLUMN, 0)

        def COLUMN_LIST(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMN_LIST, 0)

        def COLUMN_ALIAS_LIST(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLUMN_ALIAS_LIST, 0)

        def INCLUDE_NULLS(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCLUDE_NULLS, 0)

        def WRITE_NOS(self):
            return self.getToken(TeradataSQLIdentifiersParser.WRITE_NOS, 0)

        def NAMING(self):
            return self.getToken(TeradataSQLIdentifiersParser.NAMING, 0)

        def MANIFESTFILE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MANIFESTFILE, 0)

        def MANIFESTONLY(self):
            return self.getToken(TeradataSQLIdentifiersParser.MANIFESTONLY, 0)

        def OVERWRITE(self):
            return self.getToken(TeradataSQLIdentifiersParser.OVERWRITE, 0)

        def INCLUDE_ORDERING(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCLUDE_ORDERING, 0)

        def INCLUDE_HASHBY(self):
            return self.getToken(TeradataSQLIdentifiersParser.INCLUDE_HASHBY, 0)

        def MAXOBJECTSIZE(self):
            return self.getToken(TeradataSQLIdentifiersParser.MAXOBJECTSIZE, 0)

        def COMPRESSION(self):
            return self.getToken(TeradataSQLIdentifiersParser.COMPRESSION, 0)

        def ARRAY_TO_JSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.ARRAY_TO_JSON, 0)

        def BSON_CHECK(self):
            return self.getToken(TeradataSQLIdentifiersParser.BSON_CHECK, 0)

        def GEOJSONFROMGEOM(self):
            return self.getToken(TeradataSQLIdentifiersParser.GEOJSONFROMGEOM, 0)

        def GEOMFROMGEOJSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.GEOMFROMGEOJSON, 0)

        def JSON_CHECK(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_CHECK, 0)

        def JSONGETVALUE(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSONGETVALUE, 0)

        def JSONMETADATA(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSONMETADATA, 0)

        def NVP2JSON(self):
            return self.getToken(TeradataSQLIdentifiersParser.NVP2JSON, 0)

        def TD_JSONSHRED(self):
            return self.getToken(TeradataSQLIdentifiersParser.TD_JSONSHRED, 0)

        def JSON_KEYS(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_KEYS, 0)

        def JSON_TABLE(self):
            return self.getToken(TeradataSQLIdentifiersParser.JSON_TABLE, 0)

        def DEPTH(self):
            return self.getToken(TeradataSQLIdentifiersParser.DEPTH, 0)

        def QUOTES(self):
            return self.getToken(TeradataSQLIdentifiersParser.QUOTES, 0)

        def ROWEXPR(self):
            return self.getToken(TeradataSQLIdentifiersParser.ROWEXPR, 0)

        def COLEXPR(self):
            return self.getToken(TeradataSQLIdentifiersParser.COLEXPR, 0)

        def RETURNTYPES(self):
            return self.getToken(TeradataSQLIdentifiersParser.RETURNTYPES, 0)

        def NOCASE(self):
            return self.getToken(TeradataSQLIdentifiersParser.NOCASE, 0)

        def TRUNCATE(self):
            return self.getToken(TeradataSQLIdentifiersParser.TRUNCATE, 0)

        def LINK(self):
            return self.getToken(TeradataSQLIdentifiersParser.LINK, 0)

        def getRuleIndex(self):
            return TeradataSQLIdentifiersParser.RULE_nonreserved_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonreserved_word" ):
                listener.enterNonreserved_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonreserved_word" ):
                listener.exitNonreserved_word(self)




    def nonreserved_word(self):

        localctx = TeradataSQLIdentifiersParser.Nonreserved_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_nonreserved_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(((((_la - 488)) & ~0x3f) == 0 and ((1 << (_la - 488)) & -1) != 0) or ((((_la - 552)) & ~0x3f) == 0 and ((1 << (_la - 552)) & -1) != 0) or ((((_la - 616)) & ~0x3f) == 0 and ((1 << (_la - 616)) & -1) != 0) or ((((_la - 680)) & ~0x3f) == 0 and ((1 << (_la - 680)) & -1) != 0) or ((((_la - 744)) & ~0x3f) == 0 and ((1 << (_la - 744)) & -1) != 0) or ((((_la - 808)) & ~0x3f) == 0 and ((1 << (_la - 808)) & -1) != 0) or ((((_la - 872)) & ~0x3f) == 0 and ((1 << (_la - 872)) & -1) != 0) or ((((_la - 936)) & ~0x3f) == 0 and ((1 << (_la - 936)) & -1) != 0) or ((((_la - 1000)) & ~0x3f) == 0 and ((1 << (_la - 1000)) & -1) != 0) or ((((_la - 1064)) & ~0x3f) == 0 and ((1 << (_la - 1064)) & -1) != 0) or ((((_la - 1128)) & ~0x3f) == 0 and ((1 << (_la - 1128)) & -1) != 0) or _la==1192):
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





