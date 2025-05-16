CREATE FUNCTION q10conditions(
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
