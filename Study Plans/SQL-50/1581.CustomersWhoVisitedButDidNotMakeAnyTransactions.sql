-- Write your PostgreSQL query statement below
SELECT v.customer_id,COUNT(v.customer_id) 
AS count_no_trans 
FROM Visits v LEFT OUTER JOIN Transactions t 
ON v.visit_id=t.visit_id 
WHERE transaction_id IS NULL 
GROUP BY v.customer_id 
ORDER BY COUNT(v.customer_id)