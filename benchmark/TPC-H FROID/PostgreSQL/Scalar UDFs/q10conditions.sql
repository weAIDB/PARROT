CREATE OR REPLACE FUNCTION q10conditions(
    odate DATE,
    retflag CHAR(1)
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1993-10-01';
    newdate DATE := stdate + INTERVAL '3 months';
BEGIN
    IF retflag <> 'R' THEN
        RETURN 0;
    END IF;
    IF odate >= stdate AND odate < newdate THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
