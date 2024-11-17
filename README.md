# Dynein - Unified Restaurant Management Platform

## Overview
Dynein is a comprehensive restaurant management platform that unifies dine-in service and takeout management operations using FastAPI backend and Astro.js frontend.

## Project Structure

### Domain Layer (`app/domain/`)
Contains the core business logic and rules:
- `entities/` - Core business objects
  - `order.py` - Order management entities
  - `menu.py` - Menu and item entities
  - `table.py` - Table management entities
  - `inventory.py` - Inventory tracking entities
  - `user.py` - User and role entities
- `events/` - Domain events for system integration
- `value_objects/` - Immutable value objects

### Application Layer (`app/application/`)
Orchestrates the flow of data and domain objects:
- `services/` - Business logic implementation
  - `order_service.py` - Order processing logic
  - `table_service.py` - Table management logic
  - `kitchen_service.py` - Kitchen operations
  - `inventory_service.py` - Inventory management
- `interfaces/` - Abstract interfaces and protocols

### Infrastructure Layer (`app/infrastructure/`)
Handles external concerns and implementations:
- `database/` - Database implementations
  - `models/` - SQLAlchemy models
  - `repositories/` - Data access implementations
  - `session.py` - Database session management
- `messaging/` - Event handling system
- `external/` - External service integrations

### API Layer (`app/api/`)
Handles HTTP requests and responses:
- `v1/routers/` - API endpoints
  - `orders.py` - Order management endpoints
  - `tables.py` - Table management endpoints
  - `kitchen.py` - Kitchen operations endpoints
  - `inventory.py` - Inventory management endpoints
- `middleware/` - API middleware components

### Core (`app/core/`)
Core system configurations:
- `config.py` - Application configuration
- `exceptions.py` - Custom exceptions
- `logging.py` - Logging configuration

## Technology Stack
- Backend: FastAPI
- Database: PostgreSQL via SQLAlchemy
- Frontend: Astro.js
- Authentication: JWT
- API Documentation: OpenAPI/Swagger

## Setup and Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Node.js 16+

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
.\venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt
