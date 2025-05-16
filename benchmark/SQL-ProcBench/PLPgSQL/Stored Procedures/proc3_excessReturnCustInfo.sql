CREATE or replace function getExcessReturnCustInfo()
returns refcursor
AS $$
declare 
	c1 refcursor := 'mycursor';
BEGIN
	open c1 for
	WITH totalReturn 
			 AS (SELECT sr_customer_sk,    
						sr_store_sk,        
						Sum(sr_return_amt) as returnAmt
				 FROM   store_returns_history, 
						date_dim 
				 WHERE  sr_returned_date_sk = d_date_sk 
						AND d_year = 2001 
				 GROUP  BY sr_customer_sk, 
						   sr_store_sk) 
	SELECT distinct c_customer_id, c_email_address, cd_gender, cd_credit_rating
	FROM   totalReturn tr1, 
			store, 
			customer, 
			customer_demographics
	WHERE  tr1.returnAmt > (SELECT Avg(returnAmt) * 1.2 
							FROM   totalReturn tr2 
						    WHERE  tr1.sr_store_sk = tr2.sr_store_sk) 
			AND s_store_sk = tr1.sr_store_sk 
			AND tr1.sr_customer_sk = c_customer_sk
			AND c_current_cdemo_sk = cd_demo_sk;
			
	return c1;
end; $$
language plpgsql;



BEGIN;
SELECT getExcessReturnCustInfo();
FETCH ALL FROM mycursor;
CLOSE mycursor;
COMMIT;