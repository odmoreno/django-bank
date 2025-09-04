#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

python manage.py migrate --no-input
python manage.py collectstatic --no-input

if [ "$DEBUG" = "True" ]; then
  echo "==> Ejecutando con debugpy en 5678"
  exec python -m debugpy --listen 0.0.0.0:5678 --wait-for-client manage.py runserver 0.0.0.0:8000 --noreload
else
  echo "==> Ejecutando servidor Django en 8000"
  exec python manage.py runserver 0.0.0.0:8000
fi