def pontuar_hora(chuva, vento, onda):
    nota = 100
    if chuva >= 40:
        nota -= 25
    if vento >= 30:
        nota -= 20
    if (onda or 0) >= 1.5:
        nota -= 20
    return nota

def avaliar_dia(clima, mar, hora):
    horas = zip(clima["time"],
                clima["precipitation_probability"],
                clima["wind_speed_10m"],
                mar["wave_height"])
    notas = {t[-5:]: pontuar_hora(c, v, o)
             for t, c, v, o in horas}
    melhor = max(notas, key=notas.get)
    ok = "bom" if notas.get(hora, 0) >= 70 else "ruim"
    return {"veredito": ok,
            "melhor_horario": melhor}
