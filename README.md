# Base Repository Structure

A production-grade FastAPI boilerplate with Google ADK multi-agent architecture. This project demonstrates best practices for building scalable AI agent systems with FastAPI, including layered services, repositories, and proper resource management.

**Version:** 0.1.0  
**Python:** 3.13+  
**Backend Framework:** FastAPI  
**Package Manager:** `uv` (Ultra-fast Python package installer)  
**AI Framework:** Google ADK (Agent Development Kit)

---

## 📋 Table of Contents

1. [Project Structure](#project-structure)
2. [Quick Start](#quick-start)
3. [UV Setup & Installation](#uv-setup--installation)
4. [Development](#development)
5. [Architecture](#architecture)
6. [Running the Application](#running-the-application)

---

## 📁 Project Structure

This project follows **production-grade FastAPI architecture** with clear separation of concerns and Google ADK agents integration. Copy this structure when starting new services:

```
base-repo-structure/
│
├── src/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                         # FastAPI application entry point
│   │   │
│   │   ├── api/                            # API routes/endpoints (v1 versioning)
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── dependencies.py         # Dependency injection helpers
│   │   │       └── routes/
│   │   │           ├── __init__.py
│   │   │           ├── agents.py
│   │   │           ├── jobs.py
│   │   │           └── health.py
│   │   │
│   │   ├── agents/                         # Google ADK Agents (multi-agent architecture)
│   │   │   ├── __init__.py
│   │   │   ├── base_agent.py               # Base class for all agents
│   │   │   │
│   │   │   ├── agent1/                     # Top-level Agent 1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── agent.py                # Main agent definition
│   │   │   │   ├── sub_agents/             # Sub-agents for Agent 1
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── sub_agent_1a.py
│   │   │   │   │   ├── sub_agent_1b.py
│   │   │   │   │   └── sub_agent_1c.py
│   │   │   │   ├── tools/                  # Tools for Agent 1
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── tool_1a.py
│   │   │   │   │   ├── tool_1b.py
│   │   │   │   │   └── tool_1c.py
│   │   │   │   └── shared_libraries/       # Shared code within Agent 1
│   │   │   │       ├── __init__.py
│   │   │   │       ├── utils.py
│   │   │   │       └── constants.py
│   │   │   │
│   │   │   └── agent2/                     # Top-level Agent 2
│   │   │       ├── __init__.py
│   │   │       ├── agent.py                # Main agent definition
│   │   │       ├── sub_agents/             # Sub-agents for Agent 2
│   │   │       │   ├── __init__.py
│   │   │       │   ├── sub_agent_2a.py
│   │   │       │   ├── sub_agent_2b.py
│   │   │       │   └── sub_agent_2c.py
│   │   │       ├── tools/                  # Tools for Agent 2
│   │   │       │   ├── __init__.py
│   │   │       │   ├── tool_2a.py
│   │   │       │   ├── tool_2b.py
│   │   │       │   └── tool_2c.py
│   │   │       └── shared_libraries/       # Shared code within Agent 2
│   │   │           ├── __init__.py
│   │   │           ├── utils.py
│   │   │           └── constants.py
│   │   │
│   │   ├── services/                       # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── agent_orchestration_service.py  # Orchestrates agents
│   │   │   ├── job_service.py
│   │   │   └── base_service.py
│   │   │
│   │   ├── repositories/                   # Data access abstraction layer
│   │   │   ├── __init__.py
│   │   │   ├── db/                         # SQLAlchemy database access
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base_repository.py
│   │   │   │   ├── agent_repository.py
│   │   │   │   └── job_repository.py
│   │   │   └── redis/                      # Redis cache access
│   │   │       ├── __init__.py
│   │   │       ├── cache_repository.py
│   │   │       ├── agent_cache_repository.py
│   │   │       └── session_cache_repository.py
│   │   │
│   │   ├── models/                         # SQLAlchemy ORM models (database schemas)
│   │   │   ├── __init__.py
│   │   │   ├── base_model.py
│   │   │   ├── agent.py
│   │   │   └── job.py
│   │   │
│   │   ├── schemas/                        # Pydantic models (API request/response)
│   │   │   ├── __init__.py
│   │   │   ├── base_schema.py
│   │   │   ├── agent.py
│   │   │   └── job.py
│   │   │
│   │   ├── core/                           # Core infrastructure
│   │   │   ├── __init__.py
│   │   │   ├── config.py                   # Configuration management
│   │   │   ├── database.py                 # SQLAlchemy setup
│   │   │   ├── redis_manager.py            # Redis connection manager
│   │   │   ├── logger.py                   # Logging configuration
│   │   │   ├── auth.py                     # Authentication logic
│   │   │   └── agent_runtime.py            # ADK agent runtime management
│   │   │
│   │   ├── common/                         # Shared utilities
│   │   │   ├── __init__.py
│   │   │   └── utils/
│   │   │       ├── __init__.py
│   │   │       ├── agent_helpers.py        # ADK helper utilities
│   │   │       ├── validators.py
│   │   │       └── constants.py
│   │   │
│   │   ├── middleware/                     # FastAPI middleware
│   │   │   ├── __init__.py
│   │   │   ├── logging_middleware.py
│   │   │   └── error_handler_middleware.py
│   │   │
│   │   ├── metadata/                       # Project metadata
│   │   │   ├── __init__.py
│   │   │   └── project_metadata.py
│   │   │
│   │   └── tools/                          # Shared tools/utilities
│   │       ├── __init__.py
│   │       └── shared_tools.py
│   │
│   ├── migrations/                         # Database migrations (Alembic) - Optional
│   │   ├── __init__.py
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── __init__.py
│   │
│   └── scripts/                            # Utility scripts - Optional
│       ├── __init__.py
│       ├── setup_db.py
│       └── seed_data.py
│
├── tests/                                  # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── test_agent1.py
│   │   └── test_agent2.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── test_agent_orchestration_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_agents_routes.py
│   └── repositories/
│       ├── __init__.py
│       └── test_repositories.py
│
├── .env.example                            # Example environment variables
├── .gitignore                              # Git ignore configuration
├── pyproject.toml                          # Project metadata & dependencies (UV)
├── uv.lock                                 # Locked dependency versions (auto-generated by UV)
└── README.md                               # This file

```

### Architecture Layers

```
API Routes (src/app/api/)
    ↓
Services (src/app/services/)
    ↓
Repositories (src/app/repositories/)
    ├── Database (src/app/repositories/db/)
    └── Cache (src/app/repositories/redis/)
```

### Models vs Schemas - Important Distinction

**This project uses TWO distinct concepts that are often confused:**

#### **Models** (`src/app/models/`) - Database Layer
- **SQLAlchemy ORM models** that map to database tables
- Represent your actual database schema
- Used for database queries and CRUD operations
- Example:
  ```python
  from sqlalchemy import Column, String, Integer
  from sqlalchemy.orm import declarative_base
  
  Base = declarative_base()
  
  class User(Base):
      __tablename__ = "users"
      id = Column(Integer, primary_key=True)
      email = Column(String, unique=True)
      name = Column(String)
  ```

#### **Schemas** (`src/app/schemas/`) - API Layer
- **Pydantic models** for request/response validation
- Define API data structures (what clients send/receive)
- NOT directly tied to database tables
- Example:
  ```python
  from pydantic import BaseModel
  
  class UserCreate(BaseModel):
      email: str
      name: str
  
  class UserResponse(BaseModel):
      id: int
      email: str
      name: str
  ```

#### **The Complete Flow**
```
API Request (JSON)
    ↓
Pydantic Schema validates input
    ↓
Service receives data
    ↓
SQLAlchemy Model maps to database
    ↓
Database stores data
    ↓
SQLAlchemy Model reads from database
    ↓
Pydantic Schema serializes response
    ↓
API Response (JSON)
```

**Key Rules:**
- ✅ Keep Models in `src/app/models/` (database schemas)
- ✅ Keep Schemas in `src/app/schemas/` (API contracts)
- ✅ Never use database models directly in API responses
- ✅ Always validate API input with Pydantic schemas

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.13+** installed
- **UV package manager** installed (see below)

### Setup in 3 Steps

```bash
# 1. Clone the repository
git clone <repository-url>
cd base-repo-structure

# 2. Install dependencies using UV
uv sync

# 3. Run the application
uv run uvicorn src.app.main:app --reload
```

The application will be available at `http://localhost:8000`

---

## 🔧 UV Setup & Installation

### What is UV?

**UV** is an ultra-fast Python package installer and resolver written in Rust. It's **10-100x faster** than pip and handles dependency resolution much better.

Benefits:
- ⚡ **Ultra-fast** dependency resolution and installation
- 🔒 **Deterministic** lock files for reproducible environments
- 📦 **Project management** without needing separate tools
- 🎯 **Built-in virtual environment** management

### Install UV

#### **Windows**

```bash
# Using PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv

# Or using scoop
scoop install uv

# Or using chocolatey
choco install uv
```

#### **macOS/Linux**

```bash
# Using curl (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using brew (macOS)
brew install uv

# Or using pip
pip install uv
```

#### **Verify Installation**

```bash
uv --version
# Output: uv 0.x.x
```

---

## 📦 Dependency Management with UV

### Understanding `pyproject.toml`

The `pyproject.toml` file defines your project's dependencies:

```toml
[project]
name = "venv"
version = "0.1.0"
description = "AI-powered automated job application system with FastAPI backend"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.118.0",
    "uvicorn>=0.37.0",
]

[tool.uv]
dev-dependencies = []
```

### Understanding `uv.lock`

The `uv.lock` file is **auto-generated** and contains:
- Exact versions of all dependencies
- All transitive dependencies (dependencies of dependencies)
- Hash checksums for security

**DO NOT manually edit `uv.lock`** - UV manages it automatically.

### Common UV Commands

#### **Install/Update Dependencies**

```bash
# Install all dependencies (creates virtual env if needed)
uv sync

# Sync with frozen lock file (CI/CD, exact reproduction)
uv sync --frozen

# Update dependencies to latest compatible versions
uv sync --upgrade
```

#### **Add New Dependency**

```bash
# Add a package
uv add package_name

# Add with version constraint
uv add "package_name>=1.0,<2.0"

# Add as dev dependency
uv add --dev pytest

# Add multiple packages
uv add fastapi sqlalchemy redis
```

#### **Remove Dependency**

```bash
uv remove package_name
```

#### **List Dependencies**

```bash
# Show installed packages
uv pip list

# Show with versions
uv pip show package_name
```

#### **Run Commands in Project Environment**

```bash
# Run any command in project environment
uv run uvicorn src.app.main:app --reload

# Run Python script
uv run python script.py

# Run pytest
uv run pytest

# Run CLI tools
uv run black .
uv run ruff check .
```

---

## 💻 Development

### Project Setup

```bash
# Clone and enter project
git clone <repository-url>
cd base-repo-structure

# Install all dependencies
uv sync

# Activate virtual environment (optional, uv run handles this)
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### Development Workflow

```bash
# 1. Install development dependencies
uv add --dev pytest pytest-asyncio

# 2. Run the app with auto-reload
uv run uvicorn src.app.main:app --reload

# 3. In another terminal, run tests
uv run pytest

# 4. Run linting
uv run ruff check .
uv run black --check .

# 5. Format code
uv run black .
uv run ruff check . --fix
```

### Virtual Environment Management

UV automatically creates a virtual environment in `.venv/` directory:

```bash
# Activate manually (optional)
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Deactivate
deactivate

# UV handles this automatically with uv run, so activation is optional
```

---

## 🏗️ Architecture

### Multi-Agent Architecture with FastAPI

This project combines **Google ADK (Agent Development Kit)** with **FastAPI layered service architecture** for production-grade AI agent systems:

#### **Agent Architecture - Multi-Agent Pattern**

```
┌─────────────────────────────────────────────┐
│         FastAPI Application                 │
├─────────────────────────────────────────────┤
│  API Routes (v1)                            │
│  ├── POST /api/v1/agents/run/{agent_name}  │
│  └── GET  /api/v1/jobs/{job_id}            │
├─────────────────────────────────────────────┤
│  AgentOrchestrationService                  │
│  └── Routes requests to correct agent       │
├─────────────────────────────────────────────┤
│  Google ADK Agents                          │
│  ├── Agent 1 (Top-level)                    │
│  │   ├── Sub-Agent 1a                       │
│  │   ├── Sub-Agent 1b                       │
│  │   ├── Sub-Agent 1c                       │
│  │   └── Tools & Libraries                  │
│  │                                           │
│  └── Agent 2 (Top-level)                    │
│      ├── Sub-Agent 2a                       │
│      ├── Sub-Agent 2b                       │
│      ├── Sub-Agent 2c                       │
│      └── Tools & Libraries                  │
├─────────────────────────────────────────────┤
│  Repositories Layer                         │
│  ├── Database (SQLAlchemy ORM)              │
│  └── Cache (Redis)                          │
└─────────────────────────────────────────────┘
```

#### **Key Agent Concepts**

1. **Base Agent** (`base_agent.py`)
   - Common initialization for all agents
   - Shared error handling and logging
   - Standard lifecycle management

2. **Top-Level Agents** (`agent1/`, `agent2/`)
   - Independent agents with their own configuration
   - Each can be deployed/scaled separately
   - Can specialize in different domains

3. **Sub-Agents** (`sub_agents/`)
   - Belong to a specific parent agent
   - Handle specialized tasks
   - Called by parent agent when needed

4. **Agent Tools** (`tools/`)
   - Specific tools for each agent
   - Can call external APIs/services
   - Handle specialized operations

### Layered Service Architecture

This project follows **production-grade architecture** with clear separation of concerns:

#### **1. API Routes Layer** (`src/app/api/`)
- Define HTTP endpoints
- Handle request/response serialization
- Validate input using Pydantic schemas
- **Dependency Injection** for services

```python
from fastapi import APIRouter, Depends
from src.app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
async def get_user(user_id: int, service: UserService = Depends()):
    return await service.get_user(user_id)
```

#### **2. Services Layer** (`src/app/services/`)
- Implement business logic
- Orchestrate repositories and external services
- Handle transactions and state management
- **Never** call repositories directly in routes

```python
from src.app.repositories.db.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    async def get_user(self, user_id: int):
        return await self.user_repo.get_by_id(user_id)
```

#### **3. Repository Layer** (`src/app/repositories/`)
- **Database Repositories** (`db/`) - SQLAlchemy ORM operations
- **Cache Repositories** (`redis/`) - Redis cache operations
- Abstract data access from services
- **MANDATORY** - Never access DB/Redis directly outside repositories

```python
from sqlalchemy.orm import Session
from src.app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    async def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
```

#### **4. Models & Schemas**
- **Models** (`src/app/models/`) - Pydantic data models
- **Schemas** (`src/app/schemas/`) - Pydantic request/response schemas

#### **5. Core Infrastructure** (`src/app/core/`)
- `config.py` - Configuration management
- `database.py` - SQLAlchemy setup
- `redis_manager.py` - Redis connection
- `logger.py` - Logging configuration
- `auth.py` - Authentication logic

### Design Patterns Used

1. **Repository Pattern** - All data access through repositories
2. **Dependency Injection** - Services injected via `Depends()`
3. **Singleton Pattern** - Shared services initialized once
4. **Async/Await** - Fully asynchronous operations
5. **Pydantic Models** - Type-safe data validation

---

## 🎯 Running the Application

### Development Mode

```bash
# With hot-reload
uv run uvicorn src.app.main:app --reload

# Specify port
uv run uvicorn src.app.main:app --reload --port 8001

# Specify host
uv run uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
# With multiple workers
uv run uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Access the Application

- **API**: `http://localhost:8000`
- **Interactive Docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`

---

## 📚 Adding Dependencies

### Adding FastAPI Extensions

```bash
# Database ORM
uv add sqlalchemy

# PostgreSQL driver
uv add psycopg2-binary

# Redis client
uv add redis

# Data validation
uv add pydantic pydantic-settings

# Environment variables
uv add python-dotenv

# Async HTTP client
uv add httpx
```

### Adding Development Dependencies

```bash
# Testing
uv add --dev pytest pytest-asyncio pytest-cov

# Code formatting
uv add --dev black ruff

# Type checking
uv add --dev mypy

# API documentation
uv add --dev mkdocs mkdocs-material
```

---

## 🔄 Workflow for Team Members

### First Time Setup

```bash
# 1. Clone repository
git clone <repository-url>
cd base-repo-structure

# 2. Install dependencies (creates .venv and installs exact versions from uv.lock)
uv sync

# 3. Ready to develop!
uv run uvicorn src.app.main:app --reload
```

### Daily Development

```bash
# Start your work session
uv run uvicorn src.app.main:app --reload

# Run tests in another terminal
uv run pytest

# When you add dependencies
uv add new_package_name

# Before committing (commit both pyproject.toml and uv.lock)
git add pyproject.toml uv.lock
git commit -m "Add new dependency"
```

### Pulling Latest Changes

```bash
# Pull from remote
git pull origin main

# Sync any dependency changes
uv sync

# Continue development
uv run uvicorn src.app.main:app --reload
```

---

## 🐳 Docker Deployment

### Dockerfile Example

```dockerfile
FROM python:3.13-slim

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src ./src

# Install dependencies with UV (frozen = exact versions)
RUN uv sync --frozen --no-dev

# Run application
CMD ["uv", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and Run

```bash
# Build image
docker build -t base-repo-structure .

# Run container
docker run -p 8000:8000 base-repo-structure
```

---

## 🆘 Troubleshooting

### UV Installation Issues

```bash
# Check UV is installed
uv --version

# Reinstall UV
pip install --upgrade uv

# Verify Python version
python --version  # Should be 3.13+
```

### Dependency Conflicts

```bash
# Clear and reinstall everything
rm -rf .venv
uv sync --fresh

# Or check for conflicts
uv pip check
```

### Lock File Out of Sync

```bash
# Regenerate lock file
rm uv.lock
uv sync

# Or update to latest compatible versions
uv sync --upgrade
```

### Module Import Errors

```bash
# Ensure you're using uv run
uv run python your_script.py

# Or activate the virtual environment
source .venv/bin/activate
python your_script.py
```

---

## 📖 References

- **UV Documentation**: https://docs.astral.sh/uv/
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Python 3.13**: https://www.python.org/downloads/release/python-3130/

---

## 📝 License

This project is proprietary and confidential.

---

## 🤝 Contributing

When contributing, follow these guidelines:

1. **Create a feature branch** for your changes
2. **Install dev dependencies**: `uv add --dev pytest black ruff`
3. **Run tests before committing**: `uv run pytest`
4. **Format code**: `uv run black . && uv run ruff check . --fix`
5. **Commit with clear messages** referencing issues/features
6. **Ensure `pyproject.toml` and `uv.lock` are committed** if dependencies changed

---

**Happy coding! 🚀**

