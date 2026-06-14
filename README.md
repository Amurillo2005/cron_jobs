# Cron Jobs 

## Instalación

### 1. Clonar el repositorio
- git clone tu_repositorio
- cd cron_jobs

### 2. Importar la base de datos zeus
- Descargar `zeus.sql` desde Jira
- Importarlo en MySQL Workbench:
- `Server` → `Data Import` → `Import from Self-Contained File` → seleccionar `zeus.sql` → `Start Import`

### 3. Actualizar la tabla clients
Una vez importado `zeus.sql`, actualiza los datos con tus propios clientes:
```sql
UPDATE clients SET 
    name = 'nombre_cliente',
    db_name = 'nombre_base_de_datos'
WHERE id = 1;
```

### 4. Ejecutar setup.sql
- Abrir `setup.sql` en MySQL Workbench
- Reemplazar `tu_password` por la contraseña que quieras usar para `docker_user`
- Descomentar y agregar los permisos para cada base de datos de tus clientes
- Ejecutar el script

### 5. Configurar variables de entorno
```bash
cp .env.example .env
```
Debes llenar TENANT_DB_PASSWORD con la contraseña que pusiste en el paso 3 de setup.sql y TENANT_DB_USER con docker_user

### 6. Correr el proyecto
```bash
docker compose up --build
```

### 7. Verificar que funciona
```bash
docker logs -f cron_jobs-app-1
```
Deberías ver un cliente procesándose cada minuto.