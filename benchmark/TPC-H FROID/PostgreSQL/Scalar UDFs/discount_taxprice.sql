CREATE OR REPLACE FUNCTION discount_taxprice(
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2),
    tax DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
BEGIN
    RETURN discount_price(extprice, disc) * (1 + tax);
END;
$$ LANGUAGE plpgsql;
