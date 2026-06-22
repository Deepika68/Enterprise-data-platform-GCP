# Enterprise Data Platform on Google Cloud

### A Centralized Data Platform for Building a Single Source of Truth for Analytics and Reporting

## Problem statement
Organizations generate and consume data from multiple heterogeneous sources such as APIs, applications, CSV files, and JSON feeds. Due to fragmented data landscapes, deriving consistent and reliable business insights becomes challenging.

The business requirement is to establish a centralized Enterprise Data Platform that serves as a Single Source of Truth (SSOT), enabling stakeholders to make informed decisions through standardized, governed, and trusted datasets.

The platform aims to:

Consolidate data from multiple source systems.
Enable automated and scalable data ingestion.
Ensure data quality and consistency through reconciliation processes.
Provide centralized analytical datasets for reporting and business intelligence.
Support future AI and machine learning initiatives.
Improve data governance, monitoring, and operational visibility.

## Solution overview
To address these challenges, a cloud-based Enterprise Data Platform was implemented using Google Cloud Platform (GCP).

The platform integrates data from various sources including CSV files, JSON files, APIs, and application systems through automated ingestion pipelines orchestrated by Apache Airflow.

The architecture follows a layered approach consisting of:

Data Ingestion Layer
Enterprise Data Zone (EDZ)
Landing Zone
Staging Layer
Data Warehouse Layer
Semantic Layer
Data Quality and Reconciliation Framework
Reporting and Analytics Layer
Monitoring and Governance Components
Processed and curated datasets are stored in BigQuery and exposed to Power BI for business reporting and analytical insights, thereby establishing a centralized and trusted data ecosystem.

## High level architecture

                         Data Sources
      (CSV | JSON | APIs | Applications | Product Systems)
                                     │
                                     ▼
                        Data Ingestion Layer
                     (Python + Apache Airflow)
                                     │
                                     ▼
                       Enterprise Data Zone (EDZ)
         ┌─────────────────────────────────────────────────┐
         │ Landing Zone (Google Cloud Storage)             │
         │ Staging Layer                                   │
         │ Data Warehouse Layer (BigQuery)                 │
         │ Semantic Layer                                  │
         └─────────────────────────────────────────────────┘
                                     │
                                     ▼
                       Reconciliation Framework
                     (Source vs Target Validation)
                                     │
                                     ▼
                        Reporting and Analytics
                               (Power BI)
                                     │
                                     ▼
                            AI / ML Consumption


Supporting Components

• CI/CD Pipelines
• IAM and Access Management
• Cloud Logging
• Audit Tables
• Monitoring and Alerting

## Roles and key contributions

Performing data profiling and quality checks.
Executing source-to-target reconciliation processes.
Monitoring Apache Airflow DAG executions.
Investigating pipeline failures and analyzing error logs.
Performing daily operational health checks.
Maintaining audit and validation reports.
Supporting Power BI data validation across products.
Verifying API-based data feeds and schema consistency.
Communicating daily status updates to client teams.
Assisting in ensuring data quality and platform reliability.

Supported daily ETL operations and workflow monitoring.
Contributed to data quality and reconciliation activities.
Investigated and resolved data discrepancies.
Ensured reliable data availability for reporting and analytics.
Collaborated with stakeholders to maintain a trusted enterprise data platform.

## Outcome

Successfully contributed to the implementation and operation of a centralized cloud-based Enterprise Data Platform that serves as a Single Source of Truth (SSOT), enabling consistent reporting, improved data governance, and data-driven business decisions.


