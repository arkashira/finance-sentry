# Dataflow Architecture for Finance-Sentry
==============================================

## External Data Sources
------------------------

*   **Transaction Feeds**: Financial institutions' APIs (e.g., SWIFT, ACH, Wire Transfer)
*   **Customer Data**: CRM systems (e.g., Salesforce, HubSpot)
*   **Regulatory Data**: Government databases (e.g., OFAC, FinCEN)
*   **Market Data**: Financial market data providers (e.g., Bloomberg, Quandl)

## Ingestion Layer
------------------

*   **API Gateway**: Handles incoming data from external sources (e.g., AWS API Gateway)
*   **Data Ingestion Service**: Collects and buffers data from various sources (e.g., Apache Kafka)
*   **Data Validation**: Ensures data quality and integrity (e.g., Apache Beam)

## Processing/Transform Layer
-----------------------------

*   **Data Processing Service**: Performs real-time processing and transformation of data (e.g., Apache Flink)
*   **Transaction Analysis**: Identifies suspicious transactions and generates alerts (e.g., custom Python scripts)
*   **Customer Profiling**: Creates customer profiles based on transaction history (e.g., scikit-learn)

## Storage Tier
----------------

*   **Data Warehouse**: Stores processed data for analytics and reporting (e.g., Amazon Redshift)
*   **NoSQL Database**: Stores real-time transaction data for fast lookup (e.g., MongoDB)
*   **Object Storage**: Stores large files and attachments (e.g., Amazon S3)

## Query/Serving Layer
------------------------

*   **Query Service**: Handles user queries and returns results (e.g., Apache Spark)
*   **API Gateway**: Exposes API endpoints for user interaction (e.g., AWS API Gateway)
*   **Authentication**: Verifies user credentials and authorizes access (e.g., OAuth 2.0)

## Egress to User
------------------

*   **User Interface**: Provides a web-based interface for users to interact with the system (e.g., React)
*   **Notification Service**: Sends alerts and notifications to users (e.g., email, SMS)
*   **Reporting**: Generates reports for users based on transaction data (e.g., Tableau)

### Auth Boundaries

*   **API Gateway**: Authenticates incoming requests and authorizes access to the system
*   **Query Service**: Verifies user credentials and authorizes access to data
*   **Notification Service**: Authenticates users before sending notifications

### ASCII Block Diagram
```
+---------------+
|  External    |
|  Data Sources  |
+---------------+
        |
        |  Ingestion Layer
        v
+---------------+
|  API Gateway  |
|  Data Ingestion|
|  Data Validation|
+---------------+
        |
        |  Processing/Transform Layer
        v
+---------------+
|  Data Processing|
|  Transaction    |
|  Analysis      |
|  Customer Profiling|
+---------------+
        |
        |  Storage Tier
        v
+---------------+
|  Data Warehouse|
|  NoSQL Database|
|  Object Storage |
+---------------+
        |
        |  Query/Serving Layer
        v
+---------------+
|  Query Service  |
|  API Gateway    |
|  Authentication |
+---------------+
        |
        |  Egress to User
        v
+---------------+
|  User Interface |
|  Notification   |
|  Reporting      |
+---------------+
```