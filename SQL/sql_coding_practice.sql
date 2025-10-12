-- PLEASE FOLLOW THE TABLE STRUCTURE INSIDE SQL FOLDER
/*
1️⃣ INNER JOIN
	•	Find the customer names and their ordered items.
	•	Show customer name, country, and order amount (only if they placed an order).
	•	List all orders where shipping status is Delivered (requires join across 3 tables).
*/

SELECT (c.first_name || ' ' || c.last_name) as name, c.country, o.amount
FROM Customers c
INNER JOIN Orders o
 ON c.customer_id = o.customer_id
INNER JOIN Shippings s
 ON s.customer = c.customer_id
WHERE s.status = 'Delivered'


/*
2️⃣ LEFT JOIN
	•	List all customers even if they haven’t placed any orders.
	•	Show customers and their shipping status (include customers with no shipping record).
	•	List customers and total orders amount (show NULL if no orders).
*/
SELECT DISTINCT (c.first_name || ' ' || c.last_name) as name, c.age, c.country
FROM Customers c
LEFT JOIN Orders o
 ON c.customer_id = o.customer_id

SELECT (c.first_name || ' ' || c.last_name) as name, c.country, s.status
FROM Customers c
LEFT JOIN Shippings s
 ON s.customer = c.customer_id

SELECT (c.first_name || ' ' || c.last_name) as name, sum(o.amount) as total_orders_amount
FROM Customers c
LEFT JOIN Orders o
 ON c.customer_id = o.customer_id
GROUP BY c.first_name, c.last_name


/*
3️⃣ FULL OUTER JOIN
	•	Show all records from customers and shipping tables, even if no match.
	•	Show all orders and all shipping records (even if orphan records exist).
*/
SELECT *
FROM Customers c
FULL OUTER JOIN Shipping s
 ON c.customer_id = s.customer


/*
4️⃣ SUBQUERIES
	•	Find customers who have ordered items worth more than the average order amount.
	•	Find customers who never placed any order.
	•	Find maximum order amount per country.
*/
SELECT c.*
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id
WHERE o.amount > (SELECT AVG(amount) FROM Orders)

SELECT c.*
FROM Customers c
WHERE c.customer_id not in (
SELECT distinct customer_id from Orders
)

SELECT c.country, COALESCE(MAX(o.amount), 0) as max_amount
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.country


/*
5️⃣ CTEs
	•	Create a CTE to calculate total amount spent per customer and filter only those who spent more than 500.
	•	Using a CTE, rank customers by total spending.
*/

with cte as(
    SELECT c.customer_id, SUM(o.amount) as total_amount_spent
    FROM Customers c
    INNER JOIN Orders o
      ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
)
SELECT c.*, RANK()OVER(order by cte.total_amount_spent) as rank 
FROM Customers c
INNER JOIN cte
  ON cte.customer_id = c.customer_id
WHERE total_amount_spent > 500


/*
6️⃣ WINDOW FUNCTIONS
	•	Rank orders by amount (highest first).
	•	For each customer, show their order amount and total spend using SUM() OVER (PARTITION BY ...).
	•	Show running total of amounts in order of order_id.
*/
SELECT *, DENSE_RANK()OVER(ORDER BY amount DESC) AS Rank
FROM Orders o

SELECT c.*, o.amount, SUM(o.amount)OVER(PARTITION BY c.customer_id) as total_spend
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id

SELECT c.*, o.amount, SUM(o.amount)OVER(ORDER BY o.order_id) as running_total
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id

/*
8️⃣ HAVING Clause
	•	Get customers who placed more than 1 order.
	•	Find countries where total spending exceeds 1000.
*/
SELECT c.customer_id, c.first_name, c.last_name, c.age, c.country, count(*) as count
FROM Customers c
INNER JOIN Orders o
ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.age, c.country
HAVING count(*) > 1

SELECT c.country, SUM(o.amount) as total_spending
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.country
HAVING total_spending > 1000

/*
9️⃣ CASE Statements
	•	Show order_id, amount, and label as ‘High Value’ if amount > 500, else ‘Regular’.
	•	For each shipping record, return a status flag:
	•	Delivered → ‘Completed’
	•	Pending → ‘In Progress’
*/
SELECT order_id, amount, CASE WHEN amount > 500 THEN 'High Value' else 'Regular' END AS label
FROM Orders

SELECT *, CASE WHEN status = 'Delivered' THEN 'Completed' ELSE 'In Progress' END AS status_flag
FROM Shippings


/*
🔟 PIVOT / UNPIVOT
	•	Pivot: Show count of shipping status per status type (Pending vs Delivered) as columns.
	•	Unpivot: Convert order amounts into row-wise format (item, amount per customer).
*/
-- Mysql and postgres does not support PIVOT, so used case with sum to calculate the same
SELECT 
  SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END) AS Pending,
  SUM(CASE WHEN status = 'Delivered' THEN 1 ELSE 0 END) AS Delivered
FROM Shippings












"