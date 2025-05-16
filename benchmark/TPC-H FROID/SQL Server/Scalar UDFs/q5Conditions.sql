CREATE FUNCTION q5Conditions(
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
