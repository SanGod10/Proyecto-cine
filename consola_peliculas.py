"""
Agenda de peliculas.
Modulo de interaccion por consola.
"""
import modulo_peliculas as mod


def _hora_str_a_int(hora_str: str) -> int:
    """Convierte 'HH:MM' a entero HHMM."""
    partes = hora_str.strip().split(":")
    return int(partes[0]) * 100 + int(partes[1])


def construir_catalogo_nuevo() -> list:
    """Crea la lista de 25 peliculas con el nuevo catalogo."""
    datos = [
        # TODOS
        ("Wall-E", "Animacion", 98, 2008, "Todos", "14:00", "Lunes"),
        ("Ratatouille", "Animacion", 111, 2007, "Todos", "15:00", "Martes"),
        ("Monsters Inc", "Animacion", 92, 2001, "Todos", "14:00", "Miercoles"),
        ("El viaje de Chihiro", "Fantasia", 125, 2001, "Todos", "15:00", "Jueves"),
        ("Los increibles", "Animacion", 115, 2004, "Todos", "14:00", "Viernes"),

        # 7+
        ("Shrek 2", "Animacion", 93, 2004, "7+", "16:00", "Lunes"),
        ("Coraline", "Fantasia", 100, 2009, "7+", "16:00", "Martes"),
        ("Cars", "Animacion", 117, 2006, "7+", "16:00", "Miercoles"),
        ("La era de hielo", "Animacion", 81, 2002, "7+", "16:00", "Jueves"),
        ("Ponyo", "Animacion", 101, 2008, "7+", "16:00", "Viernes"),

        # 13+
        ("Matrix", "Ciencia ficcion", 136, 1999, "13+", "18:00", "Lunes"),
        ("Jurassic Park", "Ciencia ficcion", 127, 1993, "13+", "18:00", "Martes"),
        ("Gladiador", "Accion", 155, 2000, "13+", "18:00", "Miercoles"),
        ("El senor de los anillos: La comunidad del anillo", "Fantasia", 178, 2001, "13+", "18:00", "Jueves"),
        ("Volver al futuro", "Ciencia ficcion", 116, 1985, "13+", "18:00", "Viernes"),

        # 16+
        ("Whiplash", "Drama", 106, 2014, "16+", "20:00", "Lunes"),
        ("Blade Runner 2049", "Ciencia ficcion", 164, 2017, "16+", "20:00", "Martes"),
        ("Mad Max: Furia en el camino", "Accion", 120, 2015, "16+", "20:00", "Miercoles"),
        ("Oldboy", "Suspenso", 120, 2003, "16+", "20:00", "Jueves"),
        ("El resplandor", "Terror", 146, 1980, "16+", "20:00", "Viernes"),

        # 18+
        ("Taxi Driver", "Drama", 114, 1976, "18+", "21:00", "Lunes"),
        ("Pulp Fiction", "Drama", 154, 1994, "18+", "21:00", "Martes"),
        ("El silencio de los inocentes", "Terror", 118, 1991, "18+", "21:00", "Miercoles"),
        ("Django sin cadenas", "Accion", 165, 2012, "18+", "21:00", "Jueves"),
        ("Requiem por un sueno", "Drama", 102, 2000, "18+", "21:00", "Viernes"),
    ]
    return [
        mod.crear_pelicula(nom, gen, dur, anio, clas, _hora_str_a_int(hr), dia)
        for nom, gen, dur, anio, clas, hr, dia in datos
    ]


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de una pelicula."""
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + " mins")
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)

    if (hora // 100 < 10):
        hora_formato = "0" + str(hora // 100)
    else:
        hora_formato = str(hora // 100)

    if (hora % 100 < 10):
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    pelicula = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print("\nLa pelicula mas larga es:")
    mostrar_informacion_pelicula(pelicula)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("\nLa duracion promedio de las peliculas es: " + promedio)


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    try:
        anio = int(input("Ingrese el anio limite: ").strip())
    except ValueError:
        print("Debe ingresar un numero entero valido.")
        return
    resultado = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("\nPeliculas estrenadas despues de " + str(anio) + ": " + resultado)


def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("\nCantidad de peliculas con clasificacion 18+: " + str(cantidad))


def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print("Reagendar una pelicula de la agenda")
    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
        return

    nuevo_dia = input("Ingrese el nuevo dia de la semana: ").strip()
    try:
        nueva_hora = int(input("Ingrese la nueva hora en formato 24h (ej. 800, 1430, 2100): ").strip())
    except ValueError:
        print("La hora debe ser un numero entero.")
        return

    resp = input("Desea activar el control horario? (s/n): ").strip().lower()
    control_horario = resp in ("s", "si", "sí", "1", "true")

    exito = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
    if exito:
        print("La pelicula fue reagendada con exito.")
    else:
        print("No fue posible reagendar la pelicula.")


def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print("Decidir si se puede invitar a alguien a ver una pelicula")
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
        return

    try:
        edad = int(input("Ingrese la edad del invitado: ").strip())
    except ValueError:
        print("La edad debe ser un numero entero.")
        return

    resp = input("Cuenta con autorizacion de los padres? (s/n): ").strip().lower()
    autorizacion = resp in ("s", "si", "sí", "1", "true")

    puede_ver = mod.decidir_invitar(pelicula, edad, autorizacion)
    if puede_ver:
        print("Si se puede invitar a la persona a ver '" + pelicula["nombre"] + "'.")
    else:
        print("No se puede invitar a la persona a ver '" + pelicula["nombre"] + "'.")


def iniciar_aplicacion() -> None:
    catalogo = construir_catalogo_nuevo()
    pelicula1, pelicula2, pelicula3, pelicula4, pelicula5 = catalogo[:5]

    ejecutando = True
    while ejecutando:
        print("\n\nMi agenda de peliculas" + "\n" + ("-" * 50))
        for idx, peli in enumerate((pelicula1, pelicula2, pelicula3, pelicula4, pelicula5), start=1):
            print(f"Pelicula {idx}")
            mostrar_informacion_pelicula(peli)
            print("-" * 50)

        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando


if __name__ == "__main__":
    iniciar_aplicacion()
