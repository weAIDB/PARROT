--What is the ratio between the number of items sold over the internet in the morning (8 to 9am) to the number of
--items sold in the evening (7 to 8pm) of customers with a specified number of dependents. 

create or alter function morningToEveRatio(@dep int)
returns float
as
begin
	declare @morningSale int;
	declare @eveningSale int;
	declare @ratio float;
	set @morningSale = (select  count(*)
						from web_sales_history, time_dim, customer_demographics
						where ws_sold_time_sk = t_time_sk and ws_bill_customer_sk = cd_demo_sk
							and t_hour>=8 and t_hour<=9
							and cd_dep_count=@dep);

	set @eveningSale = (select count(*)
	from web_sales_history, time_dim, customer_demographics 
	where ws_sold_time_sk = t_time_sk and ws_bill_customer_sk = cd_demo_sk
		and t_hour>=19 and t_hour<=20
		and cd_dep_count=@dep);

	set @ratio = cast (@morningSale as float) / cast (@eveningSale as float);
	return @ratio;
end
go

--invocation query
select t.depCount, dbo.morningToEveRatio(t.depCount) from
(select distinct cd_dep_count as depCount from customer_demographics)t;