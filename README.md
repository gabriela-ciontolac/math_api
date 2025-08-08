# Math Microservice

A **production-ready microservice** for advanced mathematical computations (power, Fibonacci, factorial) built with **FastAPI**, **PostgreSQL**, **Redis**, **Kafka**, **Prometheus**, **Grafana**, and secured with **JWT authentication**. Designed for extensibility, observability, and modern DevOps workflows.

---

## Features

- **REST API**: Endpoints for mathematical operations (`pow`, `fibonacci`, `factorial`)
- **Persistence**: All API requests/results stored in PostgreSQL
- **Caching**: Redis for fast repeated calculations
- **Authorization**: JWT Bearer authentication for all endpoints
- **Monitoring**: Prometheus metrics & Grafana dashboards
- **Logging**: Async event logging to Kafka (with Kafdrop UI)
- **Containerized**: Easily deployable with Docker Compose
- **Extensible**: Clean MVC structure, ready for scaling and more endpoints

---

## Project Structure

math-microservice/
│
├── app/
│ ├── api/ # API route controllers
│ ├── auth/ # JWT authentication logic
│ ├── cache/ # Redis caching logic
│ ├── database/ # DB connection/session management
│ ├── logging/ # Kafka logging utilities
│ ├── metrics/ # Prometheus custom metrics
│ ├── models/ # SQLAlchemy models
│ ├── schemas/ # Pydantic request/response models
│ ├── services/ # Business logic (math functions, caching, etc.)
│ └── main.py # FastAPI app entrypoint
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic/ # DB migrations (Alembic)
├── prometheus.yml
├── README.md
└── .env # Environment configuration (not committed)

---

## Requirements

- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- Python 3.12+ (for dev/testing)
- (Optional) [Make](https://www.gnu.org/software/make/) for workflow scripts

---

## Quick Start

git clone https://github.com/gabriela-ciontolac/math_api.git
cd Python_MathApp
cp .env.example .env   # Then edit .env and set your real secrets/config values
docker-compose up --build

---

## Service URLs
- API Docs (Swagger UI): http://localhost:8000/docs
- Grafana: http://localhost:3000 (admin/admin)
- Prometheus: http://localhost:9090
- Kafdrop (Kafka UI): http://localhost:9000

---

## Environment Configuration (.env)

DB_HOST=host.docker.internal
DB_PORT=5433
DB_NAME=math_db
DB_USER=math_user
DB_PASSWORD=math_pass
REDIS_HOST=redis
REDIS_PORT=6379
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
KAFKA_LOG_TOPIC=logtopic
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
Note: For Docker Compose, use REDIS_HOST=redis and KAFKA_BOOTSTRAP_SERVERS=kafka:9092.

---

## API Usage
All endpoints are protected by JWT.

---

## 1. Get a JWT Token
POST /token
Body (application/x-www-form-urlencoded):
  username=mathuser
  password=strongpassword

Response:
{
  "access_token": "<TOKEN>",
  "token_type": "bearer"
}

Use this token as Bearer <TOKEN> in the Authorize button in Swagger UI or in your API client.

---

## 2. Endpoints
POST /pow
{
  "base": 2,
  "exp": 3
}
Response: { "result": 8.0 }

POST /fibonacci
{
  "n": 7
}
Response: { "result": 13 }

POST /factorial
{
  "n": 5
}
Response: { "result": 120 }

---

## Observability

Metrics: Exposed at /metrics (Prometheus scrapes this endpoint)

Grafana: Pre-configured dashboard templates for latency, request count, and more

Kafka Logging: Every API operation logs an event to logtopic, viewable in Kafdrop

---

## Database Migrations (Alembic)

For schema changes:
alembic revision --autogenerate -m "Describe change"
alembic upgrade head
Alembic is already configured for PostgreSQL via .env.

---

## Docker & Compose

To build and run everything:
docker-compose up --build

To stop and clean up:
docker-compose down -v
