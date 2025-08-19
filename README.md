# 🍲 EthioFlavor API

EthioFlavor API is a backend service built with Django and Django REST Framework to manage and share Ethiopian recipes. It provides a robust platform for users to create, update, and explore recipes by category, ingredients, and preparation time. The API is designed with scalability, security, and usability in mind, simulating a real-world recipe management system.

## 🚀 Features

- **User Authentication**: Secure login and registration using Django's built-in auth system (JWT optional).
- **Recipe CRUD**: Create, read, update, and delete recipes with detailed fields like ingredients, instructions, and cooking time.
- **Category & Ingredient Filtering**: View recipes by category or ingredient, with support for multi-ingredient filtering.
- **Search & Pagination**: Search recipes by title, category, or prep time, with pagination and sorting for large datasets.
- **Permissions**: Authenticated users can only modify their own recipes.

## 🧱 Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  
- SQLite (default, can be swapped for PostgreSQL)  
- JWT Authentication (optional)  
- Deployed via Heroku or PythonAnywhere

## 📦 Setup Instructions

```bash
git clone https://github.com/RedietSeleshiTsega/EthioFlavor-api.git
cd EthioFlavor-api
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

## 📬 API Endpoints (Sample)

- `POST /api/users/register/` – Register a new user  
- `POST /api/users/login/` – Login and receive token  
- `GET /api/recipes/` – List all recipes  
- `POST /api/recipes/` – Create a new recipe (auth required)  
- `GET /api/recipes/?category=Dessert` – Filter by category  
- `GET /api/recipes/?ingredient=chicken` – Filter by ingredient

