# Mi agenda de películas — Fundamentos de Programación

## Integrantes
- Integrante 1: Santiago Andres Godoy

## Descripción del proyecto
Aplicación de consola en Python desarrollada para gestionar una agenda de películas, consultar información clave (película más larga, duración promedio en formato `HH:MM`, estrenos posteriores a un año dado y conteo de películas `18+`), reagendar funciones evitando conflictos de horario y reglas de control horario, y verificar si un invitado puede ver una película según edad, clasificación y autorización parental.

## Estructura del repositorio
- `modulo_peliculas.py`: funciones de creación, consulta, reagendamiento y validación de invitaciones.
- `consola_peliculas.py`: interfaz interactiva por consola y menú principal.
- `README.md`: documentación del proyecto.

## Evidencia de pruebas
A continuación se resumen los escenarios probados sobre las opciones del menú:
1. **Película más larga:** se identifica la película de mayor duración en minutos dentro de la agenda activa.
2. **Duración promedio:** se calcula el promedio en minutos, se divide entre 60 y se formatea como `HH:MM`.
3. **Buscar estrenos:** se filtra por `anio > anio_limite` y se muestran los títulos coincidentes o `"Ninguna"`.
4. **Contar películas 18+:** se contabilizan las películas con clasificación `"18+"`.
5. **Reagendar película:** se prueban casos válidos, choques en el mismo día/horario y restricciones de control horario (documentales desde las 22:00, dramas los viernes y horarios entre semana fuera de 06:00–23:00).
6. **Verificar invitación:** se prueban mayores de edad, menores de 15 en terror, menores de 10 o menos según género familiar, y restricciones por edad (`7+`, `13+`, `16+`, `18+`) con y sin autorización parental.
7. **Salir:** cierra el ciclo del menú limpiamente.
