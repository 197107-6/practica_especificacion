# EJERCICIO 1

# CASO DE PRUEBA 1
# Entrada: 100 kWh
# Calculo: 100 * 1.00
# Resultado esperado: $100.00
# Se comprueba la primera tarifa.APROBADO

# CASO DE PRUEBA 2
# Entrada: 150 kWh
# Calculo: 150 * 1.00
# Resultado esperado: $150.00
# Se comprueba el limite de la primera tarifa.APROBADO

# CASO DE PRUEBA 3
# Entrada: 200 kWh
# Calculo: (150 * 1.00) + (50 * 1.50)
# Resultado esperado: $225.00
# Se comprueba que se apliquen las primeras dos tarifas.APROBADO

# EJERCICIO2

# CASO DE PRUEBA 1
# Entrada: (80, 70, 90)
# Calculo: (80 * 0.30) + (70 * 0.30) + (90 * 0.40)
# Resultado esperado: 81.00
# Estado esperado: Aprobado
# Se comprueba que el alumno aprueba al tener una
# calificacion mayor a 70 y todos los parciales mayores a 50.APROBADO

# CASO DE PRUEBA 2
# Entrada: (70, 70, 70)
# Calculo: (70 * 0.30) + (70 * 0.30) + (70 * 0.40)
# Resultado esperado: 70.00
# Estado esperado: Aprobado
# Se comprueba que el alumno aprueba con la
# calificacion minima de 70. APROBADO

# CASO DE PRUEBA 3
# Entrada: (100, 100, 40)
# Calculo: (100 * 0.30) + (100 * 0.30) + (40 * 0.40)
# Resultado esperado: 76.00
# Estado esperado: Reprobado
# Se comprueba que el alumno reprueba aunque su
# calificacion final sea mayor a 70, porque tiene
# un parcial menor a 50.APROBADO

# EJERCICIO 3

# CASO DE PRUEBA 1
# Entrada: $500
# Descuento: 500 * 0 = $0.00
# IVA: 500 * 0.16 = $80.00
# Total: 500 - 0 + 80 = $580.00
# Resultado esperado: $580.00
# Se comprueba que las compras menores a $1000
# no tengan descuento.APROBADO

# CASO DE PRUEBA 2
# Entrada: $900
# Descuento: 900 * 0 = $0.00
# IVA: 900 * 0.16 = $144.00
# Total: 900 - 0 + 144 = $1044.00
# Resultado esperado: $1044.00
# Se comprueba que no se aplique descuento
# cuando la compra sea menor a $1000.APROBADO

# CASO DE PRUEBA 3
# Entrada: $1000
# Descuento: 1000 * 0.10 = $100.00
# Subtotal con descuento: 1000 - 100 = $900.00
# IVA: 900 * 0.16 = $144.00
# Total: 900 + 144 = $1044.00
# Resultado esperado: $1044.00
# Se comprueba que al llegar a $1000
# se aplique el descuento del 10%.APROBADO
