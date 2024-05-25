-- Write your PostgreSQL query statement below
SELECT COALESCE((
SELECT n.num
FROM MyNumbers n
GROUP BY n.num
HAVING COUNT(n.num) = 1 
ORDER BY n.num DESC
LIMIT 1),NULL) 
AS num