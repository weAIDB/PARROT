CREATE FUNCTION checkDate(
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
