# DAX Measures — Retail Sales Dashboard

Create these as a new **Measures table** (Modeling → New Table → name it `_Measures`, then add each measure below to it via "New Measure").

## Core Measures

```DAX
Total Revenue = SUM(Sales[Revenue])

Total Cost = SUM(Sales[Cost])

Total Profit = SUM(Sales[Profit])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Total Orders = DISTINCTCOUNT(Sales[OrderID])

Total Quantity Sold = SUM(Sales[Quantity])

Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

Average Discount % = AVERAGE(Sales[Discount])
```

## Time Intelligence (requires DateTable marked as Date Table)

```DAX
Revenue LY =
CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DateTable[Date]))

Revenue YoY % =
DIVIDE([Total Revenue] - [Revenue LY], [Revenue LY], 0)

Revenue MTD =
TOTALMTD([Total Revenue], DateTable[Date])

Revenue QTD =
TOTALQTD([Total Revenue], DateTable[Date])

Revenue YTD =
TOTALYTD([Total Revenue], DateTable[Date])

Rolling 3M Revenue =
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(DateTable[Date], MAX(DateTable[Date]), -3, MONTH)
)
```

## Ranking & Contribution

```DAX
Revenue Rank (Product) =
RANKX(ALL(Products[ProductName]), [Total Revenue], , DESC)

% of Total Revenue =
DIVIDE([Total Revenue], CALCULATE([Total Revenue], ALL(Products)), 0)

Top 5 Products Revenue =
CALCULATE(
    [Total Revenue],
    TOPN(5, ALL(Products[ProductName]), [Total Revenue], DESC)
)
```

## Customer / Segment

```DAX
Distinct Customers = DISTINCTCOUNT(Sales[CustomerID])

Revenue per Customer = DIVIDE([Total Revenue], [Distinct Customers], 0)
```

## KPI Status (example: target-based)

```DAX
Revenue Target = 6000000   -- adjust to your goal

Revenue vs Target % = DIVIDE([Total Revenue], [Revenue Target], 0)

KPI Status =
SWITCH(
    TRUE(),
    [Revenue vs Target %] >= 1, "On Target",
    [Revenue vs Target %] >= 0.85, "Near Target",
    "Below Target"
)
```

---
### Notes
- Wrap any measure used in a card that could divide by zero with `DIVIDE()` (already done above) instead of `/`.
- If numbers look inflated/deflated, double check relationship cardinality (see `Build_Guide.md` → Data Model).
