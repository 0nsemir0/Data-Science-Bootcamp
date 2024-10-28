SELECT * FROM SALES; 

Go 

SELECT COUNT(*) AS total_orders
FROM SALES
WHERE Date = '2023-03-18';
 
Go

SELECT COUNT(*) AS total_orders
FROM SALES S
JOIN CUSTOMERS C ON S.Customer_id = C.Customer_id
WHERE S.Date = '2023-03-18' AND C.First_name = 'John' AND C.Last_name = 'Doe';

Go

SELECT COUNT(DISTINCT Customer_id) AS total_customers,
       AVG(Revenue) AS average_spend_per_customer
FROM SALES
WHERE Date BETWEEN '2023-01-01' AND '2023-01-31';

Go

SELECT I.Department, SUM(S.Revenue) AS total_revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
WHERE YEAR(S.Date) = 2023
GROUP BY I.Department
HAVING SUM(S.Revenue) < 600;

Go

SELECT MAX(Revenue) AS max_revenue, MIN(Revenue) AS min_revenue
FROM SALES;

Go 

WITH MaxRevenue AS (
    SELECT MAX(Revenue) AS max_revenue
    FROM SALES
)
-- Then, find the orders that generated this maximum revenue
SELECT *
FROM SALES
WHERE Revenue = (SELECT max_revenue FROM MaxRevenue);