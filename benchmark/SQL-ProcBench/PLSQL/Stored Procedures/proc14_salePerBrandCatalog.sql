--Report the total extended sales price per item brand of a specific manufacturer for all catalog sales in a specific month
--of the year. 
CREATE PROCEDURE salePerBrandCatalog (yr int, mnth int, manufacture int)
AS  c1 sys_refcursor; 
BEGIN

    open c1 for 

	select i_brand, sum(cs_ext_sales_price) as totalSale
	from catalog_sales_history, item, date_dim
	where i_item_sk = cs_item_sk 
		and i_manufact_id = manufacture
		and cs_sold_date_sk = d_date_sk
		and d_year = yr
		and d_moy = mnth
	group by i_brand;
    
     dbms_sql.return_result(c1);
END; 