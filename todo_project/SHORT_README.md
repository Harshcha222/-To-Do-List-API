# Todo Project

A Django API for managing tasks (Todos). Supports creating, reading, updating, and deleting Todo items.

## Prerequisites
- Python 3.6+
- Django 5.0.6
- Django REST framework 3.15.2

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Harshcha222/-To-Do-List-API.git
    cd todo_project
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints
- `GET /todos/` - Retrieve all Todos
- `POST /todos/` - Create a new Todo
- `PUT /todos/<id>/` - Update a Todo
- `DELETE /todos/<id>/` - Delete a Todo

## Dependencies
- Django==5.0.6
- djangorestframework==3.15.2
