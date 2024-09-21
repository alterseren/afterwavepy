import os
import sys

# Додай шлях до директорії з проектом
path = '/home/alterseren/alterserenity'
if path not in sys.path:
    sys.path.append(path)

# Налаштування для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alterwave')  # Зміни на назву твого проекту
import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
