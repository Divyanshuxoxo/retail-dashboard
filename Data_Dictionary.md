# Data Dictionary

## Sales.csv (Fact table — 15,000 rows)
| Column | Type | Description |
|---|---|---|
| OrderID | Text | Unique order identifier |
| Date | Date | Order date (2023-01-01 to 2024-12-31) |
| ProductID | Text | FK → Products |
| StoreID | Text | FK → Stores |
| CustomerID | Text | FK → Customers |
| Quantity | Integer | Units sold in the order |
| Discount | Decimal | Discount rate applied (0–0.2) |
| Revenue | Decimal | Net revenue after discount |
| Cost | Decimal | Total cost of goods for the order |
| Profit | Decimal | Revenue − Cost |

## Products.csv (30 products, 5 categories)
| Column | Type | Description |
|---|---|---|
| ProductID | Text | Primary key |
| ProductName | Text | Product name |
| Category | Text | Electronics / Apparel / Home & Kitchen / Beauty / Sports |
| UnitCost | Decimal | Cost per unit |
| UnitPrice | Decimal | List price per unit |

## Stores.csv (15 stores, 5 regions)
| Column | Type | Description |
|---|---|---|
| StoreID | Text | Primary key |
| City | Text | Store city |
| Region | Text | North / South / East / West / Central |

## Customers.csv (400 customers)
| Column | Type | Description |
|---|---|---|
| CustomerID | Text | Primary key |
| Segment | Text | Consumer / Small Business / Corporate / Online |

## DateTable.csv (2023–2024, daily)
| Column | Type | Description |
|---|---|---|
| Date | Date | Calendar date |
| Year | Integer | Year |
| Month | Integer | Month number |
| MonthName | Text | Jan–Dec |
| Quarter | Text | Q1–Q4 |
| DayOfWeek | Text | Monday–Sunday |
| YearMonth | Text | e.g. 2023-01 (good for chart axes) |

**Notes on the data**: it's synthetically generated with built-in seasonality (Nov–Dec sales spike ~60%, February dip, weekend boost) so trend charts and YoY comparisons look realistic. Numbers won't match any real business — swap in your own CSVs with matching column names to reuse the whole model and DAX layer as-is.
