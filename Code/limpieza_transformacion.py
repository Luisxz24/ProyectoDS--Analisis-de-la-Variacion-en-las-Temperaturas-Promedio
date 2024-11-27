##LIMPIEZA
#Eliminar 3 de las 12 veces que se repite el pais en el archivo montly para usarlo en la limpieza del archivo co2

import pandas as pd
# -*- coding: utf-8 -*-

df = pd.read_csv('C:/Users/lugej/OneDrive/Documentos/monthly-average-surface-temperatures-by-year.csv', encoding='UTF-8')

df_reducido = df.groupby('Entity').head(9)

df_reducido.to_csv('archivo_reducido.csv', index=False)

print("Se ha creado un archivo con los datos ajustados.")

###
#Crear lista de variables que se repiten cada vez por el numero de filas del dataset de co2
##
# -*- coding: utf-8 -*-

columnas = [
    "co2",
    "co2_per_capita",
    "consumption_co2",
    "consumption_co2_per_capita",
    "total_ghg",
    "ghg_per_capita",
    "population",
    "primary_energy_consumption",
    "energy_per_capita"
]

total_filas = 1755

repeticiones = -(-total_filas // len(columnas))

df = pd.DataFrame({"Variables": (columnas * repeticiones)[:total_filas]})

df.to_csv("archivo_1755_filas.csv", index=False)

print("Se ha generado el archivo CSV con exactamente 1755 filas.")
###
#Mantener solo datos entre 1950 y 2020
##

# -*- coding: utf-8 -*-

df = pd.read_excel("C:/Users/lugej/OneDrive/Escritorio/Libro4.xlsx")

df_filtrado = df[(df['Year'] >= 1950) & (df['Year'] <= 2020)]

df_filtrado.to_excel("archivo_filtrado_1950_2020.xlsx", index=False)

print("Se ha generado un archivo CSV con los datos de 1950 a 2020.")

##
#Pivotar datos de filas a columnas
##
df = pd.read_excel("C:/Users/lugej/OneDrive/Documentos/Escuela/Pycharm/INT_PROG_CD/archivo_filtrado_1950_20201.xlsx")

print(df.columns)

df_filtrado = df[(df['year'] >= 1950) & (df['year'] <= 2020)]

df_melted = df_filtrado.melt(id_vars=['entity', 'year'], value_vars=[
    'co2', 'co2_per_capita', 'consumption_co2', 'consumption_co2_per_capita',
    'total_ghg', 'ghg_per_capita', 'population', 'primary_energy_consumption',
    'energy_per_capita'], var_name='Variable', value_name='Value')

print(df_melted.head())

df_pivotado = df_melted.pivot_table(index=['entity', 'Variable'], columns='year', values='Value', aggfunc='first')

df_pivotado = df_pivotado[sorted(df_pivotado.columns, reverse=True)]

df_pivotado.reset_index(inplace=True)

df_pivotado.to_excel("archivo_pivotado_1950_20202.xlsx", index=False)

print("Se ha generado un archivo Excel con los años como columnas (de 2020 a 1950).")
###
# promediar dataset temperaturas
###
file_path = r"C:/Users/lugej/OneDrive/Documentos/monthly-average-surface-temperatures-by-year.csv"

data = pd.read_csv(file_path)

years = [col for col in data.columns if col.isdigit()]
entity_col = "Entity"

average_temperatures = data.groupby(entity_col)[years].mean().reset_index()

output_path = r"C:\Users\lugej\OneDrive\Documentos\promedio_anual_por_pais.csv"

average_temperatures.to_csv(output_path, index=False)

print(f"Archivo procesado y guardado en: {output_path}")
####
# filtrar paises que se repiten en ambos datasets
####

dataset_temperaturas = pd.read_csv("C:/Users/lugej/OneDrive/Documentos/promedio_anual_por_pais.csv")
dataset_co2 = pd.read_excel(r"C:/Users/lugej/OneDrive/Documentos/Escuela/Pycharm/INT_PROG_CD/archivo_pivotado_1950_20202.xlsx")

dataset_temperaturas.columns = dataset_temperaturas.columns.str.strip().str.lower()
dataset_co2.columns = dataset_co2.columns.str.strip().str.lower()

print("Columnas en dataset de temperaturas:", dataset_temperaturas.columns)
print("Columnas en dataset de CO2:", dataset_co2.columns)

columna_entidades_temperaturas = "entity"
columna_entidades_co2 = "entity"

entidades_temperaturas = set(dataset_temperaturas[columna_entidades_temperaturas])
entidades_co2 = set(dataset_co2[columna_entidades_co2])

entidades_comunes = entidades_temperaturas.intersection(entidades_co2)

dataset_temperaturas_filtrado = dataset_temperaturas[dataset_temperaturas[columna_entidades_temperaturas].isin(entidades_comunes)]
dataset_co2_filtrado = dataset_co2[dataset_co2[columna_entidades_co2].isin(entidades_comunes)]

dataset_temperaturas_filtrado.to_csv(r"C:/Users/lugej/OneDrive/Documentos/temperaturas_filtrado.csv", index=False)
dataset_co2_filtrado.to_excel(r"C:/Users/lugej/OneDrive/Documentos/co2_filtrado.xlsx", index=False)

print("Los datasets han sido filtrados y guardados.")

##
#pivote el dataset para que sea a lo largo
###
# -*- coding: utf-8 -*-
file_path = 'C:/Users/lugej/OneDrive/Documentos/dataset_co2_temperaturas_limpioyconcatenado.xlsx'
df = pd.read_excel(file_path)


df_long = df.melt(id_vars=["entity", "var"], var_name="year", value_name="value")

df_long["year"] = df_long["year"].astype(int)

export_path = "dataset_transformado.xlsx"
df_long.to_excel(export_path, index=False)

print(f"Dataset transformado y exportado como '{export_path}'")