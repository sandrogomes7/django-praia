# django-praia

    python3 -m venv .venv
    source .venv/bin/activate
    pip install django
    python manage.py migrate
    python manage.py runserver

Abra http://127.0.0.1:8000/ (Hello, World!) e
http://127.0.0.1:8000/api/avaliar/?local=Maceio&dia=2026-10-28&hora=14:00
(precisa de internet: Nominatim, Overpass e Open-Meteo).
