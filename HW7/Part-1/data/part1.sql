--DROP TABLE IF EXISTS "Employees"     CASCADE;
--DROP TABLE IF EXISTS "Salaries"      CASCADE;
--DROP TABLE IF EXISTS "titles"        CASCADE;
--DROP TABLE IF EXISTS "Departments"   CASCADE;
--DROP TABLE IF EXISTS "DeptManager"   CASCADE;
--DROP TABLE IF EXISTS "DeptEmployees" CASCADE;

CREATE TABLE "Employees" (
    "emp_no" int           NOT NULL,
    "birt_hdate" date      NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar    NOT NULL,
    "gender" varchar(1)    NOT NULL,
    "hire_date" date       NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Salaries" (
    "emp_no" INT       NOT NULL,
    "salary" int       NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date     NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "titles" (
    "emp_no" INT       NOT NULL,
    "title" varchar    NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date     NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "emp_no"
     )
);

-- Table documentation comment 2
CREATE TABLE "Departments" (
    "dept_no"   varchar        NOT NULL,
    "dept_name" varchar(200)   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     ),
    CONSTRAINT "uc_Departments_dept_name" UNIQUE (
        "dept_name"
    )
);

CREATE TABLE "DeptManager" (
    "dept_no" varchar  NOT NULL,
    "emp_no" int       NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date     NOT NULL,
    CONSTRAINT "pk_DeptManager" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "DeptEmployees" (
    "emp_no" int       NOT NULL,
    "dept_no" varchar  NOT NULL,
    "to_date" date     NOT NULL,
    "from_date" date   NOT NULL,
    CONSTRAINT "pk_DeptEmployees" PRIMARY KEY (
        "emp_no"
     )
);

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "DeptManager" ADD CONSTRAINT "fk_DeptManager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "DeptManager" ADD CONSTRAINT "fk_DeptManager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "DeptEmployees" ADD CONSTRAINT "fk_DeptEmployees_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "DeptEmployees" ADD CONSTRAINT "fk_DeptEmployees_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select "Employees".emp_no, 
		"Employees".last_name, 
		"Employees".first_name, 
		"Employees".gender, 
		"Salaries".salary
FROM "Employees"
INNER JOIN "Salaries" ON
"Employees".emp_no = "Salaries".emp_no;

--2. List employees who were hired in 1986
select emp_no, hire_date from "Employees" where hire_date >= '1/1/1986' and hire_date <= '12/31/1986'

--3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name, and start and end employment dates.

SELECT
"Departments".dept_no,
"Departments".dept_name,
"DeptManager".emp_no,
"Employees".last_name,
"Employees".first_name,
"DeptManager".from_date,
"DeptManager".to_date
FROM "Departments"
INNER JOIN "DeptManager" 
	ON "Departments".dept_no = "DeptManager".dept_no
INNER JOIN "Employees"
	ON "DeptManager".emp_no = "Employees".emp_no
	
--4. List the department of each employee with the following information: employee number, last name, first name, 
--and department name.

SELECT
"Employees".emp_no,
"Employees".last_name,
"Employees".first_name,
"Departments".dept_name
FROM "Employees"
INNER JOIN "DeptEmployees" 
	ON "Employees".emp_no = "DeptEmployees".emp_no
INNER JOIN "Departments"
	ON "DeptEmployees".dept_no = "Departments".dept_no
	
--5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT 
last_name,
first_name
FROM "Employees"
	WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
	
--6. List all employees in the Sales department, including their employee number, last name, first name, and 
--department name.
SELECT
"Employees".emp_no,
"Employees".last_name,
"Employees".first_name,
"Departments".dept_name
FROM "Employees"
INNER JOIN "DeptEmployees"
	ON "Employees".emp_no = "DeptEmployees".emp_no
INNER JOIN "Departments"
	ON "DeptEmployees".dept_no = "Departments".dept_no
WHERE "Departments".dept_name = 'Sales'

--7. List all employees in the Sales and Development departments, including their employee number, last name, 
--first name, and department name.

SELECT
"Employees".emp_no,
"Employees".last_name,
"Employees".first_name,
"Departments".dept_name
FROM "Employees"
INNER JOIN "DeptEmployees"
	ON "Employees".emp_no = "DeptEmployees".emp_no
INNER JOIN "Departments"
	ON "DeptEmployees".dept_no = "Departments".dept_no
WHERE "Departments".dept_name = 'Sales' OR "Departments".dept_name = 'Development'

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each
--last name.
SELECT last_name, COUNT(last_name) AS "Count of Last Names"
FROM "Employees"
GROUP BY last_name
ORDER by "Count of Last Names" DESC;