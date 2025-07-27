--# db_init/init.sql
-- Creación de la tabla orders
-- Esta tabla almacena información sobre pedidos realizados por empresas
CREATE TABLE IF NOT EXISTS orders(
    id_order SERIAL PRIMARY KEY,
    id VARCHAR(50) NOT NULL,
    company_name VARCHAR(130) NULL,
    company_id VARCHAR(50) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    paid_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);

-- Restricción para evitar duplicados por combinación de columnas clave
ALTER TABLE orders 
ADD CONSTRAINT orders_unique_id_company_name_company_id
UNIQUE (id, company_name, company_id);

-- Restricción para evitar duplicados por combinación de columnas clave
ALTER TABLE orders 
ADD CONSTRAINT orders_unique_id_company_id
UNIQUE (id, company_id);



-- Validación para que el monto sea mayor a 0.1
ALTER TABLE orders 
	ADD CONSTRAINT check_amount 
	CHECK(
		amount >= 0.1
	);

-- Creacion tabla companies
CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    company_id VARCHAR(50) UNIQUE NOT NULL,
    company_name VARCHAR(130)
);

-- Creacion tabla charges
CREATE TABLE IF NOT EXISTS charges (
    id_order INT PRIMARY KEY,  
    charge_id VARCHAR(50), 
    company_ref_id INT NOT NULL,   
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    paid_at TIMESTAMP,
    FOREIGN KEY (company_ref_id) REFERENCES companies(id)
);


-- Insertar datos únicos en la tabla companies desde orders
INSERT INTO companies (company_id, company_name)
SELECT DISTINCT company_id, company_name
FROM orders
WHERE company_id IS NOT NULL
ON CONFLICT (company_id) DO NOTHING;

-- Insertar datos en la tabla charges desde orders
INSERT INTO charges (id_order, charge_id, company_ref_id, amount, status, created_at, paid_at)
SELECT 
    o.id_order,
    o.id,
    c.id,
    o.amount,
    o.status,
    o.created_at,
    o.paid_at
FROM orders o
JOIN companies c ON o.company_id = c.company_id;

-- Vista para obtener el total de transacciones por dia, mes, año y compañia
-- Vista para obtener el total de transacciones por día
CREATE OR REPLACE VIEW vista_monto_diario AS
SELECT
    companies.company_id,
    companies.company_name,
    charges.created_at::DATE AS fecha_transaccion,
    SUM(charges.amount) AS monto_total
FROM charges 
JOIN companies ON charges.company_ref_id = companies.id
GROUP BY companies.company_id, companies.company_name, fecha_transaccion
ORDER BY fecha_transaccion, companies.company_name;


-- Vista para obtener el total de transacciones por mes
CREATE OR REPLACE VIEW vista_monto_mensual AS
SELECT
    companies.company_id,
    companies.company_name,
    DATE_TRUNC('month', charges.created_at)::DATE AS mes_transaccion,
    SUM(charges.amount) AS monto_total
FROM charges 
JOIN companies ON charges.company_ref_id = companies.id
GROUP BY companies.company_id, companies.company_name, mes_transaccion
ORDER BY mes_transaccion, companies.company_name;

-- Vista para obtener el total de transacciones por año
CREATE OR REPLACE VIEW vista_monto_anual AS
SELECT
    companies.company_id,
    companies.company_name,
    DATE_TRUNC('year', charges.created_at)::DATE AS año_transaccion,
    SUM(charges.amount) AS monto_total
FROM charges 
JOIN companies ON charges.company_ref_id = companies.id
GROUP BY companies.company_id, companies.company_name, año_transaccion
ORDER BY año_transaccion, companies.company_name;