Proyecto Final — El Desafío Jerárquico

Tema: Gestión jerárquica de celulares

Integrantes:

Lucas Godoy

Ramiro Salcedo

Descripción del proyecto

El objetivo del proyecto es implementar un sistema jerárquico de almacenamiento de datos utilizando carpetas, archivos CSV y recursividad, aplicando los tres pilares del desafío:

Diseño jerárquico de tres niveles.

Uso de la librería os para creación dinámica de carpetas.

Lectura recursiva global de todos los archivos.

El proyecto permite agregar, mostrar, buscar y eliminar registros de celulares organizados por marca, serie y modelo, garantizando persistencia mediante archivos CSV.

Cada celular se representa mediante un diccionario con tres claves:

{
  "marca": "Samsung",
  "serie": "Galaxy S",
  "modelo": "S24 Ultra"
}

Esta estructura se mapea directamente al sistema de archivos con tres niveles de carpetas:

datos/
├── Samsung/
│   ├── Galaxy S/
│   │   └── S24 Ultra.csv
│   └── Galaxy A/
│       └── A54.csv
└── Apple/
    └── iPhone/
        └── iPhone 15.csv

La función cargar_celulares_recursivo() se encarga de recorrer todas las carpetas de forma recursiva para consolidar los datos de todos los CSV en una única lista de diccionarios.

Caso base:

Si la ruta no existe → se crea con os.makedirs() y se retorna una lista vacía.

Paso recursivo:

Si el elemento es una carpeta → la función se llama a sí misma.

Si es un archivo CSV → lo abre con with open() y carga los datos.

Ejemplo visual del recorrido:

datos/
 ├─ Samsung/ → llama recursivamente
 │   ├─ Galaxy S/ → encuentra S24 Ultra.csv
 │   └─ Galaxy A/ → encuentra A54.csv
 └─ Apple/ → encuentra iPhone 15.csv

Conclusión

El proyecto cumple con los tres pilares del desafío jerárquico:

Estructura clara de datos,

Gestión dinámica de carpetas y archivos,

y recursividad funcional para el recorrido completo.