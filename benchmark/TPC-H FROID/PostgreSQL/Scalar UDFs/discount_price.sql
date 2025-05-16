CREATE OR REPLACE FUNCTION discount_price(
    extprice DECIMAL(12,2),
    disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2) AS $$
DECLARE
    result DECIMAL(12,2);
BEGIN
    result := extprice * (1 - disc);
    RETURN result;
END;
$$ LANGUAGE plpgsql;
