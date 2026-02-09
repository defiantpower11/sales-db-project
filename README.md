
# sales-db-project
Sales data analysis project built with Python and SQL, generating reports from relational databases.

# Sales Database Analysis Project

## Descripción
Proyecto de análisis de ventas utilizando una base de datos relacional en PostgreSQL y Python para el consumo de datos.  

El objetivo es calcular el gasto total por cliente utilizando una VIEW para simplificar
consultas complejas con múltiples JOIN.

## Tecnologías utilizadas
PostgreSQL
SQL (JOIN, VIEW, GROUP BY)
Python
pandas
SQLAlchemy

## Estructura del proyecto
sales-db-project/
├── output/              # Resultados generados (CSV)
├── python/              # Scripts de Python
├── sql/                 # Scripts SQL (schema, data, views)
├── venv/                # Entorno virtual
├── .gitignore
└── README.md

## Base de datos
`schema.sql`: definición de tablas y relaciones
`data.sql`: inserción de datos de prueba
`views.sql`: creación de la vista `customer_sales`

La vista encapsula la lógica de negocio y permite consultas simples desde la aplicación.

## Script en Python
El script `sales_analysis.py`:
se conecta a PostgreSQL usando SQLAlchemy
consulta la vista `customer_sales`
exporta los resultados a un archivo CSV

## Resultado
Se genera el archivo:

sales_report.csv

con el total gastado por cada cliente.

## Cómo ejecutar el proyecto

1. Crear la base de datos en PostgreSQL
2. Ejecutar en orden:
    `schema.sql`
    `data.sql`
    `views.sql`
3. Activar el entorno virtual
4. Ejecutar:

```bash
python python/sales_analysis.py
533f987 (Initial sales database analysis project)
