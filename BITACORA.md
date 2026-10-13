# EJERCICIO 1

# CASO DE PRUEBA 1
# Entrada: 100 kWh
# Calculo: 100 * 1.00
# Resultado esperado: $100.00
# Se comprueba la primera tarifa.

# CASO DE PRUEBA 2
# Entrada: 150 kWh
# Calculo: 150 * 1.00
# Resultado esperado: $150.00
# Se comprueba el limite de la primera tarifa.

# CASO DE PRUEBA 3
# Entrada: 200 kWh
# Calculo: (150 * 1.00) + (50 * 1.50)
# Resultado esperado: $225.00
# Se comprueba que se apliquen las primeras dos tarifas.

# EJERCICIO2

# CASO DE PRUEBA 1
# Entrada: (80, 70, 90)
# Calculo: (80 * 0.30) + (70 * 0.30) + (90 * 0.40)
# Resultado esperado: 81.00
# Estado esperado: Aprobado
# Se comprueba que el alumno aprueba al tener una
# calificacion mayor a 70 y todos los parciales mayores a 50.

# CASO DE PRUEBA 2
# Entrada: (70, 70, 70)
# Calculo: (70 * 0.30) + (70 * 0.30) + (70 * 0.40)
# Resultado esperado: 70.00
# Estado esperado: Aprobado
# Se comprueba que el alumno aprueba con la
# calificacion minima de 70.

# CASO DE PRUEBA 3
# Entrada: (100, 100, 40)
# Calculo: (100 * 0.30) + (100 * 0.30) + (40 * 0.40)
# Resultado esperado: 76.00
# Estado esperado: Reprobado
# Se comprueba que el alumno reprueba aunque su
# calificacion final sea mayor a 70, porque tiene
# un parcial menor a 50.