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

vendedores_data = [
    {"ID_Vendedor": 1042, "Nombre_Ingeniero":"Ing. Roberto Ventas", "Zona":"Norte"},
    {"ID_Vendedor": 1035, "Nombre_Ingeniero":"Ing. Roberto Ventas", "Zona":"Norte"},
    {"ID_Vendedor": 1089, "Nombre_Ingeniero":"Ing. Roberto Ventas", "Zona":"Norte"},
    {"ID_Vendedor": 1010, "Nombre_Ingeniero":"Ing. Roberto Ventas", "Zona":"Norte"}
]

df_vendedores = pd.DataFrame(vendedores_data)

# ---------- 4. Tabla de Hechos: Órdenes de producción (ventas) --------------
num_ordenes = 800
ordenes_data = []

for _ in range(num_ordenes):
    cliente = random.choice(clientes_data)
    parte = random.choice(partes_data)
    vendedor = random.choice(vendedores_data)

    cantidad = random.choice([10, 50, 100, 200, 500])

    fecha = faker.date_between(start_date='-1y', end_date='today')

    ordenes_data.append({
        "ID_Orden": faker.uuid4(),
        "Fecha_Orden": fecha,
        "ID_Cliente": cliente["ID_Cliente"]
    })