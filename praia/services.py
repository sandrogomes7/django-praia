import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode

HEADERS = {"User-Agent": "praia-app/1.0"}
def get_json(url, params=None):
    if params:
        url += "?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=10) as r:
        return json.loads(r.read())
GEO = "https://nominatim.openstreetmap.org/search"

def geocodificar(local):
    p = {"q": local, "format": "json"}
    r = get_json(GEO, p)
    return r[0] if r else None
OVERPASS = "https://overpass-api.de/api/interpreter"

def tem_agua(lat, lon, raio=1500):
    filtro = '[natural~"beach|water"]'
    q = (f"[out:json];nwr(around:{raio},"
         f"{lat},{lon}){filtro};out 1;")
    r = get_json(OVERPASS, {"data": q})
    return len(r["elements"]) > 0
FORECAST = "https://api.open-meteo.com/v1/forecast"
CAMPOS = "precipitation_probability,wind_speed_10m"

def buscar_clima(lat, lon, dia):
    p = {"latitude": lat, "longitude": lon,
         "hourly": CAMPOS, "timezone": "auto",
         "start_date": dia, "end_date": dia}
    return get_json(FORECAST, p)["hourly"]
MARINE = "https://marine-api.open-meteo.com/v1/marine"
CAMPOS_MAR = "wave_height"

def buscar_mar(lat, lon, dia):
    p = {"latitude": lat, "longitude": lon,
         "hourly": CAMPOS_MAR, "timezone": "auto",
         "start_date": dia, "end_date": dia}
    return get_json(MARINE, p)["hourly"]
