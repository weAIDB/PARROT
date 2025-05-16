select
    l_returnflag,
    l_linestatus,
    sum(l_quantity) as sum_qty,
    sum(l_extendedprice) as sum_base_price,
    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
    avg(l_quantity) as avg_qty,
    avg(l_extendedprice) as avg_price,
    avg(l_discount) as avg_disc,
    count(*) as count_order
from
    lineitem
where
    l_shipdate <= DATEADD(DAY, -90, CAST('1998-12-01' AS DATE))
group by
    l_returnflag,
    l_linestatus
order by
    l_returnflag,
    l_linestatus;

-- 上一次改动：
-- 1. 确保 `DATEADD` 函数的日期参数为 SQL Server 支持的格式。
-- 2. 将日期字符串显式转换为 `DATE` 类型。