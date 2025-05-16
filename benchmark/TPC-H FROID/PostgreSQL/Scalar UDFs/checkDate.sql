CREATE OR REPLACE FUNCTION checkDate(
    d VARCHAR(10),
    odate DATE,
    shipdate DATE
) RETURNS INT AS $$
BEGIN
    IF odate < d::DATE AND shipdate > d::DATE THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
