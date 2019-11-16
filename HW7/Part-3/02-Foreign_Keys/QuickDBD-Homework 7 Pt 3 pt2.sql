-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/LnjKtA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "employees" (
    "employee_id" INT   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "department_id" INT   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "employee_id"
     )
);

CREATE TABLE "departments" (
    "id" INT   PRIMARY KEY NOT NULL,
    "dept_name" varchar   NOT NULL
);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_department_id" FOREIGN KEY("department_id")
REFERENCES "departments" ("id");

select * from employees, departments