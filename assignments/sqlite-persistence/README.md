# 📘 Assignment: Python Data Persistence with SQLite

## 🎯 Objective

Build a Python application that uses SQLite to store and manage data persistently, while practicing SQL table creation and CRUD operations.

## 📝 Tasks

### 🛠️ Create the Database and Table

#### Description
Set up a SQLite database and create a table to store items with specific fields.

#### Requirements
Completed program should:

- Use Python's `sqlite3` module to connect to a database file
- Create a table with columns for `id`, `name`, `quantity`, and `price`
- Ensure the table is created if it does not already exist
- Use `INTEGER`, `TEXT`, and `REAL` column types appropriately

### 🛠️ Implement CRUD Operations

#### Description
Build functions to create, read, update, and delete records in the SQLite table.

#### Requirements
Completed program should:

- Add a new item to the database using an `INSERT` statement
- Retrieve a single item by `id` using a `SELECT` statement
- List all items from the database
- Update an existing item using an `UPDATE` statement
- Delete an item by `id` using a `DELETE` statement

### 🛠️ Add User Interaction and Validation

#### Description
Create a simple command-line interface so users can interact with the database safely.

#### Requirements
Completed program should:

- Present a menu or functions for the user to choose actions
- Prompt the user for item details when creating or updating records
- Display clear messages when items are created, updated, deleted, or not found
- Handle invalid input gracefully without crashing the program
