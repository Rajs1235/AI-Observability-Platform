# AI Observability Platform

An AI-powered observability platform for intelligent log analysis, system metrics monitoring, semantic log understanding, and anomaly detection using Machine Learning and Natural Language Processing.

> 🚧 **Status:** Active Development

---

# Overview

Modern distributed systems continuously generate application logs and infrastructure metrics. Identifying failures, performance degradation, and recurring incidents from this data using traditional rule-based monitoring is difficult.

This project aims to build a production-oriented AI observability platform capable of collecting, processing, analyzing, and learning from application logs and system metrics in real time.

The long-term vision is to combine modern Software Engineering, NLP, Machine Learning, Deep Learning, and MLOps into an intelligent observability system capable of:

- Detecting anomalous logs and system metrics
- Understanding log semantics
- Retrieving similar historical incidents
- Predicting failures before they occur
- Assisting with root cause analysis
- Supporting production-scale deployment

---

# Architecture

```text
                    Running Application
                            │
                     Python Logging
                            │
                            ▼
                    Log Generator
                            │
                            ▼
                     File Watcher
                            │
                            ▼
                 Log Processing Service
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
     SQLite Database                    Drain3 Engine
          │                                   │
          └─────────────────┬─────────────────┘
                            ▼
                     FastAPI Backend
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
      Logs API        Templates API     Analytics API
                            │
                            ▼
                AI / ML Processing Layer
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
    Metrics Models     NLP Models      Future Deep Learning
                            │
                            ▼
                   React Dashboard (WIP)
```

---

# Features

## Log Collection

- ✅ Synthetic log generation
- ✅ Live log monitoring
- ✅ File watching
- ✅ Structured log parsing
- ✅ SQLite persistence

---

## Log Intelligence

- ✅ Automatic template extraction using Drain3
- ✅ Log clustering
- ✅ Template analytics
- ✅ Structured template storage

---

## Metrics Monitoring

- ✅ CPU monitoring
- ✅ Memory monitoring
- ✅ Disk monitoring
- ✅ Network monitoring
- ✅ Process monitoring

---

## Backend APIs

- ✅ FastAPI backend
- ✅ Logs API
- ✅ Templates API
- ✅ Analytics API

---

# Machine Learning

## Metrics Pipeline

Completed:

- Feature Engineering
- Exploratory Data Analysis
- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- Elliptic Envelope
- DBSCAN
- PCA Visualization
- Model Comparison
- Model Serialization

---

## Logs NLP Pipeline

Completed:

- Exploratory Data Analysis
- Feature Engineering
- TF-IDF Vectorization
- Isolation Forest Baseline
- Sentence Transformer Embeddings (all-MiniLM-L6-v2)
- Isolation Forest on Transformer Embeddings
- PCA Visualization
- Anomaly Visualization
- Model Serialization

---

## Current Work

- 🚧 Semantic Search
- 🚧 Similar Incident Retrieval
- 🚧 FAISS Integration

---

# Tech Stack

## Backend

- Python
- FastAPI

## Database

- SQLite

## Log Processing

- Drain3

## Machine Learning

- Scikit-learn
- Isolation Forest
- One-Class SVM
- Local Outlier Factor
- Elliptic Envelope
- DBSCAN

## NLP

- Sentence Transformers
- TF-IDF
- Hugging Face Transformers
- FAISS *(Planned)*

## Data Processing

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Model Serialization

- Joblib

## Frontend

- React
- Tailwind CSS

## Deployment

- Docker *(Planned)*

---

# Project Roadmap

## Phase 1 — Data Collection ✅

- [x] Project setup
- [x] Synthetic log generator
- [x] File watcher
- [x] Log parser
- [x] SQLite repositories
- [x] Metrics collector
- [x] FastAPI backend

---

## Phase 2 — Data Preparation ✅

- [x] Dataset preprocessing
- [x] Feature engineering
- [x] Exploratory Data Analysis
- [x] Template extraction using Drain3
- [x] Dataset cleaning

---

## Phase 3 — Metrics Anomaly Detection ✅

- [x] Isolation Forest
- [x] One-Class SVM
- [x] Local Outlier Factor
- [x] Elliptic Envelope
- [x] DBSCAN
- [x] PCA Visualization
- [x] Model Serialization

---

## Phase 4 — Log Intelligence & NLP ✅

- [x] TF-IDF Vectorization
- [x] Isolation Forest Baseline
- [x] Sentence Transformer Embeddings
- [x] Transformer-based Anomaly Detection
- [x] PCA Visualization
- [x] Model Serialization

---

## Phase 5 — Semantic Retrieval 🚧

- [ ] Semantic Search
- [ ] Similar Incident Retrieval
- [ ] FAISS Indexing

---

## Phase 6 — Deep Learning 🚧

- [ ] DeepLog Implementation
- [ ] Log Sequence Modeling
- [ ] Next Event Prediction
- [ ] Failure Prediction

---

## Phase 7 — Production Platform 🚧

- [ ] React Dashboard
- [ ] Real-time Inference
- [ ] Prometheus Integration
- [ ] Docker Deployment
- [ ] MLflow Integration
- [ ] BentoML Deployment
- [ ] AI-assisted Root Cause Analysis

---

# Repository Structure

```text
AI-Observability-Platform/

├── backend/
├── collector/
├── config/
├── database/
├── docker/
├── frontend/
├── parser/
├── preprocessing/
├── services/
├── Training/
│   ├── Metricstraining.ipynb
│   ├── Logstrain.ipynb
│   └── models/
│       ├── metrics/
│       └── logs/
├── tests/
├── utils/
├── generate_logs.py
├── view_logs.py
└── README.md
```

---

# Datasets

The platform combines **synthetic datasets** with **public benchmark datasets** to evaluate anomaly detection models across different environments.

## Synthetic Datasets

Generated by the platform.

### Application Logs

- 15,000+ structured log entries
- Generated using a custom synthetic log generator
- Parsed and clustered using Drain3

### System Metrics

Collected continuously using the metrics collector.

Includes:

- CPU utilization
- Memory utilization
- Disk utilization
- Network I/O
- Process count

These datasets are used for:

- Feature Engineering
- Exploratory Data Analysis
- Machine Learning
- Anomaly Detection

---

## Public Benchmark Datasets

Public datasets from **LogHub** are used to improve robustness and evaluate NLP models.

Current datasets include:

- Linux
- Apache
- HDFS
- Hadoop
- Mac
- HealthApp

These datasets support:

- Template Extraction
- Semantic Log Analysis
- Log Clustering
- Anomaly Detection Benchmarking
- Cross-System Generalization

> **Note:** Due to their size, generated datasets are not included in this repository. Synthetic datasets can be regenerated using the provided scripts, while public benchmark datasets can be downloaded from the LogHub project.

---

# Current Progress

| Module | Status |
|---------|--------|
| Log Collection | ✅ Complete |
| Metrics Collection | ✅ Complete |
| FastAPI Backend | ✅ Complete |
| Drain3 Template Mining | ✅ Complete |
| Feature Engineering | ✅ Complete |
| Exploratory Data Analysis | ✅ Complete |
| Metrics ML Pipeline | ✅ Complete |
| Logs NLP Pipeline | ✅ Complete |
| Model Serialization | ✅ Complete |
| Semantic Search | 🚧 In Progress |
| FAISS Integration | 🚧 Planned |
| DeepLog | 🚧 Planned |
| Dashboard | 🚧 Planned |
| Production Deployment | 🚧 Planned |

---

# Future Enhancements

- Semantic Log Retrieval
- FAISS Vector Search
- DeepLog Sequence Learning
- Failure Prediction
- Root Cause Analysis
- AI-assisted Troubleshooting
- Unified Log & Metrics Incident Scoring
- LLM-powered Incident Explanation
- Production-grade Observability Dashboard

---

# License

This project is intended for educational and research purposes.