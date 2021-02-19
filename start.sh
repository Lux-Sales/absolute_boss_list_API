#!/bin/bash
echo "Esperando o banco de dados conectar"
postgres_ready() {
python3 << END
import os
import sys
import psycopg2
try:
    conn = psycopg2.connect(
      dbname=os.environ.get('POSTGRES_NAME'),
      user=os.environ.get('POSTGRES_USER'),
      password=os.environ.get('POSTGRES_PASSWORD'),
      host=os.environ.get('POSTGRES_HOST')
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "PostgreSQL não está disponível ainda - Espere..."
  sleep 1
done
echo "rodando migrações"
python manage.py migrate

echo "rodando servidor"
gunicorn list.wsgi -b 0.0.0.0:8000 --reload --graceful-timeout=900 --timeout=900 --log-level DEBUG --workers 1