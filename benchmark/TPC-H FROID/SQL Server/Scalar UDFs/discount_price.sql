CREATE FUNCTION discount_price(
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN @extprice * (1 - @disc);
END;
