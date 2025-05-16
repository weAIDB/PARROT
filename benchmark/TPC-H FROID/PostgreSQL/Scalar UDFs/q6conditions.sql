CREATE OR REPLACE FUNCTION q6conditions(
    shipdate DATE,
    discount DECIMAL(12,2),
    qty INT
) RETURNS INT AS $$
DECLARE
    stdate DATE := '1994-01-01';
    newdate DATE := stdate + INTERVAL '1 year';
    val DECIMAL(12,2) := 0.06;
    epsilon DECIMAL(12,2) := 0.01;
    lowerbound DECIMAL(12,2) := val - epsilon;
    upperbound DECIMAL(12,2) := val + epsilon;
BEGIN
    IF shipdate < stdate THEN
        RETURN 0;
    END IF;
    IF shipdate >= newdate THEN
        RETURN 0;
    END IF;
    IF qty >= 24 THEN
        RETURN 0;
    END IF;
    IF discount >= lowerbound AND discount <= upperbound THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
