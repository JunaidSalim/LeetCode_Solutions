-- Write your PostgreSQL query statement below
SELECT c.name AS Customers
FROM customers c
WHERE c.id NOT IN (SELECT o.customerId FROM Orders o)