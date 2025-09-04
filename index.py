import pandas as pd
import numpy as np


### Numpy


### 1

ciudades = np.array([
    ["Buenos Aires", "CABA", "3070", "1580"],
    ["Córdoba", "Córdoba", "1390", "1573"],
    ["Rosario", "Santa Fe", "1170", "1689"],
    ["Mendoza", "Mendoza", "937", "1561"],
    ["La Plata", "Buenos Aires", "740", "1882"]
])


#### 2
poblaciones = ciudades[:, 2].astype(int)

media = np.mean(poblaciones)
print(f"La población media de las ciudades es: {media} miles de habitantes.")

mediana = np.median(poblaciones)
print(f"La mediana de la población de las ciudades es: {mediana} miles de habitantes.")

desviacion_estandar = np.std(poblaciones)
print(f"La desviación estándar de la población de las ciudades es: {desviacion_estandar} miles de habitantes.")


#### 3
años_fundacion = ciudades[:, 3].astype(int)
mas_antigua = np.min(años_fundacion)
ciudad_mas_antigua = ciudades[np.argmin(años_fundacion), 0]
print(f"La ciudad más antigua es {ciudad_mas_antigua}, fundada en {mas_antigua}.")


### 4

matriz = np.column_stack((poblaciones, años_fundacion))
suma_columnas = np.sum(matriz, axis=0)
print(f"Suma de poblaciones: {suma_columnas[0]}, Suma de años de fundación: {suma_columnas[1]}")



### Pandas

### 1

data = {
    "Ciudad": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata"],
    "Provincia": ["CABA", "Córdoba", "Santa Fe", "Mendoza", "Buenos Aires"],
    "Población (miles)": [3070, 1390, 1170, 937, 740],
    "Año de fundación": [1580, 1573, 1689, 1561, 1882],
}

df = pd.DataFrame(data)


## 2
siglo_fundacion = (df["Año de fundación"] // 100) + 1
df["Siglo de fundación"] = siglo_fundacion  


### 3

ciudad_mayor_poblacion = df.loc[df["Población (miles)"].idxmax()]
print(f"La ciudad con mayor población es {ciudad_mayor_poblacion['Ciudad']} con {ciudad_mayor_poblacion['Población (miles)']} miles de habitantes.")
edad_promedio_provincias = df.groupby("Provincia")["Año de fundación"].mean()
print("Edad promedio de las provincias:")
print(edad_promedio_provincias)


### 4
ciudades_menores_1600 = df[df["Año de fundación"] > 1600]
print("Ciudades fundadas después del año 1600:")
print(ciudades_menores_1600)

### 5

export_csv = df.to_csv("ciudades_arg.csv", index=False)
print("Datos exportados a 'ciudades.csv'")      
