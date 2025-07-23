import pandas as pd 

from conexion_db import Conexion

print('hola mundo')

ruta = "./data/data_prueba_técnica.csv"
df = pd.read_csv(ruta)

print(df)

Conexion.iniciarConexion()

