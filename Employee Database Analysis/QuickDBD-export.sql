-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments"."csv" (
    "dept_no" str   NOT NULL,
    "dept_name" str   NOT NULL
);

CREATE TABLE "dept_emp"."csv" (
    "emp_no" str   NOT NULL,
    "dept_no" str   NOT NULL
);

CREATE TABLE "dept_manager"."csv" (
    "dept_no" str   NOT NULL,
    "emp_no" str   NOT NULL
);

CREATE TABLE "employees"."csv" (
    "emp_no" str   NOT NULL,
    "emp_title_id" str   NOT NULL,
    "birth_date" str   NOT NULL,
    "first_name" str   NOT NULL,
    "last_name" str   NOT NULL,
    "sex" str   NOT NULL,
    "hire_date" str   NOT NULL
);

CREATE TABLE "salaries"."csv" (
    "emp_no" str   NOT NULL,
    "salary" str   NOT NULL
);

CREATE TABLE "titles"."csv" (
    "title_id" str   NOT NULL,
    "title" str   NOT NULL
);

ALTER TABLE "departments"."csv" ADD CONSTRAINT "fk_csv_dept_no" FOREIGN KEY("dept_no")
REFERENCES "dept_emp"."csv" ("dept_no");

ALTER TABLE "dept_manager"."csv" ADD CONSTRAINT "fk_csv_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments"."csv" ("dept_no");

ALTER TABLE "employees"."csv" ADD CONSTRAINT "fk_csv_emp_no" FOREIGN KEY("emp_no")
REFERENCES "dept_emp"."csv" ("emp_no");

ALTER TABLE "salaries"."csv" ADD CONSTRAINT "fk_csv_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees"."csv" ("emp_no");

ALTER TABLE "titles"."csv" ADD CONSTRAINT "fk_csv_title_id" FOREIGN KEY("title_id")
REFERENCES "employees"."csv" ("emp_title_id");

