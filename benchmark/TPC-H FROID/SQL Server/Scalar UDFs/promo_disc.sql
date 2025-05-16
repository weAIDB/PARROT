CREATE FUNCTION promo_disc(
    @ptype VARCHAR(25),
    @extprice DECIMAL(12,2),
    @disc DECIMAL(12,2)
) RETURNS DECIMAL(12,2)
AS
BEGIN
    DECLARE @val DECIMAL(12,2);

    IF @ptype LIKE 'PROMO%'
        SET @val = dbo.discount_price(@extprice, @disc);
    ELSE
        SET @val = 0.0;

    RETURN @val;
END;
