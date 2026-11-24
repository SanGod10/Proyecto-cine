"""
Agenda de peliculas.
Modulo de calculos.
"""


def _a_minutos(hora_24: int) -> int:
    """Convierte una hora en formato HHMM (ej. 1400 o 800) a minutos desde las 00:00."""
    horas = hora_24 // 100
    minutos = hora_24 % 100
    return horas * 60 + minutos


def _limpiar_texto(texto: str) -> str:
    """Normaliza espacios y minusculas para comparar textos."""
    return texto.strip().lower()


def _tiene_genero(peli: dict, genero_buscado: str) -> bool:
    """Verifica si un genero aparece entre los generos separados por comas."""
    generos = [_limpiar_texto(g) for g in peli["genero"].split(",")]
    return _limpiar_texto(genero_buscado) in generos


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva pelicula."""
    return {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia,
    }


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Busca una pelicula por nombre entre las 5 recibidas. Retorna None si no existe."""
    objetivo = _limpiar_texto(nombre_pelicula)
    for peli in (p1, p2, p3, p4, p5):
        if _limpiar_texto(peli["nombre"]) == objetivo:
            return peli
    return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Retorna la pelicula de mayor duracion entre las 5 recibidas."""
    mas_larga = p1
    for peli in (p2, p3, p4, p5):
        if peli["duracion"] > mas_larga["duracion"]:
            mas_larga = peli
    return mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula el promedio de duracion y lo retorna en formato HH:MM."""
    total_minutos = (
        p1["duracion"]
        + p2["duracion"]
        + p3["duracion"]
        + p4["duracion"]
        + p5["duracion"]
    )
    promedio = total_minutos // 5
    horas = promedio // 60
    minutos = promedio % 60
    return f"{horas:02d}:{minutos:02d}"


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Retorna nombres de peliculas estrenadas estrictamente despues de anio, separados por comas."""
    estrenos = []
    for peli in (p1, p2, p3, p4, p5):
        if peli["anio"] > anio:
            estrenos.append(peli["nombre"])
    if not estrenos:
        return "Ninguna"
    return ", ".join(estrenos)


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Cuenta cuantas peliculas tienen clasificacion 18+."""
    contador = 0
    for peli in (p1, p2, p3, p4, p5):
        if peli["clasificacion"].strip() == "18+":
            contador += 1
    return contador


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Intenta reagendar una pelicula verificando conflictos de horario y reglas de control."""
    if nueva_hora < 0 or nueva_hora > 2359 or (nueva_hora % 100) >= 60:
        return False

    dia_limpio = _limpiar_texto(nuevo_dia)
    inicio_nuevo = _a_minutos(nueva_hora)
    fin_nuevo = inicio_nuevo + peli["duracion"]

    # Evitar conflictos o superposicion de duracion en el mismo dia
    for otra in (p1, p2, p3, p4, p5):
        if otra is peli:
            continue
        if _limpiar_texto(otra["dia"]) == dia_limpio:
            inicio_otra = _a_minutos(otra["hora"])
            fin_otra = inicio_otra + otra["duracion"]
            if inicio_nuevo < fin_otra and fin_nuevo > inicio_otra:
                return False

    if control_horario:
        # No documentales desde las 22:00 (2200)
        if _tiene_genero(peli, "Documental") and nueva_hora >= 2200:
            return False

        # No dramas los viernes
        if _tiene_genero(peli, "Drama") and dia_limpio == "viernes":
            return False

        # Entre semana (lunes a jueves): no antes de las 06:00 (600) ni desde las 23:00 (2300)
        entre_semana = ("lunes", "martes", "miercoles", "miércoles", "jueves")
        if dia_limpio in entre_semana:
            if nueva_hora < 600 or nueva_hora >= 2300:
                return False

    peli["dia"] = nuevo_dia.strip().capitalize()
    peli["hora"] = nueva_hora
    return True


def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si se puede invitar a una persona segun edad, genero, clasificacion y autorizacion."""
    if edad_invitado >= 18:
        return True

    if edad_invitado < 15 and _tiene_genero(peli, "Terror"):
        return False

    if edad_invitado <= 10 and not _tiene_genero(peli, "Familiar"):
        return False

    clasif = peli["clasificacion"].strip()
    edad_minima = 0
    if clasif == "7+":
        edad_minima = 7
    elif clasif == "13+":
        edad_minima = 13
    elif clasif == "16+":
        edad_minima = 16
    elif clasif == "18+":
        edad_minima = 18

    if edad_invitado < edad_minima:
        if _tiene_genero(peli, "Documental"):
            return True
        return autorizacion_padres

    return True
