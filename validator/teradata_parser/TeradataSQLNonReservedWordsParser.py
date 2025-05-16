# Generated from sql/teradata/TeradataSQLNonReservedWordsParser.g4 by ANTLR 4.13.2
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
        4,1,1233,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,488,1192,3,0,2,1,
        0,0,0,2,3,7,0,0,0,3,1,1,0,0,0,0
    ]

class TeradataSQLNonReservedWordsParser ( Parser ):

    grammarFileName = "TeradataSQLNonReservedWordsParser.g4"

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

    RULE_nonreserved_word = 0

    ruleNames =  [ "nonreserved_word" ]

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




    class Nonreserved_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABORTSESSIONS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ABORTSESSIONS, 0)

        def ABSENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ABSENT, 0)

        def ACCESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ACCESS, 0)

        def ACCORDING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ACCORDING, 0)

        def ACCUMULATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ACCUMULATE, 0)

        def AG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AG, 0)

        def AGGGEOMINTERSECTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AGGGEOMINTERSECTION, 0)

        def AGGGEOMUNION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AGGGEOMUNION, 0)

        def ALLDBQL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLDBQL, 0)

        def ALLOCATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLOCATE, 0)

        def ALLOCATION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLOCATION, 0)

        def ALLOW(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLOW, 0)

        def ALLPARAMS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLPARAMS, 0)

        def ALLTDWM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALLTDWM, 0)

        def ALWAYS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ALWAYS, 0)

        def AMPCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AMPCOUNT, 0)

        def ANALYSIS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANALYSIS, 0)

        def ANCHOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANCHOR, 0)

        def ANCHOR_HOUR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANCHOR_HOUR, 0)

        def ANCHOR_MILLISECOND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANCHOR_MILLISECOND, 0)

        def ANCHOR_MINUTE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANCHOR_MINUTE, 0)

        def ANCHOR_SECOND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ANCHOR_SECOND, 0)

        def APPLNAME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.APPLNAME, 0)

        def ARCHIVE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARCHIVE, 0)

        def ARRAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY, 0)

        def ARRAY_ADD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_ADD, 0)

        def ARRAY_AGG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_AGG, 0)

        def ARRAY_AVG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_AVG, 0)

        def ARRAY_COMPARE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_COMPARE, 0)

        def ARRAY_CONCAT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_CONCAT, 0)

        def ARRAY_COUNT_DISTINCT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_COUNT_DISTINCT, 0)

        def ARRAY_DIV(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_DIV, 0)

        def ARRAY_EQ(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_EQ, 0)

        def ARRAY_GE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_GE, 0)

        def ARRAY_GET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_GET, 0)

        def ARRAY_GT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_GT, 0)

        def ARRAY_LE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_LE, 0)

        def ARRAY_LT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_LT, 0)

        def ARRAY_MAX(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_MAX, 0)

        def ARRAY_MIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_MIN, 0)

        def ARRAY_MOD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_MOD, 0)

        def ARRAY_MUL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_MUL, 0)

        def ARRAY_NE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_NE, 0)

        def ARRAY_SUB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_SUB, 0)

        def ARRAY_SUM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_SUM, 0)

        def ARRAY_UPDATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_UPDATE, 0)

        def ARRAY_UPDATE_STRIDE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_UPDATE_STRIDE, 0)

        def ASCII(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ASCII, 0)

        def ASSIGNMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ASSIGNMENT, 0)

        def ATTR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ATTR, 0)

        def ATTRIBUTE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ATTRIBUTE, 0)

        def ATTRIBUTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ATTRIBUTES, 0)

        def ATTRIBUTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ATTRIBUTION, 0)

        def ATTRS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ATTRS, 0)

        def AUTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AUTH, 0)

        def AUTO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AUTO, 0)

        def AUTOTEMP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AUTOTEMP, 0)

        def AVRO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.AVRO, 0)

        def BIT_LENGTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BIT_LENGTH, 0)

        def BITAND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BITAND, 0)

        def BITNOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BITNOT, 0)

        def BITOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BITOR, 0)

        def BITXOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BITXOR, 0)

        def BLOCKCOMPRESSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BLOCKCOMPRESSION, 0)

        def BLOCKCOMPRESSIONALGORITHM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BLOCKCOMPRESSIONALGORITHM, 0)

        def BLOCKCOMPRESSIONLEVEL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BLOCKCOMPRESSIONLEVEL, 0)

        def BOM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BOM, 0)

        def BOTTOM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BOTTOM, 0)

        def BSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BSON, 0)

        def C(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.C, 0)

        def CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CALENDAR, 0)

        def CALLED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CALLED, 0)

        def CALLER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CALLER, 0)

        def CAMSET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CAMSET, 0)

        def CAMSET_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CAMSET_L, 0)

        def CAPTURE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CAPTURE, 0)

        def CARDINALITY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CARDINALITY, 0)

        def CEIL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CEIL, 0)

        def CEILING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CEILING, 0)

        def CHANGERATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHANGERATE, 0)

        def CHARACTERISTICS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHARACTERISTICS, 0)

        def CHARSET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHARSET, 0)

        def CHARSET_COLL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHARSET_COLL, 0)

        def CHECKSUM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHECKSUM, 0)

        def CHR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CHR, 0)

        def CLASS_ORIGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CLASS_ORIGIN, 0)

        def CLICKLAG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CLICKLAG, 0)

        def CLIENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CLIENT, 0)

        def CNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CNT, 0)

        def COLOCATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLOCATE, 0)

        def COLUMNMETA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMNMETA, 0)

        def COLUMNS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMNS, 0)

        def COLUMNSPERINDEX(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMNSPERINDEX, 0)

        def COLUMNSPERJOININDEX(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMNSPERJOININDEX, 0)

        def COMMAND_FUNCTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMMAND_FUNCTION, 0)

        def COMMAND_FUNCTION_CODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMMAND_FUNCTION_CODE, 0)

        def COMPARISON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMPARISON, 0)

        def COMPILE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMPILE, 0)

        def CONCAT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONCAT, 0)

        def CONCURRENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONCURRENT, 0)

        def CONDITION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONDITION, 0)

        def CONDITION_IDENTIFIER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONDITION_IDENTIFIER, 0)

        def CONDITION_NUMBER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONDITION_NUMBER, 0)

        def CONTAINED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONTAINED, 0)

        def CONTAINEDTOKEN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONTAINEDTOKEN, 0)

        def CONTENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONTENT, 0)

        def CONTIGUOUS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONTIGUOUS, 0)

        def COST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COST, 0)

        def COSTS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COSTS, 0)

        def COUNTSET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COUNTSET, 0)

        def CPP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CPP, 0)

        def CPUTIME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CPUTIME, 0)

        def CPUTIMENORM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CPUTIMENORM, 0)

        def CREATEDATASET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CREATEDATASET, 0)

        def CREATOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CREATOR, 0)

        def CUME_DIST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CUME_DIST, 0)

        def CURDATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CURDATE, 0)

        def CURTIME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CURTIME, 0)

        def DATA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DATA, 0)

        def DATASET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DATASET, 0)

        def DAY_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAY_OF_CALENDAR, 0)

        def DAY_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAY_OF_MONTH, 0)

        def DAY_OF_WEEK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAY_OF_WEEK, 0)

        def DAY_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAY_OF_YEAR, 0)

        def DAYNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYNUMBER_OF_CALENDAR, 0)

        def DAYNUMBER_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYNUMBER_OF_MONTH, 0)

        def DAYNUMBER_OF_WEEK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYNUMBER_OF_WEEK, 0)

        def DAYNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYNUMBER_OF_YEAR, 0)

        def DAYOCCURRENCE_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYOCCURRENCE_OF_MONTH, 0)

        def DBA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DBA, 0)

        def DBC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DBC, 0)

        def DEBUG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DEBUG, 0)

        def DECAMSET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DECAMSET, 0)

        def DECAMSET_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DECAMSET_L, 0)

        def DECODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DECODE, 0)

        def DECOMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DECOMPRESS, 0)

        def DEFINER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DEFINER, 0)

        def DELIMITER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DELIMITER, 0)

        def DELTA_T(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DELTA_T, 0)

        def DEMOGRAPHICS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DEMOGRAPHICS, 0)

        def DENIALS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DENIALS, 0)

        def DENSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DENSE, 0)

        def DENSE_RANK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DENSE_RANK, 0)

        def DESCRIBE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DESCRIBE, 0)

        def DETAILED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DETAILED, 0)

        def DIAGNOSTICS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DIAGNOSTICS, 0)

        def DIGITS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DIGITS, 0)

        def DIMENSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DIMENSION, 0)

        def DOCUMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DOCUMENT, 0)

        def DOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DOT, 0)

        def DOWN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DOWN, 0)

        def DR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DR, 0)

        def DUPCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DUPCOUNT, 0)

        def DUPCOUNTCUM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DUPCOUNTCUM, 0)

        def EBCDIC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EBCDIC, 0)

        def EDITDISTANCE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EDITDISTANCE, 0)

        def ELAPSEDSEC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ELAPSEDSEC, 0)

        def ELAPSEDTIME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ELAPSEDTIME, 0)

        def ELEMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ELEMENT, 0)

        def ELZS_H(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ELZS_H, 0)

        def EMITNULL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EMITNULL, 0)

        def EMPTY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EMPTY, 0)

        def EMPTY_BLOB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EMPTY_BLOB, 0)

        def EMPTY_CLOB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EMPTY_CLOB, 0)

        def ENCODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ENCODE, 0)

        def ENCODING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ENCODING, 0)

        def ENCRYPT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ENCRYPT, 0)

        def ERRORS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ERRORS, 0)

        def ERRORTBL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ERRORTBL, 0)

        def EVENTCOLUMN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EVENTCOLUMN, 0)

        def EXCEPTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXCEPTION, 0)

        def EXCL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXCL, 0)

        def EXCLUDE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXCLUDE, 0)

        def EXCLUDING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXCLUDING, 0)

        def EXCLUSIVE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXCLUSIVE, 0)

        def EXPIRE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXPIRE, 0)

        def EXPORT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXPORT, 0)

        def EXPORTWIDTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXPORTWIDTH, 0)

        def FALSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FALSE, 0)

        def FEATUREINFO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FEATUREINFO, 0)

        def FILE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FILE, 0)

        def FILL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FILL, 0)

        def FILTER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FILTER, 0)

        def FINAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FINAL, 0)

        def FIRST_NOTNULL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FIRST_NOTNULL, 0)

        def FIRST_VALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FIRST_VALUE, 0)

        def FLOOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FLOOR, 0)

        def FOLLOWING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FOLLOWING, 0)

        def FOREIGNFUNCTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FOREIGNFUNCTION, 0)

        def FORTOKEN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FORTOKEN, 0)

        def FRIDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FRIDAY, 0)

        def FROM_BYTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FROM_BYTES, 0)

        def FUNCTIONPARAMETER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FUNCTIONPARAMETER, 0)

        def G(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.G, 0)

        def GETBIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GETBIT, 0)

        def GETPSFVERSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GETPSFVERSION, 0)

        def GETQUERYBAND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GETQUERYBAND, 0)

        def GETQUERYBANDVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GETQUERYBANDVALUE, 0)

        def GETTIMEZONEDISPLACEMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GETTIMEZONEDISPLACEMENT, 0)

        def GLOBAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GLOBAL, 0)

        def GLOP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GLOP, 0)

        def GREATEST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GREATEST, 0)

        def HIGH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.HIGH, 0)

        def HOST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.HOST, 0)

        def IDENTIFYDATABASE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IDENTIFYDATABASE, 0)

        def IDENTIFYSESSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IDENTIFYSESSION, 0)

        def IDENTIFYTABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IDENTIFYTABLE, 0)

        def IDENTIFYUSER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IDENTIFYUSER, 0)

        def IFP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IFP, 0)

        def IGNORE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IGNORE, 0)

        def IMMEDIATELY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IMMEDIATELY, 0)

        def IMPORT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IMPORT, 0)

        def INCLUDE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCLUDE, 0)

        def INCLUDING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCLUDING, 0)

        def INCREMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCREMENT, 0)

        def INCREMENTAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCREMENTAL, 0)

        def INDENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INDENT, 0)

        def INDEXESPERTABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INDEXESPERTABLE, 0)

        def INDEXMAINTMODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INDEXMAINTMODE, 0)

        def INIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INIT, 0)

        def INITCAP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INITCAP, 0)

        def INLINE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INLINE, 0)

        def INSTANTIABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INSTANTIABLE, 0)

        def INSTR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INSTR, 0)

        def INTERNAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INTERNAL, 0)

        def INVOKER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INVOKER, 0)

        def IOCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IOCOUNT, 0)

        def IPARTITION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.IPARTITION, 0)

        def ISOLATED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISOLATED, 0)

        def ISOLATION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISOLATION, 0)

        def JAVA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JAVA, 0)

        def JIS_COLL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JIS_COLL, 0)

        def JSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON, 0)

        def JSON_AGG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_AGG, 0)

        def JSON_COMPOSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_COMPOSE, 0)

        def K(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.K, 0)

        def KANJI1(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KANJI1, 0)

        def KANJISJIS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KANJISJIS, 0)

        def KBYTE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KBYTE, 0)

        def KBYTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KBYTES, 0)

        def KEEP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KEEP, 0)

        def KILOBYTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KILOBYTES, 0)

        def LAG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LAG, 0)

        def LAST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LAST, 0)

        def LAST_DAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LAST_DAY, 0)

        def LAST_NOTNULL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LAST_NOTNULL, 0)

        def LAST_VALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LAST_VALUE, 0)

        def LATIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LATIN, 0)

        def LDIFF(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LDIFF, 0)

        def LEAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LEAD, 0)

        def LEAST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LEAST, 0)

        def LENGTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LENGTH, 0)

        def LEVEL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LEVEL, 0)

        def LIST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LIST, 0)

        def LOAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOAD, 0)

        def LOCATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOCATE, 0)

        def LOCKEDUSEREXPIRE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOCKEDUSEREXPIRE, 0)

        def LOW(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOW, 0)

        def LPAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LPAD, 0)

        def LTRIM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LTRIM, 0)

        def LZCOMP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LZCOMP, 0)

        def LZCOMP_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LZCOMP_L, 0)

        def LZDECOMP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LZDECOMP, 0)

        def LZDECOMP_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LZDECOMP_L, 0)

        def M(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.M, 0)

        def MAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAD, 0)

        def MANUAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MANUAL, 0)

        def MAPPING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAPPING, 0)

        def MATCHED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MATCHED, 0)

        def MAX_CHOOSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAX_CHOOSE, 0)

        def MAXCHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXCHAR, 0)

        def MAXINTERVALS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXINTERVALS, 0)

        def MAXLOGONATTEMPTS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXLOGONATTEMPTS, 0)

        def MAXVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXVALUE, 0)

        def MAXVALUELENGTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXVALUELENGTH, 0)

        def MEDIAN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MEDIAN, 0)

        def MEDIUM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MEDIUM, 0)

        def MEETS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MEETS, 0)

        def MEMBER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MEMBER, 0)

        def MERGEBLOCKRATIO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MERGEBLOCKRATIO, 0)

        def MESSAGE_LENGTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MESSAGE_LENGTH, 0)

        def MESSAGE_TEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MESSAGE_TEXT, 0)

        def MIN_CHOOSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MIN_CHOOSE, 0)

        def MINCHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MINCHAR, 0)

        def MINVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MINVALUE, 0)

        def MODIFIED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MODIFIED, 0)

        def MONDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONDAY, 0)

        def MONITORQUERYBAND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONITORQUERYBAND, 0)

        def MONITORSESSIONRATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONITORSESSIONRATE, 0)

        def MONITORVERSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONITORVERSION, 0)

        def MONTH_BEGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTH_BEGIN, 0)

        def MONTH_END(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTH_END, 0)

        def MONTH_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTH_OF_CALENDAR, 0)

        def MONTH_OF_QUARTER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTH_OF_QUARTER, 0)

        def MONTH_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTH_OF_YEAR, 0)

        def MONTHNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTHNUMBER_OF_CALENDAR, 0)

        def MONTHNUMBER_OF_QUARTER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTHNUMBER_OF_QUARTER, 0)

        def MONTHNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTHNUMBER_OF_YEAR, 0)

        def MONTHS_BETWEEN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MONTHS_BETWEEN, 0)

        def MORE_(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MORE_, 0)

        def MULTINATIONAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MULTINATIONAL, 0)

        def NAME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NAME, 0)

        def NAMESPACE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NAMESPACE, 0)

        def NEVER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NEVER, 0)

        def NEXT_DAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NEXT_DAY, 0)

        def NGRAM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NGRAM, 0)

        def NIL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NIL, 0)

        def NODDLTEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NODDLTEXT, 0)

        def NODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NODE, 0)

        def NONOPTCOST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NONOPTCOST, 0)

        def NONOPTINIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NONOPTINIT, 0)

        def NONSEQUENCED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NONSEQUENCED, 0)

        def NORIGHT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NORIGHT, 0)

        def NOSEXTRACTVARFROMPATH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NOSEXTRACTVARFROMPATH, 0)

        def NOTATION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NOTATION, 0)

        def NOW(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NOW, 0)

        def NPATH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NPATH, 0)

        def NTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NTH, 0)

        def NULLS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NULLS, 0)

        def NUMFPFNS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NUMFPFNS, 0)

        def NUMTODSINTERVAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NUMTODSINTERVAL, 0)

        def NUMTOYMINTERVAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NUMTOYMINTERVAL, 0)

        def NVL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NVL, 0)

        def NVL2(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NVL2, 0)

        def NVP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NVP, 0)

        def OA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OA, 0)

        def OADD_MONTHS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OADD_MONTHS, 0)

        def OCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OCOUNT, 0)

        def ODELETE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ODELETE, 0)

        def OEXISTS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OEXISTS, 0)

        def OEXTEND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OEXTEND, 0)

        def OFIRST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OFIRST, 0)

        def OLAST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OLAST, 0)

        def OLD_NEW_TABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OLD_NEW_TABLE, 0)

        def OLIMIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OLIMIT, 0)

        def ONEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ONEXT, 0)

        def ONLINE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ONLINE, 0)

        def OPRIOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OPRIOR, 0)

        def OPTIONS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OPTIONS, 0)

        def ORDERBYVALUES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ORDERBYVALUES, 0)

        def ORDERED_ANALYTIC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ORDERED_ANALYTIC, 0)

        def ORDINALITY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ORDINALITY, 0)

        def OREPLACE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OREPLACE, 0)

        def OTRANSLATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OTRANSLATE, 0)

        def OTRIM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OTRIM, 0)

        def OVERLAYS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OVERLAYS, 0)

        def OWNER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OWNER, 0)

        def P_INTERSECT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.P_INTERSECT, 0)

        def P_NORMALIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.P_NORMALIZE, 0)

        def PARAMID(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARAMID, 0)

        def PARAMINFO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARAMINFO, 0)

        def PARENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARENT, 0)

        def PARTITION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARTITION, 0)

        def PARTITION_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARTITION_L, 0)

        def PARTITIONED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARTITIONED, 0)

        def PARTITIONNAMES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PARTITIONNAMES, 0)

        def PASS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PASS, 0)

        def PASSING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PASSING, 0)

        def PATH_GENERATOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATH_GENERATOR, 0)

        def PATH_START(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATH_START, 0)

        def PATH_SUMMARIZER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATH_SUMMARIZER, 0)

        def PATTERN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATTERN, 0)

        def PERCENTILE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PERCENTILE, 0)

        def PERCENTILE_CONT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PERCENTILE_CONT, 0)

        def PERCENTILE_DISC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PERCENTILE_DISC, 0)

        def PERIOD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PERIOD, 0)

        def PIVOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PIVOT, 0)

        def PORTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PORTION, 0)

        def POWER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.POWER, 0)

        def PRECEDES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PRECEDES, 0)

        def PRECEDING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PRECEDING, 0)

        def PREFIX(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PREFIX, 0)

        def PRINT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PRINT, 0)

        def PRIOR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PRIOR, 0)

        def PROTECTED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PROTECTED, 0)

        def QUARTER_BEGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTER_BEGIN, 0)

        def QUARTER_END(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTER_END, 0)

        def QUARTER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTER_OF_CALENDAR, 0)

        def QUARTER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTER_OF_YEAR, 0)

        def QUARTERNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTERNUMBER_OF_CALENDAR, 0)

        def QUARTERNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUARTERNUMBER_OF_YEAR, 0)

        def QUERY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUERY, 0)

        def QUERY_BAND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUERY_BAND, 0)

        def QUOTECHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUOTECHAR, 0)

        def RANDOMIZED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RANDOMIZED, 0)

        def RANGE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RANGE, 0)

        def RANGE_L(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RANGE_L, 0)

        def RAPIDFIRE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RAPIDFIRE, 0)

        def RDIFF(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RDIFF, 0)

        def READ(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.READ, 0)

        def RECALC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RECALC, 0)

        def REGEXP_INSTR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REGEXP_INSTR, 0)

        def REGEXP_REPLACE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REGEXP_REPLACE, 0)

        def REGEXP_SIMILAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REGEXP_SIMILAR, 0)

        def REGEXP_SUBSTR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REGEXP_SUBSTR, 0)

        def REPLACEMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REPLACEMENT, 0)

        def RESET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RESET, 0)

        def RESPECT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RESPECT, 0)

        def RESTRICTWORDS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RESTRICTWORDS, 0)

        def RETAIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RETAIN, 0)

        def RETURNED_SQLSTATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RETURNED_SQLSTATE, 0)

        def RETURNING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RETURNING, 0)

        def REUSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REUSE, 0)

        def ROOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROOT, 0)

        def ROTATELEFT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROTATELEFT, 0)

        def ROTATERIGHT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROTATERIGHT, 0)

        def ROUND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROUND, 0)

        def ROW_COUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROW_COUNT, 0)

        def ROWIDGEN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROWIDGEN, 0)

        def ROWIDGEN2(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROWIDGEN2, 0)

        def RPAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RPAD, 0)

        def RTRIM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RTRIM, 0)

        def RU(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RU, 0)

        def RULES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RULES, 0)

        def RULESET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RULESET, 0)

        def SAMPLES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SAMPLES, 0)

        def SATURDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SATURDAY, 0)

        def SCHEMA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SCHEMA, 0)

        def SCRIPT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SCRIPT, 0)

        def SCRIPT_COMMAND(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SCRIPT_COMMAND, 0)

        def SEARCHSPACE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEARCHSPACE, 0)

        def SEARCHUIFDBPATH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEARCHUIFDBPATH, 0)

        def SECURITY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SECURITY, 0)

        def SEED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEED, 0)

        def SELF(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SELF, 0)

        def SEQ(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEQ, 0)

        def SEQUENCE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEQUENCE, 0)

        def SEQUENCED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SEQUENCED, 0)

        def SERIALIZABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SERIALIZABLE, 0)

        def SERVER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SERVER, 0)

        def SESSIONIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SESSIONIZE, 0)

        def SETBIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SETBIT, 0)

        def SETRESOURCERATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SETRESOURCERATE, 0)

        def SETSESSIONACCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SETSESSIONACCOUNT, 0)

        def SETSESSIONRATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SETSESSIONRATE, 0)

        def SHARE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SHARE, 0)

        def SHIFTLEFT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SHIFTLEFT, 0)

        def SHIFTRIGHT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SHIFTRIGHT, 0)

        def SIGN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SIGN, 0)

        def SIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SIZE, 0)

        def SNAPPY_COMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SNAPPY_COMPRESS, 0)

        def SNAPPY_DECOMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SNAPPY_DECOMPRESS, 0)

        def SOURCE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SOURCE, 0)

        def SPARSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SPARSE, 0)

        def SPECCHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SPECCHAR, 0)

        def SPL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SPL, 0)

        def SQLSTATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SQLSTATE, 0)

        def SR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SR, 0)

        def ST_GEOMETRY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ST_GEOMETRY, 0)

        def STAT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STAT, 0)

        def STATIC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STATIC, 0)

        def STATS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STATS, 0)

        def STATSUSAGE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STATSUSAGE, 0)

        def STORAGE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STORAGE, 0)

        def STRIP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STRIP, 0)

        def STRTOK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STRTOK, 0)

        def STYLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STYLE, 0)

        def SUBBITSTR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SUBBITSTR, 0)

        def SUBCLASS_ORIGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SUBCLASS_ORIGIN, 0)

        def SUCCEEDS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SUCCEEDS, 0)

        def SUMMARYONLY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SUMMARYONLY, 0)

        def SUNDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SUNDAY, 0)

        def SYMBOLS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYMBOLS, 0)

        def SYSTEM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYSTEM, 0)

        def SYSTEM_TIME(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYSTEM_TIME, 0)

        def SYSTEMTEST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYSTEMTEST, 0)

        def TARGET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TARGET, 0)

        def TD_ARRAY2P(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_ARRAY2P, 0)

        def TD_DATASET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_DATASET, 0)

        def TD_DAY_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_DAY_OF_CALENDAR, 0)

        def TD_DAY_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_DAY_OF_MONTH, 0)

        def TD_DAY_OF_WEEK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_DAY_OF_WEEK, 0)

        def TD_DAY_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_DAY_OF_YEAR, 0)

        def TD_GENERAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_GENERAL, 0)

        def TD_GETTIMEBUCKET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_GETTIMEBUCKET, 0)

        def TD_INTERNAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_INTERNAL, 0)

        def TD_LZ_COMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_LZ_COMPRESS, 0)

        def TD_LZ_DECOMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_LZ_DECOMPRESS, 0)

        def TD_MONTH_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_MONTH_OF_CALENDAR, 0)

        def TD_MONTH_OF_QUARTER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_MONTH_OF_QUARTER, 0)

        def TD_MONTH_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_MONTH_OF_YEAR, 0)

        def TD_QUARTER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_QUARTER_OF_CALENDAR, 0)

        def TD_QUARTER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_QUARTER_OF_YEAR, 0)

        def TD_TIME_BUCKET_NUMBER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_TIME_BUCKET_NUMBER, 0)

        def TD_WEEK_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_WEEK_OF_CALENDAR, 0)

        def TD_WEEK_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_WEEK_OF_MONTH, 0)

        def TD_WEEK_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_WEEK_OF_YEAR, 0)

        def TD_WEEKDAY_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_WEEKDAY_OF_MONTH, 0)

        def TD_YEAR_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_YEAR_OF_CALENDAR, 0)

        def TDWMEVENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TDWMEVENT, 0)

        def TDWMEXCEPTION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TDWMEXCEPTION, 0)

        def TDWMHISTORY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TDWMHISTORY, 0)

        def TEMPORAL_DATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TEMPORAL_DATE, 0)

        def TEMPORAL_TIMESTAMP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TEMPORAL_TIMESTAMP, 0)

        def TEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TEXT, 0)

        def THRESHOLDPERCENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.THRESHOLDPERCENT, 0)

        def THROUGH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.THROUGH, 0)

        def THURSDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.THURSDAY, 0)

        def TIES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIES, 0)

        def TIMECODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIMECODE, 0)

        def TIMECOLUMN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIMECOLUMN, 0)

        def TIMEOUT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIMEOUT, 0)

        def TIMESTAMPCOLUMN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIMESTAMPCOLUMN, 0)

        def TO_BYTE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_BYTE, 0)

        def TO_BYTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_BYTES, 0)

        def TO_CHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_CHAR, 0)

        def TO_DATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_DATE, 0)

        def TO_DSINTERVAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_DSINTERVAL, 0)

        def TO_NUMBER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_NUMBER, 0)

        def TO_TIMESTAMP(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_TIMESTAMP, 0)

        def TO_TIMESTAMP_TZ(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_TIMESTAMP_TZ, 0)

        def TO_YMINTERVAL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TO_YMINTERVAL, 0)

        def TOTOKEN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TOTOKEN, 0)

        def TPA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TPA, 0)

        def TRANSACTION_ACTIVE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRANSACTION_ACTIVE, 0)

        def TRANSUNICODETOUTF8(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRANSUNICODETOUTF8, 0)

        def TRANSUTF8TOUNICODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRANSUTF8TOUNICODE, 0)

        def TRUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUE, 0)

        def TRUNC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUNC, 0)

        def TRUST_ONLY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUST_ONLY, 0)

        def TTGRANULARITY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TTGRANULARITY, 0)

        def TUESDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TUESDAY, 0)

        def UBJSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UBJSON, 0)

        def UCASE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UCASE, 0)

        def UDFSEARCHPATH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UDFSEARCHPATH, 0)

        def UNBOUNDED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNBOUNDED, 0)

        def UNCOMMITTED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNCOMMITTED, 0)

        def UNICODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNICODE, 0)

        def UNKNOWN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNKNOWN, 0)

        def UNPIVOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNPIVOT, 0)

        def USE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.USE, 0)

        def USECOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.USECOUNT, 0)

        def UTILITYINFO(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UTILITYINFO, 0)

        def VARRAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VARRAY, 0)

        def VERBOSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VERBOSE, 0)

        def VERSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VERSION, 0)

        def VERSIONING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VERSIONING, 0)

        def WARNING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WARNING, 0)

        def WEDNESDAY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEDNESDAY, 0)

        def WEEK_BEGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK_BEGIN, 0)

        def WEEK_END(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK_END, 0)

        def WEEK_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK_OF_CALENDAR, 0)

        def WEEK_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK_OF_MONTH, 0)

        def WEEK_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK_OF_YEAR, 0)

        def WEEKDAY_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEKDAY_OF_MONTH, 0)

        def WEEKNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEKNUMBER_OF_CALENDAR, 0)

        def WEEKNUMBER_OF_MONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEKNUMBER_OF_MONTH, 0)

        def WEEKNUMBER_OF_QUARTER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEKNUMBER_OF_QUARTER, 0)

        def WEEKNUMBER_OF_YEAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEKNUMBER_OF_YEAR, 0)

        def WHITESPACE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WHITESPACE, 0)

        def WINDOWSIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WINDOWSIZE, 0)

        def WITHIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WITHIN, 0)

        def WORKLOAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WORKLOAD, 0)

        def WRITE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WRITE, 0)

        def XML(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XML, 0)

        def XMLAGG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLAGG, 0)

        def XMLATTRIBUTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLATTRIBUTES, 0)

        def XMLCOMMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLCOMMENT, 0)

        def XMLCONCAT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLCONCAT, 0)

        def XMLDECLARATION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLDECLARATION, 0)

        def XMLDOCUMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLDOCUMENT, 0)

        def XMLELEMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLELEMENT, 0)

        def XMLFOREST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLFOREST, 0)

        def XMLNAMESPACES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLNAMESPACES, 0)

        def XMLPARSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLPARSE, 0)

        def XMLPI(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLPI, 0)

        def XMLQUERY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLQUERY, 0)

        def XMLSCHEMA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLSCHEMA, 0)

        def XMLSERIALIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLSERIALIZE, 0)

        def XMLTABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLTABLE, 0)

        def XMLTEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLTEXT, 0)

        def XMLTYPE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLTYPE, 0)

        def XMLVALIDATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLVALIDATE, 0)

        def YEAR_BEGIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.YEAR_BEGIN, 0)

        def YEAR_END(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.YEAR_END, 0)

        def YEAR_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.YEAR_OF_CALENDAR, 0)

        def YEARNUMBER_OF_CALENDAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.YEARNUMBER_OF_CALENDAR, 0)

        def ZLIB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ZLIB, 0)

        def BUCKET(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BUCKET, 0)

        def COMMITTED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMMITTED, 0)

        def CREATEXML(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CREATEXML, 0)

        def CS_LATIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CS_LATIN, 0)

        def CS_UNICODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CS_UNICODE, 0)

        def CS_KANJISJIS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CS_KANJISJIS, 0)

        def CS_GRAPHIC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CS_GRAPHIC, 0)

        def CSV(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CSV, 0)

        def CSVLD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CSVLD, 0)

        def DATASIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DATASIZE, 0)

        def DAYOFMONTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYOFMONTH, 0)

        def DAYS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DAYS, 0)

        def DEFINITION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DEFINITION, 0)

        def DELETED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DELETED, 0)

        def FAST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FAST, 0)

        def LISTAGG(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LISTAGG, 0)

        def PATH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATH, 0)

        def REGEXP_SPLIT_TO_TABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REGEXP_SPLIT_TO_TABLE, 0)

        def REVERSE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.REVERSE, 0)

        def SAS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SAS, 0)

        def SQLTABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SQLTABLE, 0)

        def STRTOK_SPLIT_TO_TABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STRTOK_SPLIT_TO_TABLE, 0)

        def SYSLIB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYSLIB, 0)

        def SYSUDTLIB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SYSUDTLIB, 0)

        def TD_SERVER_DB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_SERVER_DB, 0)

        def TD_SYSFNLIB(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_SYSFNLIB, 0)

        def TD_SYSXML(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_SYSXML, 0)

        def TIMEDATEWZCONTROL(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TIMEDATEWZCONTROL, 0)

        def TRUST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUST, 0)

        def TRYCAST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRYCAST, 0)

        def UDT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UDT, 0)

        def USAGE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.USAGE, 0)

        def VARIANT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VARIANT, 0)

        def WEEK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WEEK, 0)

        def WIDTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WIDTH, 0)

        def XMLPUBLISH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLPUBLISH, 0)

        def XMLPUBLISH_STREAM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLPUBLISH_STREAM, 0)

        def XMLSPLIT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLSPLIT, 0)

        def LATIN_TO_UNICODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LATIN_TO_UNICODE, 0)

        def UNICODE_TO_LATIN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNICODE_TO_LATIN, 0)

        def LOCALE_TO_UNICODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOCALE_TO_UNICODE, 0)

        def UNICODE_TO_LOCALE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNICODE_TO_LOCALE, 0)

        def ASBSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ASBSON, 0)

        def ASBSONTEXT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ASBSONTEXT, 0)

        def COMBINE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMBINE, 0)

        def EXISTVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXISTVALUE, 0)

        def JSONEXTRACT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSONEXTRACT, 0)

        def JSONEXTRACTVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSONEXTRACTVALUE, 0)

        def JSONEXTRACTLARGEVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSONEXTRACTLARGEVALUE, 0)

        def KEYCOUNT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.KEYCOUNT, 0)

        def METADATA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.METADATA, 0)

        def STORAGE_SIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STORAGE_SIZE, 0)

        def CREATESCHEMABASEDXML(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CREATESCHEMABASEDXML, 0)

        def CREATENONSCHEMABASEDXML(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CREATENONSCHEMABASEDXML, 0)

        def EXISTSNODE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.EXISTSNODE, 0)

        def ISCONTENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISCONTENT, 0)

        def ISDOCUMENT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISDOCUMENT, 0)

        def ISSCHEMAVALID(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISSCHEMAVALID, 0)

        def ISSCHEMAVALIDATED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ISSCHEMAVALIDATED, 0)

        def XMLEXTRACT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLEXTRACT, 0)

        def XMLTRANSFORM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.XMLTRANSFORM, 0)

        def PROC_ID(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PROC_ID, 0)

        def LOCATION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LOCATION, 0)

        def PAYLOAD(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PAYLOAD, 0)

        def TRUSTED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUSTED, 0)

        def PATHPATTERN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PATHPATTERN, 0)

        def MANIFEST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MANIFEST, 0)

        def ROWFORMAT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROWFORMAT, 0)

        def STOREDAS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STOREDAS, 0)

        def HEADER(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.HEADER, 0)

        def STRIP_EXTERIOR_SPACES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STRIP_EXTERIOR_SPACES, 0)

        def STRIP_ENCLOSING_CHAR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.STRIP_ENCLOSING_CHAR, 0)

        def RLS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RLS, 0)

        def SINGLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SINGLE, 0)

        def MULTIPLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MULTIPLE, 0)

        def JSON_COMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_COMPRESS, 0)

        def JSON_DECOMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_DECOMPRESS, 0)

        def TS_COMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TS_COMPRESS, 0)

        def TS_DECOMPRESS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TS_DECOMPRESS, 0)

        def CONTIGUOUSMAPAMPS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CONTIGUOUSMAPAMPS, 0)

        def SPARSEMAPAMPS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SPARSEMAPAMPS, 0)

        def SPARSETABLEAMPS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SPARSETABLEAMPS, 0)

        def UNNEST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNNEST, 0)

        def CALCMATRIX(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CALCMATRIX, 0)

        def PHRASE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.PHRASE, 0)

        def CALCTYPE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.CALCTYPE, 0)

        def OUTPUT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OUTPUT, 0)

        def NULL_HANDLING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NULL_HANDLING, 0)

        def READ_NOS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.READ_NOS, 0)

        def BUFFERSIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BUFFERSIZE, 0)

        def RETURNTYPE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RETURNTYPE, 0)

        def SAMPLE_PERC(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.SAMPLE_PERC, 0)

        def FULLSCAN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.FULLSCAN, 0)

        def TD_UNPIVOT(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_UNPIVOT, 0)

        def VALUE_COLUMNS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.VALUE_COLUMNS, 0)

        def UNPIVOT_COLUMN(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.UNPIVOT_COLUMN, 0)

        def COLUMN_LIST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMN_LIST, 0)

        def COLUMN_ALIAS_LIST(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLUMN_ALIAS_LIST, 0)

        def INCLUDE_NULLS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCLUDE_NULLS, 0)

        def WRITE_NOS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.WRITE_NOS, 0)

        def NAMING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NAMING, 0)

        def MANIFESTFILE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MANIFESTFILE, 0)

        def MANIFESTONLY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MANIFESTONLY, 0)

        def OVERWRITE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.OVERWRITE, 0)

        def INCLUDE_ORDERING(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCLUDE_ORDERING, 0)

        def INCLUDE_HASHBY(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.INCLUDE_HASHBY, 0)

        def MAXOBJECTSIZE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.MAXOBJECTSIZE, 0)

        def COMPRESSION(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COMPRESSION, 0)

        def ARRAY_TO_JSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ARRAY_TO_JSON, 0)

        def BSON_CHECK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.BSON_CHECK, 0)

        def GEOJSONFROMGEOM(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GEOJSONFROMGEOM, 0)

        def GEOMFROMGEOJSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.GEOMFROMGEOJSON, 0)

        def JSON_CHECK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_CHECK, 0)

        def JSONGETVALUE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSONGETVALUE, 0)

        def JSONMETADATA(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSONMETADATA, 0)

        def NVP2JSON(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NVP2JSON, 0)

        def TD_JSONSHRED(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TD_JSONSHRED, 0)

        def JSON_KEYS(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_KEYS, 0)

        def JSON_TABLE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.JSON_TABLE, 0)

        def DEPTH(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.DEPTH, 0)

        def QUOTES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.QUOTES, 0)

        def ROWEXPR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.ROWEXPR, 0)

        def COLEXPR(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.COLEXPR, 0)

        def RETURNTYPES(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.RETURNTYPES, 0)

        def NOCASE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.NOCASE, 0)

        def TRUNCATE(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.TRUNCATE, 0)

        def LINK(self):
            return self.getToken(TeradataSQLNonReservedWordsParser.LINK, 0)

        def getRuleIndex(self):
            return TeradataSQLNonReservedWordsParser.RULE_nonreserved_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonreserved_word" ):
                listener.enterNonreserved_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonreserved_word" ):
                listener.exitNonreserved_word(self)




    def nonreserved_word(self):

        localctx = TeradataSQLNonReservedWordsParser.Nonreserved_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nonreserved_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
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





