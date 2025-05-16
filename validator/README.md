## Preprocessing Steps

1. Verify the correctness of the given SQL in source dialect via: 
   (1) syntax checking based on different parsers (antlr, SQLGlot, sqlparse)
   (2) semantic checking based on corresponding database engine (skip (1) if possible)

2. Translate to different dialects via SQLGlot (**all the supported dialects** in SQLGlot)
```python
import sqlglot
sqlglot.transpile("SELECT STRFTIME(x, '%y-%-m-%S')", read="duckdb", write="hive")[0]
```

3. Verify the validity of the translated SQL in target dialect via:
   (1) deduplicate if the given SQL and the translated SQL is identical regardless of different formats
   (2) syntax checking based on different parsers (antlr, SQLGlot, sqlparse)
   (3) semantic checking based on corresponding database engine (skip (1) if possible)
   
4. Store the given SQL and the translated SQL in the following unified format:
**Note: the given SQL should be in the first place !!!!!**
```json
{
    "mysql": "SELECT # comment1\n  x, # comment2\n  y # comment3",
    "bigquery": "SELECT # comment1\n  x, # comment2\n  y # comment3",
    "clickhouse": "SELECT # comment1\n  x, # comment2\n  y # comment3",
    "sql": "/* comment1 */\nSELECT\n  x, /* comment2 */\n  y /* comment3 */"
}
```