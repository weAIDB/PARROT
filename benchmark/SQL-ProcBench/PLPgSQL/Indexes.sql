-- 为历史表创建 BRIN 索引
CREATE INDEX cci_ws ON web_sales_history USING brin (ws_sold_date_sk);
CREATE INDEX cci_wrh ON web_returns_history USING brin (wr_returned_date_sk);
CREATE INDEX cci_cs ON catalog_sales_history USING brin (cs_sold_date_sk);
CREATE INDEX cci_crh ON catalog_returns_history USING brin (cr_returned_date_sk);
CREATE INDEX cci_ssh ON store_sales_history USING brin (ss_sold_date_sk);
CREATE INDEX cci_srh ON store_returns_history USING brin (sr_returned_date_sk);
CREATE INDEX cci_ih ON inventory_history USING brin (inv_date_sk);

-- 为销售和库存表创建 B-Tree 索引
CREATE INDEX csDate ON catalog_sales (cs_sold_date_sk);
CREATE INDEX ssDate ON store_sales (ss_sold_date_sk);
CREATE INDEX wsDate ON web_sales (ws_sold_date_sk);
CREATE INDEX invDate ON inventory (inv_date_sk);
