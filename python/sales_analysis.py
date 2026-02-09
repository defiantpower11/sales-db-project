from sqlalchemy import create_engine
import pandas as pd

# Crear engine de conexión
engine = create_engine(
    "postgresql+psycopg2://postgres:Reynoso0320@localhost:5432/sales_db"
)

# Consulta SQL
query = """
SELECT customer_name, total_spent
FROM customer_sales
ORDER BY total_spent DESC;
"""

# Ejecutar consulta
df = pd.read_sql(query, engine)

# Mostrar resultados
print(df)

# Exportar a CSV
df.to_csv("output/sales_report.csv", index=False)


