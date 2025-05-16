-- $ID$
-- TPC-H/TPC-R Discounted Revenue Query (Q19)
-- Functional Query Definition
-- Approved February 1998

-- select
--     sum(l_extendedprice * (1 - l_discount)) as revenue
-- from
--     lineitem,
--     part
-- where
--     (
--         p_partkey = l_partkey
--         and p_brand = 'Brand#1'
--         and p_container in ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG')
--         and l_quantity >= 1 and l_quantity <= 11
--         and p_size between 1 and 5
--         and l_shipmode in ('AIR', 'AIR REG')
--         and l_shipinstruct = 'DELIVER IN PERSON'
--     )
--     or
--     (
--         p_partkey = l_partkey
--         and p_brand = 'Brand#2'
--         and p_container in ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK')
--         and l_quantity >= 10 and l_quantity <= 20
--         and p_size between 1 and 10
--         and l_shipmode in ('AIR', 'AIR REG')
--         and l_shipinstruct = 'DELIVER IN PERSON'
--     )
--     or
--     (
--         p_partkey = l_partkey
--         and p_brand = 'Brand#3'
--         and p_container in ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG')
--         and l_quantity >= 20 and l_quantity <= 30
--         and p_size between 1 and 15
--         and l_shipmode in ('AIR', 'AIR REG')
--         and l_shipinstruct = 'DELIVER IN PERSON'
--     );

-- 上一次改动：
-- 1. 替换占位符 `:1`, `:2`, `:3` 为实际值。
-- 2. 确保日期格式符合 SQL Server 的要求。

SELECT
    SUM(l_extendedprice * (1 - l_discount)) AS revenue
FROM
    lineitem
JOIN
    part ON p_partkey = l_partkey
WHERE
    (
        p_brand = 'Brand#12'
        AND p_container IN ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG')
        AND l_quantity BETWEEN 1 AND 11
        AND p_size BETWEEN 1 AND 5
        AND l_shipmode IN ('AIR', 'AIR REG')
        AND l_shipinstruct = 'DELIVER IN PERSON'
    )
    OR
    (
        p_brand = 'Brand#23'
        AND p_container IN ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK')
        AND l_quantity BETWEEN 10 AND 20
        AND p_size BETWEEN 1 AND 10
        AND l_shipmode IN ('AIR', 'AIR REG')
        AND l_shipinstruct = 'DELIVER IN PERSON'
    )
    OR
    (
        p_brand = 'Brand#34'
        AND p_container IN ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG')
        AND l_quantity BETWEEN 20 AND 30
        AND p_size BETWEEN 1 AND 15
        AND l_shipmode IN ('AIR', 'AIR REG')
        AND l_shipinstruct = 'DELIVER IN PERSON'
    );
