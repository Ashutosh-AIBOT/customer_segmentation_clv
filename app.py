import os

from dashboard_core import ProjectConfig, run_project_app


CONFIG = ProjectConfig(
    key="Project 03",
    title="Customer Segmentation and CLV",
    subtitle="Behavioral segmentation with customer lifetime value intelligence",
    icon="🧩",
    domain="Marketing analytics and CRM",
    objective="Segment customers and estimate value potential for retention and growth strategies.",
    business_value="Improves campaign ROI, retention prioritization, and budget allocation quality.",
    prediction_label="Customer Value",
    highlights=[
        "Blends unsupervised segmentation and CLV regression in one analytical workflow.",
        "Supports portfolio-level targeting through scalable batch inference.",
        "Links modeling outcomes to actionable CRM and growth recommendations.",
        "Presents decision-grade metrics and visual evidence for business stakeholders.",
        "Demonstrates full analytics maturity from exploration to deployment-style app.",
    ],
)


run_project_app(CONFIG, os.path.dirname(__file__))
