CREATE FUNCTION q12conditions(
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
