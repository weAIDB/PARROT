-- $ID$
-- TPC-H/TPC-R Promotion Effect Query (Q14)
-- Functional Query Definition
-- Approved February 1998

--select
--    100.00 * sum(case
--        when p_type like 'PROMO%'
--            then l_extendedprice * (1 - l_discount)
--        else 0
--    end) / sum(l_extendedprice * (1 - l_discount)) as promo_revenue
--from
--    lineitem,
--    part
--where
--    l_partkey = p_partkey
--    and l_shipdate >= CAST('1995-01-01' AS DATE)
--    and l_shipdate < DATEADD(MONTH, 1, CAST('1995-01-01' AS DATE));

-- 上一次改动：
-- 1. 替换日期占位符 `:1` 为实际值。
-- 2. 使用 `DATEADD` 替代 `+ interval`。

SELECT
    100.00 * SUM(CASE
        WHEN p_type LIKE 'PROMO%' THEN l_extendedprice * (1 - l_discount)
        ELSE 0
    END) / SUM(l_extendedprice * (1 - l_discount)) AS promo_revenue
FROM
    lineitem
JOIN
    part ON l_partkey = p_partkey
WHERE
    l_shipdate >= '1995-09-01'
    AND l_shipdate < DATEADD(MONTH, 1, '1995-09-01');
