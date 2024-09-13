# Todo Project

## Overview
A Django-based API for managing tasks (Todos). It allows you to create, read, update, and delete Todo items.

## Prerequisites
- Python 3.6 or higher
- Django 5.0.6
- Django REST framework 3.15.2

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/todo_project.git
    cd todo_project
    ```

2. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    ```
    **Activate the virtual environment:**

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7. **Test the API**
    Use Postman or cURL to test the following endpoints:

    - **Retrieve All Todos**: `GET /todos/`
    - **Create a New Todo**: `POST /todos/` with JSON body
    - **Update a Todo**: `PUT /todos/<id>/` with JSON body
    - **Delete a Todo**: `DELETE /todos/<id>/`

## Dependencies
- Django==5.0.6
- djangorestframework==3.15.2
- ipdb==0.13.13
- ipython==8.26.0
- sqlparse==0.5.0
