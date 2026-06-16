# TECH_SPEC.md – Finance‑Sentry  

**Version:** 1.0.0  
**Last Updated:** 2026‑06‑16  
**Owner:** Finance‑Sentry Product Team (AxentX)  

---  

## Table of Contents
1. [Overview](#overview)  
2. [Architecture Diagram](#architecture-diagram)  
3. [Core Components](#core-components)  
4. [Data Model](#data-model)  
5. [Key APIs & Interfaces](#key-apis--interfaces)  
6. [Technology Stack](#technology-stack)  
7. [External Dependencies](#external-dependencies)  
8. [Deployment & Operations](#deployment--operations)  
9. [Security & Compliance](#security--compliance)  
10. [Scalability & Performance](#scalability--performance)  
11. [Observability & Alerting](#observability--alerting)  
12. [CI/CD Pipeline](#cicd-pipeline)  
13. [Glossary](#glossary)  

---  

## Overview
Finance‑Sentry is a **real‑time transaction monitoring and automated issue‑resolution platform** for financial‑service providers (banks, PSPs, fintechs).  

* **Ingestion** – high‑throughput capture of transaction streams (ISO‑20022, SWIFT, ACH, internal APIs).  
* **Detection** – rule‑based and AI‑driven anomaly detection (fraud, compliance breaches, processing errors).  
* **Resolution** – automated ticket creation, suggested remediation actions via LLM, and workflow orchestration for human analysts.  
* **Visibility** – unified dashboard, REST/GraphQL APIs, and webhook integrations for downstream systems.  

The product is **revenue‑validated**: early‑stage pilots have shown a willingness‑to‑pay of $0.12 per transaction for monitoring + $2 per resolved ticket.

---  

## Architecture Diagram  

```
+-------------------+        +-------------------+        +-------------------+
|   Transaction     |  -->   |   Ingestion API   |  -->   |   Kafka (Events)  |
|   Sources (API,   |        |   (gRPC/REST)     |        |   (topic per env) |
|   File, DB)       |        +-------------------+        +-------------------+
+-------------------+                |                         |
                                      |                         |
                                      v                         v
                         +-------------------+        +-------------------+
                         |   Stream Processor|        |   Rule Engine     |
                         |   (Kafka Streams) |        |   (Drools)        |
                         +-------------------+        +-------------------+
                                      |                         |
                                      |                         |
                +---------------------+-------------------------+-------------------+
                |                     |                         |                   |
                v                     v                         v                   v
   +-------------------+   +-------------------+   +-------------------+   +-------------------+
   |   AI Detector     |   |   Alert Service   |   |   Ticket Engine   |   |   Notification Hub|
   |   (vLLM + SGLang) |   |   (Redis Cache)   |   |   (Temporal.io)   |   |   (Webhooks, SMTP)|
   +-------------------+   +-------------------+   +-------------------+   +-------------------+
                |                     |                         |
                |                     |                         |
                v                     v                         v
          +---------------------------------------------------------------+
          |                     PostgreSQL (Core DB)                      |
          |  Tables: transaction, alert, ticket, customer, account, audit |
          +---------------------------------------------------------------+
                |
                v
          +-------------------+
          |   API Gateway     |
          | (Kong + OIDC)     |
          +-------------------+
                |
                v
          +-------------------+
          |   Front‑end UI    |
          | (React + TypeScript) |
          +-------------------+
```

---  

## Core Components  

| Component | Responsibility | Implementation Details |
|-----------|----------------|------------------------|
| **Ingestion API** | Securely receive transaction payloads (JSON, protobuf, CSV). | gRPC + HTTP/REST (Go 1.22). Rate‑limit per client via Kong. |
| **Kafka Cluster** | Durable, ordered event log. | 3‑node Confluent‑compatible cluster, replication factor 3, topic per environment (dev, staging, prod). |
| **Stream Processor** | Normalise, enrich, and forward events. | Kafka Streams (Java 21) – stateless transformations + schema registry (Avro). |
| **Rule Engine** | Deterministic checks (AML, KYC, threshold limits). | Drools 8.38, rules authored in DRL, hot‑reload via Zookeeper watcher. |
| **AI Detector** | Probabilistic anomaly scoring & suggested remediation. | vLLM (GPU‑accelerated inference) serving a fine‑tuned LLM (Finance‑Sentry‑LLM, 7B). Structured response generation via SGLang. |
| **Alert Service** | Persist alerts, de‑duplicate, expose real‑time feed. | Redis 7 (Streams) for low‑latency fan‑out, TTL 48 h. |
| **Ticket Engine** | Create, route, and track resolution tickets. | Temporal.io workflow orchestration (Go SDK). SLA timers, escalation policies. |
| **Notification Hub** | Push alerts to external systems & analysts. | Webhook dispatcher, SMTP, Slack bot. |
| **Core DB** | Authoritative store for
