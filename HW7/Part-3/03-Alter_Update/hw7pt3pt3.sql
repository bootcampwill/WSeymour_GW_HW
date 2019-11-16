--1. Explain the difference between alter and update in SQL statements.
--Alter is used to chane the ctructure of the table.  Update is used to change the data.

--2. Change the name of the column from department_id to dept_id. Add a column named annual_salary to the table.


ALTER TABLE employees
RENAME COLUMN department_id TO dept_id;

ALTER TABLE employees
ADD COLUMN annual_salary INT;
select * from employees;