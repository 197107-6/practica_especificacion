'''
Ejercicio 2. Calificación final

La calificación final de una materia se obtiene de tres
parciales que valen 30%, 30% y 40%.
La materia se aprueba con 70.
Un parcial menor a 50 reprueba la materia.
Se necesita mostrar la calificación final y si el alumno aprobó.
'''

# PROBLEMA
# Calcular la calificacion final de un alumno usando tres
# parciales y determinar si aprobo o reprobo la materia.

# ENTRADAS
# parcial1 : float, puntos, de 0 a 100.
# parcial2 : float, puntos, de 0 a 100.
# parcial3 : float, puntos, de 0 a 100.

# SALIDAS
# final : float, puntos, mostrar con 2 decimales.
# estado : str, mostrar "Aprobado" o "Reprobado".

# REGLAS Y SUPUESTOS
# - El primer parcial vale 30%.
# - El segundo parcial vale 30%.
# - El tercer parcial vale 40%.
# - La calificacion minima para aprobar es 70.
# - Si algun parcial es menor a 50, el alumno reprueba.
# - Si un parcial es exactamente 50, no reprueba
#   automaticamente por esa condicion.
# - Si el promedio es menor a 70, el alumno reprueba.
# - Para aprobar debe tener al menos 70 de calificacion
#   final y ningun parcial menor a 50.
# - Las calificaciones pueden tener decimales.
# - Se supone que las entradas son validas.
# - La calificacion final se muestra con 2 decimales.

# ALGORITMO
# 1. Leer las calificaciones de los tres parciales.
# 2. Calcular la calificacion final:
#       final = parcial1 * 0.30 + parcial2 * 0.30
#               + parcial3 * 0.40
# 3. Si algun parcial es menor a 50:
#       estado = "Reprobado"
# 4. En caso contrario, si final es mayor o igual a 70:
#       estado = "Aprobado"
# 5. En caso contrario:
#       estado = "Reprobado"
# 6. Mostrar la calificacion final con 2 decimales
#    y el estado del alumno.

# CASOS DE PRUEBA
# (80, 70, 90) -> 81.00, Aprobado
# (70, 70, 70) -> 70.00, Aprobado
# (100, 100, 40) -> 76.00, Reprobado
# (69, 70, 70) -> 69.70, Reprobado

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa unicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni calculos que no esten aqui.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerParciales() -> tuple :
#   Pide las tres calificaciones y las devuelve.

# calcularFinal(parcial1, parcial2, parcial3) -> float :
#   Calcula la calificacion final usando los porcentajes
#   de cada parcial y devuelve el resultado.

# determinarEstado(parcial1, parcial2, parcial3, final) -> str :
#   Determina si el alumno aprobo o reprobo considerando
#   la calificacion final y que ningun parcial sea menor a 50.

# mostrarResultado(final, estado) -> None :
#   Muestra la calificacion final con 2 decimales
#   y si el alumno aprobo o reprobo.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.

def leerParciales() -> tuple:
    parcial1 = float(input("Ingrese la calificacion del primer parcial: "))
    parcial2 = float(input("Ingrese la calificacion del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificacion del tercer parcial: "))
    return (parcial1, parcial2, parcial3)

def calcularFinal(parcial1, parcial2, parcial3) -> float:
    final = parcial1 * 0.30 + parcial2 * 0.30 + parcial3 * 0.40
    return final

def determinarEstado(parcial1, parcial2, parcial3, final) -> str:
    if parcial1 < 50 or parcial2 < 50 or parcial3 < 50:
        return "Reprobado"
    elif final >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrarResultado(final, estado) -> None:
    print(f"Calificacion final: {final:.2f}")
    print(f"Estado: {estado}")
