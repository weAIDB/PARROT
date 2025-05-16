# TPC-H V3.0.1
### Purpose
- Generate test data
- Download from https://www.tpc.org/tpch/
## Usage
1. Add the following code fields to `\dbgen\tpcd.h` to support PostgreSQL:
   ```c
   #ifdef POSTGRESQL
   #define GEN_QUERY_PLAN  "explain"
   #define START_TRAN      "start transaction"
   #define END_TRAN        "commit;"
   #define SET_OUTPUT      ""
   #define SET_ROWCOUNT    "limit %d;\n"
   #define SET_DBASE       ""
   #endif
   ```
2. Complete the following content in `\dbgen\makefile.suite`:
   ```makefile
   CC = gcc
   DATABASE = DB SYSTEM
   MACHINE = OS
   WORKLOAD = TPCH
   ```
3. Compile using the `makefile`.
4. Generate data:
   ```bash
   ./dbgen -vf -s [size] 
   ```
   - `[size]` is in GB.
   - After successful execution, 8 `.tbl` files will be generated in the `\dbgen` directory.
5. For PostgreSQL, run the `processing_tbl.sh` script to process `.tbl` files and remove the trailing `|` symbol at the end of each line to adapt to PostgreSQL.

---