import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connect DB
engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/amman_market")

# Load data
orders = pd.read_sql("SELECT * FROM orders WHERE status != 'cancelled'", engine)
order_items = pd.read_sql("SELECT * FROM order_items WHERE quantity <= 100", engine)
products = pd.read_sql("SELECT * FROM products", engine)

# Merge
df = order_items.merge(orders, on="order_id") \
                .merge(products, on="product_id")

df["revenue"] = df["quantity"] * df["unit_price"]

# Aggregate
category_rev = df.groupby("category")["revenue"].sum().sort_values()

# Plot
plt.figure(figsize=(12, 8))
sns.barplot(x=category_rev.values, y=category_rev.index, palette="viridis")

for i, v in enumerate(category_rev.values):
    plt.text(v + 200, i, f"{v:.0f}", va='center')

plt.title("Electronics and Books Drive Most Revenue in the Market")
plt.xlabel("Revenue (JOD)")
plt.ylabel("Category")

plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.close()