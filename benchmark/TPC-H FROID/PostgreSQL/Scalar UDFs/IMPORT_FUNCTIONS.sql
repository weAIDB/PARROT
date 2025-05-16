-- Import all functions

CREATE OR REPLACE FUNCTION discount_price(
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
DECLARE
    result DECIMAL(12,2);
BEGIN
    result := extprice * (1 - disc);
    RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION discount_taxprice(
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2),
    tax DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
BEGIN
    RETURN discount_price(extprice, disc) * (1 + tax);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION profit_amount(
    extprice DECIMAL(12,2),
    discount DECIMAL(12,2),
    suppcost DECIMAL(12,2),
    qty INT
) RETURNS DECIMAL(12,2) AS $$
BEGIN
    RETURN extprice * (1 - discount) - suppcost * qty;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION isShippedBefore(
    shipdate DATE,
    duration INT,
    stdatechar VARCHAR(10)
) RETURNS INT AS $$
DECLARE
    stdate DATE := stdatechar::DATE;
    newdate DATE := stdate + (duration || ' days')::INTERVAL;
BEGIN
    IF shipdate > newdate THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION checkDate(
    d VARCHAR(10),
    odate DATE,
    shipdate DATE
) RETURNS INT AS $$
BEGIN
    IF odate < d::DATE AND shipdate > d::DATE THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q3conditions(
    cmkt VARCHAR(10),
    odate DATE,
    shipdate DATE
) RETURNS INT AS $$
DECLARE
    thedate DATE := '1995-03-15';
BEGIN
    IF cmkt <> 'BUILDING' THEN
        RETURN 0;
    END IF;
    IF checkDate(thedate::VARCHAR, odate, shipdate) = 0 THEN
        RETURN 0;
    END IF;
    IF isShippedBefore(shipdate, 122, thedate::VARCHAR) = 0 THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q5Conditions(
    rname CHAR(25),
    odate DATE
) RETURNS INT AS $$
DECLARE
    beginDate DATE := '1994-01-01';
    newdate DATE := beginDate + INTERVAL '1 year';
BEGIN
    IF rname <> 'ASIA' THEN
        RETURN 0;
    END IF;
    IF odate < beginDate THEN
        RETURN 0;
    END IF;
    IF odate >= newdate THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q6conditions(
    shipdate DATE,
    discount DECIMAL(12,2),
    qty INT
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1994-01-01';
    newdate DATE := stdate + INTERVAL '1 year';
    val DECIMAL(12,2) := 0.06;
    epsilon DECIMAL(12,2) := 0.01;
    lowerbound DECIMAL(12,2) := val - epsilon;
    upperbound DECIMAL(12,2) := val + epsilon;
BEGIN
    IF shipdate < stdate THEN
        RETURN 0;
    END IF;
    IF shipdate >= newdate THEN
        RETURN 0;
    END IF;
    IF qty >= 24 THEN
        RETURN 0;
    END IF;
    IF discount >= lowerbound AND discount <= upperbound THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q7conditions(
    n1name VARCHAR(25),
    n2name VARCHAR(25),
    shipdate DATE
) RETURNS INT AS $$
BEGIN
    IF shipdate NOT BETWEEN '1995-01-01' AND '1996-12-31' THEN
        RETURN 0;
    END IF;
    IF n1name = 'FRANCE' AND n2name = 'GERMANY' THEN
        RETURN 1;
    END IF;
    IF n1name = 'GERMANY' AND n2name = 'FRANCE' THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q10conditions(
    odate DATE,
    retflag CHAR(1)
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1993-10-01';
    newdate DATE := stdate + INTERVAL '3 months';
BEGIN
    IF retflag <> 'R' THEN
        RETURN 0;
    END IF;
    IF odate >= stdate AND odate < newdate THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q12conditions(
    shipmode CHAR(10),
    commitdate DATE,
    receiptdate DATE,
    shipdate DATE
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1995-09-01';
    newdate DATE := stdate + INTERVAL '1 month';
BEGIN
    IF shipmode IN ('MAIL', 'SHIP') THEN
        IF receiptdate < '1994-01-01' THEN
            RETURN 0;
        END IF;
        IF commitdate < receiptdate AND shipdate < commitdate AND receiptdate < newdate THEN
            RETURN 1;
        END IF;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION promo_disc(
    ptype VARCHAR(25),
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
DECLARE
    val DECIMAL(12,2);
BEGIN
    IF ptype LIKE 'PROMO%' THEN
        val := discount_price(extprice, disc);
    ELSE
        val := 0.0;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION q19conditions(
    pcontainer CHAR(10),
    lqty INT,
    psize INT,
    shipmode CHAR(10),
    shipinst CHAR(25),
    pbrand CHAR(10)
) RETURNS INT AS $$
DECLARE
    val INT := 0;
BEGIN
    IF shipmode IN ('AIR', 'AIR REG') AND shipinst = 'DELIVER IN PERSON' THEN
        IF pbrand = 'Brand#12' AND pcontainer IN ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG') AND lqty >= 1 AND lqty <= 11 AND psize BETWEEN 1 AND 5 THEN
            val := 1;
        END IF;
        IF pbrand = 'Brand#23' AND pcontainer IN ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK') AND lqty >= 10 AND lqty <= 20 AND psize BETWEEN 1 AND 10 THEN
            val := 1;
        END IF;
        IF pbrand = 'Brand#34' AND pcontainer IN ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG') AND lqty >= 20 AND lqty <= 30 AND psize BETWEEN 1 AND 15 THEN
            val := 1;
        END IF;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION total_value() RETURNS DECIMAL(12,2) AS $$
DECLARE
    total DECIMAL(12,2);
BEGIN
    SELECT SUM(PS_SUPPLYCOST * PS_AVAILQTY) * 0.0001000000
    INTO total
    FROM PARTSUPP, SUPPLIER, NATION
    WHERE PS_SUPPKEY = S_SUPPKEY
      AND S_NATIONKEY = N_NATIONKEY
      AND N_NAME = 'GERMANY';

    RETURN total;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION line_count(
    oprio CHAR(15),
    mode VARCHAR(4)
) RETURNS INT AS $$
DECLARE
    val INT := 0;
BEGIN
    IF mode = 'high' THEN
        IF oprio = '1-URGENT' OR oprio = '2-HIGH' THEN
            val := 1;
        END IF;
    ELSIF mode = 'low' THEN
        IF oprio = '1-URGENT' AND oprio = '2-HIGH' THEN
            val := 1;
        END IF;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION avg_actbal() RETURNS DECIMAL(12,2) AS $$
BEGIN
    RETURN (
        SELECT AVG(C_ACCTBAL)
        FROM CUSTOMER
        WHERE C_ACCTBAL > 0.00
        AND SUBSTRING(C_PHONE, 1, 2) IN ('13', '31', '23', '29', '30', '18', '17')
    );
END;
$$ LANGUAGE plpgsql;