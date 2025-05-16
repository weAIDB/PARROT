CREATE OR REPLACE FUNCTION promo_disc(
    ptype VARCHAR(25),
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
DECLARE
    val DECIMAL(12,2);
BEGIN
    IF ptype LIKE 'PROMO%' THEN
        val := discount_price(extprice, disc);
    ELSE
        val := 0.0;
    END IF;
    RETURN val;
END;
$$ LANGUAGE plpgsql;
