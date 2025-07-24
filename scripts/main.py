from carga_data import Data
from importacion_data_db import Importacion
from consumo_vistas import ConsumoVistas


data = Data.obtenerData()
importador = Importacion.importador(data)
vista_dia = ConsumoVistas.consultaVistaDiario()
vista_mes = ConsumoVistas.consultaVistaMensual()
vista_año = ConsumoVistas.consultaVistaAnual()




