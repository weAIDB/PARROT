CREATE FUNCTION isShippedBefore(
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