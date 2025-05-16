CREATE FUNCTION q19conditions(
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
