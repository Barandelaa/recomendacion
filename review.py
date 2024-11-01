import pandas as pd

def obtener_datos():
    df = pd.read_csv('Processed_interactions.csv')
    return df

def obtener_nombre_receta(id_receta):
    df = pd.read_csv('Processed_recipes.csv')

    if df is not None:
        receta = df[df['id'] == id_receta]
        if not receta.empty:
            return receta['name'].values[0]
        else:
            print(f"La receta con id {id_receta} no se encontró.")
            return None

print(obtener_nombre_receta(277748))