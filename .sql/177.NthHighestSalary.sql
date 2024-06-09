CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT E1.salary 
    FROM Employee E1
    WHERE N-1 = (SELECT COUNT(DISTINCT E2.salary) 
    FROM Employee E2 
    WHERE E2.salary>E1.salary) LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;