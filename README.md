# Context
Build a RESTfull API to manage an online library. This API shoul handle **books** and **authors** with basic CRUD functions.

# Specifications
## Models
```
Author:
    id: Unique Identifier (automatic)
    name: Author name (string)

Book:
    id: Unique Identifier (automatic)
    title: Book's title (string)
    author: Foreign key to author (many-to-one relationship)
```
## Endpoints
1. Authors:
    - `GET /authors/: Authors' list`
    - `POST /authors/: Add a new author`
2. Books:
    - `GET /books/: Books' list`
    - `POST /books/: Add a new book`

## Instructions
1. Create Django's models
    - Create models `Author` and `Book` with specified attributes
2. Migrations
    - Create and apply migrations for both models.
3. Serializers
    - Create serializers for both models (`Author` and `Book`)
4. Views and routes
    - Use DRF to create corresponding views and routes for each endpoint
5. Validation
    - Add basic validation with serializers
6. Tests
    - Write unit tests with Pytest for main endpoints to check if CRUD operations works has expected

# Bonus
1. Pagination: add a pagination for `Authors` and `Books`
2. Documentation: add a documentation of the API with your preferred method
3. Authentication: add a simple authentatication method to secure the API

# How to run the API
## Requirements
- Python 3.12
- Poetry
- Tox
- Docker

Add an `.env` file to the root of the project (see `env.example`).

## Commands
- lint/format check: `tox -e lint`
- run the API: `tox -e start` (automatically apply migrations)
- run tests: `tox -e py312`
- make migrations: once the dev stack is up run `tox -e makemigrations`

## API documentation:
- documentation: http://0.0.0.0:8000/api/schema/swagger-ui/
