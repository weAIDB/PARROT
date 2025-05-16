--most frequent reason for returns on the web

create or replace function maxReturnReasonWeb()
returns char (100)
language plpgsql
as
$$
declare
    reason_desc char(100);
    reason_id char(16);
begin
	
	select dt1.r_reason_id, dt1.r_reason_desc
    into reason_id, reason_desc
	from
		(select r_reason_id, r_reason_desc, count(*) as cnt
		from web_returns_history, reason
		where wr_reason_sk = r_reason_sk
		group by r_reason_id, r_reason_desc) dt1
	where dt1.cnt = (select max(cnt) 
					 from (select r_reason_id, r_reason_desc, count(*) as cnt
						from web_returns_history, reason
						where wr_reason_sk = r_reason_sk
						group by r_reason_id, r_reason_desc)dt2
					 );
	return reason_desc;
end;
$$;

--invocation query
select maxReturnReasonWeb() as ans;