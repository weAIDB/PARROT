CREATE OR REPLACE FUNCTION q12conditions(
    shipmode CHAR(10),
    commitdate DATE,
    receiptdate DATE,
    shipdate DATE
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1995-09-01';
    newdate DATE := stdate + INTERVAL '1 month';
BEGIN
    IF shipmode IN ('MAIL', 'SHIP') THEN
        IF receiptdate < '1994-01-01' THEN
            RETURN 0;
        END IF;
        IF commitdate < receiptdate AND shipdate < commitdate AND receiptdate < newdate THEN
            RETURN 1;
        END IF;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
