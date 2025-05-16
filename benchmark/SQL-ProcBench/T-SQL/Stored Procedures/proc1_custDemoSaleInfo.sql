--Calculate the average sales quantity, average sales price, average wholesale cost, total wholesale cost for store
--sales of different customer types (based on marital status and gender) from the given state.

CREATE PROCEDURE customerDemographicSaleInfo (@state char(2))
AS
BEGIN

	select ca_state, cd_gender, cd_marital_status, avg(ss_quantity) as avg_qty, avg(ss_sales_price) avg_sale, 
			avg(ss_ext_wholesale_cost) as avg_wholsesale, sum(ss_ext_wholesale_cost) as sum_wholesale
	from store_sales_history, customer_demographics, customer,  customer_address
	where ss_cdemo_sk = cd_demo_sk
		and c_customer_sk = ss_customer_sk
		and c_current_cdemo_sk = ca_address_sk
		and ca_state = '@state'
	group by ca_state, cd_gender, cd_marital_status  
END