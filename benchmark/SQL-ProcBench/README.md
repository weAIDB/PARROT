# SQL-ProcBench

This repository contains the SQL-ProcBench benchmark source code in 3 SQL dialects: T-SQL, PLPgSQL and PLSQL.

## Source

https://github.com/microsoft/SQL-ProcBench


## Directory Structure	
<pre> 
T-SQL/ 
  Scalar UDFs/
  Stored Procedures/
  Table Valued UDFs/
  Triggers/
PLSQL/
  Scalar UDFs/
  Stored Procedures/
  Table Valued UDFs/
  Triggers/
PLPgSQL/
  Scalar UDFs/
  Stored Procedures/
  Table Valued UDFs/
  Triggers/
SQL-ProcBench Schema.txt
indexes.txt
data/
  TPC-DS/     # Used for generating test data (TPC-DS dataset)
</pre>

There is a top level directory for each of the three dialects. Each top directory contains 4 sub-directories - one each for Scalar UDFs, Table UDFs, Stored Procedures and Triggers. Each of these directories contain the individual object files which follow the naming convention as described below. Each file has an object definition as a CREATE statement and some also include invocation query examples with plausible parameter values.

The file 'SQL-ProcBench Schema.txt' contains details about the augmented TPCDS schema used for procbench and includes the DML statements used to create the augmented tables. The same file also describes the process of loading data into the augmented tables. 

The file 'indexes.text' contains the information on indexes and index creation statements.

***File Naming Convention:*** Stored procedures are named as proc\_\<i\>\_\<name\>, scalar UDFs are named as sudf\_\<i\>\_\<name\>, table valued functions named as tvf\_\<i\>\_\<name\> and triggers are named as trig\_\<i\>\_\<name\>; where \<i\> is a number identifying the object and \<name\> is the name of the object as created inside the database.

## Setup
1. Create the required tables and indexes using the SQL-ProcBench Schema.txt and indexes.txt files.
2. Load tpc-ds data into the tables. Data loading instructions for augmented tables can be found in 'SQL-ProcBench Schema.txt' file.
3. Create procedures by using the create statement commands from the appropriate SQL dialect.
4. The query examples are given along with each procedure, which can be used to run it. 

### Known limitations:
1) The primary implementation of the benchmark has been done in T-SQL which is then translated to the other dialects. PLPgSQL and PLSQL do not have table variables and these have been implemented using set of records for some of the objects. Implementation for a few other objects which use table variables in these two dialects is still ongoing.
2) PLPgSQL and PLSQL do not support non-result accumulating select statements inside stored procedures. These have been implemented using REF CURSORS in both these dialects.


