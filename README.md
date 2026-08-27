# 🛍️ Online Retail Customer Segmentation

An end-to-end Data Science and Machine Learning project that analyzes online retail transactions and segments customers based on their purchasing behavior using **RFM Analysis** and **K-Means Clustering**.

The project also includes an interactive **Streamlit dashboard** for business and customer analytics.

---

## 📌 Project Overview

Understanding customer behavior is important for businesses to improve customer retention, marketing strategies, and revenue.

This project uses the **Online Retail dataset** to:

- Clean and preprocess retail transaction data
- Perform Exploratory Data Analysis (EDA)
- Analyze sales and revenue trends
- Calculate customer-level RFM metrics
- Apply K-Means clustering
- Segment customers based on purchasing behavior
- Build an interactive Streamlit dashboard
- Generate business-oriented insights

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze online retail transaction data.
2. Identify important sales and revenue patterns.
3. Understand customer purchasing behavior.
4. Calculate Recency, Frequency, and Monetary values.
5. Group customers using K-Means clustering.
6. Identify valuable customer segments.
7. Provide an interactive dashboard for business analysis.

---

## 📊 Dataset

The project uses the **Online Retail Dataset** containing retail transactions.

### Dataset Size

- **Rows:** 541,909
- **Columns:** 8

### Original Features

| Feature | Description |
|---|---|
| `InvoiceNo` | Unique invoice/order number |
| `StockCode` | Product code |
| `Description` | Product description |
| `Quantity` | Number of products purchased |
| `InvoiceDate` | Date and time of transaction |
| `UnitPrice` | Price per product |
| `CustomerID` | Unique customer identifier |
| `Country` | Customer's country |

---

## 🧹 Data Cleaning

The dataset was cleaned before analysis.

The cleaning process included:

- Handling missing values
- Converting `InvoiceDate` into datetime format
- Identifying cancelled transactions
- Removing invalid transaction records
- Handling invalid quantities and prices
- Creating a revenue feature

## 👩‍💻 Author

**Reena Shah**

Final Year Engineering Student  
Artificial Intelligence & Data Science

### Skills & Interests

- Data Science
- Artificial Intelligence
- Machine Learning
- Python
- Data Analysis
- Customer Analytics

---

## ⭐ Conclusion

This project demonstrates an end-to-end Data Science and Machine Learning workflow, starting from raw retail transaction data and progressing through data cleaning, exploratory data analysis, RFM feature engineering, K-Means customer segmentation, and interactive Streamlit dashboard development.

The project provides both **technical machine learning analysis** and **business-oriented customer insights**.

```text
Revenue = Quantity × UnitPrice
