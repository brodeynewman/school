CREATE TABLE coffee_shops (
  shop_id integer PRIMARY KEY,
  shop_name VARCHAR(50),
  city VARCHAR(50),
  state CHAR(2)
);

CREATE TABLE suppliers (
  supplier_id integer PRIMARY KEY,
  company_name VARCHAR(50),
  country VARCHAR(30),
  sales_contact_name VARCHAR(60),
  email VARCHAR(50) NOT NULL
);

CREATE TABLE coffee (
  coffee_id integer PRIMARY KEY,
  shop_id INTEGER REFERENCES coffee_shops (shop_id),
  supplier_id INTEGER REFERENCES suppliers (supplier_id),
  coffee_name VARCHAR(30),
  price_per_pound NUMERIC(5, 2)
);

CREATE TABLE employees (
  employee_id integer PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  hire_date DATE,
  job_title VARCHAR(30),
  shop_id INTEGER REFERENCES coffee_shops (shop_id)
);

-- insert into coffee shops --
INSERT INTO coffee_shops (shop_id, shop_name, city, state) VALUES (1, 'Hex Coffee', 'Charlotte', 'NC');
INSERT INTO coffee_shops (shop_id, shop_name, city, state) VALUES (2, 'Stable Hand', 'Charlotte', 'NC');
INSERT INTO coffee_shops (shop_id, shop_name, city, state) VALUES (3, 'Rowan Coffee', 'Asheville', 'NC');

-- insert into suppliers --
INSERT INTO suppliers (supplier_id, company_name, country, sales_contact_name, email)
VALUES (1, 'Westrock Coffee Company, LLC', 'United States', 'Jerry Smith', 'info@westrockcoffee.com');

INSERT INTO suppliers (supplier_id, company_name, country, sales_contact_name, email)
VALUES (2, 'Red Diamond', 'United States', 'Allyson Deak', 'contact@reddiamondcoffee.com');

INSERT INTO suppliers (supplier_id, company_name, country, sales_contact_name, email)
VALUES (3, 'Mother Parkers', 'United States', 'Dillon Brys', 'sales@motherparkers.co');

-- insert into coffee --
INSERT INTO coffee (coffee_id, shop_id, supplier_id, coffee_name, price_per_pound)
VALUES (1, 1, 1, 'Hex Light Roast', 11.25);

INSERT INTO coffee (coffee_id, shop_id, supplier_id, coffee_name, price_per_pound)
VALUES (2, 2, 2, 'Medium Roast Batch Brew', 8.49);

INSERT INTO coffee (coffee_id, shop_id, supplier_id, coffee_name, price_per_pound)
VALUES (3, 3, 3, 'Sweet Ethiopian', 12.99);

-- insert into employees --
INSERT INTO employees (employee_id, first_name, last_name, hire_date, job_title, shop_id)
VALUES (1, 'Brodey', 'Newman', now(), 'CTO', 1);

INSERT INTO employees (employee_id, first_name, last_name, hire_date, job_title, shop_id)
VALUES (2, 'Bobby', 'Smedley', now(), 'CEO', 2);

INSERT INTO employees (employee_id, first_name, last_name, hire_date, job_title, shop_id)
VALUES (3, 'Jessi', 'Cord', now(), 'CEO', 3);

-- create employee view --
CREATE VIEW vw_employees_formatted AS
SELECT
  employees.employee_id,
  CONCAT(employees.first_name, ' ', employees.last_name) AS employee_full_name,
  employees.hire_date,
  employees.job_title,
  employees.shop_id
FROM employees;

-- create coffe_name index --
create index coffee_name_idx on coffee(coffee_name);

-- complex select 1 --
select *
from vw_employees_formatted as emp
inner join coffee_shops on coffee_shops.shop_id = emp.shop_id
inner join coffee on coffee.shop_id = coffee_shops.shop_id
inner join suppliers on coffee.supplier_id = coffee.shop_id
where emp.job_title = 'CTO';
