# Tech Spec: Finance Sentry v1
## Stack
- **Language**: Node.js (14.x)
- **Framework**: Express.js (4.x)
- **Runtime**: Docker (20.x) with Alpine Linux (3.x)
- **Database**: PostgreSQL (13.x) with TimescaleDB (2.x) for time-series data
- **Message Queue**: RabbitMQ (3.x) for asynchronous processing
- **Cache**: Redis (7.x) for session data and API rate limiting

## Hosting
- **Cloud Provider**: AWS (free-tier-first)
- **Platform**: Elastic Beanstalk (for Node.js)
- **Containerization**: Docker Hub (for image storage and deployment)

## Data Model
- **Transaction Table**:
  - `id` (UUID): unique transaction ID
  - `timestamp` (TIMESTAMP): transaction timestamp
  - `amount` (DECIMAL): transaction amount
  - `type` (VARCHAR): transaction type (e.g., deposit, withdrawal)
  - `status` (VARCHAR): transaction status (e.g., pending, completed)
- **Issue Table**:
  - `id` (UUID): unique issue ID
  - `transaction_id` (UUID): related transaction ID
  - `description` (TEXT): issue description
  - `status` (VARCHAR): issue status (e.g., open, closed)
- **User Table**:
  - `id` (UUID): unique user ID
  - `email` (VARCHAR): user email
  - `role` (VARCHAR): user role (e.g., admin, operations)

## API Surface
- **GET /transactions**: retrieve all transactions
- **GET /transactions/{id}**: retrieve a single transaction by ID
- **POST /transactions**: create a new transaction
- **GET /issues**: retrieve all issues
- **GET /issues/{id}**: retrieve a single issue by ID
- **POST /issues**: create a new issue
- **PUT /issues/{id}**: update an existing issue
- **DELETE /issues/{id}**: delete an existing issue
- **GET /users**: retrieve all users
- **GET /users/{id}**: retrieve a single user by ID
- **POST /users**: create a new user

## Security Model
- **Authentication**: JSON Web Tokens (JWT) with refresh tokens
- **Authorization**: Role-Based Access Control (RBAC) with user roles
- **Secrets**: environment variables with encrypted values
- **IAM**: AWS IAM roles for service accounts

## Observability
- **Logs**: CloudWatch Logs (for AWS) with log rotation and retention
- **Metrics**: Prometheus (for monitoring) with Grafana (for visualization)
- **Traces**: OpenTelemetry (for distributed tracing) with Jaeger (for visualization)

## Build/CI
- **Build Tool**: npm (for Node.js) with Docker (for containerization)
- **CI Tool**: GitHub Actions (for automated testing and deployment)
- **Test Framework**: Jest (for unit testing) with Cypress (for integration testing)
- **Code Quality**: ESLint (for code linting) with Prettier (for code formatting)