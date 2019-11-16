--2. Create a view, called `all_parties` using `UNION` and write a PostgreSQL statement to return all of the actors,
--staff, and customers. Return the `first_name` and `last_name` columns from each of those tables and also indicate
--the type of record. (Hint: Hardcode the type of record in each of the queries that will be part of the union)
ALTER TABLE actor
ADD COLUMN "type" varchar(10);
update actor
set "type" = 'actor';

ALTER TABLE staff
ADD COLUMN "type" varchar(10);
UPDATE staff
set "type" = 'staff';

CREATE VIEW all_parties AS
SELECT first_name, last_name, "type" from actor
UNION
SELECT first_name, last_name, "type" from staff
ORDER BY "type";
select * from all_parties;
--3. Use `UNION` to display from the tables `customer` and `customer_list` the ID of all customers who live in the 
--city of London. Determine whether both tables contain the same customers by using `UNION ALL`. (Hint: Consider 
--using subqueries or joins... either will work).

select id from customer_list WHERE city = 'London'
UNION ALL
select 
customer.customer_id
from customer
Inner JOIN address
	ON customer.address_id = address.address_id
INNER JOIN city
	ON address.city_id = city.city_id
WHERE city.city = 'London';