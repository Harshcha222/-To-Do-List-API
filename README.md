# Todo Project

## Overview
This project is a Django-based application for managing tasks (Todos). It provides functionality to create, read, update, and delete Todo items using Django REST framework.

## Prerequisites
To run this project locally, you need:
- Python 3.6 or higher
- Django 5.0.6
- Django REST framework 3.15.2
- Git (for version control)

## Setup Instructions

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/Harshcha222/-To-Do-List-API.git
cd todo_project
```
### 2. Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage your project dependencies in isolation:

```bash
python -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
### 3. Install Dependencies
Install the required Python packages
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
Set up the database by applying migrations:
```bash
python manage.py migrate
```
### 5. 5. Create a Superuser
To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
### 6. Run the Development Server
Start the development server:
```bash
python manage.py runserver
```
### 7. Access the Application
Open your web browser and go to http://127.0.0.1:8000/ to view the application. The endpoints for managing Todos are:
## API Endpoints
## API Endpoints
## API Endpoints

- **GET /api/todos/** - Retrieve all to-do items
- **POST /api/todos/** - Create a new to-do item
- **PUT /api/todos/<id>/** - Update an existing to-do item by ID
- **DELETE /api/todos/<id>/** - Delete a to-do item by ID


### Usage Instructions
- **Retrieve All Tasks**: Send a GET request to `/api/todos/` to get a list of all to-do items.
- **Create Task**: Send a POST request to `/api/todos/` with JSON data including `title`, `description`, and `completed` fields.
- **Update Task**: Send a PUT request to `/api/todos/<id>/` with updated JSON data.
- **Delete Task**: Send a DELETE request to `/api/todos/<id>/` to remove a specific to-do item.


### Dependencies
Django==5.0.6

djangorestframework==3.15.2

sqlparse==0.5.0

### License
For any questions or feedback, please contact rchaturvedi087@gmail.com.
