CREATE FUNCTION discount_taxprice(
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2),
    @tax DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN dbo.discount_price(@extprice, @disc) * (1 + @tax);
END;
