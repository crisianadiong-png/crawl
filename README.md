# Personal Finance Tracker

A full-stack personal finance management system that allows users to record, manage, and analyze their income and expenses.

## Features

* User registration and login
* Create, view, update, and delete income records
* Create, view, update, and delete expense records
* Organize transactions by categories
* Weekly and monthly financial reports
* Interactive charts and graphs
* Financial analysis dashboard
* CSV export
* Data analysis using Pandas and NumPy

## Technology Stack

### Frontend

* React
* Next.js
* Chart.js

### Backend

* FastAPI or Node.js

### Database

* PostgreSQL or MySQL

### ORM

* SQLAlchemy or Prisma

### Data Analysis

* Pandas
* NumPy
* Streamlit

## Project Structure

```text
personal-finance-tracker/
├── frontend/
├── backend/
├── database/
├── analytics/
├── README.md
├── PROJECT.md
├── ARCHITECTURE.md
├── DATABASE.md
├── API.md
├── TODO.md
├── CHANGELOG.md
└── CONTRIBUTING.md
```

## Main Workflow

```text
User
 ↓
Next.js Frontend
 ↓
Backend API
 ↓
SQLAlchemy / Prisma
 ↓
PostgreSQL / MySQL
 ↓
Financial Data
 ↓
Pandas / NumPy
 ↓
Streamlit Analytics
```

## Getting Started

Clone the project and install the required dependencies for the frontend, backend, and analytics components.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

Install the required backend dependencies and start the API server.

### Analytics

Start the Streamlit dashboard after configuring the database connection.

## Development Status

This project is currently under development.

See `TODO.md` for the current development tasks.
