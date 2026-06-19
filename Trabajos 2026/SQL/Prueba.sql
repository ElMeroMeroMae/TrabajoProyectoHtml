CREATE DATABASE empresa_db;
USE empresa_db;

CREATE TABLE clientes(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
correo VARCHAR(100)
);

CREATE TABLE pedidos(
id_pedido INT PRIMARY KEY auto_increment,
fecha DATE NOT NULL,
monto DECIMAL(10,2),
id_cliente INT,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO clientes (nombre, correo)
VALUES 
("Juan Perez", "juan@mail.com"),
("Ana Lopez", "ana@mail.com"),
("Carlos Ruiz", "carlo@mail.com");

INSERT INTO pedidos (fecha,monto,id_cliente)
VALUES 
("2026-03-01", 1200.00, 1),
("2026-03-02", 800.00, 2), 
("2026-03-03", 450.00, 3); 

SELECT c.nombre, p.id_pedido, p.monto 
FROM clientes c 
JOIN pedidos p ON c.id_cliente = p.id_cliente;
