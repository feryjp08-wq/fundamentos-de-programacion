Algoritmo Caja_Bella_Studio
	Definir nombreCliente Como Cadena
	Definir servicios Como Cadena
	Definir precios Como Real
	Definir seleccionados Como L�gico
	Definir opcionPrincipal, opcionServicio, metodoPago, i, cantidadVentas Como Entero
	Definir totalCliente, totalEfectivo, totalTarjeta, totalCaja Como Real
	Dimensionar servicios(6)
	Dimensionar precios(6)
	Dimensionar seleccionados(6)
	// Catalogo de servicios
	servicios[1] <- 'Corte de cabello'
	servicios[2] <- 'Aplicacion de tinte'
	servicios[3] <- 'Manicure'
	servicios[4] <- 'Pedicure'
	servicios[5] <- 'Peinado'
	servicios[6] <- 'Tratamiento capilar'
	precios[1] <- 150
	precios[2] <- 450
	precios[3] <- 120
	precios[4] <- 180
	precios[5] <- 200
	precios[6] <- 300
	// Inicializar acumuladores
	totalEfectivo <- 0
	totalTarjeta <- 0
	totalCaja <- 0
	cantidadVentas <- 0
	opcionPrincipal <- 0
	Mientras opcionPrincipal<>3 Hacer
		Escribir '===== BELLA STUDIO ====='
		Escribir '1. Registrar venta'
		Escribir '2. Corte de caja'
		Escribir '3. Salir'
		Escribir 'Selecciona una opcion:'
		Leer opcionPrincipal
		Si opcionPrincipal=1 Entonces
			Escribir 'Nombre del cliente:'
			Leer nombreCliente
			totalCliente <- 0
			Para i<-1 Hasta 6 Hacer
				seleccionados[i] <- Falso
			FinPara
			opcionServicio <- 0
			Mientras opcionServicio<>7 Hacer
				Escribir '===== SERVICIOS ====='
				Para i<-1 Hasta 6 Hacer
					Escribir i, '. ', servicios[i], ' - $', precios[i]
				FinPara
				Escribir '7. Terminar seleccion'
				Escribir 'Selecciona un servicio:'
				Leer opcionServicio
				Si opcionServicio>=1 Y opcionServicio<=6 Entonces
					Si seleccionados[opcionServicio]=Falso Entonces
						seleccionados[opcionServicio] <- Verdadero
						Escribir 'Servicio agregado: ', servicios[opcionServicio]
					SiNo
						Escribir 'Este servicio ya fue agregado'
					FinSi
				SiNo
					Si opcionServicio<>7 Entonces
						Escribir 'Opcion no valida'
					FinSi
				FinSi
			FinMientras
			// Sumar los servicios seleccionados
			Para i<-1 Hasta 6 Hacer
				Si seleccionados[i]=Verdadero Entonces
					totalCliente <- totalCliente+precios[i]
				FinSi
			FinPara
			Si totalCliente>0 Entonces
				Escribir 'Cliente: ', nombreCliente
				Escribir 'Total a pagar: $', totalCliente
				metodoPago <- 0
				Mientras metodoPago<>1 Y metodoPago<>2 Hacer
					Escribir '1. Efectivo'
					Escribir '2. Tarjeta'
					Escribir 'Selecciona el metodo de pago:'
					Leer metodoPago
					Si metodoPago<>1 Y metodoPago<>2 Entonces
						Escribir 'Metodo de pago no valido'
					FinSi
				FinMientras
				Si metodoPago=1 Entonces
					totalEfectivo <- totalEfectivo+totalCliente
				SiNo
					totalTarjeta <- totalTarjeta+totalCliente
				FinSi
				totalCaja <- totalEfectivo+totalTarjeta
				cantidadVentas <- cantidadVentas+1
				Escribir 'Venta registrada correctamente'
			SiNo
				Escribir 'No se registraron servicios'
			FinSi
		SiNo
			Si opcionPrincipal=2 Entonces
				Escribir '===== CORTE DE CAJA ====='
				Escribir 'Ventas realizadas: ', cantidadVentas
				Escribir 'Total en efectivo: $', totalEfectivo
				Escribir 'Total en tarjeta: $', totalTarjeta
				Escribir 'Total general: $', totalCaja
			SiNo
				Si opcionPrincipal<>3 Entonces
					Escribir 'Opcion no valida'
				FinSi
			FinSi
		FinSi
	FinMientras
	Escribir 'Gracias por utilizar Bella Studio'
FinAlgoritmo
