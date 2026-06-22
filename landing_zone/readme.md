# Landing Zone

## Overview

The Landing Zone acts as the raw storage layer of the Enterprise Data Platform.

Raw data extracted from source systems is stored without applying business transformations.

## Purpose

- Preserve original source files.
- Enable traceability and auditability.
- Support reprocessing when required.
- Serve as the source for staging transformations.

## Data Stored

### customers_raw.csv
Customer master data.

### products_raw.csv
Product master data.

### orders_raw.json
Transactional order data.

## GCP Equivalent

Google Cloud Storage (GCS)

In production environments, Apache Airflow pipelines load extracted datasets into GCS buckets before downstream processing.
