# SQLBench

## TPC-H FROID

### Source

https://arxiv.org/abs/1712.00498  Section 11

### File Directory Structure
```
TPC-H FROID/
   Database-name/
      create_tables.sql       # SQL script for creating database tables
      import_data.sql         # SQL script for importing data
      import_data.py          # Python script for importing data
      create_constraints.sql  # SQL script for creating constraints
      Queries with UDFs       # SQL queries using UDFs defined 
      Queries without UDFs    # SQL queries of the initial form
      Scalar UDFs             # UDFs defined
   data/
      TPC-H V3.0.1/           # used for generating test data
```
### Usage

see `README` under each directory

---

## SQL-ProcBench

### Source

https://github.com/microsoft/SQL-ProcBench

### Directory Structure	
```
T-SQL/ 
├── Scalar UDFs/
├── Stored Procedures/
├── Table Valued UDFs/
└── Triggers
PLSQL/
├── Scalar UDFs/
├── Stored Procedures/
├── Table Valued UDFs/
└──Triggers/
PLPgSQL/
├── Scalar UDFs/
├── Stored Procedures/
├── Table Valued UDFs/
├──Triggers/
└──Indexes.sql # Converted from Indexes.txt with AI assistant
data/
└── TPC-DS/       # used for generating test data
SQL-ProcBench Schema.txt
Indexes.txt

```
### Usage

1. Create tables: see`\src\SQL-ProcBench Schema.txt`

2. Create indexes: see`\src\Indexes.txt`

3. Load TPC-DS data: see `\data\TPC-DS\` download from https://www.tpc.org/tpcds/ .It is recommended to load all TPC-DS data directly into the history fact tables.

4. Create function/procedure/trigger: Use SQL statements in the corresponding SQL dialect folder

5. Run queries: Each file contains query examples for running these functions/procedures/triggers

### Extra Tips

1. `PLPgSQL/Scalar UDFs/sudf_2`: function `promoVsNoPromoItems` defined at sudf16
2. `PLPgSQL/Stored Procedures/proc60`: tckt does not exist
3. `PLPgSQL/Triggers/trig6`: modified by replace `:old` by `old`
4. `T-SQL/Scalar UDFs/sudf_2`: function `promoVsNoPromoItems` defined at sudf16



