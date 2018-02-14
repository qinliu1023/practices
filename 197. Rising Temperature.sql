/*
SQL Schema

Create table If Not Exists Weather (Id int, Date date, Temperature int)
Truncate table Weather
insert into Weather (Id, Date, Temperature) values ('1', '2015-01-01', '10')
insert into Weather (Id, Date, Temperature) values ('2', '2015-01-02', '25')
insert into Weather (Id, Date, Temperature) values ('3', '2015-01-03', '20')
insert into Weather (Id, Date, Temperature) values ('4', '2015-01-04', '30')



Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/
SELECT Id
FROM Weather LEFT JOIN (
    SELECT Temperature AS yesterday_temperature, (Date + 1) AS Date_forward_move
    FROM Weather) AS temp_table
ON Weather.Date = temp_table.Date_forward_move
WHERE Temperature > yesterday_temperature; -- Wrong Answer 13/14 Passed

# Solution
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature
;
