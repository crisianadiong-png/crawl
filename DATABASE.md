# Database Design

## 1. Database Overview

The Personal Finance Tracker uses a relational database to store users, financial transactions, and categories.

Recommended database:

**PostgreSQL**

Recommended ORM:

**SQLAlchemy**

## 2. Main Tables

The initial database consists of:

```text
users
categories
transactions
```

## 3. Users Table

Stores user account information.

| Column        | Type      | Description           |
| ------------- | --------- | --------------------- |
| id            | INTEGER   | Primary key           |
| username      | VARCHAR   | User's username       |
| email         | VARCHAR   | User's email          |
| password_hash | VARCHAR   | Hashed password       |
| created_at    | TIMESTAMP | Account creation date |

## 4. Categories Table

Stores transaction categories.

| Column  | Type    | Description       |
| ------- | ------- | ----------------- |
| id      | INTEGER | Primary key       |
| user_id | INTEGER | Owner of category |
| name    | VARCHAR | Category name     |
| type    | VARCHAR | Income or expense |

## 5. Transactions Table

Stores financial transactions.

| Column           | Type      | Description                  |
| ---------------- | --------- | ---------------------------- |
| id               | INTEGER   | Primary key                  |
| user_id          | INTEGER   | User who created transaction |
| category_id      | INTEGER   | Transaction category         |
| type             | VARCHAR   | Income or expense            |
| amount           | DECIMAL   | Transaction amount           |
| description      | TEXT      | Transaction description      |
| transaction_date | DATE      | Date of transaction          |
| created_at       | TIMESTAMP | Record creation date         |

## 6. Relationships

```text
Users
 │
 ├──────────< Categories
 │
 └──────────< Transactions
                  │
                  ▼
             Categories
```

One user can have many categories.

One user can have many transactions.

One category can contain many transactions.

## 7. Important Rules

### Users

* Email should be unique.
* Passwords must never be stored as plain text.

### Transactions

* Amount must be greater than zero.
* Every transaction must belong to a user.
* A transaction should have a valid category.
* Transaction type must be either `income` or `expense`.

### Categories

Category type should match the transaction type.

For example:

```text
Salary → income
Food → expense
Transportation → expense
```

## 8. Example Transaction

```text
Transaction
-------------------------
ID: 102
User: 1
Category: Food
Type: expense
Amount: 250.00
Description: Lunch
Date: 2026-10-06
```

## 9. Future Tables

The following tables may be added later:

```text
budgets
savings_goals
recurring_transactions
financial_goals
```

These should only be implemented when the core system is stable.
