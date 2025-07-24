# Prueba Técnica

# Sección 1: Procesamiento y transferencia de datos

Este proyecto implementa un proceso completo que incluye la carga, extracción, limpieza, procesamiento, importación, utilización y análisis de datos.

La fuente de datos proviene de una compañía ficticia, pero el programa está diseñado para ser útil en entornos empresariales reales. Su desarrollo se enfocó en la automatización de procesos, la optimización del tiempo, así como en la usabilidad y escalabilidad del sistema.

# Tecnologías implementadas
- Python
- PostgreSQL
- Pandas
- Psycopg2
- Docker
- Git
- GitHub

# Requerimientos (requirements.txt)

El repositorio cuenta con las librerias necesarias para su optimo funcionamientos, estas se instalaran de forma automatica cuando se corra el contenedor.

- numpy==2.3.1
- pandas==2.3.1
- psycopg2-binary==2.9.10
- sqlalchemy==2.0.20
- sqlalchemy-utils==0.37.8
- uvicorn==0.23.2
- tabulate==0.9.0

# Recomendaciones de Instalacion

# Requsitos 

- Docker 
    -Docker compose 
    -Docker desktop (Windows y MacOS)
    https://www.docker.com/products/docker-desktop/

- Python 3.10 o superior
    https://www.python.org/downloads/

- Git y Github


# Clonar Repositorio desde Github

- https://github.com/luisloa/Prueba-Tecnica.git

# ****** INSTRUCCIONES DE USO ******
# Desde teminal

1. git clone https://github.com/luisloa/        Prueba-Tecnica.git
2. cd Prueba-Tecnica
3. docker-compose up --build 

# Proceso 

El software se ejecuta dentro de contenedores Docker. Al levantar el entorno con docker-compose, se inician los siguientes servicios:

- Un contenedor con PostgreSQL (servidor de base de datos)

- Un contenedor con Python que ejecuta los scripts de procesamiento

# Scripts principales
# carga_data.py

Funciones:

- Lectura de datos: Lee archivos .csv ubicados en el directorio /data. Por defecto, se usa un archivo incluido, pero puedes cambiar el archivo modificando la variable de clase __RUTA.

- Extracción de datos: Usa la biblioteca Pandas para leer y manipular los datos.

- Creación de DataFrame: Los datos se estructuran en un DataFrame para facilitar su limpieza y análisis.

- Limpieza de datos:

    - Corrección de formatos de fecha no compatibles con PostgreSQL.

    - Manejo de valores nulos en campos no admitidos.

    - Filtrado de cantidades irreales o inconsistentes.

    - Aplicación de reglas para asegurar la calidad sin eliminar transacciones potencialmente útiles.

- Resultado: Se obtiene un DataFrame limpio, listo para ser importado a la base de datos PostgreSQL.

# conexion_db.py

Funciones:

- El programa establece una conexión con un servidor PostgreSQL. Si los datos del servidor cambian, deberás actualizar las siguientes variables de clase en el script:

    __DATABASE = 'prueba_tecnica_db'
    __USERNAME = 'admin'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = 'postgres-pt-db'

- Métodos clave

    iniciarConexion()
    Método de clase encargado de establecer una conexión óptima con el servidor de base de datos. Incluye manejo de errores para asegurar una conexión estable.
    Retorna: un objeto de conexión activo.

    obtenerCursor()
    Método de clase que inicializa y retorna un cursor asociado a la conexión. Este cursor permite ejecutar consultas SQL para insertar, consultar y manipular datos en la base de datos.
    Retorna: un cursor listo para operar sobre la base de datos.

# Importacion_data_db.py

Funciones:

- El programa solicita servicios al módulo conexion_db.py, desde el cual obtiene:

    - La conexión activa a la base de datos.

    - Un cursor funcional para ejecutar sentencias SQL.

- Asimismo, se invoca el módulo carga_data.py, que devuelve un DataFrame limpio y estructurado, listo para ser cargado en la base de datos PostgreSQL.

# Proceso de inserción de datos

- El DataFrame resultante se recorre mediante un bucle iterativo. Para cada fila:

    - Se ejecuta el comando cursor.execute() utilizando la variable __INSERTAR.

    - Se vinculan los valores de cada fila como parámetros de inserción.

- El comando de inserción implementa una política de no duplicidad de datos mediante:

    ON CONFLICT (id, company_name, company_id) DO NOTHING

Esto asegura que no se inserten registros duplicados si se ejecuta el programa varias veces con el mismo archivo de datos.

- Es posible cargar múltiples archivos .csv, uno a la vez. Cada registro cuenta con un identificador interno único autoincremental, lo cual garantiza la unicidad de cada entrada en la base de datos, independientemente del archivo de origen.

- Resultado: Los datos son cargados en la base de datos PostgreSQL cumpliendo con criterios de:

    - Integridad
    - No duplicidad
    - Confiabilidad

Esto permite realizar futuros análisis con datos consistentes y precisos.


# init.sql 
# Estructura de la base de datos

El archivo init.sql se ejecuta de manera automatica al al correr el contenedor. El archivo db_init/init.sql define la estructura inicial de la base de datos utilizada por el sistema. Este script incluye:

- Creación de la tabla orders, que almacena información relacionada con pedidos realizados por distintas empresas. Se agregan restricciones para:

    - Evitar duplicidad de registros mediante claves compuestas.

    - Validar que los montos sean mayores a 0.1.

- Creación de la tabla companies, que contiene los datos únicos de cada empresa registrada en los pedidos.

- Creación de la tabla charges, la cual representa las transacciones finales con referencias a las empresas y pedidos. Se usa una clave foránea para relacionar los cargos con las empresas.

# Inserciones automáticas:

- Empresas únicas extraídas desde los pedidos se insertan en companies.

- Los registros de orders se transforman en charges, relacionados correctamente con su empresa respectiva.

-Vistas consolidadas para análisis:

    - vista_monto_diario: Monto total de transacciones por día.

    - vista_monto_mensual: Monto total de transacciones por mes.

    - vista_monto_anual: Monto total de transacciones por año.

Estas vistas permiten consultas agregadas para análisis de comportamiento empresarial y reportes históricos.

# Diagrama Entidad Relación

![ERD](<imagen/Untitled (1).png>)

# Estructura proyecto

prueba_tecnica/
├── data
│   └── data_prueba_técnica.csv
├── db_init
│   └── init.sql
├── docker-compose.yml
├── Dockerfile
├── imagen
│   └── Untitled (1).png  
├── intrucciones
│   ├── Instrucciones para la prueba técnica.docx
│   └── Prueba técnica Python.docx
├── README.md
├── requirements.txt
└── scripts
    ├── carga_data.py
    ├── conexion_db.py
    ├── consumo_vistas.py
    ├── importacion_data_db.py
    └── main.py









