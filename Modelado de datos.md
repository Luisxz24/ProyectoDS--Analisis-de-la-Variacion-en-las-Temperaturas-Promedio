# Modelamiento de los datos

# Selección de Variables:
## Descripción de las variables seleccionadas:

## Variable dependiente (objetivo):
* Temperatura global (temp): Esta variable representa el cambio en la temperatura global alo largo del tiempo, que es la principal variable de interés para evaluar el impacto de las emisiones de CO₂ en el calentamiento global.
## Variables independientes (predictoras):
* Emisiones de CO₂ (co2): Representa las emisiones de dióxido de carbono por país a lo largo de los años. Se seleccionó como variable predictora porque se espera que haya una relación directa entre el aumento de las emisiones de CO₂ y el incremento de las temperaturas globales.
* Población (population): La población se incluye como variable predictora debido a que puede tener un efecto indirecto en las emisiones per cápita y, por ende, en la temperatura global.

# Proceso utilizado para seleccionar las variables:
## Correlación: Se realizó un análisis de correlación para examinar cómo se relacionaban las variables entre sí. Este análisis mostró que CO₂ y la temperatura tienen una relación positiva, lo que hace que su inclusión en el modelo de regresión sea justificable.

## Relevancia teórica: Se eligieron las variables según su importancia teórica en el contexto del cambio climático. En particular, CO₂ y la población fueron seleccionadas por ser factores clave que influyen en el calentamiento global.

# Descripción del Modelo:
## Tipo de modelo utilizado:

## Regresión lineal: Se utilizó un modelo de regresión lineal para estudiar la relación entre las variables independientes (emisiones de CO₂ y población) y la variable dependiente (temperatura global). Sin embargo, en otros análisis se utilizaron herramientas como correlación para estudiar la relación entre las variables, y análisis de tendencias para observar la evolución a lo largo del tiempo.

* Justificación de la elección del modelo:
* La regresión lineal fue seleccionada debido a que permite modelar de manera sencilla y efectiva la relación entre variables numéricas. En este caso, la relación entre CO₂ y temperatura es plausible que sea lineal, ya que el aumento de las emisiones de CO₂ está asociado históricamente con un aumento en la temperatura global. Además, este modelo ofrece una interpretación directa de los coeficientes, lo que facilita la comprensión de cómo las emisiones y la población impactan en la temperatura.

# Proceso de Modelamiento: El proceso de modelamiento consistió en los siguientes pasos:

* Filtrado de los datos: Se filtraron los datos para obtener solo las variables de interés, CO₂ y temperatura.
* Cálculo de promedios anuales globales: Se agruparon los datos por año y variable, y se alcularon los promedios anuales de cada una de las variables seleccionadas.
* Pivotado de los datos: Se reestructuraron los datos para tener las emisiones de CO₂ y las temperaturas promedio como columnas separadas, lo que permitió trabajar directamente con las series de tiempo de ambas variables.
* Entrenamiento del modelo de regresión lineal: Se entrenó el modelo utilizando las emisiones de CO₂ como variable independiente (X) y la temperatura como variable dependiente (y).
* Proyecciones futuras: Se realizaron predicciones de la temperatura futura basadas en distintos niveles de CO₂, para lo que se utilizaron valores proyectados de CO₂ como entradas al modelo.

# Implementación del Modelo: El código para implementar el modelo de regresión lineal se encuentra en el siguiente apartadoo [codigo_modelo](https://github.com/Luisxz24/ProyectoDS--Analisis-de-la-Variacion-en-las-Temperaturas Promedio/blob/main/Code/analisis_y_graficos.py)

# Evaluación del Modelo:

## Métricas utilizadas:
* Coeficiente de regresión (pendiente): Este valor indica cuánto cambia la temperatura promedio global por cada incremento en las emisiones de CO₂.
* Intercepto: Representa la temperatura base cuando las emisiones de CO₂ son cero.
* R² (coeficiente de determinación): Esta métrica indica qué tan bien las emisiones de CO₂ explican la variabilidad de la temperatura global. Un valor cercano a 1 indica una fuerte relación.

# Gráficos de Evaluación:

* Gráfico de dispersión con la línea de regresión ajustada.
* Gráfico de proyecciones futuras de temperatura en función de niveles de CO₂ estimados.
* Gráfico de residuos para validar la calidad del modelo, mostrando si hay patrones sistemáticos en los errores.

## Los gráficos pueden ser visualizados en el siguiente apartado [Gráficos](https://github.com/Luisxz24/ProyectoDS--Analisis-de-la-Variacion-en-las-Temperaturas-Promedio/tree/main/visualizations)
  


