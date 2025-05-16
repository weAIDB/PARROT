-- $ID$
-- TPC-H/TPC-R Shipping Modes and Order Priority Query (Q12)
-- Functional Query Definition
-- Approved February 1998

select
    l_shipmode,
    sum(case
        when o_orderpriority = '1-URGENT'
            or o_orderpriority = '2-HIGH'
            then 1
        else 0
    end) as high_line_count,
    sum(case
        when o_orderpriority <> '1-URGENT'
            and o_orderpriority <> '2-HIGH'
            then 1
        else 0
    end) as low_line_count
from
    orders,
    lineitem
where
    o_orderkey = l_orderkey
    and l_shipmode in ('MAIL', 'SHIP')
    and l_commitdate < l_receiptdate
    and l_shipdate < l_commitdate
    and l_receiptdate >= CAST('1994-01-01' AS DATE)
    and l_receiptdate < DATEADD(YEAR, 1, CAST('1994-01-01' AS DATE))
group by
    l_shipmode
order by
    l_shipmode;

-- 上一次改动：
-- 1. 替换占位符 `:1`, `:2`, `:3` 为实际值。
-- 2. 使用 `DATEADD` 替代 `+ interval`。