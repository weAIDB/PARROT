CREATE FUNCTION profit_amount(
    @extprice DECIMAL(12,2),
    @discount DECIMAL(12,2),
    @suppcost DECIMAL(12,2),
    @qty INT
) RETURNS DECIMAL(12,2)
AS
BEGIN
    RETURN @extprice * (1 - @discount) - @suppcost * @qty;
END;