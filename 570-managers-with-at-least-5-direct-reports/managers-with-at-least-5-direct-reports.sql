# Write your MySQL query statement below
SELECT E.NAME FROM EMPLOYEE AS E
WHERE E.ID IN (SELECT MANAGERID FROM EMPLOYEE GROUP BY MANAGERID HAVING COUNT(*) >= 5);
