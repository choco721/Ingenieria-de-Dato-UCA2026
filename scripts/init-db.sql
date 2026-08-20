-- Se ejecuta UNA sola vez, cuando el contenedor de Postgres se crea por
-- primera vez (base vacía). Deja los esquemas separados para cada rol.

-- Esquema para la metadata interna de Airflow.
CREATE SCHEMA IF NOT EXISTS airflow;

-- Esquema de serving: acá viven las tablas gold que consume Metabase.
CREATE SCHEMA IF NOT EXISTS serving;

-- Tabla de humo para verificar la conexión desde Metabase el primer día.
CREATE TABLE IF NOT EXISTS serving.hola_mundo (
    id          SERIAL PRIMARY KEY,
    mensaje     TEXT        NOT NULL,
    creado_en   TIMESTAMP   DEFAULT now()
);

INSERT INTO serving.hola_mundo (mensaje)
VALUES ('El stack está andando 🎉');
