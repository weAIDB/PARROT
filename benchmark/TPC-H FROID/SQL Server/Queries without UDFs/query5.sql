-- $ID$
-- TPC-H/TPC-R Local Supplier Volume Query (Q5)
-- Functional Query Definition
-- Approved February 1998

select
    n_name,
    sum(l_extendedprice * (1 - l_discount)) as revenue
from
    customer,
    orders,
    lineitem,
    supplier,
    nation,
    region
where
    c_custkey = o_custkey
    and l_orderkey = o_orderkey
    and l_suppkey = s_suppkey
    and c_nationkey = s_nationkey
    and s_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name = 'ASIA'
    and o_orderdate >= CAST('1994-01-01' AS DATE)
    and o_orderdate < DATEADD(YEAR, 1, CAST('1994-01-01' AS DATE))
group by
    n_name
order by
    revenue desc;

-- 上一次改动：
-- 1. 替换占位符 `:1`, `:2` 为实际值。
-- 2. 使用 `DATEADD` 替代 `+ interval`。