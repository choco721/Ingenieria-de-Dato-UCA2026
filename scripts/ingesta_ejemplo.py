"""Ingesta de ejemplo hacia la capa bronze del lake (MinIO).

Placeholder para la Entrega 1. Todavía no trae datos reales: solo demuestra
el patrón de conexión a MinIO y deja el esqueleto de una ingesta idempotente.
Cuando definas el dominio del proyecto (API del BCRA, Datos Argentina, etc.),
este script se completa con la fuente real.
"""

from __future__ import annotations

import io

import boto3
import pandas as pd


def cliente_minio(
    endpoint: str = "http://localhost:9000",
    access_key: str = "minioadmin",
    secret_key: str = "minioadmin",
) -> "boto3.client":
    """Crea un cliente S3 apuntando a MinIO.

    Args:
        endpoint: URL del API S3 de MinIO.
        access_key: usuario de MinIO.
        secret_key: contraseña de MinIO.

    Returns:
        boto3.client: cliente S3 configurado para MinIO.
    """
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )


def escribir_parquet(df: pd.DataFrame, bucket: str, key: str) -> None:
    """Escribe un DataFrame como Parquet en el lake.

    La escritura por key fija es idempotente: correr dos veces la misma
    ingesta deja el mismo objeto, no lo duplica.

    Args:
        df: datos a persistir.
        bucket: bucket destino (ej. "lake").
        key: ruta del objeto dentro del bucket (ej. "bronze/demo.parquet").
    """
    buffer = io.BytesIO()
    df.to_parquet(buffer, engine="pyarrow", index=False)
    buffer.seek(0)
    cliente_minio().put_object(Bucket=bucket, Key=key, Body=buffer.getvalue())
    print(f"Escrito: s3://{bucket}/{key} ({len(df)} filas)")


if __name__ == "__main__":
    demo = pd.DataFrame({"id": [1, 2, 3], "valor": [10.0, 20.0, 30.0]})
    escribir_parquet(demo, bucket="lake", key="bronze/demo.parquet")
