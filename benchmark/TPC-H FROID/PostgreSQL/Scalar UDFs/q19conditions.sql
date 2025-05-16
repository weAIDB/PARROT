CREATE OR REPLACE FUNCTION q19conditions(
    pcontainer CHAR(10),
    lqty INT,
    psize INT,
    shipmode CHAR(10),
    shipinst CHAR(25),
    pbrand CHAR(10)
) RETURNS INT AS $$
DECLARE
    val INT := 0;
BEGIN
    IF shipmode IN ('AIR', 'AIR REG') AND shipinst = 'DELIVER IN PERSON' THEN
        IF pbrand = 'Brand#12' AND pcontainer IN ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG') AND lqty >= 1 AND lqty <= 11 AND psize BETWEEN 1 AND 5 THEN
            val := 1;
        END IF;
        IF pbrand = 'Brand#23' AND pcontainer IN ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK') AND lqty >= 10 AND lqty <= 20 AND psize BETWEEN 1 AND 10 THEN
            val := 1;
        END IF;
        IF pbrand = 'Brand#34' AND pcontainer IN ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG') AND lqty >= 20 AND lqty <= 30 AND psize BETWEEN 1 AND 15 THEN
            val := 1;
        END IF;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;
