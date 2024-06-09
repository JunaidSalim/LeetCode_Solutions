-- Write your PostgreSQL query statement below
SELECT DISTINCT p.email AS Email
FROM Person p,Person p2
WHERE p.email = p2.email AND p.id <> p2.id