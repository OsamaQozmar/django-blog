# Django Blog API

A blog backend built with Django and Django REST Framework, using PostgreSQL as the database.

## Overview

The project exposes a REST API for managing blog posts, categories, comments and users. Models, serializers and views are split into separate packages under `blog/` to keep the code easy to navigate.

## Features

- Models for posts, categories, comments and users
- CRUD endpoints for posts through a DRF `ModelViewSet` and `DefaultRouter`
- Paginated posts endpoint using `page` and `limit` query parameters
- Django admin with list display, filters, search and ordering
- Configuration through environment variables

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL

## Project Structure

```
blog/
  models/        Post, Category, Comment, User
  serializers/   DRF serializers
  views/         API views and viewsets
  urls.py        Blog routes
config/          Project settings and root URLs
```

## Getting Started

Clone the repository and create a virtual environment:

```
git clone https://github.com/OsamaQozmar/django-blog.git
cd django-blog
python -m venv .venv
.venv\Scripts\activate
```

Install Django, Django REST Framework and a PostgreSQL driver such as psycopg2.

Copy `.env.example` to `.env` and fill in your values:

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_SCHEMA=
```

Apply migrations, create an admin user and run the server:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET, POST | `/blog/posts/` | List and create posts |
| GET, PUT, PATCH, DELETE | `/blog/posts/{id}/` | Retrieve, update or delete a post |
| GET | `/blog/posts/get_post/?page=1&limit=10` | Paginated list of posts |

The admin panel is available at `/admin/`.

## Author

Osama Qozmar
[LinkedIn](https://linkedin.com/in/osamaqozmar)
