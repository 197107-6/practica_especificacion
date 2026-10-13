'''
Ejercicio 3. Total de compra

Una tienda aplica 10% de descuento en compras de $1,000
o mas y 20% en compras de $5,000 o mas.
A la compra se le agrega el 16% de IVA.
Se necesita mostrar el ticket con subtotal, descuento,
IVA y total.
'''

# PROBLEMA
# Calcular el total de una compra aplicando el descuento
# correspondiente y agregando el 16% de IVA.

# ENTRADAS
# subtotal : float, pesos, valor mayor o igual a 0.

# SALIDAS
# subtotal : float, pesos, mostrar con 2 decimales.
# descuento : float, pesos, mostrar con 2 decimales.
# iva : float, pesos, mostrar con 2 decimales.
# total : float, pesos, mostrar con 2 decimales.

# REGLAS Y SUPUESTOS
# - Si la compra es menor a $1000, no hay descuento.
# - Si la compra es de $1000 o mas, se aplica 10%.
# - Si la compra es de $5000 o mas, se aplica 20%.
# - Los descuentos no se acumulan.
# - Si el subtotal es exactamente $1000, se aplica 10%.
# - Si el subtotal es exactamente $5000, se aplica 20%.
# - El IVA es del 16%.
# - El IVA se calcula despues de aplicar el descuento.
# - El total es la compra con descuento mas el IVA.
# - Se supone que el subtotal ingresado es valido.
# - Los resultados se muestran con 2 decimales.

# ALGORITMO
# 1. Leer el subtotal de la compra.
# 2. Si el subtotal es mayor o igual a 5000:
#       descuento = subtotal * 0.20
# 3. En caso contrario, si el subtotal es mayor o igual a 1000:
#       descuento = subtotal * 0.10
# 4. En caso contrario:
#       descuento = 0
# 5. Calcular el subtotal con descuento:
#       subtotalDescontado = subtotal - descuento
# 6. Calcular el IVA:
#       iva = subtotalDescontado * 0.16
# 7. Calcular el total:
#       total = subtotalDescontado + iva
# 8. Mostrar el subtotal, descuento, IVA y total
#    con 2 decimales.

# CASOS DE PRUEBA
# $500  -> Descuento: $0.00, IVA: $80.00, Total: $580.00
# $900  -> Descuento: $0.00, IVA: $144.00, Total: $1044.00
# $1000 -> Descuento: $100.00, IVA: $144.00, Total: $1044.00
# $5000 -> Descuento: $1000.00, IVA: $640.00, Total: $4640.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa unicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni calculos que no esten aqui.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerSubtotal() -> float :
#   Pide al usuario el subtotal de la compra y lo devuelve.

# calcularDescuento(subtotal) -> float :
#   Calcula el descuento dependiendo del subtotal
#   y devuelve la cantidad descontada.

# calcularIVA(subtotal, descuento) -> float :
#   Calcula el 16% de IVA sobre el subtotal
#   despues de aplicar el descuento y lo devuelve.

# calcularTotal(subtotal, descuento, iva) -> float :
#   Calcula el total restando el descuento al subtotal
#   y sumando el IVA. Devuelve el total de la compra.

# mostrarTicket(subtotal, descuento, iva, total) -> None :
#   Muestra el ticket con subtotal, descuento, IVA
#   y total, todos con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.

def leerSubtotal() -> float:
    subtotal = float(input("Ingrese el subtotal de la compra: "))
    return subtotal

def calcularDescuento(subtotal) -> float:
    if subtotal >= 5000:
        return subtotal * 0.20
    elif subtotal >= 1000:
        return subtotal * 0.10
    else:
        return 0

def calcularIVA(subtotal, descuento) -> float:
    subtotalDescontado = subtotal - descuento
    iva = subtotalDescontado * 0.16
    return iva

def calcularTotal(subtotal, descuento, iva) -> float:
    total = subtotal - descuento + iva
    return total

def mostrarTicket(subtotal, descuento, iva, total) -> None:
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
