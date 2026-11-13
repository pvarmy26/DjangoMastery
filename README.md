# DjangoMastery — Student Management System

A Django-based Student Management System featuring user authentication, student management, document uploads, and RESTful APIs. Built as a practical project to learn Django development and production deployment.

## Live Demo

**Live Application:** https://django-mastery-lfc1.onrender.com/students/

**Django Admin:** https://django-mastery-lfc1.onrender.com/admin/

**GitHub Repository:** https://github.com/pvarmy26/DjangoMastery

## Features

- User registration, login, and logout.
- Authenticated student management.
- Student creation and data validation.
- Document upload functionality.
- Django Admin integration.
- RESTful APIs using Django REST Framework.
- Token and session authentication.
- Custom API permissions.
- PostgreSQL database in production.
- Static file serving using WhiteNoise.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Backend framework |
| Django REST Framework | REST API development |
| SQLite | Local development database |
| PostgreSQL | Production database |
| HTML / CSS | Frontend |
| WhiteNoise | Static file serving |
| Gunicorn | Production WSGI server |
| Render | Deployment platform |
| Git & GitHub | Version control |

## API Endpoints

Base URL: `/students/api/`

| Endpoint | HTTP Methods | Description |
|---|---|---|
| `/students/` | GET, POST | List and create students |
| `/students/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, and delete a student |
| `/admin/` | GET | Admin-only API endpoint |

### API Permissions

- GET requests are publicly accessible.
- POST, PUT, and PATCH require authentication.
- DELETE requires staff permissions.
- Admin API requires administrator permissions.

### Student Validation

- Student age must be at least 16.
- Marks must be between 0 and 100.
- Advanced Python requires students to be at least 18.

## Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/pvarmy26/DjangoMastery.git
cd DjangoMastery
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Never commit your actual secret key or `.env` file.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/students/

## Production Deployment

Deployed on Render using:

- Gunicorn as the WSGI server.
- PostgreSQL as the production database.
- WhiteNoise for static files.
- Environment variables for production configuration.
- Django migrations during deployment.

## Learning Outcomes

Through this project, I gained practical experience with:

- Django project and application architecture.
- Models, migrations, and ORM operations.
- Forms, validation, and authentication.
- Django Admin customization.
- REST API development and serializers.
- API authentication and custom permissions.
- Production configuration and deployment.
- PostgreSQL integration and Git-based deployment.

## Author

**Pradeep**

B.Tech — Computer Science and Engineering

GitHub: https://github.com/pvarmy26