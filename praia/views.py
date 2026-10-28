from django.http import JsonResponse
from . import services, regras

def avaliar(request):
    local = request.GET["local"]
    dia = request.GET["dia"]
    hora = request.GET["hora"]
    ponto = services.geocodificar(local)
    if ponto is None:
        return JsonResponse(
            {"erro": "local inexistente"},
            status=404)
    lat, lon = ponto["lat"], ponto["lon"]
    if not services.tem_agua(lat, lon):
        return JsonResponse(
            {"erro": "sem água"}, status=422)
    clima = services.buscar_clima(lat, lon, dia)
    mar = services.buscar_mar(lat, lon, dia)
    return JsonResponse(
        regras.avaliar_dia(clima, mar, hora))
