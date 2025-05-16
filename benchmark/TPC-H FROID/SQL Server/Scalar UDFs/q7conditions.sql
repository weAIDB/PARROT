CREATE FUNCTION q7conditions(
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
