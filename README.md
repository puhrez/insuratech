# InsuraTech
---

Welcome to InsuraTech!

This is repo is proof of concept for a Data Pipeline responsible for processing insurance agency performance data and an API for flexibly exposing the processed data.

### Tools
- Python3.6 for the codebase
- Docker for dev development and CI testing
- SQLAlchemy + cubes for Data Modeling and DB communication
- Flask for incremental ingestion and batch S3 persistent
- Slice for API for cube analysis
- AWS Redshift for Persistence Layer
- AWS Lambda for execution context of APIs and S3-triggered ingestion
- AWS S3 for storage of record batches.


### ETL Pipeline Diagram

Batch
CSV -> POST to Lambda for storage in S3 -> Trigger Lambda for batch record ingestion -> Redshift

Incremental
POST to Lambda for incremental ingestion -> Persist to redshift -> Save to append-only S3 file


### API

/register - register analytics user
/login - login as an analytics user
/auth - authenticate an analytics user to receive JWT for querying
/records - post batch records in .csv
/record - post individual records as json
