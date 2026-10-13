from ejercicios.ejercicioo1_luz import leerConsumo, calcularPago, mostrarRecibo
from ejercicios.ejercicioo2_calificacion import leerParciales, calcularFinal, determinarEstado, mostrarResultado
from ejercicios.ejercicioo3_compra import leerSubtotal, calcularDescuento, calcularIVA, calcularTotal, mostrarTicket
def ejecutar_ejercicio1():
    consumo = leerConsumo()
    pago = calcularPago(consumo)
    mostrarRecibo(consumo, pago)

def ejecutar_ejercicio2():
    parciales = leerParciales()
    final = calcularFinal(*parciales)
    estado = determinarEstado(*parciales, final)
    mostrarResultado(final, estado)

def ejecutar_ejercicio3():
    subtotal = leerSubtotal()
    descuento = calcularDescuento(subtotal)
    iva = calcularIVA(subtotal, descuento)
    total = calcularTotal(subtotal, descuento, iva)
    mostrarTicket(subtotal, descuento, iva, total)

def mostrar_menu():
    print("Seleccione un ejercicio para ejecutar:")
    print("1. Ejercicio 1: Calculo de pago de luz")
    print("2. Ejercicio 2: Calificacion final y estado del alumno")
    print("3. Ejercicio 3: Calculo de total de compra con descuento e IVA")
    print("4. Salir")

def menus():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el numero de la opcion deseada: ")
        if opcion == "1":
            ejecutar_ejercicio1()
        elif opcion == "2":
            ejecutar_ejercicio2()
        elif opcion == "3":
            ejecutar_ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida. Por favor, intente de nuevo.")