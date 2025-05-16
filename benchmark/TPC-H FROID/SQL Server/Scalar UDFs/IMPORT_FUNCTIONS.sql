-- Import all functions

-- Include each function script here
-- Ensure the scripts are executed in the correct order

-- discount_price.sql
GO
CREATE FUNCTION dbo.discount_price(
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN @extprice * (1 - @disc);
END;

-- discount_taxprice.sql
GO
CREATE FUNCTION dbo.discount_taxprice(
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2),
    @tax DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN dbo.discount_price(@extprice, @disc) * (1 + @tax);
END;

-- profit_amount.sql
GO
CREATE FUNCTION dbo.profit_amount(
    @extprice DECIMAL(12,2),
    @discount DECIMAL(12,2),
    @suppcost DECIMAL(12,2),
    @qty INT
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN @extprice * (1 - @discount) - @suppcost * @qty;
END;

-- isShippedBefore.sql
GO
CREATE FUNCTION dbo.isShippedBefore(
    @shipdate DATE,
    @duration INT,
    @stdatechar VARCHAR(10)
) RETURNS INT
AS
BEGIN
    DECLARE @stdate DATE = CAST(@stdatechar AS DATE);
    DECLARE @newdate DATE = DATEADD(DAY, @duration, @stdate);

    IF @shipdate > @newdate
        RETURN 0;

    RETURN 1;
END;

-- checkDate.sql
GO
CREATE FUNCTION dbo.checkDate(
    @d DATE,
    @odate DATE,
    @shipdate DATE
) RETURNS INT
AS
BEGIN
    IF @odate < @d AND @shipdate > @d
        RETURN 1;

    RETURN 0;
END;

-- q3conditions.sql
GO
CREATE FUNCTION dbo.q3conditions(
    @cmkt VARCHAR(10),
    @odate DATE,
    @shipdate DATE
) RETURNS INT
AS
BEGIN
    DECLARE @thedate DATE = '1995-03-15';

    IF @cmkt <> 'BUILDING'
        RETURN 0;

    IF dbo.checkDate(@thedate, @odate, @shipdate) = 0
        RETURN 0;

    IF dbo.isShippedBefore(@shipdate, 122, @thedate) = 0
        RETURN 0;

    RETURN 1;
END;

-- q5Conditions.sql
GO
CREATE FUNCTION dbo.q5Conditions(
    @rname CHAR(25),
    @odate DATE
) RETURNS INT
AS
BEGIN
    DECLARE @beginDate DATE = '1994-01-01';
    DECLARE @newdate DATE = DATEADD(YEAR, 1, @beginDate);

    IF @rname <> 'ASIA' OR @odate < @beginDate OR @odate >= @newdate
        RETURN 0;

    RETURN 1;
END;

-- q6conditions.sql
GO
CREATE FUNCTION dbo.q6conditions(
    @shipdate DATE,
    @discount DECIMAL(12,2),
    @qty INT
) RETURNS INT
AS
BEGIN
    DECLARE @stdate DATE = '1994-01-01';
    DECLARE @newdate DATE = DATEADD(YEAR, 1, @stdate);
    DECLARE @val DECIMAL(12,2) = 0.06;
    DECLARE @epsilon DECIMAL(12,2) = 0.01;
    DECLARE @lowerbound DECIMAL(12,2) = @val - @epsilon;
    DECLARE @upperbound DECIMAL(12,2) = @val + @epsilon;

    IF @shipdate < @stdate OR @shipdate >= @newdate OR @qty >= 24
        RETURN 0;

    IF @discount BETWEEN @lowerbound AND @upperbound
        RETURN 1;

    RETURN 0;
END;

-- q7conditions.sql
GO
CREATE FUNCTION dbo.q7conditions(
    @n1name VARCHAR(25),
    @n2name VARCHAR(25),
    @shipdate DATE
) RETURNS INT
AS
BEGIN
    IF @shipdate NOT BETWEEN '1995-01-01' AND '1996-12-31'
        RETURN 0;

    IF (@n1name = 'FRANCE' AND @n2name = 'GERMANY') OR (@n1name = 'GERMANY' AND @n2name = 'FRANCE')
        RETURN 1;

    RETURN 0;
END;

-- q10conditions.sql
GO
CREATE FUNCTION dbo.q10conditions(
    @odate DATE,
    @retflag CHAR(1)
) RETURNS INT
AS
BEGIN
    DECLARE @stdate DATE = '1993-10-01';
    DECLARE @newdate DATE = DATEADD(MONTH, 3, @stdate);

    IF @retflag <> 'R'
        RETURN 0;

    IF @odate >= @stdate AND @odate < @newdate
        RETURN 1;

    RETURN 0;
END;

-- total_value.sql
GO
CREATE FUNCTION dbo.total_value() RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN (
        SELECT SUM(PS_SUPPLYCOST * PS_AVAILQTY) * 0.0001000000
        FROM PARTSUPP
        JOIN SUPPLIER ON PS_SUPPKEY = S_SUPPKEY
        JOIN NATION ON S_NATIONKEY = N_NATIONKEY
        WHERE N_NAME = 'GERMANY'
    );
END;

-- line_count.sql
GO
CREATE FUNCTION dbo.line_count(
    @oprio CHAR(15),
    @mode VARCHAR(4)
) RETURNS INT
AS
BEGIN
    DECLARE @val INT = 0;

    IF @mode = 'high'
    BEGIN
        IF @oprio IN ('1-URGENT', '2-HIGH')
            SET @val = 1;
    END
    ELSE IF @mode = 'low'
    BEGIN
        IF @oprio IN ('1-URGENT', '2-HIGH')
            SET @val = 1;
    END;

    RETURN @val;
END;

-- q12conditions.sql
GO
CREATE FUNCTION dbo.q12conditions(
    @shipmode CHAR(10),
    @commitdate DATE,
    @receiptdate DATE,
    @shipdate DATE
) RETURNS INT
AS
BEGIN
    DECLARE @stdate DATE = '1995-09-01';
    DECLARE @newdate DATE = DATEADD(MONTH, 1, @stdate);

    IF @shipmode IN ('MAIL', 'SHIP')
    BEGIN
        IF @receiptdate < '1994-01-01'
            RETURN 0;

        IF @commitdate < @receiptdate AND @shipdate < @commitdate AND @receiptdate < @newdate
            RETURN 1;
    END;

    RETURN 0;
END;

-- promo_disc.sql
GO
CREATE FUNCTION dbo.promo_disc(
    @ptype VARCHAR(25),
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    DECLARE @val DECIMAL(12,2);

    IF @ptype LIKE 'PROMO%'
        SET @val = dbo.discount_price(@extprice, @disc);
    ELSE
        SET @val = 0.0;

    RETURN @val;
END;

-- q19conditions.sql
GO
CREATE FUNCTION dbo.q19conditions(
    @pcontainer CHAR(10),
    @lqty INT,
    @psize INT,
    @shipmode CHAR(10),
    @shipinst CHAR(25),
    @pbrand CHAR(10)
) RETURNS INT
AS
BEGIN
    DECLARE @val INT = 0;

    IF @shipmode IN ('AIR', 'AIR REG') AND @shipinst = 'DELIVER IN PERSON'
    BEGIN
        IF @pbrand = 'Brand#12' AND @pcontainer IN ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG') AND @lqty BETWEEN 1 AND 11 AND @psize BETWEEN 1 AND 5
            SET @val = 1;

        IF @pbrand = 'Brand#23' AND @pcontainer IN ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK') AND @lqty BETWEEN 10 AND 20 AND @psize BETWEEN 1 AND 10
            SET @val = 1;

        IF @pbrand = 'Brand#34' AND @pcontainer IN ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG') AND @lqty BETWEEN 20 AND 30 AND @psize BETWEEN 1 AND 15
            SET @val = 1;
    END;

    RETURN @val;
END;

-- avg_actbal.sql
GO
CREATE FUNCTION dbo.avg_actbal() RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN (
        SELECT AVG(C_ACCTBAL)
        FROM CUSTOMER
        WHERE C_ACCTBAL > 0.00
        AND LEFT(C_PHONE, 2) IN ('13', '31', '23', '29', '30', '18', '17')
    );
END;

GO