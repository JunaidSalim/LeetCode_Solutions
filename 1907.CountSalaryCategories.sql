-- Write your PostgreSQL query statement below
SELECT 'Low Salary' AS Category,
COUNT(*) AS accounts_count
FROM Accounts 
WHERE income<20000
UNION
SELECT 'Average Salary' AS Category,
COUNT(*) AS accounts_count
FROM Accounts 
WHERE income>=20000 AND income<=50000
UNION
SELECT 'High Salary' AS Category,
COUNT(*) AS accounts_count
FROM Accounts 
WHERE income>50000