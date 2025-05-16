CREATE OR REPLACE FUNCTION isShippedBefore(
    shipdate DATE,
    duration INT,
    stdatechar VARCHAR(10)
) RETURNS INT AS $$
DECLARE
    stdate DATE := stdatechar::DATE;
    newdate DATE := stdate + (duration || ' days')::INTERVAL;
BEGIN
    IF shipdate > newdate THEN
        RETURN 0;
    END IF;
    RETURN 1;
END;
$$ LANGUAGE plpgsql;