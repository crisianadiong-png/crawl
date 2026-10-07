# API Documentation

## 1. API Overview

The backend provides a REST API used by the Next.js frontend.

Base URL:

```text
/api
```

## 2. Authentication

### Register

```http
POST /api/auth/register
```

Creates a new user account.

Request:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

### Login

```http
POST /api/auth/login
```

Authenticates a user.

Request:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

## 3. Transactions

### Get Transactions

```http
GET /api/transactions
```

Returns the authenticated user's transactions.

### Get Transaction

```http
GET /api/transactions/{id}
```

Returns a specific transaction.

### Create Transaction

```http
POST /api/transactions
```

Request:

```json
{
  "category_id": 1,
  "type": "expense",
  "amount": 250.00,
  "description": "Lunch",
  "transaction_date": "2026-10-06"
}
```

### Update Transaction

```http
PUT /api/transactions/{id}
```

Updates an existing transaction.

### Delete Transaction

```http
DELETE /api/transactions/{id}
```

Deletes a transaction.

## 4. Categories

### Get Categories

```http
GET /api/categories
```

Returns the user's categories.

### Create Category

```http
POST /api/categories
```

Creates a new category.

Request:

```json
{
  "name": "Food",
  "type": "expense"
}
```

### Update Category

```http
PUT /api/categories/{id}
```

Updates a category.

### Delete Category

```http
DELETE /api/categories/{id}
```

Deletes a category.

## 5. Reports

### Monthly Report

```http
GET /api/reports/monthly?year=2026&month=10
```

Returns financial information for a specific month.

Example response:

```json
{
  "total_income": 25000,
  "total_expenses": 12500,
  "net_balance": 12500
}
```

### Weekly Report

```http
GET /api/reports/weekly
```

Returns the user's weekly financial summary.

## 6. Analytics

### Spending by Category

```http
GET /api/analytics/spending-by-category
```

Returns expense totals grouped by category.

Example:

```json
{
  "Food": 3500,
  "Transportation": 1800,
  "Bills": 4200
}
```

## 7. CSV Export

```http
GET /api/export/transactions
```

Returns the user's transactions as a CSV file.

Pandas can be used on the backend to generate the CSV.

## 8. Response Status Codes

| Status | Meaning            |
| ------ | ------------------ |
| 200    | Request successful |
| 201    | Resource created   |
| 400    | Invalid request    |
| 401    | Unauthorized       |
| 403    | Forbidden          |
| 404    | Resource not found |
| 500    | Server error       |

## 9. API Design Principle

The frontend should communicate with the backend through the API instead of directly accessing the database.

```text
Frontend → API → Backend → Database
```

The frontend should never contain database credentials.
