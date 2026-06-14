-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS zeus;

-- 2. Usar la base de datos
USE zeus;

-- 3. Crear el usuario docker_user
CREATE USER 'docker_user'@'%' IDENTIFIED WITH mysql_native_password BY 'tu_password';
CREATE USER 'docker_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'tu_password';

-- 4. Dar permisos sobre zeus
GRANT ALL PRIVILEGES ON zeus.* TO 'docker_user'@'%';
GRANT ALL PRIVILEGES ON zeus.* TO 'docker_user'@'localhost';

-- 5. Dar permisos sobre las bases de datos de los clientes
-- Agrega una línea por cada base de datos de tus clientes
-- GRANT ALL PRIVILEGES ON nombre_base_de_datos.* TO 'docker_user'@'%';
-- GRANT ALL PRIVILEGES ON nombre_base_de_datos.* TO 'docker_user'@'localhost';

FLUSH PRIVILEGES;