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
            
            except Exception as e:
                print(f'Error: {e}. Cierre de conexión forzada...')
                sys.exit()

            finally:
                cls.__conexion.close()

        else:
            return f'Conexion abierta: {cls.__conexion}'


if __name__ == '__main__':
    Conexion()

