-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE id NOT IN (SELECT c.id FROM Customer c WHERE referee_id=2)