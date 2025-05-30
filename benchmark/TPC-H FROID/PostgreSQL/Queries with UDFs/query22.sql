SELECT 
    CNTRYCODE, 
    COUNT(*) AS NUMCUST, 
    SUM(C_ACCTBAL) AS TOTACCTBAL
FROM 
    (
        SELECT 
            SUBSTRING(C_PHONE FROM 1 FOR 2) AS CNTRYCODE, 
            C_ACCTBAL
        FROM 
            CUSTOMER
        WHERE 
            SUBSTRING(C_PHONE FROM 1 FOR 2) IN ('13', '31', '23', '29', '30', '18', '17') 
            AND C_ACCTBAL > AVG_ACTBAL() 
            AND NOT EXISTS (
                SELECT 
                    * 
                FROM 
                    ORDERS 
                WHERE 
                    O_CUSTKEY = C_CUSTKEY
            )
    ) AS CUSTSALE
GROUP BY 
    CNTRYCODE
ORDER BY 
    CNTRYCODE NULLS FIRST;