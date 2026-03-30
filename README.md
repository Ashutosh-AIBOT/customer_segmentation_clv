# Customer Segmentation and CLV

Behavioral segmentation with customer lifetime value intelligence.

customer-segmentation-clv-intelligence

## Domain

Marketing analytics and CRM

## Objective

Segment customers and estimate value potential for retention and growth strategies.

## Business Value

Improves campaign ROI, retention prioritization, and budget allocation quality.

## Dataset

Verified: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

## Run Locally

conda run -n ml-env streamlit run app.py

## Dashboard Features

- Executive overview and business framing
- Prediction Center (single input + batch CSV)
- Model ranking leaderboard
- Model registry (all discovered model artifacts)
- Charts gallery (auto-load from charts/)
- Notebook traceability panel

## Notebook Path Setup

Inside notebooks:

from path_setup import BASE, RAW, PROCESSED, MODELS, CHARTS, load_raw_csv

Project path helpers:

- path_utils.py
- notebooks/path_setup.py
## Deploy on Render

This repo includes render.yaml. Connect repo in Render and deploy.

Start command used:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0

## Git LFS

Large assets are tracked with Git LFS (models, charts, data artifacts).
