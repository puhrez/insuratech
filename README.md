# InsuraTech

Welcome to InsuraTech!

[![Build Status](https://travis-ci.org/puhrez/insuratech.svg?branch=master)](https://travis-ci.org/puhrez/insuratech)

This is repo is proof of concept for a Data Pipeline responsible for processing insurance agency performance data and an API for flexibly exposing the processed data.

### Tools
- Python3.6 for the codebase
- Docker for dev development and CI testing
- SQLAlchemy + cubes for Data Modeling and DB communication
- Flask/Slice for HTTP handling and public query-based API
- AWS Redshift for Persistence Layer
- AWS Lambda for execution context of API


### Local installation

Make sure you have Docker installed for local service installation

#### Make commands

```
backend                        Run the backend service
setup                          Install reqs
test                           Run tests
```

To setup:
```
$ make setup
```

To run tests:
```
make test
```

To run the backend service:
```
make backend
```
