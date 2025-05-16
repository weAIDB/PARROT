CREATE OR REPLACE FUNCTION q7conditions(
    n1name VARCHAR(25),
    n2name VARCHAR(25),
    shipdate DATE
) RETURNS INT AS $$
BEGIN
    IF shipdate NOT BETWEEN '1995-01-01' AND '1996-12-31' THEN
        RETURN 0;
    END IF;
    IF n1name = 'FRANCE' AND n2name = 'GERMANY' THEN
        RETURN 1;
    END IF;
    IF n1name = 'GERMANY' AND n2name = 'FRANCE' THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
