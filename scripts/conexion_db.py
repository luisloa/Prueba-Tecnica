import psycopg2 as psy2
import sys

class Conexion:
    __DATABASE = 'prueba_tecnica_db'
    __USERNAME = 'admin'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = 'postgres-pt-db'
    __conexion = None
    __cursor = None

    @classmethod
    def iniciarConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = psy2.connect(
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                print('Conexion exitosa')
                return cls.__conexion
                
            
            except Exception as e:
                print(f'Error al intentar iniciar conexión: {e}. Cierre de conexión forzada...')
                sys.exit()
        else:
            print(f'Ya existe una conexión: {cls.__conexion}')
            return cls.__conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.iniciarConexion().cursor()
                print(f'Obtencion del cursor exitosa. Cursor {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                print(f'Error al intentar obtener cursor: {e}. Cierre de conexión forzada...')
                sys.exit()
        else:
            print(f'Cursor {cls.__cursor} obtenido previamente : {cls.__conexion}')
            return cls.__cursor




