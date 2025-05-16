BULK INSERT customer
FROM 'dbgen/customer.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT lineitem
FROM 'dbgen/lineitem.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT nation
FROM 'dbgen/nation.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT orders
FROM 'dbgen/orders.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT part
FROM 'dbgen/part.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT partsupp
FROM 'dbgen/partsupp.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT region
FROM 'dbgen/region.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);

BULK INSERT supplier
FROM 'dbgen/supplier.tbl'
WITH (
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n',
    KEEPNULLS
);