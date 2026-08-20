# Imagen propia de Airflow con las dependencias de la materia adentro.
# Partimos de la imagen oficial y le agregamos: dbt, DuckDB, y las librerías
# de Python para ingesta desde APIs y escritura al lake.
FROM apache/airflow:2.9.3-python3.11

# Copiamos el archivo de dependencias y las instalamos como usuario airflow
# (la imagen oficial NO permite pip install como root).
COPY requirements.txt /requirements.txt

USER airflow
RUN pip install --no-cache-dir -r /requirements.txt
