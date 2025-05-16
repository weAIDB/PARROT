CREATE OR REPLACE FUNCTION q5Conditions(
    rname CHAR(25),
    odate DATE
) RETURNS INT AS $$
DECLARE
    beginDate DATE := '1994-01-01';
    newdate DATE := beginDate + INTERVAL '1 year';
BEGIN
    IF rname <> 'ASIA' THEN
        RETURN 0;
    END IF;
    IF odate < beginDate THEN
        RETURN 0;
    END IF;
    IF odate >= newdate THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;
