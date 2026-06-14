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

### 4. Configurar variables de entorno

Mac/Linux
```bash
cp .env.example .env
```
Windows:
```bash
copy .env.example .env
```

Llenar el `.env` con tu usuario y contraseña de MySQL

### 5. Correr el proyecto
```bash
docker compose up --build
```

### 6. Verificar que funciona
```bash
docker logs -f cron_jobs-app-1
```
Deberías ver un cliente procesándose cada minuto.