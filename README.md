# Ingeniería de Datos — Entorno de la materia

Stack completo de la materia corriendo en Docker. LCD · UCA Rosario · 2026.

## Requisitos

- Docker Desktop (con al menos 4 GB asignados; ideal 6)
- Git
- 5 GB de disco libre

> **Windows:** cloná este repo en una ruta simple, sin espacios, sin tildes y
> **fuera de OneDrive**. Ejemplo: `C:\datos\ing-datos`.

## Cómo levantar el stack

```bash
make up      # levanta todo (la primera vez tarda 5-15 min: construye imágenes)
make ps      # ver qué está corriendo
```

Si estás en Windows sin `make`:

```bash
docker compose up -d --build
```

## Interfaces

| Herramienta | Dirección               | Usuario / Contraseña          |
|-------------|-------------------------|-------------------------------|
| MinIO       | http://localhost:9001   | minioadmin / minioadmin       |
| Airflow     | http://localhost:8080   | admin / admin                 |
| Metabase    | http://localhost:3000   | se configura en el primer uso |

> Airflow tarda uno o dos minutos más que el resto en quedar disponible:
> es normal, inicializa su base interna.

## Apagar

```bash
make down    # apaga y CONSERVA los datos
make clean   # apaga y BORRA los datos (usar solo si algo está muy roto)
```

## Estructura

| Carpeta / archivo    | Qué es                                              |
|----------------------|-----------------------------------------------------|
| `docker-compose.yml` | Definición del stack: qué servicios corren y cómo.  |
| `Makefile`           | Atajos para no escribir comandos largos.            |
| `docker/`            | Imágenes propias (Airflow con dbt y DuckDB).        |
| `dags/`              | Pipelines de Airflow. Hay uno de ejemplo.           |
| `dbt/`               | Proyecto de transformaciones (Medallion).           |
| `scripts/`           | Código auxiliar: ingesta, inicialización.           |
| `seed/`              | Datos de ejemplo para trabajar sin depender de red. |
| `notebooks/`         | Notebooks de las clases prácticas.                  |

## El stack en una línea

MinIO (data lake) → Airflow (orquestación) → dbt + DuckDB (transformación por
capas bronze/silver/gold) → PostgreSQL (serving) → Metabase (visualización).
