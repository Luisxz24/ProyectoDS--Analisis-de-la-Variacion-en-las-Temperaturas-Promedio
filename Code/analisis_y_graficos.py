# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#####
#Promedio global a lo largo del tiempo
####
file_path = "C:/Users/lugej/OneDrive/Documentos/dataset_co2_temperaturas_largo.xlsx"
df = pd.read_excel(file_path)

df_global = df.groupby(["year", "var"])["value"].mean().reset_index()

variable = "temp"
df_variable = df_global[df_global["var"] == variable]

plt.figure(figsize=(10, 6))
plt.plot(df_variable["year"], df_variable["value"], marker='o', label=f"Promedio global de temperatura")
plt.title(f"Tendencia Global de temperatura (1950-2020)", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Promedio Global", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
#####
#correlacion temp co2
###
variables_interes = ["temp", "co2"]
df_filtrado = df[df["var"].isin(variables_interes)]

df_promedio_anual = df_filtrado.groupby(["year", "var"])["value"].mean().reset_index()

df_pivot = df_promedio_anual.pivot(index="year", columns="var", values="value")

correlacion = df_pivot.corr().loc["temp", "co2"]

print(f"Correlación entre CO2 y temperatura globalmente: {correlacion:.2f}")

plt.figure(figsize=(10, 6))
sns.regplot(x=df_pivot["co2"], y=df_pivot["temp"], ci=None, color="steelblue")
plt.title("Relación entre CO2 y Temperatura Global", fontsize=14)
plt.xlabel("CO2 Promedio Global", fontsize=12)
plt.ylabel("Temperatura Promedio Global", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

###
#correlaciones temp population y co2 population
###

variables_interes = ["co2", "population", "temp"]
df_filtrado = df[df["var"].isin(variables_interes)]

df_promedio_anual = df_filtrado.groupby(["year", "var"])["value"].mean().reset_index()

df_pivot = df_promedio_anual.pivot(index="year", columns="var", values="value")

correlacion_co2_poblacion = df_pivot.corr().loc["co2", "population"]
correlacion_poblacion_temp = df_pivot.corr().loc["population", "temp"]

print(f"Correlación entre CO2 y población globalmente: {correlacion_co2_poblacion:.2f}")
print(f"Correlación entre población y temperatura globalmente: {correlacion_poblacion_temp:.2f}")

plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
sns.regplot(x=df_pivot["population"], y=df_pivot["co2"], ci=None, color="green")
plt.title("Relación entre CO2 y Población Global", fontsize=14)
plt.xlabel("Población Promedio Global", fontsize=12)
plt.ylabel("CO2 Promedio Global", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

plt.subplot(1, 2, 2)
sns.regplot(x=df_pivot["population"], y=df_pivot["temp"], ci=None, color="orange")
plt.title("Relación entre Población y Temperatura Global", fontsize=14)
plt.xlabel("Población Promedio Global", fontsize=12)
plt.ylabel("Temperatura Promedio Global", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()

###
#Tendencia temporal de CO₂ y temperatura
###
df_trend = df[df["var"].isin(["co2", "temp"])].groupby(["year", "var"])["value"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_trend, x="year", y="value", hue="var", marker="o")
plt.title("Tendencias globales de CO₂ y Temperatura", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Promedio Global", fontsize=12)
plt.legend(title="Variable", labels=["CO₂", "Temperatura"])
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

###
##regresion lineal co2 y temp
###
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df_filtered = df[df["var"].isin(["co2", "temp"])]

df_global = df_filtered.groupby(["year", "var"])["value"].mean().reset_index()

df_reg = df_global.pivot(index="year", columns="var", values="value").dropna()

X = df_reg["co2"].values.reshape(-1, 1)  # Variable independiente (CO₂)
y = df_reg["temp"].values  # Variable dependiente (temperatura)

reg = LinearRegression()
reg.fit(X, y)

y_pred = reg.predict(X)

r2 = r2_score(y, y_pred)
print(f"Coeficiente de regresión (pendiente): {reg.coef_[0]:.2f}")
print(f"Intercepto: {reg.intercept_:.2f}")
print(f"R² del modelo: {r2:.2f}")

future_co2 = np.array([450, 500, 550, 600]).reshape(-1, 1)
predicted_temp = reg.predict(future_co2)

print("\nProyecciones de temperaturas futuras basadas en emisiones de CO2")
for co2, temp in zip(future_co2.flatten(), predicted_temp):
    print(f"CO2: {co2} ppm, Temperatura proyectada: {temp:.2f}°C")

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", alpha=0.5, label="Datos históricos")
plt.plot(X, y_pred, color="red", label="Línea de regresión (histórica)")
plt.scatter(future_co2, predicted_temp, color="green", label="Proyecciones futuras")
plt.plot(future_co2, predicted_temp, color="green", linestyle="--")
plt.title("Relación CO2 vs Temperatura (con proyecciones)", fontsize=14)
plt.xlabel("CO2 Promedio Global (ppm)", fontsize=12)
plt.ylabel("Temperatura Promedio Global (°C)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

residuals = y - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(X, residuals, color="purple", alpha=0.5)
plt.axhline(y=0, color="black", linestyle="--", linewidth=1)
plt.title("Gráfico de residuos: CO2 vs Temperatura", fontsize=14)
plt.xlabel("CO2 Promedio Global (ppm)", fontsize=12)
plt.ylabel("Residuos (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()