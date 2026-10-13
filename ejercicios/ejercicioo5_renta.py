'''
Ejercicio 5. Renta de bicicletas

Un parque renta bicicletas a $30 por hora.
Si se rentan 3 horas o mas, se aplica un 15% de descuento.
Se necesita mostrar el importe a pagar segun las horas de renta.
'''

# PROBLEMA
# Calcular el importe a pagar por la renta de una bicicleta
# dependiendo de las horas rentadas y del descuento.

# ENTRADAS
# horas : int, horas, valor mayor o igual a 0.

# SALIDAS
# pago : float, pesos, mostrar con 2 decimales.

# REGLAS Y SUPUESTOS
# - Cada hora de renta cuesta $30.
# - Si se rentan menos de 3 horas, no hay descuento.
# - Si se rentan 3 horas o mas, se aplica 15% de descuento.
# - Si son exactamente 3 horas, se aplica el descuento.
# - El descuento se aplica sobre el importe total.
# - Se consideran solamente horas completas.
# - Se supone que las horas ingresadas son validas.
# - El resultado se muestra con 2 decimales.

# ALGORITMO
# 1. Leer las horas de renta.
# 2. Calcular el importe:
#       importe = horas * 30
# 3. Si las horas son mayores o iguales a 3:
#       descuento = importe * 0.15
# 4. En caso contrario:
#       descuento = 0
# 5. Calcular el pago:
#       pago = importe - descuento
# 6. Mostrar las horas rentadas y el importe a pagar
#    con 2 decimales.

# CASOS DE PRUEBA
# 1 hora  -> $30.00
# 2 horas -> $60.00
# 3 horas -> $76.50
# 4 horas -> $102.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa unicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni calculos que no esten aqui.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerHoras() -> int :
#   Pide al usuario las horas de renta y las devuelve.

# calcularRenta(horas) -> float :
#   Calcula el importe de la renta, aplicando el descuento
#   del 15% si corresponde, y devuelve el pago total.

# mostrarRenta(horas, pago) -> None :
#   Muestra las horas rentadas y el importe total
#   a pagar con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.

def leerHoras():
    horas = int(input("Ingrese las horas de renta: "))
    return horas

def calcularRenta(horas) -> float:
    importe = horas * 30
    if horas >= 3:
        descuento = importe * 0.15
    else:
        descuento = 0
    pago = importe - descuento
    return pago

def mostrarRenta(horas, pago) -> None:
    print(f"Horas de renta: {horas}")
    print(f"Importe a pagar: ${pago:.2f}")
