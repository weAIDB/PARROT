CREATE FUNCTION q6conditions(
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
