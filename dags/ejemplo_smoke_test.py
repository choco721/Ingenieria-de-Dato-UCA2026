"""DAG de ejemplo para verificar que Airflow lee los DAGs correctamente.

No hace nada útil todavía: solo imprime un mensaje. Sirve para confirmar,
el primer día, que la carpeta dags/ está bien montada y que el scheduler
la ve. Cuando arranque la Unidad VI, este archivo se reemplaza por los
DAGs reales del pipeline.
"""

from __future__ import annotations

from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="ejemplo_smoke_test",
    schedule=None,               # solo se corre manualmente (trigger)
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["ejemplo", "setup"],
)
def ejemplo_smoke_test() -> None:
    """Pipeline mínimo de una sola tarea, para probar que Airflow funciona."""

    @task()
    def saludar() -> str:
        """Imprime un saludo y devuelve un mensaje.

        Returns:
            str: mensaje de confirmación que queda en los logs de la tarea.
        """
        mensaje = "Airflow está leyendo los DAGs correctamente."
        print(mensaje)
        return mensaje

    saludar()


ejemplo_smoke_test()
