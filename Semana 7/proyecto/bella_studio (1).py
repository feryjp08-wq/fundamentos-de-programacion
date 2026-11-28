# BELLA STUDIO - Registro de servicios y caja
# Autora: Fernanda Yvonne Juárez Plaza
# Registra clientes, servicios y pagos sin perder el historial.
import time
from datetime import datetime
import os


def pedir_fecha():
    """Pide y valida la fecha de operación."""
    while True:
        try:
            texto = input("Fecha de operación (dd/mm/aaaa): ").strip()
            fecha = datetime.strptime(texto, "%d/%m/%Y")
            if fecha.strftime("%d/%m/%Y") == texto:
                dia = fecha.day
                mes = fecha.month
                anio = fecha.year
                Fecha = dia, mes, anio
                return Fecha
            else:
                print("Escribe la fecha como dd/mm/aaaa.")
        except ValueError:
            print("Fecha inválida. Usa dd/mm/aaaa y una fecha existente.")


def fecha_texto(Fecha):
    """Convierte la tupla a texto para guardar la fecha."""
    return f"{Fecha[0]:02d}/{Fecha[1]:02d}/{Fecha[2]:04d}"


def carga():
    """Muestra cinco pasos de carga, con un segundo de pausa cada uno."""
    for i in range(1, 6):
        time.sleep(1)
        print("Cargando...", i * 20, "%")
    print("Carga completa.")


def inactividad():
    """Simula diez minutos en cinco segundos y pregunta si desea seguir."""
    for minuto in range(1, 11):
        time.sleep(0.5)
        print("Inactividad:", minuto, "minuto(s)")
    while True:
        respuesta = input("¿Deseas seguir con el programa? (si/no): ").strip().lower()
        if respuesta == "si" or respuesta == "sí":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Responde si o no.")


def texto_seguro(mensaje):
    """Solicita texto no vacío y evita romper los separadores de registros."""
    while True:
        dato = input(mensaje).strip()
        if dato != "" and "|" not in dato:
            return dato
        print("Escribe un dato válido sin el carácter |.")

def nombre_archivo(nombre):
    """Revisa que el nombre corresponda a un archivo TXT local."""
    nombre = nombre.strip()
    if nombre == "" or nombre.startswith("."):
        raise ValueError("Nombre de archivo inválido.")
    for caracter in nombre:
        if caracter in '/\\:*?"<>|':
            raise ValueError("Nombre de archivo inválido.")
    if not nombre.lower().endswith(".txt"):
        nombre = nombre + ".txt"
    return nombre


def listar_archivos():
    """Muestra los archivos TXT disponibles en una lista."""
    try:
        archivos = []
        for nombre in os.listdir("."):
            if nombre.endswith('.txt') and os.path.isfile(nombre):
                archivos.append(nombre)
        archivos.sort()
        print("Archivos disponibles:")
        for i in range(len(archivos)):
            print(i + 1, archivos[i])
        return archivos
    except OSError as error:
        print("No se pudieron listar los archivos:", error)
        return []

def leer_archivo():
    """Permite elegir un archivo por número o nombre y muestra su contenido."""
    archivos = listar_archivos()
    try:
        nombre = input("Número o nombre del archivo: ").strip()
        if nombre.isdigit():
            numero = int(nombre)
            if not 1 <= numero <= len(archivos):
                raise ValueError("Número de archivo inválido.")
            nombre = archivos[numero-1]
        with open(nombre_archivo(nombre), 'r', encoding='utf-8') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para leer el archivo.")
    except (ValueError, OSError, UnicodeError) as error:
        print("No se pudo leer:", error)

def crear_archivo(Fecha, usuario):
    """Crea un TXT con fecha sin sobrescribir otro existente."""
    try:
        ruta = nombre_archivo(input("Nombre del nuevo archivo: "))
        contenido = texto_seguro("Contenido inicial: ")
        with open(ruta, 'x', encoding='utf-8') as archivo:
            archivo.write(f"{fecha_texto(Fecha)} | {usuario} | {contenido}\n")
        print("Archivo creado correctamente.")
    except FileExistsError:
        print("El archivo ya existe; no se sobrescribió.")
    except PermissionError:
        print("No tienes permiso para crear el archivo.")
    except (ValueError, OSError, UnicodeError) as error:
        print("No se pudo crear:", error)

def agregar_registro(Fecha, usuario):
    """Anexa información a un TXT existente sin alterar datos comerciales."""
    listar_archivos()
    try:
        ruta = nombre_archivo(input("Nombre del archivo: "))
        if ruta.lower() in PROTEGIDOS:
            print("Este archivo se actualiza desde las operaciones del negocio.")
            return
        if not os.path.isfile(ruta):
            raise FileNotFoundError
        dato = texto_seguro("Registro a agregar: ")
        with open(ruta, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{fecha_texto(Fecha)} | {usuario} | {dato}\n")
        print("Registro agregado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para modificar el archivo.")
    except (ValueError, OSError, UnicodeError) as error:
        print("No se pudo agregar:", error)

def guardar(nombre, registro):
    """Agrega un registro comercial y comunica cualquier error de escritura."""
    try:
        with open(nombre, 'a', encoding='utf-8') as archivo:
            archivo.write(registro + '\n')
        return True
    except PermissionError:
        print("Sin permisos para guardar en", nombre)
    except OSError as error:
        print("No se pudo guardar:", error)
    return False

def pago():
    """Valida el método de pago."""
    while True:
        opcion = input("1. Efectivo | 2. Tarjeta: ").strip()
        if opcion == '1':
            return 'Efectivo'
        if opcion == '2':
            return 'Tarjeta'
        print("Método de pago inválido.")

PROTEGIDOS = {'servicios.txt', 'registro_servicios.txt', 'caja.txt'}
servicios = [
    ('Corte de cabello', 150.0),
    ('Aplicacion de tinte', 450.0),
    ('Manicure', 120.0),
    ('Pedicure', 180.0),
    ('Peinado', 200.0),
    ('Tratamiento capilar', 300.0),
]

def mostrar_servicios():
    """Enumera los servicios y precios del catálogo original."""
    print('\n===== SERVICIOS DISPONIBLES =====')
    for i in range(len(servicios)):
        print(f"{i + 1}. {servicios[i][0]} - ${servicios[i][1]:.2f}")

def registrar_servicio(Fecha, usuario):
    """Registra una visita del cliente y evita seleccionar servicios repetidos."""
    cliente = texto_seguro('Nombre del cliente: ')
    seleccionados = []
    servicios_agregados = set()
    while True:
        mostrar_servicios()
        print('7. Terminar selección')
        try:
            numero = int(input('Selecciona un servicio: ').strip())
            if numero == 7:
                break
            if not 1 <= numero <= len(servicios):
                print('Servicio inválido.')
            elif numero in servicios_agregados:
                print('Este servicio ya fue agregado.')
            else:
                servicios_agregados.add(numero)
                seleccionados.append(numero)
                print('Servicio agregado:', servicios[numero-1][0])
        except ValueError:
            print('Ingresa un número válido.')
    if not seleccionados:
        print('Venta cancelada: no se registraron servicios.')
        return
    total = 0.0
    nombres_elegidos = []
    print('\n===== RESUMEN DE VENTA =====')
    print('Cliente:', cliente)
    for numero in seleccionados:
        nombre, precio = servicios[numero-1]
        total += precio
        nombres_elegidos.append(nombre)
        print(f'{nombre}: ${precio:.2f}')
    print(f'Total a pagar: ${total:.2f}')
    metodo = pago()
    # El historial de visitas es la fuente de ingresos y de consultas por cliente.
    detalle = ", ".join(nombres_elegidos)
    linea = f"{fecha_texto(Fecha)}|{usuario}|{cliente}|{detalle}|{metodo}|{total:.2f}"
    if guardar('registro_servicios.txt', linea):
        print('Venta registrada correctamente.')
        if not guardar('clientes.txt', f'{fecha_texto(Fecha)} | {usuario} | {cliente}'):
            print('La venta se conservó; no se pudo actualizar el directorio de clientes.')
    else:
        print('No se registró la venta.')

def recuperar_visitas():
    """Lee los registros de visitas y valida su formato antes de utilizarlos."""
    visitas = []
    try:
        with open('registro_servicios.txt', 'r', encoding='utf-8') as archivo:
            numero = 0
            for linea in archivo:
                numero = numero + 1
                if not linea.strip() or linea.startswith('#'):
                    continue
                try:
                    fecha, operador, cliente, detalle, metodo, importe = linea.strip().split('|')
                    datetime.strptime(fecha, '%d/%m/%Y')
                    importe = float(importe)
                    if metodo not in ('Efectivo', 'Tarjeta') or not 0 < importe < float('inf'):
                        raise ValueError
                    visitas.append((fecha, cliente, detalle, metodo, importe))
                except ValueError:
                    print(f'Registro incorrecto en línea {numero}. Consulta cancelada.')
                    return None
        return visitas
    except (OSError, UnicodeError) as error:
        print('No se pudo consultar el historial:', error)
        return None

def corte_caja(Fecha, usuario):
    """Calcula ingresos y número de visitas para la fecha de operación."""
    visitas = recuperar_visitas()
    if visitas is None:
        return
    total_efectivo = 0.0
    total_tarjeta = 0.0
    cantidad_ventas = 0
    for fecha, cliente, detalle, metodo, importe in visitas:
        if fecha == fecha_texto(Fecha):
            if metodo == "Efectivo":
                total_efectivo += importe
            else:
                total_tarjeta += importe
            cantidad_ventas += 1
    total_caja = total_efectivo + total_tarjeta
    print('\n===== CORTE DE CAJA =====')
    print('Ventas realizadas:', cantidad_ventas)
    print(f"Total en efectivo: ${total_efectivo:.2f}")
    print(f"Total en tarjeta: ${total_tarjeta:.2f}")
    print(f'Total general: ${total_caja:.2f}')
    guardar('caja.txt', f"{fecha_texto(Fecha)}|{usuario}|{cantidad_ventas}|{total_efectivo:.2f}|{total_tarjeta:.2f}|{total_caja:.2f}")

def historial_cliente():
    """Busca las visitas de un cliente sin distinguir mayúsculas."""
    nombre = texto_seguro('Nombre del cliente a buscar: ').lower()
    visitas = recuperar_visitas()
    if visitas is None:
        return
    encontrados = 0
    for fecha, cliente, detalle, metodo, importe in visitas:
        if cliente.lower() == nombre:
            print(f'{fecha} | {cliente} | {detalle} | ${importe:.2f} | {metodo}')
            encontrados += 1
    if not encontrados:
        print('No se encontraron visitas de ese cliente.')

def main():
    """Administra las sesiones y las opciones del sistema de Bella Studio."""
    opciones = [
        ['1', 'Registrar servicio y pago'],
        ['2', 'Corte de caja'],
        ['3', 'Consultar servicios'],
        ['4', 'Historial de cliente'],
        ['5', 'Mostrar archivos'],
        ['6', 'Leer archivo'],
        ['7', 'Crear archivo'],
        ['8', 'Agregar registro'],
        ['9', 'Cerrar sistema'],
    ]
    salir = False
    while not salir:
        usuario = texto_seguro('Nombre o nickname del operador: ')
        print('Bienvenido(a), ' + usuario.title() + ', al sistema de Bella Studio.')
        carga()
        Fecha = pedir_fecha()
        sesion = True
        while sesion and not salir:
            print('\n===== BELLA STUDIO =====')
            for fila in opciones:
                print(fila[0] + '. ' + fila[1])
            entrada = input('Selecciona una opción: ').strip()
            if not entrada:
                sesion = inactividad()
            elif entrada == '1':
                registrar_servicio(Fecha, usuario)
            elif entrada == '2':
                corte_caja(Fecha, usuario)
            elif entrada == '3':
                mostrar_servicios()
            elif entrada == '4':
                historial_cliente()
            elif entrada == '5':
                listar_archivos()
            elif entrada == '6':
                leer_archivo()
            elif entrada == '7':
                crear_archivo(Fecha, usuario)
            elif entrada == '8':
                agregar_registro(Fecha, usuario)
            elif entrada == '9':
                salir = True
                print('Gracias por utilizar Bella Studio.')
            else:
                print('Opción inválida. Intenta nuevamente.')

main()
