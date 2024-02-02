# Django task

## Description

This project is a test assignment that involves the implementation of two models, `Team` and `Member`, with a Many-to-Many relationship. The project provides API endpoints for CRUD operations on these models.
___

## Prerequisites

- **Required**: Python 3.x, Docker
- **For pip method**: pip
- **For poetry method**: poetry
- **For Docker method**: only Docker
___
## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Olderestin/django_task1.git

2. Navigate to the project directory:
   ```bash
   cd django_task1

3. Create a .env file based on the provided example (<font color='red'>**don't forget to fill it**</font>):
   ```bash
   cp .env.example .env

___

## Method 1: Using pip

1. Install dependencies:
    ```bash
    pip install -r requirements.txt

2. Up the database with docker:
   ```bash
   docker compose -f docker-compose-local.yml up --build -d

3. Make migrations:
    ```bash
    python manage.py migrate

4.  Run the app:
    ```bash
    python manage.py runserver

___

## Method 2: Using Poetry

1. Install dependencies:
    ```bash
    poetry install

2. Up the database with docker:
   ```bash
   docker compose -f docker-compose-local.yml up --build -d

3. Make migrations:
    ```bash
    poetry run python manage.py migrate

4. Create superuser:
   ```bash
   poetry run python manage.py createsuperuser

5.  Run the app:
    ```bash
    poetry run python manage.py runserver

___

## Method 3: Using Docker

1. Build and run app with Docker container:
   ```bash
   docker compose up --build

2. Perform database migrations:
   ```bash
    docker exec -it django python manage.py migrate

3. Create superuser:
   ```bash
   docker exec -it django python manage.py createsuperuser

___
## Note:

- after using one of this methods you can find api documantation on this link [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/)