SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e, Department d
WHERE e.DepartmentId = d.id AND (d.id,salary) 
IN 
(SELECT e2.DepartmentId,MAX(salary) 
FROM Employee e2, Department d2 
GROUP BY e2.DepartmentId)