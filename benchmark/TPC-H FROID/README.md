# TPC-H FROID
## Source

1. `Scalar UDFs` and `Queries with UDFs`: https://arxiv.org/abs/1712.00498 Section 11

2. `Queries without UDFs`: TPC-H V3.0.1/dbgen/queries

3. `create_tables`: TPC-H V3.0.1/dbgen/dss.ddl

4. `create_constraints`:TPC-H V3.0.1/dbgen/dss.ri

5. `import data`:written with AI assistant

## File Directory Structure
```
TPC-H FROID/
    PostgreSQL/
        Queries with UDFs/       
        Queries without UDFs/    
        Scalar UDFs/
        create_tables.sql       # SQL script for creating database tables.
        import_data.sql         # SQL script for importing data.   
        create_constraints.sql  # SQL script for creating constraints. 
    SQL Server/
        Queries with UDFs/       
        Queries without UDFs/    
        Scalar UDFs/
        create_tables.sql       # SQL script for creating database tables.
        import_data.sql         # SQL script for importing data.
        import_data.py          # Python script for importing data. There might be some problems while importing data using SQL script when the data load is huge. Then, use python script instead.
        create_constraints.sql  # SQL script for creating constraints.
    data/
        TPC-H V3.0.1/           # TPC-H FROID uses data from TPC-H.Using this file to generate data and queries.
    notebooks/
        queries_with_udfs/      # src and converted versions(sqlglot or AI) of sql quries and running results
        queries_without_udfs/   # src and converted versions(sqlglot or AI) of sql quries and running results
        scalar_udfs/            # src and converted versions(sqlglot or AI) of sql udfs and installing results
```

---

## Converted Method
```
TPC-H FROID/
    PostgreSQL/
        Queries with UDFs/      #   sqlglot converted and mannually fixed some parameter type issues (Q6,Q9,Q14,Q19)
        Queries without UDFs/   #   source code from TCPH
        Scalar UDFs/            #   AI converted (sqlglot cannot handdle with 'create function')
        create_tables.sql       #   edited from `SQL Server/create_table.sql`
        import_data.sql           
        create_constraints.sql  #   AI converted from source
    SQL Server/
        Queries with UDFs/      #   source code from FROID   
        Queries without UDFs/   #   AI converted (sqlglot converted version cannot work)
        Scalar UDFs/            #   source code from FROID
        create_tables.sql       #   source code 
        import_data.sql         
        import_data.py          
        create_constraints.sql  #   AI converted from source
```

