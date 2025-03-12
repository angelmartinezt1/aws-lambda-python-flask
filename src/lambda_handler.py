import sys
import os

# Agregar el directorio actual al path para evitar problemas de importación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import awsgi
from app import app


def handler(event, context):
    return awsgi.response(app, event, context)
