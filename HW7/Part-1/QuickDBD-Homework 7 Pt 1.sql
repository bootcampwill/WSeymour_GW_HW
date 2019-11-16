-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/LnjKtA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Employees" (
    "emp_no" int   NOT NULL,
    "birt_hdate" date   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varhar(1)   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Salaries" (
    "emp_no" INT   NOT NULL,
    "salary" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "titles" (
    "emp_no" INT   NOT NULL,
    "title" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "emp_no"
     )
);

-- Table documentation comment 2
CREATE TABLE "Departments" (
    "dept_no" int   NOT NULL,
    "dept_name" varchar(200)   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     ),
    CONSTRAINT "uc_Departments_dept_name" UNIQUE (
        "dept_name"
    )
);

CREATE TABLE "DeptManager" (
    "dept_no" int   NOT NULL,
    "emp_no" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_DeptManager" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "DeptEmployees" (
    "emp_no" int   NOT NULL,
    "dept_no" int   NOT NULL,
    "to_date" date   NOT NULL,
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

