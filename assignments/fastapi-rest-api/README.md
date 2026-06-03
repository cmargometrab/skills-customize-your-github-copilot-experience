# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework by defining routes, request/response models, and handling CRUD operations.

## 📝 Tasks

### 🛠️ Define API Models and Endpoints

#### Description
Create a FastAPI application that defines a data model for items and exposes API endpoints to work with those items.

#### Requirements
Completed program should:

- Use FastAPI to create the app instance
- Define a Pydantic `Item` model with fields such as `id`, `name`, `description`, and `price`
- Add a `GET /items` endpoint that returns a list of items
- Add a `GET /items/{item_id}` endpoint that returns a single item by ID

### 🛠️ Implement CRUD Operations

#### Description
Expand the API so users can create, update, and delete items using standard HTTP methods.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint to create a new item
- Add a `PUT /items/{item_id}` endpoint to update an existing item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Store items in an in-memory list or dictionary for simplicity

### 🛠️ Add Validation and API Documentation

#### Description
Improve the API by validating input data, using descriptive responses, and taking advantage of FastAPI's automatic docs.

#### Requirements
Completed program should:

- Validate input data using Pydantic types and field constraints
- Return clear error responses when an item is not found
- Use descriptive response models where appropriate
- Verify the API documentation is available at `/docs` or `/redoc` when the server is running
