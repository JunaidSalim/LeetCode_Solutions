-- Write your PostgreSQL query statement below
SELECT name
FROM Employee 
WHERE id IN (
    SELECT e.managerId From Employee e
    GROUP BY e.managerId 
    HAVING COUNT(id)>=5
)
