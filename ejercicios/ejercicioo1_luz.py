'''
Ejercicio 1. Recibo de luz

Una compañía eléctrica cobra el consumo mensual con tres tarifas:
$1.00 por kWh hasta 150 kWh, $1.50 por kWh de 151 a 280 kWh
y $3.00 por kWh arriba de 280 kWh.

Se necesita calcular el importe del recibo a partir del consumo
del mes.
'''

# PROBLEMA
# Calcular cuánto debe pagar una persona por su consumo mensual
# de electricidad, dependiendo de los kWh consumidos.

# ENTRADAS
# consumo : float, kWh, valor mayor o igual a 0.

# SALIDAS
# pago : float, pesos mexicanos, mostrar con 2 decimales.
# Mostrar el consumo en kWh y el total a pagar en pesos.

# REGLAS Y SUPUESTOS
# - Los primeros 150 kWh cuestan $1.00 cada uno.
# - Los siguientes 130 kWh cuestan $1.50 cada uno.
# - Los kWh que superen 280 cuestan $3.00 cada uno.
# - Si el consumo es exactamente 150, se cobra la primera tarifa.
# - Si el consumo es exactamente 280, se cobran las primeras
#   dos tarifas.
# - Las tarifas se aplican por bloques de consumo.
# - El consumo puede tener decimales.
# - Se supone que el consumo ingresado es válido y no negativo.
# - El pago se muestra redondeado a 2 decimales.

# ALGORITMO
# 1. Leer el consumo mensual de electricidad en kWh.
# 2. Si el consumo es menor o igual a 150:
#       pago = consumo * 1.00
# 3. En caso contrario, si el consumo es menor o igual a 280:
#       pago = 150 * 1.00 + (consumo - 150) * 1.50
# 4. En caso contrario:
#       pago = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00
# 5. Mostrar el consumo ingresado y el total a pagar
#    con 2 decimales.

# CASOS DE PRUEBA
# 100 kWh -> $100.00
# 150 kWh -> $150.00
# 200 kWh -> $225.00
# 280 kWh -> $345.00
# 300 kWh -> $405.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo;
#   se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerConsumo() -> float :
#   Pide al usuario el consumo mensual en kWh y lo devuelve.

# calcularPago(consumo) -> float :
#   Recibe el consumo, calcula el pago según las tres tarifas
#   y devuelve el importe total.

# mostrarRecibo(consumo, pago) -> None :
#   Muestra el consumo mensual y el importe total a pagar
#   en pesos con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones
# del contrato.