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

```bash
git clone <your-repo-url>
cd Python_MathApp
cp .env.example .env   # Then edit .env and set your real secrets/config values
docker-compose up --build