-- Write your PostgreSQL query statement below
select name as Employee from Employee e1 where salary>(Select salary from Employee e2 where e1.managerId=e2.id)