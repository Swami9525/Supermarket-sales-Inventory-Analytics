# 🛒 Supermarket Sales & Inventory Analytics

An end-to-end data analytics project designed to analyze supermarket sales, monitor inventory, identify top-performing products, and support data-driven business decisions using Python, SQL, PostgreSQL, and Power BI.

## 📌 Project Overview

Supermarkets generate sales and inventory data every day. Analyzing this data helps businesses understand sales performance, customer purchasing patterns, product demand, and stock availability.

This project combines data processing, database management, SQL analysis, and interactive Power BI dashboards to turn raw supermarket data into meaningful business insights.

## 🎯 Project Objectives

* Analyze total sales revenue and units sold.
* Identify top-performing products and categories.
* Understand sales trends over time.
* Analyze payment method distribution.
* Monitor available and out-of-stock products.
* Identify products that need replenishment.
* Automate data validation and cleaning using Python.
* Present business insights through interactive Power BI dashboards.

## 🛠️ Technologies Used

| Technology            | Purpose                                            |
| --------------------- | -------------------------------------------------- |
| Python                | Data validation, cleaning, and automation          |
| Pandas                | Data manipulation and processing                   |
| PostgreSQL            | Storing and managing structured data               |
| SQL                   | Business analysis and data extraction              |
| Power BI              | Interactive dashboards and visualization           |
| DAX                   | Calculated measures and analytical KPIs            |
| Microsoft Excel / CSV | Source data and data inspection                    |
| GitHub                | Project version control and portfolio presentation |

## 📂 Project Structure

```text
Supermarket-Sales-Inventory-Analytics/
│
├── python/
│   ├── main.py
│   ├── validate_data.py
│   └── clean_data.py
│
├── sql/
│   └── SQL analysis files
│
├── powerbi/
│   └── Power BI dashboard file
│
├── reports/
│   └── Project report
│
├── presentation/
│   └── Project presentation
│
└── README.md
```

*Note: Update the folder and file names above to match the actual structure of your repository.*

## 📊 Dataset Description

The project uses three datasets.

### 1. Products Dataset

Contains product details and pricing information.

| Column          | Description                                        |
| --------------- | -------------------------------------------------- |
| `product_id`    | Unique product identifier                          |
| `product_name`  | Name of the product                                |
| `category`      | Product category                                   |
| `cost_price`    | Product cost price                                 |
| `selling_price` | Product selling price                              |
| `reorder_level` | Stock level at which replenishment may be required |

### 2. Sales Dataset

Contains transaction-level sales information.

| Column           | Description                           |
| ---------------- | ------------------------------------- |
| `bill_number`    | Bill or transaction identifier        |
| `sale_date`      | Date of the sale                      |
| `product_id`     | Product identifier                    |
| `quantity`       | Quantity sold                         |
| `discount`       | Discount recorded for the transaction |
| `payment_method` | Payment method used                   |

### 3. Inventory Dataset

Contains inventory and stock movement information.

| Column           | Description                          |
| ---------------- | ------------------------------------ |
| `inventory_date` | Inventory record date                |
| `product_id`     | Product identifier                   |
| `opening_stock`  | Stock at the beginning of the period |
| `stock_received` | Stock received                       |
| `damaged_units`  | Damaged stock units                  |
| `stock_count`    | Recorded physical stock count        |
| `closing_stock`  | Recorded closing stock               |

## 🐍 Python Data Processing

Python scripts are used to support data preparation and automation.

The intended processing workflow includes:

* Validating incoming data files.
* Checking required columns and data quality.
* Cleaning inconsistent or incomplete records.
* Checking for duplicate files or invalid product references.
* Preparing data for database loading.
* Recording import outcomes where configured.

The exact operations depend on the implemented scripts and their configuration.

## 🗄️ SQL Analysis

SQL and PostgreSQL are used to organize data and perform business analysis.

Example analytical questions include:

* What is the total sales revenue?
* Which products generate the highest revenue?
* Which product categories perform best?
* How many units were sold?
* Which payment methods are most frequently used?
* Which products have low or zero stock?
* Which products may require replenishment?

## 📈 Power BI Dashboards

### 1. Sales Performance Dashboard

The sales dashboard is designed to present:

* Total Revenue
* Total Orders
* Units Sold
* Average Order Value
* Sales Trend Over Time
* Top 10 Products
* Revenue by Product Category
* Sales by Payment Method

* 

### 2. Inventory Monitoring Dashboard

The inventory dashboard is designed to present:

* Total Products
* Available Stock
* Out-of-Stock Products
* Low-Stock Products
* Stock Status Distribution
* Stock by Category
* Products with the Lowest Stock
* Reorder Alert Table
  

*Add screenshots of your completed dashboards here to make the project easier to understand.*

## 📐 Key Business Metrics

| Metric                | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| Revenue               | Measures sales value                                             |
| Orders                | Counts distinct bills or transactions                            |
| Units Sold            | Measures total quantity sold                                     |
| Average Order Value   | Measures average revenue per bill                                |
| Low-Stock Products    | Identifies products at or below their reorder level              |
| Out-of-Stock Products | Identifies products with zero or negative recorded closing stock |

**Important:** Revenue calculations must account for the discount field if the goal is to calculate net sales. Inventory calculations should also account for the inventory date when multiple stock snapshots exist for the same product.

## 🔄 Project Workflow

1. Collect supermarket product, sales, and inventory data.
2. Validate and clean the data using Python.
3. Store and manage structured data in PostgreSQL.
4. Use SQL to analyze business performance.
5. Connect the prepared data to Power BI.
6. Build sales and inventory dashboards.
7. Interpret insights and identify opportunities for improvement.

## 💼 Business Value

This project demonstrates how data analytics can help a supermarket:

* Understand product and category performance.
* Monitor sales trends.
* Identify inventory shortages.
* Improve stock replenishment planning.
* Support operational decision-making.
* Reduce manual reporting effort through automation.

## 🚀 Future Improvements

* Automate scheduled data refreshes.
* Add customer-level analysis if suitable customer data becomes available.
* Build demand forecasting models.
* Add profit-margin analysis using cost and selling prices.
* Implement automated low-stock notifications.
* Improve database integration and data quality monitoring.

## 👨‍💻 Skills Demonstrated

* Data Cleaning and Validation
* Python and Pandas
* SQL Queries and Business Analysis
* PostgreSQL
* Power BI Dashboard Development
* DAX Measures
* KPI Reporting
* Inventory Analysis
* Sales Analytics
* Data Visualization

## 📁 Project Files

Explore the repository for the Python scripts, SQL queries, Power BI report, project documentation, and presentation.

## ⚠️ Disclaimer

This is a portfolio project for demonstrating data analytics skills. Business insights depend on the quality and completeness of the underlying datasets. Any results presented should be validated against the actual project data.

## ⭐ Feedback

Suggestions and feedback are welcome. This project reflects my learning and practical application of data analytics tools.

---

**Built with Python, SQL, PostgreSQL, and Power BI.**
