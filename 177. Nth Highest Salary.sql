/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
     
      SELECT IF((SELECT COUNT(Salary) FROM (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N) AS temp_table)<N, 
                null, 
                (SELECT Salary FROM 
                  (SELECT DISTINCT Salary 
                   FROM Employee ORDER BY Salary DESC LIMIT N) AS temp_table 
                   ORDER BY Salary ASC 
                   LIMIT 1)) -- Select distinct salaries from Employee and display only top N, if count of distinct salaries is 
                             -- less than N, then nth highest does not exist, return null
                             -- Otherwise, using limit 1 and asc ordering to return the nth highest salary

  );
END
