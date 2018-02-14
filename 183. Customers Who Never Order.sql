/*
SQL Schema

Create table If Not Exists Customers (Id int, Name varchar(255))
Create table If Not Exists Orders (Id int, CustomerId int)
Truncate table Customers
insert into Customers (Id, Name) values ('1', 'Joe')
insert into Customers (Id, Name) values ('2', 'Henry')
insert into Customers (Id, Name) values ('3', 'Sam')
insert into Customers (Id, Name) values ('4', 'Max')
Truncate table Orders
insert into Orders (Id, CustomerId) values ('1', '3')
insert into Orders (Id, CustomerId) values ('2', '1')



Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/
# Write your MySQL query statement below
SELECT Name AS Customers
FROM (
    SELECT Customers.Id, Customers.Name, Orders.CustomerId 
    FROM Customers LEFT JOIN Orders
    ON Customers.Id = Orders.CustomerID) AS temp_table
WHERE CustomerId is null ;

# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers LEFT JOIN Orders
ON Customers.Id = Orders.CustomerID
WHERE CustomerId is null ;

# Another Solution
SELECT Customers.Name AS Customers
FROM Customers
WHERE Customers.Id NOT IN
(
    SELECT CustomerId from Orders
);
