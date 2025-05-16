CREATE FUNCTION line_count(
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
