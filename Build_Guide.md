# Build Guide — Retail Sales Dashboard (Power BI Desktop)

Estimated time: 45–60 minutes.

## 1. Load the Data
1. Open Power BI Desktop → **Get Data → Text/CSV**.
2. Import all 5 files from `/data`:
   - `Sales.csv` (fact table)
   - `Products.csv`
   - `Stores.csv`
   - `Customers.csv`
   - `DateTable.csv`
3. Click **Transform Data** and set correct types:
   - `Sales[Date]` → Date
   - `Sales[Revenue]`, `Cost`, `Profit` → Fixed Decimal Number
   - `Sales[Discount]` → Percentage
   - `DateTable[Date]` → Date
4. Close & Apply.

## 2. Build the Data Model (star schema)
Go to **Model view** and create these relationships (single direction, one-to-many):

| From | To | Cardinality |
|---|---|---|
| Products[ProductID] | Sales[ProductID] | 1 → * |
| Stores[StoreID] | Sales[StoreID] | 1 → * |
| Customers[CustomerID] | Sales[CustomerID] | 1 → * |
| DateTable[Date] | Sales[Date] | 1 → * |

Then: select `DateTable` → **Table tools → Mark as Date Table** → pick `Date` column.

Result should look like a star: `Sales` in the center, four dimension tables around it.

## 3. Add Measures
Create a blank table called `_Measures` (Modeling → New Table: `_Measures = ROW("Blank", BLANK())`), then paste in the measures from `DAX_Measures.md` one by one via **New Measure**. Keeping measures in their own table keeps the field list clean.

## 4. Build the Report Pages

### Page 1 — Executive Overview
- **Cards**: Total Revenue, Total Profit, Profit Margin %, Total Orders, Revenue YoY %
- **Line chart**: Revenue by Month (X: DateTable[YearMonth], Y: Total Revenue), split by Year for comparison
- **Bar chart**: Revenue by Category (Products[Category])
- **Map or filled map**: Revenue by Region (Stores[Region])
- **Slicers** across the top: Year, Region, Category (sync across pages via Format → Sync Slicers)

### Page 2 — Product Performance
- **Table/Matrix**: Category → Product, with Total Revenue, Total Profit, Profit Margin %, Revenue Rank
- **Top N bar chart**: Top 10 products by revenue (use "Top 5 Products Revenue" pattern or a Top N filter)
- **Scatter chart**: Profit Margin % vs Quantity Sold, bubble size = Revenue, by Product — good for spotting low-margin high-volume items

### Page 3 — Customer & Store Insights
- **Donut chart**: Revenue by Customer Segment
- **Bar chart**: Revenue by City/Store
- **KPI visual**: Revenue vs Target with `KPI Status` measure
- **Table**: Store-level Revenue, Orders, Avg Order Value

## 5. Styling
- Use a consistent theme: **View → Themes** → pick a built-in theme or import a JSON theme.
- Keep 1 accent color for "good" (green) and 1 for "attention" (red/orange) via conditional formatting on cards and KPI table.
- Add a title text box + your name/date on each page footer for portfolio presentation.

## 6. Publish / Export for GitHub
Power BI `.pbix` files are binary — GitHub can host them (via Git LFS if >100MB, unlikely here) but won't render them inline. To make the repo genuinely useful to viewers:
1. Save your file as `RetailSalesDashboard.pbix` in the repo root.
2. Export a few screenshots (**File → Export → Export to PDF**, or just screenshot each page) into `/screenshots` and embed them in `README.md` so visitors see the dashboard without opening Power BI.
3. Optionally publish to Power BI Service (**Publish** button) and link the public/shareable URL in the README.

See `README.md` for the suggested repo write-up.
