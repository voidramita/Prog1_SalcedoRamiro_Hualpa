import os
import csv

# --------------------------------- UTILIDADES --------------------------------- #

def cargar_celulares_recursivo(ruta="datos"):
    celulares = []

    # Listar los elementos dentro de la ruta actual
    try:
        elementos = os.listdir(ruta)
    except FileNotFoundError:
        print(f"⚠️  La ruta '{ruta}' no existe.")
        os.makedirs(ruta, exist_ok=True)
        print(f"✅ Se creó la carpeta '{ruta}'.")
        return celulares

    # Recorrer cada elemento dentro de la carpeta
    for elemento in elementos:
        path = os.path.join(ruta, elemento)

        # Si es carpeta → llamada recursiva
        if os.path.isdir(path):
            celulares.extend(cargar_celulares_recursivo(path))

        # Si es archivo CSV → leerlo y agregarlo a la lista
        elif elemento.endswith(".csv"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        celulares.append(row)
            except Exception as e:
                print(f"⚠️  Error leyendo '{path}': {e}")

    return celulares

# --------------------------------- FUNCIONES AUXILIARES --------------------------------- #

def pedir_marca_serie_modelo():   
    # se encarga de pedir los datos al usuario y formatearlos
    while True:
        marca = input("Marca: ").strip().capitalize()
        if marca:
            break
        else:
            print("La marca no puede estar vacía. Por favor, ingresá una marca válida.")
    while True: 
        serie = input("Serie: ").strip().title()
        if serie:
            break
        else:
            print("La serie no puede estar vacía. Por favor, ingresá una serie válida.")
    while True:
        modelo = input("Modelo: ").strip().title()
        if modelo:
            break
        else:
            print("El modelo no puede estar vacío. Por favor, ingresá un modelo válido.")
    return marca, serie, modelo


def recursion(funcion):
    # se encarga de preguntar al usuario si desea repetir la acción
    while True:
        respuesta = input("Desea repetir la acción (s/n): ").lower().strip()
        if respuesta == "s":
            funcion()
            break
        elif respuesta == "n":
            break
        else:
            print("Debe ingresar s/n")

def eliminar_directorio_vacio(ruta="datos"):
    # Recorre la estructura de directorios de abajo hacia arriba
    for root, dirs, files in os.walk(ruta, topdown=False):
        for dir in dirs: 
            try:   
                dir_path = os.path.join(root, dir)

              # Si el directorio está vacío, eliminarlo
                if not os.listdir(dir_path):
                    print(f"🗑️  Directorio vacío '{dir_path}' eliminado.")
                    os.rmdir(dir_path)
            # Captura errores específicos
            except OSError as e:
                print(f"Error al eliminar directorio vacío '{dir_path}': {e}")
            except Exception as e:
                print(f"Error inesperado al eliminar directorio vacío '{dir_path}': {e}")

            

# --------------------------------- FUNCIONES PRINCIPALES --------------------------------- #
    

def agregar_celular():
    print("\n=== AGREGAR CELULAR ===")
    marca, serie, modelo = pedir_marca_serie_modelo()

# Crear la estructura de carpetas si no existe
    ruta = os.path.join("datos", marca, serie)
    os.makedirs(ruta, exist_ok=True)

    archivo_csv = os.path.join(ruta, f"{modelo}.csv")

# Guardar los datos en el archivo CSV
    existe = os.path.exists(archivo_csv)
    with open(archivo_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["marca", "serie", "modelo"])
        if not existe:
            writer.writeheader()
        writer.writerow({"marca": marca, "serie": serie, "modelo": modelo})

    print(f"✅ Celular '{marca} {modelo}' agregado correctamente.")
# Preguntar si desea agregar otro celular
    recursion(agregar_celular)

def mostrar_todos():
    # Mostrar todos los celulares cargados
    celulares = cargar_celulares_recursivo()
    if not celulares:
        print("No hay celulares cargados.")
        return
    print("\n=== CELULARES DISPONIBLES ===")
    # Mostrar encabezados
    print("Marca | Serie | Modelo")
    print("-" * 30)
    for c in celulares:
        print(f"{c['marca']} | {c['serie']} | {c['modelo']}")
    input("\nPresioná Enter para volver al menú...")

def buscar_un_modelo():
    # Buscar celulares por marca o modelo
    celulares = cargar_celulares_recursivo()
    if not celulares:
        print("No hay celulares cargados.")
        return
    while True:
        texto = input("Buscar por marca, serie o modelo: ").lower().strip()
        if texto:
            break
        else:
            print("El texto de búsqueda no puede estar vacío. Por favor, ingresá un término válido.")

    resultados = []

# Buscar coincidencias

    for cel in celulares:
        if texto in cel["marca"].lower() or texto in cel["modelo"].lower() or texto in cel["serie"].lower():
            resultados.append(cel)

# Mostrar resultados
    if resultados:
        print(f"=== RESULTADOS PARA: {texto.upper()} ===")
        for c in resultados:
            print(f"{c['marca']} | {c['serie']} | {c['modelo']}")
    else:
        print("No se encontró ningún celular con ese término.")


def eliminar():
# Eliminar un celular específico
    catalogo = cargar_celulares_recursivo()
    print("\n=== ELIMINAR CELULAR ===")     
    marca, serie, modelo = pedir_marca_serie_modelo()
    archivo = os.path.join("datos", marca, serie, f"{modelo}.csv")
# Verificar si el archivo existe y eliminarlo
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"🗑️  Archivo '{modelo}.csv' eliminado.")
    else:
        print("No se encontró ese celular.")

# Limpiar directorios vacíos
    eliminar_directorio_vacio()
# Preguntar si desea eliminar otro celular
    recursion(eliminar)
    
# --------------------------------- MENÚ --------------------------------- #

def mostrar_menu():
    # Colores
    RED = "\033[91m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    print(f"\n{RED}{'═' * 42}{RESET}")
    print(f"{WHITE} 📱  MENÚ PRINCIPAL  📱".center(42))
    print(f"{RED}{'═' * 42}{RESET}")
    print(f"{RED}1.{WHITE} Agregar celular")
    print(f"{RED}2.{WHITE} Mostrar todos los celulares")
    print(f"{RED}3.{WHITE} Buscar por marca o modelo")
    print(f"{RED}4.{WHITE} Eliminar celular")
    print(f"{RED}0.{WHITE} Salir")
    print(f"{RED}{'═' * 42}{RESET}")
