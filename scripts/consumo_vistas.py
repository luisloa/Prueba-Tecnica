from conexion_db import Conexion
from tabulate import tabulate

class ConsumoVistas:
    __VISTA_DIA = "SELECT * FROM vista_monto_diario;" 
    __VISTA_MES = "SELECT * FROM vista_monto_mensual;" 
    __VISTA_AÑO = "SELECT * FROM vista_monto_anual;" 

    @classmethod
    def consultaVistaDiario(cls):
        print('\n' + ' Informacion total de transacciones por día '.center(70, '*'))
        cls.__mostrarVista(cls.__VISTA_DIA)

    @classmethod
    def consultaVistaMensual(cls):
        print('\n' + ' Informacion total de transacciones por mes '.center(70, '*'))
        cls.__mostrarVista(cls.__VISTA_MES)

    @classmethod
    def consultaVistaAnual(cls):
        print('\n' + ' Informacion total de transacciones por año '.center(70, '*'))
        cls.__mostrarVista(cls.__VISTA_AÑO)

    @classmethod
    def __mostrarVista(cls, query):
        with Conexion.iniciarConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(query)
                registros = cursor.fetchall()
                columnas = [desc[0] for desc in cursor.description]  
                print(tabulate(registros, headers=columnas, tablefmt="grid"))



