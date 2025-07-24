from carga_data import Data
from conexion_db import Conexion
import pandas as pd 
import sys


class Importacion:
    __INSERTAR = '''INSERT INTO orders 
                        (id, company_name, company_id, amount, status, created_at, paid_at) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (id, company_name, company_id) DO NOTHING'''
    
    @classmethod
    def importador(cls, data):
        filas_insertadas = 0
        try:
            with Conexion.iniciarConexion() as conexion:
                with conexion.cursor() as cursor:
                    for index , fila in Data.obtenerData().iterrows():
                            try:
                                value = (fila['id'], 
                                        fila['company_name'], 
                                        fila['company_id'], 
                                        fila['amount'], 
                                        fila['status'], 
                                        fila['created_at'] if pd.notnull(fila['created_at']) else None,
                                        fila['paid_at'] if pd.notnull(fila['paid_at']) else None,)

                                cursor.execute(cls.__INSERTAR, value)
                                print('Orden insertada: {fila}')
                                filas_insertadas += cursor.rowcount
                            except Exception as e:
                                print(f'Error de inserción en la fila: {fila}. Excepción: {e}') 
                                break
        except Exception as e:
            print(f'Error en la transacción: {e}')
            sys.exit()

        print(f'Total de filas insertadas: {filas_insertadas}')

   
                    








