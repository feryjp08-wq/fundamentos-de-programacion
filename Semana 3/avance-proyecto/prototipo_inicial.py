
# SISTEMA DE REGISTRO DE CAJA - BELLA STUDIO

# Catalogo de servicios
servicios = [
    ("Corte de cabello", 150.00),
    ("Aplicacion de tinte", 450.00),
    ("Manicure", 120.00),
    ("Pedicure", 180.00),
    ("Peinado", 200.00),
    ("Tratamiento capilar", 300.00)
]

# Acumuladores de caja
total_efectivo = 0.0
total_tarjeta = 0.0
total_caja = 0.0
cantidad_ventas = 0

# Menu principal
opcion_principal = 0

while opcion_principal != 3:

    print("\n===== BELLA STUDIO =====")
    print("1. Registrar venta")
    print("2. Corte de caja")
    print("3. Salir")

    entrada = input("Selecciona una opcion: ")

    if entrada.isdigit():
        opcion_principal = int(entrada)
    else:
        opcion_principal = 0

    # REGISTRAR VENTA
    if opcion_principal == 1:

        nombre_cliente = input("\nNombre del cliente: ").strip()

        while nombre_cliente == "":
            print("Debes ingresar el nombre del cliente.")
            nombre_cliente = input("Nombre del cliente: ").strip()

        # Servicios seleccionados por el cliente
        seleccionados = []
        servicios_agregados = set()

        opcion_servicio = 0

        while opcion_servicio != 7:

            print("\n===== SERVICIOS DISPONIBLES =====")

            for i in range(len(servicios)):
                print(
                    i + 1, ".",
                    servicios[i][0],
                    "- $", format(servicios[i][1], ".2f")
                )

            print("7. Terminar seleccion")

            entrada = input("Selecciona un servicio: ")

            if entrada.isdigit():
                opcion_servicio = int(entrada)
            else:
                opcion_servicio = 0

            if 1 <= opcion_servicio <= 6:

                if opcion_servicio not in servicios_agregados:

                    servicios_agregados.add(opcion_servicio)
                    seleccionados.append(opcion_servicio)

                    print(
                        "Servicio agregado:",
                        servicios[opcion_servicio - 1][0]
                    )

                else:
                    print("Este servicio ya fue agregado.")

            elif opcion_servicio != 7:
                print("Opcion no valida.")

        # Calcular total de la venta
        total_cliente = 0.0

        for numero in seleccionados:
            total_cliente = total_cliente + servicios[numero - 1][1]

        if total_cliente > 0:

            print("\n===== RESUMEN DE VENTA =====")
            print("Cliente:", nombre_cliente)

            for numero in seleccionados:
                print(
                    servicios[numero - 1][0],
                    "- $",
                    format(servicios[numero - 1][1], ".2f")
                )

            print("Total a pagar: $", format(total_cliente, ".2f"))

            # Seleccionar metodo de pago
            metodo_pago = 0

            while metodo_pago != 1 and metodo_pago != 2:

                print("\n===== METODO DE PAGO =====")
                print("1. Efectivo")
                print("2. Tarjeta")

                entrada = input("Selecciona el metodo de pago: ")

                if entrada.isdigit():
                    metodo_pago = int(entrada)
                else:
                    metodo_pago = 0

                if metodo_pago != 1 and metodo_pago != 2:
                    print("Metodo de pago no valido.")

            # Actualizar acumuladores
            if metodo_pago == 1:
                total_efectivo = total_efectivo + total_cliente
                print("Pago realizado en efectivo.")

            else:
                total_tarjeta = total_tarjeta + total_cliente
                print("Pago realizado con tarjeta.")

            total_caja = total_efectivo + total_tarjeta
            cantidad_ventas = cantidad_ventas + 1

            print("Venta registrada correctamente.")

        else:
            print("No se registraron servicios. Venta cancelada.")

    # CORTE DE CAJA
    elif opcion_principal == 2:

        print("\n===== CORTE DE CAJA =====")
        print("Ventas realizadas:", cantidad_ventas)
        print("Total en efectivo: $", format(total_efectivo, ".2f"))
        print("Total en tarjeta: $", format(total_tarjeta, ".2f"))
        print("Total general: $", format(total_caja, ".2f"))

    # SALIR
    elif opcion_principal == 3:
        print("\nGracias por utilizar Bella Studio.")

    else:
        print("Opcion no valida. Intenta nuevamente.")
