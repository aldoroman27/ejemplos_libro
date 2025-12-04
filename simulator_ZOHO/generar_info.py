import pandas as pd
from faker import Faker
import random

# Creamos una instancia de Faker y la configuramos en español
faker = Faker('es_MX')
faker.seed(101) # Creamos una semilla para lo aleatorio de los datos
random.seed(101)

# ------ Comenzamos a llenar nuestros productos -------------
categorias_maquinado = {
    'Torneado CNC': [50, 500],
    'Fresado 3 ejes CNC' : [200, 1500],
    'Fresado 5 ejes CNC' : [1500, 8000],
    'Rectificado' : [100, 1000],
    'Erosionado' : [500, 4000]
}

partes_data = []
id_parte = 1

nombres_base = ["Eje", "Buje", "Placa", "Soporte", "Molde", "Engrane", "Carcasa", "Piston"]

for categoria, rango in categorias_maquinado.items():
    for _ in range(10): # 10 tipos de partes por categoría
        precio_base = round(random.uniform(rango[0], rango[1]), 2)
        # Generamos los nombres técnicos.
        nombre_tecnico = f"{random.choice(nombres_base)}{faker.lexify(text='????').upper()}-{random.randint(10,99)}"
        
        partes_data.append({
            "ID_Parte": id_parte,
            "Proceso": categoria,
            "Nombre_parte": nombre_tecnico,
            "Costo_Unitario": round(precio_base * 0.6, 2), # Margen aprox del 40%
            "Precio_Venta": precio_base
        })
        id_parte += 1

df_partes = pd.DataFrame(partes_data)

# ----------- 2. Cartera de Clientes ------------------
# Aquí usamos fake, con su metodo fake.company() porque nuestros clientes son empresas.
num_clientes = 30
clientes_data = []

for i in range(1, num_clientes +1):
    clientes_data.append({
        "ID_Cliente": i,
        "Empresa": Faker.company(),
        "Industria": random.choice(["Automotriz", "Aeronautica", "Medica", "Metalurgica"]),
        "Contacto": faker.name(),
        "Email_Contacto": faker.email()
    })

df_clientes = pd.DataFrame(clientes_data)