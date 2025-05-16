CREATE FUNCTION q3conditions(
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
