/*
SQL Schema
Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')


Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. 
If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/
# Write your MySQL query statement below
# order descendingly and select top two as a temp_table 
# and then select top one when order ascendingly 
SELECT Salary AS SecondHighestSalary
FROM (SELECT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 2) AS temp_table
ORDER BY Salary ASC
LIMIT 1;

# getting the second one by excluding first 1 record
SELECT Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;

# Above two failed when the highest value is duplicated, say [4,300], [5, 300]
# then the second highest value would be 300 instead of 200
# Adding DISTINCT
SELECT Salary AS SecondHighestSalary
FROM (SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 2) AS temp_table
ORDER BY Salary ASC
LIMIT 1;
# Failed when all Salaries are the same, it returns the Salary value instead of []

SELECT DISTINCT Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;
# Failed when all Salaries are the same, it returns the [] instead of null

# Final SQL
SELECT 
    IFNULL( 
        (SELECT DISTINCT Salary AS SecondHighestSalary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
        NULL) AS SecondHighestSalary;
