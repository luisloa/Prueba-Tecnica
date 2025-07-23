import pandas as pd 

class Data:
    __RUTA = "./data/data_prueba_técnica.csv"

    @classmethod
    def ObtenerData(cls):
        try:
            df = pd.read_csv(cls.__RUTA)
            print('Se obtuvo acceso a la data correctamente')

        except Exception as e:
            print(f'Ocurrio un Error: {e}')


