CREATE OR REPLACE FUNCTION line_count(
    oprio CHAR(15),
    mode VARCHAR(4)
) RETURNS INT AS $$
DECLARE
    val INT := 0;
BEGIN
    IF mode = 'high' THEN
        IF oprio = '1-URGENT' OR oprio = '2-HIGH' THEN
            val := 1;
        END IF;
    ELSIF mode = 'low' THEN
        IF oprio = '1-URGENT' AND oprio = '2-HIGH' THEN
            val := 1;
        END IF;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;
