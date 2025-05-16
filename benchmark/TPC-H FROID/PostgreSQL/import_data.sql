-- 导入 REGION 表数据
\COPY tpch.REGION FROM 'dbgen/region.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 NATION 表数据
\COPY tpch.NATION FROM 'dbgen/nation.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 PART 表数据
\COPY tpch.PART FROM 'dbgen/part.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 SUPPLIER 表数据
\COPY tpch.SUPPLIER FROM 'dbgen/supplier.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 CUSTOMER 表数据
\COPY tpch.CUSTOMER FROM 'dbgen/customer.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 ORDERS 表数据
\COPY tpch.ORDERS FROM 'dbgen/orders.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 PARTSUPP 表数据
\COPY tpch.PARTSUPP FROM 'dbgen/partsupp.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');

-- 导入 LINEITEM 表数据
\COPY tpch.LINEITEM FROM 'dbgen/lineitem.tbl' WITH (FORMAT csv, DELIMITER '|', NULL '');
