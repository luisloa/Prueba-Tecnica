import pandas as pd 

class Data:
    __RUTA = "./data/data_prueba_técnica.csv"

    @classmethod
    def obtenerData(cls):
        try:
            df = pd.read_csv(cls.__RUTA)

            df.rename(columns={"name": "company_name"}, inplace=True)

            # Se realiza la vonversion 
            df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
            df['paid_at'] = pd.to_datetime(df['paid_at'], errors='coerce')

            #Asignacion de palabra clave para valores null
            df['company_id'] = df['company_id'].fillna('sin_company_id')

            #Asignacion de fecha fija para valore null
            df['created_at'] = df['created_at'].fillna(pd.to_datetime('1900-01-01'))

            # Asignar IDs artificiales a registros sin ID
            asignacion_id_artificial = df['id'].isnull()
            df.loc[asignacion_id_artificial, 'id'] = [f'fake_id_{i}' for i in range(1, asignacion_id_artificial.sum() + 1)]
 
            #Asignacion de promedio toltal en valores null
            # Filtrar montos válidos para calcular el promedio
            montos_validos = df.loc[df['amount'].abs() < 1e14, 'amount']
            # Calcular el monto promedio válido
            monto_promedio = montos_validos.mean()
            # Reemplazar montos "exorbitantes" por el promedio calculado
            df.loc[df['amount'].abs() >= 1e14, 'amount'] = monto_promedio

            # Asignar 0.1 a cantidades 0.0
            df.loc[df['amount'] == 0.0, 'amount'] = 0.1


            df = df.where(pd.notnull(df), None)

            print('Se obtuvo acceso a la data correctamente')
            return df

        except Exception as e:
            raise RuntimeError(f"No se pudo leer el archivo CSV: {e}")


