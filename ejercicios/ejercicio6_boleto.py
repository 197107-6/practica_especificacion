'''
Ejercicio 6. Boleto de cine

Un cine cobra $80 por boleto.
Los niños de hasta 12 años y los adultos de 60 años
o mas pagan la mitad.
Se necesita mostrar el precio del boleto segun la edad.
'''

# PROBLEMA
# Calcular el precio de un boleto de cine dependiendo
# de la edad de la persona.

# ENTRADAS
# edad : int, años, valor mayor o igual a 0.

# SALIDAS
# precio : float, pesos, mostrar con 2 decimales.

# REGLAS Y SUPUESTOS
# - El precio normal del boleto es de $80.
# - Los niños de 12 años o menos pagan la mitad.
# - Los adultos de 60 años o mas pagan la mitad.
# - El precio con descuento es de $40.
# - Las personas de 13 a 59 años pagan $80.
# - Si la edad es exactamente 12, paga $40.
# - Si la edad es exactamente 60, paga $40.
# - Se consideran edades en años completos.
# - Se supone que la edad ingresada es valida.
# - El precio se muestra con 2 decimales.

# ALGORITMO
# 1. Leer la edad de la persona.
# 2. Si la edad es menor o igual a 12:
#       precio = 80 * 0.50
# 3. En caso contrario, si la edad es mayor o igual a 60:
#       precio = 80 * 0.50
# 4. En caso contrario:
#       precio = 80
# 5. Mostrar la edad y el precio del boleto
#    con 2 decimales.

# CASOS DE PRUEBA
# 8 años  -> $40.00
# 12 años -> $40.00
# 13 años -> $80.00
# 59 años -> $80.00
# 60 años -> $40.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa unicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni calculos que no esten aqui.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerEdad() -> int :
#   Pide al usuario su edad y la devuelve.

# calcularPrecio(edad) -> float :
#   Calcula el precio del boleto dependiendo de la edad
#   y devuelve el importe correspondiente.

# mostrarPrecio(edad, precio) -> None :
#   Muestra la edad de la persona y el precio
#   del boleto con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.

def leerEdad() -> int:
    edad = int(input("Ingrese su edad: "))
    return edad

def calcularPrecio(edad) -> float:
    if edad <= 12 or edad >= 60:
        precio = 80 * 0.50
    else:
        precio = 80
    return precio

def mostrarPrecio(edad, precio) -> None:
    print(f"Edad: {edad} años")
    print(f"Precio del boleto: ${precio:.2f}")
