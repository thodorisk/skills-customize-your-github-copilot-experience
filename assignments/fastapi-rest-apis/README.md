# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. You will define request and response models, implement endpoint logic, and add validation so your API can safely create, read, update, and delete resources.

## 📝 Tasks

### 🛠️ Define API models and setup

#### Description
Create Pydantic models for your API data and set up a FastAPI app with a collection of sample items.

#### Requirements
Completed program should:

- Define an `Item` model with `id`, `name`, `price`, and optional `description`.
- Define a `ItemCreate` model for incoming POST requests.
- Create a FastAPI app instance and a sample in-memory item list.
- Include a root endpoint `/` that returns a welcome message.

### 🛠️ Implement CRUD endpoints

#### Description
Add REST endpoints to create, read, update, and delete items.

#### Requirements
Completed program should:

- Add `GET /items` to return all items.
- Add `GET /items/{item_id}` to return a single item by `id`.
- Add `POST /items` to create a new item using `ItemCreate` and return the created item.
- Add `PUT /items/{item_id}` to update an existing item.
- Add `DELETE /items/{item_id}` to remove an item.
- Use proper HTTP status codes for success and failure.

### 🛠️ Add validation and error handling

#### Description
Make your API validate input data and return helpful error responses.

#### Requirements
Completed program should:

- Validate incoming request data with Pydantic.
- Return a 404 error when an item cannot be found.
- Return a 400 error when data is invalid or required fields are missing.
- Use clear response messages for errors.

### ⭐ Bonus: Search and filter items

#### Description
Add a query parameter to search items by name or to filter items by a maximum price.

#### Requirements
If implemented, the API should:

- Support `GET /items?search=...` to filter items by name.
- Support `GET /items?max_price=...` to filter items by price.
- Return filtered item results when query parameters are provided.
