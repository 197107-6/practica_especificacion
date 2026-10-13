'''
Ejercicio 7. Multa por velocidad

En una avenida el limite es de 60 km/h.
Si se excede hasta por 20 km/h, la multa es de $500.
Si se excede por mas de 20 km/h, la multa es de $1,000.
Se necesita mostrar la multa a partir de la velocidad
del vehiculo.
'''

# PROBLEMA
# Calcular el importe de una multa dependiendo
# de la velocidad a la que circula un vehiculo.

# ENTRADAS
# velocidad : float, km/h, valor mayor o igual a 0.

# SALIDAS
# multa : float, pesos, mostrar con 2 decimales.

# REGLAS Y SUPUESTOS
# - El limite de velocidad es de 60 km/h.
# - Si la velocidad es menor o igual a 60, no hay multa.
# - Si la velocidad es mayor a 60 y menor o igual a 80,
#   la multa es de $500.
# - Si la velocidad es mayor a 80, la multa es de $1000.
# - Si circula exactamente a 60 km/h, no hay multa.
# - Si circula exactamente a 80 km/h, la multa es de $500.
# - La velocidad puede tener decimales.
# - Se supone que la velocidad ingresada es valida.
# - La multa se muestra con 2 decimales.

# ALGORITMO
# 1. Leer la velocidad del vehiculo en km/h.
# 2. Si la velocidad es menor o igual a 60:
#       multa = 0
# 3. En caso contrario, si la velocidad es menor o igual a 80:
#       multa = 500
# 4. En caso contrario:
#       multa = 1000
# 5. Mostrar la velocidad del vehiculo y el importe
#    de la multa con 2 decimales.

# CASOS DE PRUEBA
# 50 km/h  -> $0.00
# 60 km/h  -> $0.00
# 61 km/h  -> $500.00
# 80 km/h  -> $500.00
# 81 km/h  -> $1000.00
# 100 km/h -> $1000.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa unicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni calculos que no esten aqui.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVelocidad() -> float :
#   Pide al usuario la velocidad del vehiculo
#   en km/h y la devuelve.

# calcularMulta(velocidad) -> float :
#   Calcula el importe de la multa dependiendo
#   de la velocidad y devuelve el resultado.

# mostrarMulta(velocidad, multa) -> None :
#   Muestra la velocidad del vehiculo y el importe
#   de la multa con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.

def leerVelocidad() -> float:
    velocidad = float(input("Ingrese la velocidad del vehiculo (km/h): "))
    return velocidad

def calcularMulta(velocidad) -> float:
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000
    return multa

def mostrarMulta(velocidad, multa) -> None:
    print(f"Velocidad del vehiculo: {velocidad} km/h")
    print(f"Importe de la multa: ${multa:.2f}")
