# Conjunto de datos
# Fuente de los datos: 
## Este proyecto utiliza datos provenientes de dos fuentes confiables:
## Temperaturas mensuales promedio por año:
* Obtenidos de Our World in Data. El conjunto de datos puede consultarse en: [Monthly Average Surface Temperatures by Year](https://ourworldindata.org/grapher/monthly-average-surface-temperatures-by-year)
## Emisiones de CO₂ (1750-2020):
* Recuperados de Kaggle, específicamente del dataset titulado CO2 Emissions Dataset (1750-2020), disponible en: [CO2 Emissions Dataset.](https://www.kaggle.com/datasets/kvnxls/co2-emissions-dataset-1750-2020)
  
# Características principales del dataset final:

* Número de filas: Aproximadamente 132,061 registros.
* Número de columnas: 4 columnas , donde se encuentran:
* entity: Los países.
 *var: El tipo de variable (e.g., temp, co2, population, etc.).
 *Años: De 1950 a 2020.
 *Value: Valor correspondiente a la variable en un año específico.

# Tipos de variables:
* Numéricas: value (valores cuantitativos de temperatura, emisiones de CO₂, población, etc.), year.
* Categóricas: entity (país o región), var (tipo de variable medida).

# Procedencia de los Datos:
* Los datos sobre temperaturas globales provienen de Our World in Data, una fuente pública y gratuita.
* Los datos de emisiones de CO₂ provienen de Kaggle, una plataforma ampliamente utilizada en la comunidad de ciencia de datos. Ambos conjuntos de datos son públicos y gratuitos, accesibles a través de los enlaces mencionados anteriormente.


# Procesamiento inicial:
### Para preparar los datos para el análisis, se realizaron varias transformaciones en los conjuntos de datos de emisiones de CO2 y temperaturas promedio. A continuación se detallan las transformaciones llevadas a cabo, junto con los fragmentos de código correspondientes:

## Eliminación de Variables No Relevantes: En el dataset de CO2, se eliminaron manualmente las variables que no serían útiles para el análisis. Este paso ayudó a reducir la complejidad del conjunto de datos y a centrarse solo en las variables relevantes.

## Filtrado de Datos por Año (1950-2020): Para asegurar que ambos datasets tuvieran el mismo rango temporal, se filtraron los datos por año:

### Dataset de CO2: Se conservaron solo los datos de los años 1950 a 2020, eliminando las entradas previas a 1950.

`df = pd.read_excel("C:/Users/lugej/OneDrive/Escritorio/Libro4.xlsx")
df_filtrado = df[(df['Year'] >= 1950) & (df['Year'] <= 2020)]
df_filtrado.to_excel("archivo_filtrado_1950_2020.xlsx", index=False)
print("Se ha generado un archivo CSV con los datos de 1950 a 2020.")`

### Dataset de Temperaturas: Se eliminaron los datos de los años 2021 a 2024, ya que estos no estaban presentes en el dataset de CO2, esto se realizo de forma manual dentro del dataset en excel.

# Transformación de Datos:

## En el dataset de CO2, se convirtió el formato de los datos de "ancho" a "largo", utilizando el método melt(). Este paso permitió transformar las variables en filas, mientras que los años se mantuvieron como columnas.

`df = pd.read_excel("C:/Users/lugej/OneDrive/Documentos/Escuela/Pycharm/INT_PROG_CD/archivo_filtrado_1950_20201.xlsx")
df_filtrado = df[(df['year'] >= 1950) & (df['year'] <= 2020)]
df_melted = df_filtrado.melt(id_vars=['entity', 'year'], value_vars=['co2', 'co2_per_capita', 'consumption_co2', 'consumption_co2_per_capita', 'total_ghg', 'ghg_per_capita', 'population', 'primary_energy_consumption', 'energy_per_capita'], var_name='Variable', value_name='Value')
df_pivotado = df_melted.pivot_table(index=['entity', 'Variable'], columns='year', values='Value', aggfunc='first')
df_pivotado.reset_index(inplace=True)
df_pivotado.to_excel("archivo_pivotado_1950_20202.xlsx", index=False)`

# En el dataset de temperaturas, se calcularon los promedios anuales de temperatura por país, lo que facilitó el análisis posterior. Esto se logró utilizando el método groupby() y mean() de pandas.

`data = pd.read_csv(file_path)
years = [col for col in data.columns if col.isdigit()]
entity_col = "Entity"
average_temperatures = data.groupby(entity_col)[years].mean().reset_index()
output_path = r"C:\Users\lugej\OneDrive\Documentos\promedio_anual_por_pais.csv"
average_temperatures.to_csv(output_path, index=False)`

# Filtrado de Países Comunes: 
## Para asegurarse de que ambos datasets solo incluyeran los países comunes, se realizaron los siguientes pasos:
* Se cargaron ambos datasets y se identificaron los países presentes en ambos conjuntos.
* Se filtraron los datos para mantener únicamente los países comunes en ambos datasets.

`dataset_temperaturas = pd.read_csv("C:/Users/lugej/OneDrive/Documentos/promedio_anual_por_pais.csv")
dataset_co2 = pd.read_excel(r"C:/Users/lugej/OneDrive/Documentos/Escuela/Pycharm/INT_PROG_CD/archivo_pivotado_1950_20202.xlsx")
dataset_temperaturas.columns = dataset_temperaturas.columns.str.strip().str.lower()
dataset_co2.columns = dataset_co2.columns.str.strip().str.lower()
entidades_temperaturas = set(dataset_temperaturas['entity'])
entidades_co2 = set(dataset_co2['entity'])
entidades_comunes = entidades_temperaturas.intersection(entidades_co2)
dataset_temperaturas_filtrado = dataset_temperaturas[dataset_temperaturas['entity'].isin(entidades_comunes)]
dataset_co2_filtrado = dataset_co2[dataset_co2['entity'].isin(entidades_comunes)]
dataset_temperaturas_filtrado.to_csv(r"C:/Users/lugej/OneDrive/Documentos/temperaturas_filtrado.csv", index=False)
dataset_co2_filtrado.to_excel(r"C:/Users/lugej/OneDrive/Documentos/co2_filtrado.xlsx", index=False)`

# Concatenación de los Conjuntos de Datos:
## Después de realizar los filtrados, los datasets de CO2 y temperaturas fueron concatenados. Para esto, se utilizaron macros en Excel para alinear y unir ambos conjuntos de datos en un único archivo, asegurándose de que los datos estuvieran correctamente organizados y listos para el análisis.

# Transformación Final (Pivoteo a Largo): 
## Finalmente, se realizó un pivoteo de los datos concatenados a formato largo, lo que permitió una mejor manipulación y análisis posterior:

`df = pd.read_excel(file_path)
df_long = df.melt(id_vars=["entity", "var"], var_name="year", value_name="value")
df_long["year"] = df_long["year"].astype(int)
export_path = "dataset_transformado.xlsx"
df_long.to_excel(export_path, index=False)
print(f"Dataset transformado y exportado como '{export_path}'")`

