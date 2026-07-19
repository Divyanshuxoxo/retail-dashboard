import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# ---------- Dimension: Products ----------
categories = {
    "Electronics": ["Wireless Earbuds", "Smart Watch", "Bluetooth Speaker", "Laptop Stand", "Power Bank", "USB-C Hub"],
    "Apparel": ["Men's T-Shirt", "Women's Jeans", "Running Shoes", "Winter Jacket", "Baseball Cap", "Hoodie"],
    "Home & Kitchen": ["Air Fryer", "Coffee Maker", "Non-Stick Pan Set", "LED Desk Lamp", "Blender", "Storage Bins"],
    "Beauty": ["Face Serum", "Shampoo Set", "Lip Balm Kit", "Sunscreen SPF50", "Hair Dryer", "Makeup Brush Set"],
    "Sports": ["Yoga Mat", "Dumbbell Set", "Resistance Bands", "Cricket Bat", "Football", "Cycling Helmet"],
}

products = []
pid = 1000
for cat, items in categories.items():
    for item in items:
        base_cost = np.random.uniform(5, 150)
        margin = np.random.uniform(1.3, 2.2)
        products.append({
            "ProductID": f"P{pid}",
            "ProductName": item,
            "Category": cat,
            "UnitCost": round(base_cost, 2),
            "UnitPrice": round(base_cost * margin, 2),
        })
        pid += 1
products_df = pd.DataFrame(products)

# ---------- Dimension: Regions/Stores ----------
regions = {
    "North": ["Delhi", "Chandigarh", "Lucknow"],
    "South": ["Bengaluru", "Chennai", "Hyderabad"],
    "East": ["Kolkata", "Bhubaneswar", "Patna"],
    "West": ["Mumbai", "Pune", "Ahmedabad"],
    "Central": ["Nagpur", "Bhopal", "Indore"],
}
stores = []
sid = 1
for region, cities in regions.items():
    for city in cities:
        stores.append({"StoreID": f"S{sid:03d}", "City": city, "Region": region})
        sid += 1
stores_df = pd.DataFrame(stores)

# ---------- Dimension: Customers ----------
segments = ["Consumer", "Small Business", "Corporate", "Online"]
n_customers = 400
customers_df = pd.DataFrame({
    "CustomerID": [f"C{i:04d}" for i in range(1, n_customers + 1)],
    "Segment": np.random.choice(segments, n_customers, p=[0.5, 0.2, 0.15, 0.15]),
})

# ---------- Dimension: Date ----------
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start_date, end_date, freq="D")
date_df = pd.DataFrame({"Date": date_range})
date_df["Year"] = date_df["Date"].dt.year
date_df["Month"] = date_df["Date"].dt.month
date_df["MonthName"] = date_df["Date"].dt.strftime("%b")
date_df["Quarter"] = "Q" + date_df["Date"].dt.quarter.astype(str)
date_df["DayOfWeek"] = date_df["Date"].dt.strftime("%A")
date_df["YearMonth"] = date_df["Date"].dt.strftime("%Y-%m")

# ---------- Fact: Sales ----------
n_rows = 15000
order_dates = np.random.choice(date_range, n_rows)
# Add seasonality: boost Nov-Dec and reduce Feb
order_dates = pd.to_datetime(order_dates)

sales_records = []
discount_choices = [0, 0, 0, 0.05, 0.1, 0.15, 0.2]

for i in range(n_rows):
    d = order_dates[i]
    seasonal_multiplier = 1.6 if d.month in (11, 12) else (0.8 if d.month == 2 else 1.0)
    weekend_multiplier = 1.2 if d.weekday() >= 5 else 1.0

    prod = products_df.sample(1).iloc[0]
    store = stores_df.sample(1).iloc[0]
    cust = customers_df.sample(1).iloc[0]

    qty = max(1, int(np.random.poisson(3) * seasonal_multiplier * weekend_multiplier))
    discount = np.random.choice(discount_choices)
    unit_price = prod["UnitPrice"]
    revenue = round(qty * unit_price * (1 - discount), 2)
    cost = round(qty * prod["UnitCost"], 2)
    profit = round(revenue - cost, 2)

    sales_records.append({
        "OrderID": f"ORD{100000 + i}",
        "Date": d.strftime("%Y-%m-%d"),
        "ProductID": prod["ProductID"],
        "StoreID": store["StoreID"],
        "CustomerID": cust["CustomerID"],
        "Quantity": qty,
        "Discount": discount,
        "Revenue": revenue,
        "Cost": cost,
        "Profit": profit,
    })

sales_df = pd.DataFrame(sales_records)

# ---------- Save ----------
out = "/home/claude/retail-dashboard/data"
sales_df.to_csv(f"{out}/Sales.csv", index=False)
products_df.to_csv(f"{out}/Products.csv", index=False)
stores_df.to_csv(f"{out}/Stores.csv", index=False)
customers_df.to_csv(f"{out}/Customers.csv", index=False)
date_df.to_csv(f"{out}/DateTable.csv", index=False)

print("Sales rows:", len(sales_df))
print("Total Revenue:", sales_df["Revenue"].sum())
print("Total Profit:", sales_df["Profit"].sum())
print("Files written:", out)
