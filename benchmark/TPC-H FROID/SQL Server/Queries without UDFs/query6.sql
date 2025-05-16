-- $ID$
-- TPC-H/TPC-R Forecasting Revenue Change Query (Q6)
-- Functional Query Definition
-- Approved February 1998

select
    sum(l_extendedprice * l_discount) as revenue
from
    lineitem
where
    l_shipdate >= CAST('1994-01-01' AS DATE)
    and l_shipdate < DATEADD(YEAR, 1, CAST('1994-01-01' AS DATE))
    and l_discount between 0.06 - 0.01 and 0.06 + 0.01
    and l_quantity < 24;

-- 上一次改动：
-- 1. 替换占位符 `:1`, `:2`, `:3` 为实际值。
-- 2. 使用 `DATEADD` 替代 `+ interval`。