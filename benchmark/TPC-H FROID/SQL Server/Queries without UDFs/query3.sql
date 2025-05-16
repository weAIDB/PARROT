-- $ID$
-- TPC-H/TPC-R Shipping Priority Query (Q3)
-- Functional Query Definition
-- Approved February 1998

select
    l_orderkey,
    sum(l_extendedprice * (1 - l_discount)) as revenue,
    o_orderdate,
    o_shippriority
from
    customer,
    orders,
    lineitem
where
    c_mktsegment = 'BUILDING'
    and c_custkey = o_custkey
    and l_orderkey = o_orderkey
    and o_orderdate < CAST('1995-03-15' AS DATE)
    and l_shipdate > CAST('1995-03-15' AS DATE)
group by
    l_orderkey,
    o_orderdate,
    o_shippriority
order by
    revenue desc,
    o_orderdate;

-- 上一次改动：
-- 1. 替换占位符 `:1`, `:2` 为实际值。
-- 2. 确保日期格式符合 SQL Server 的要求。