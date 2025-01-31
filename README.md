# Order-management-system

## Tech Stack

Backend: Django + DRF (Python)

Database: PostgreSQL

Auth: OpenID Connect

Messaging: Africa's Talking SMS

CI/CD: GitHub Actions

Deployment: Docker

## Features

Manage customers & orders

Auth via OpenID Connect

SMS alerts via Africa’s Talking

Unit tests & CI/CD automation

## To review code

git clone https://github.com/edah-hub1/Order-management-system.git

cd savanna_backend

python -m venv env && env/Scripts/activate

pip install -r requirements.txt

python manage.py migrate && python manage.py createsuperuser

python manage.py runserver

## API Endpoints

| Method | Endpoint          | Description    |
| ------ | ----------------- | -------------- |
| POST   | `/api/customers/` | Add customer   |
| GET    | `/api/customers/` | List customers |
| POST   | `/api/orders/`    | Add order      |
| GET    | `/api/orders/`    | List orders    |
