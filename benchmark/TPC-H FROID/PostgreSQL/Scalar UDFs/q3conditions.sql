CREATE OR REPLACE FUNCTION q3conditions(
    cmkt VARCHAR(10),
    odate DATE,
    shipdate DATE
) RETURNS INT AS $$
DECLARE
    thedate DATE := '1995-03-15';
BEGIN
    IF cmkt <> 'BUILDING' THEN
        RETURN 0;
    END IF;
    IF checkDate(thedate::VARCHAR, odate, shipdate) = 0 THEN
        RETURN 0;
    END IF;
    IF isShippedBefore(shipdate, 122, thedate::VARCHAR) = 0 THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;
