# 📊 Retail Pulse — Sales Intelligence Dashboard

A retail sales dashboard analyzing products, regions, and customer segments — built as a portfolio project. Ships as **both**:
- a **live, no-install web dashboard** (`index.html`) — open it directly or deploy free on GitHub Pages, no Power BI required
- a **Power BI-ready dataset + build guide**, if you get access to Power BI Desktop later and want the full DAX/star-schema version

---

## 🚀 Step-by-step: upload this to GitHub

### 1. Create the repo
Go to [github.com/new](https://github.com/new) → name it (e.g. `retail-pulse-dashboard`) → keep it **Public** (so GitHub Pages can serve it for free) → **do not** initialize with a README (you already have one) → **Create repository**.

### 2. Get all these files onto your computer
Download every file from this project into one folder on your computer, keeping the same structure:
```
retail-dashboard/
├── index.html
├── README.md
├── .gitignore
├── generate_data.py
├── DAX_Measures.md
├── Build_Guide.md
├── Data_Dictionary.md
├── data/
│   ├── Sales.csv
│   ├── Products.csv
│   ├── Stores.csv
│   ├── Customers.csv
│   └── DateTable.csv
└── screenshots/          (empty folder — fine to skip if git won't track it)
```

### 3. Push it up
Open a terminal in that folder and run:
```bash
git init
git add .
git commit -m "Initial commit: retail sales dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```
Replace `<your-username>` and `<repo-name>` with your actual GitHub username and the repo name from step 1.

### 4. Make the dashboard live (optional but recommended)
1. In your repo on GitHub, go to **Settings → Pages**.
2. Under **Source**, choose **Deploy from a branch**.
3. Branch: `main`, folder: `/ (root)` → **Save**.
4. Wait ~1 minute, then visit `https://<your-username>.github.io/<repo-name>/` — your dashboard is live.

### 5. Double check
- Open the GitHub Pages link (or just double-click `index.html` locally) and confirm the charts render and the **year filter buttons** (All Years / 2023 / 2024) actually change the numbers.
- If anything looks broken, open the browser console (F12 → Console tab) and check for red errors.

---

## ▶ View it now (without GitHub)
Just open `index.html` in any browser — it's fully self-contained (data is embedded, charts render via Chart.js loaded from a CDN). No build step, no server needed, no Power BI needed.

## Overview
- **15,000 transactions** across **30 products / 5 categories**, **15 stores / 5 regions**, **400 customers**, spanning **Jan 2023 – Dec 2024**
- Dark "control room" visual style — KPI strip, revenue trend, category/region/segment breakdowns, margin-vs-volume scatter, top products, store leaderboard
- Year filter (All / 2023 / 2024) that live-updates every chart and KPI
- Same dataset also modeled as a proper star schema for Power BI if you want to go further later

## 🗂 Repo Structure
```
retail-dashboard/
├── index.html              # ⭐ Web dashboard — open directly or deploy via GitHub Pages
├── data/
│   ├── Sales.csv          # Fact table (15,000 rows)
│   ├── Products.csv       # 30 products / 5 categories
│   ├── Stores.csv         # 15 stores / 5 regions
│   ├── Customers.csv      # 400 customers / 4 segments
│   └── DateTable.csv      # 2023–2024 calendar table
├── generate_data.py       # Script that generated the dataset (re-run to regenerate/reshuffle)
├── DAX_Measures.md        # DAX measures (only needed if you build the Power BI version)
├── Build_Guide.md         # Power BI build steps (optional path)
├── Data_Dictionary.md     # Column-level documentation for every table
├── screenshots/           # Optional: dashboard screenshots for this README
├── .gitignore
└── README.md
```

## 🛠 Optional: build the Power BI version too
If you get access to Power BI Desktop later, the same `/data` files and `DAX_Measures.md` measures build into a full star-schema report — follow `Build_Guide.md` step by step.

## 🔍 Insights from the Data

Findings pulled from the 15,000-transaction dataset — this is the "so what" a stakeholder would actually want out of the dashboard, not just the chart list.

**Growth**
- Total revenue: ₹52.6L, total profit: ₹20.6L, blended margin: **39.2%**
- Revenue grew **6.9% year-over-year** (2023 → 2024), with every quarter of 2024 outperforming its 2023 counterpart

**Seasonality**
- November–December together account for **23.3%** of full-year revenue — the clearest seasonal spike in the data, consistent across both years
- February is the weakest month both years, roughly 20% below the monthly average
- Weekends run **~8% higher** average daily revenue than weekdays — a smaller but consistent lift

**Category performance**
- **Sports** is the top category by revenue (₹14.6L) but **Electronics (43.9%) and Sports (44.4%)** carry the highest margins — Sports is a rare case of leading on both volume and margin
- **Apparel** has the lowest category margin (29.9%) despite solid revenue — a candidate for pricing review
- Beauty is the smallest category by revenue (₹7.2L) and mid-pack on margin

**Product-level**
- Top 3 by revenue: **Dumbbell Set, Resistance Bands, Storage Bins** — all in the ₹4.5L+ range and none of them the highest-margin items, so they're volume plays
- Highest-margin products: **USB-C Hub, Wireless Earbuds, Blender** (all ~50% margin) — high margin but low revenue, meaning they're under-promoted relative to their profitability
- Lowest-margin products: **Non-Stick Pan Set (19.7%), Face Serum (22.3%), Baseball Cap (24.7%)** — worth a cost or pricing review given they still sell steadily

**Regional & store**
- Regional revenue is fairly balanced — only an **8.8% spread** between the highest (East) and lowest (North) region, so no single region is carrying or dragging the business
- Store performance by city is similarly tight (Patna leads, Delhi trails), suggesting demand is broad-based rather than concentrated

**Customer segments**
- **Consumer** is the dominant segment at **47.3% of revenue** — nearly half the business from a single segment
- Average order value is nearly identical across all four segments (₹347–₹358), meaning the revenue gap between segments is purely a function of order volume, not basket size

**What this suggests as next steps** (the kind of narrative this dashboard is built to support): protect Nov–Dec inventory/staffing for the seasonal peak, consider a Feb promotion to smooth the trough, review pricing on Apparel and the lowest-margin SKUs, and test increased marketing spend on the high-margin, low-revenue products (USB-C Hub, Wireless Earbuds, Blender) since they have room to scale profitably.

> Note: this is a synthetic dataset generated for portfolio purposes (see `generate_data.py`), so treat these as illustrative findings, not real business conclusions. The dashboard and this write-up are meant to demonstrate the analysis workflow — swap in your own data and the same structure applies.

## 📈 Key Metrics Modeled
- Total Revenue, Total Profit, Profit Margin %
- Revenue YoY, monthly trend
- Top-N product ranking & % contribution to total revenue
- Revenue by Region / City / Category / Segment
- Margin vs. sales volume by product

## 🛠 Tech Stack
- **HTML + Chart.js** for the live dashboard (no build tools, no dependencies to install)
- **Python (pandas, numpy)** for synthetic data generation
- **Power BI Desktop** (optional) — data model, DAX, visuals

## 📄 License
MIT — feel free to fork and adapt with your own data.
