SELECT 
    NATION, 
    O_YEAR, 
    SUM(AMOUNT) AS SUM_PROFIT
FROM 
    (
        SELECT 
            N_NAME AS NATION, 
            TO_CHAR(CAST(O_ORDERDATE AS TIMESTAMP), 'YY') AS O_YEAR, 
            PROFIT_AMOUNT(L_EXTENDEDPRICE, L_DISCOUNT, PS_SUPPLYCOST, L_QUANTITY::INT) AS AMOUNT
        FROM 
            PART, 
            SUPPLIER, 
            LINEITEM, 
            PARTSUPP, 
            ORDERS, 
            NATION
        WHERE 
            S_SUPPKEY = L_SUPPKEY 
            AND PS_SUPPKEY = L_SUPPKEY 
            AND PS_PARTKEY = L_PARTKEY 
            AND P_PARTKEY = L_PARTKEY 
            AND O_ORDERKEY = L_ORDERKEY 
            AND S_NATIONKEY = N_NATIONKEY 
            AND P_NAME LIKE '%green%'
    ) AS PROFIT
GROUP BY 
    NATION, 
    O_YEAR
ORDER BY 
    NATION NULLS FIRST, 
    O_YEAR DESC NULLS LAST;