-- Drop table if exists
DROP TABLE employees;

-- Create employee table
CREATE TABLE employees (
  emp_no VARCHAR(30),
  emp_title_id VARCHAR(30),
  birth_date VARCHAR(30),
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  sex VARCHAR(30),
  hire_date VARCHAR(30)
);
SELECT * FROM employees;



-- Drop table if exists
DROP TABLE salaries;

-- Create salary table
CREATE TABLE salaries (
  emp_no VARCHAR(30),
  salary VARCHAR(30)
);
SELECT * FROM salaries;



-- Drop table if exists
DROP TABLE departments;

-- Create department table
CREATE TABLE departments (
  dept_no VARCHAR(30),
  dept_name VARCHAR(30)
);
SELECT * FROM departments;




-- Drop table if exists
DROP TABLE dept_emp;

-- Create department table
CREATE TABLE dept_emp (
  emp_no VARCHAR(30),
  dept_no VARCHAR(30)
);
SELECT * FROM dept_emp;



-- Drop table if exists
DROP TABLE dept_manager;

-- Create department table
CREATE TABLE dept_manager (
  dept_no VARCHAR(30),
  emp_no VARCHAR(30)
);
SELECT * FROM dept_manager;




-- Drop table if exists
DROP TABLE titles;

-- Create department table
CREATE TABLE titles (
  title_id VARCHAR(30),
  title VARCHAR(30)
);
SELECT * FROM titles;



-- Join tables
SELECT employees.emp_no, employees.birth_date, employees.first_name, employees.last_name,  titles.title,
employees.emp_title_id, employees.sex, employees.hire_date, dept_emp.dept_no, departments.dept_name, salaries.salary
FROM employees
INNER JOIN titles ON employees.emp_title_id = titles.title_id
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
INNER JOIN salaries ON employees.emp_no = salaries.emp_no;

SELECT * FROM employees;

-- Manually save this as a CSV file
