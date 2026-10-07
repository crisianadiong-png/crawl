# System Architecture

## 1. Architecture Overview

The Personal Finance Tracker uses a full-stack architecture consisting of:

```text
┌─────────────────────────┐
│       User / Browser    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Next.js + React         │
│ Frontend                │
│                         │
│ Chart.js                │
└────────────┬────────────┘
             │ HTTP / REST API
             ▼
┌─────────────────────────┐
│ FastAPI / Node.js       │
│ Backend                 │
│                         │
│ Authentication          │
│ Business Logic          │
│ Validation              │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ SQLAlchemy / Prisma     │
│ ORM                     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ PostgreSQL / MySQL      │
│ Database                │
└─────────────────────────┘

             │
             ▼
┌─────────────────────────┐
│ Pandas + NumPy          │
│ Data Processing         │
└────────────┬────────────┘
             ▼
┌─────────────────────────┐
│ Streamlit               │
│ Analytics Dashboard     │
└─────────────────────────┘
```

## 2. Frontend

The frontend is responsible for the user interface and user interaction.

### Technologies

* React
* Next.js
* TypeScript
* Chart.js

### Responsibilities

* Display financial information
* Provide forms for transactions
* Handle user interaction
* Display reports
* Display charts
* Communicate with the backend API

## 3. Backend

The backend provides the API and handles application logic.

The project can use either:

* FastAPI
* Node.js

FastAPI is recommended if Python will also be heavily used for the data analysis component.

### Responsibilities

* Authentication
* API endpoints
* Request validation
* Business logic
* Database operations
* Financial calculations
* User authorization

## 4. Database Layer

The database stores persistent application data.

Supported options:

* PostgreSQL
* MySQL

The ORM can be:

* SQLAlchemy
* Prisma

For a Python-based backend, SQLAlchemy is recommended.

## 5. Analytics Layer

The analytics component processes financial data using:

* Pandas
* NumPy
* Streamlit

Pandas handles data manipulation while NumPy can be used for numerical calculations.

Streamlit provides a separate dashboard for deeper financial analysis.

## 6. Data Flow

A typical transaction follows this process:

```text
User enters expense
        ↓
Next.js form
        ↓
API request
        ↓
Backend validation
        ↓
ORM
        ↓
Database
        ↓
Response
        ↓
Frontend updates
```

## 7. Analytics Flow

```text
Database
    ↓
Financial records
    ↓
Pandas
    ↓
Data cleaning
    ↓
Data transformation
    ↓
NumPy calculations
    ↓
Financial analysis
    ↓
Streamlit dashboard
```

## 8. Recommended Architecture

For this project, the recommended combination is:

```text
Next.js
    +
FastAPI
    +
PostgreSQL
    +
SQLAlchemy
    +
Pandas
    +
NumPy
    +
Streamlit
```

This keeps the main application and analytics components primarily within the Python ecosystem while still using Next.js for the frontend.
