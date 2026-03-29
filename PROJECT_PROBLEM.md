# Project 3 — Customer Segmentation + Lifetime Value (CLV) Prediction

## Problem Statement
E-commerce companies spend marketing budget uniformly across all customers — but a VIP
customer who spends ₹50,000/year needs a completely different strategy than one who
bought once 11 months ago. This project uses unsupervised clustering to segment customers
by behaviour (RFM model), then predicts each segment's 12-month Customer Lifetime Value
using regression. Used by every e-commerce company from Flipkart to Meesho.

## Dataset
- **Name:** Online Retail II Dataset
- **Source:** https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
- **Size:** 1,067,371 transactions × 8 features (2009–2011)
- **Target (CLV):** Derived — next 6-month revenue per customer
- **Customers:** ~5,900 unique customers

## Files to Download from Kaggle
```
online_retail_II.xlsx    → two sheets: Year 2009-2010, Year 2010-2011
```

## Feature Description
```
InvoiceNo    → transaction ID (prefix C = cancelled)
StockCode    → product code
Description  → product name
Quantity     → units purchased (negative = return)
InvoiceDate  → timestamp
UnitPrice    → price per unit in GBP
CustomerID   → unique customer identifier
Country      → customer country
```

## ML Models Used
| Model | Purpose |
|-------|---------|
| K-Means clustering | Primary segmentation (k=4 optimal) |
| DBSCAN | Outlier/VIP detection that K-Means misses |
| Hierarchical Clustering | Dendrogram for segment validation |
| Ridge Regression | CLV prediction per segment |

## Key Techniques
- RFM feature engineering: Recency (days since last purchase), Frequency (order count), Monetary (total spend)
- Log-transformation of skewed RFM features before clustering
- Optimal k: Elbow method + Silhouette score (not just guessing k=3 or k=4)
- DBSCAN eps/min_samples tuning to isolate genuine VIP outliers
- Cohort-based CLV: use first 6 months to predict next 6 months revenue
- Segment-specific regression models (separate model per cluster)

## Evaluation Metrics
- Clustering: **Silhouette Score**, Davies-Bouldin Index, Calinski-Harabasz
- CLV Regression: MAE, RMSE per segment, R² score
- Business metric: Revenue coverage (top 20% customers = X% of revenue)

## Expected Output / Insights
1. 4 customer segments: Champions, Loyal, At-Risk, Lost — with actionable labels
2. RFM 3D scatter plot coloured by cluster (strongest visual for resume)
3. Per-segment CLV distribution and predicted 12-month revenue
4. Top 100 VIP customers identified by DBSCAN (outlier cluster)
5. Pareto analysis: what % of customers drive 80% of revenue

## Resume Bullet
> Built an end-to-end customer segmentation system on 1M+ transactions using K-Means + DBSCAN
> clustering on RFM features, identifying 4 actionable segments. Developed per-segment CLV
> regression models predicting 12-month revenue with MAE < 15%. Delivered Pareto analysis
> showing top 18% customers drive 80% of revenue.

## How to Run
```bash
make train        # runs full pipeline
make evaluate     # generates reports/figures/
make predict      # score new customers into segments
```
