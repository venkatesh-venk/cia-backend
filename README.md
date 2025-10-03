# Robert Portfolio Backend API

A modern, high-performance backend API built with FastAPI, PostgreSQL, and Alembic migrations for the Robert Portfolio project.

## 🚀 Features

- **FastAPI Framework**: Modern, fast (high-performance) web framework
- **Async/Await Support**: Asynchronous database operations with SQLAlchemy
- **PostgreSQL Database**: Robust and scalable relational database
- **Alembic Migrations**: Database schema versioning and migrations
- **Swagger/OpenAPI**: Automatic interactive API documentation
- **Docker Support**: Containerized development and deployment
- **CORS Enabled**: Cross-Origin Resource Sharing configured
- **Pydantic Validation**: Request/response validation with Pydantic
- **Environment Configuration**: Flexible configuration with environment variables

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL 14+ (or use Docker)
- Docker & Docker Compose (optional but recommended)

## 🛠️ Installation

### Option 1: Using Docker (Recommended)

1. **Clone and navigate to the project**:
   ```bash
   cd cia-backend
   ```

2. **Create environment file**:
   ```bash
   cp .env.example .env
   ```

3. **Start services**:
   ```bash
   docker-compose up -d
   ```

   To include PgAdmin for database management:
   ```bash
   docker-compose --profile tools up -d
   ```

4. **Access the API**:
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - PgAdmin: http://localhost:5050 (if using tools profile)

### Option 2: Local Development

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start PostgreSQL** (if not using Docker):
   ```bash
   # Install and start PostgreSQL on your system
   createdb robert_portfolio
   ```

5. **Run migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Start the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

## 📁 Project Structure

```
cia-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   └── database.py        # Database connection and session
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py            # Base models and mixins
│   │   └── contact.py         # Contact model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── contact.py         # Pydantic schemas
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── api.py         # Main router
│           └── endpoints/
│               ├── __init__.py
│               └── contacts.py # Contact endpoints
├── alembic/
│   ├── env.py                 # Alembic environment
│   ├── script.py.mako         # Migration template
│   └── versions/              # Migration files
├── .env.example               # Example environment variables
├── .gitignore
├── alembic.ini                # Alembic configuration
├── docker-compose.yml         # Docker services
├── Dockerfile                 # Docker image
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Configuration

Key environment variables in `.env`:

```env
# Application
APP_NAME=Robert Portfolio API
APP_ENV=development
DEBUG=True

# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=robert_portfolio
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["http://localhost:3000"]

# Frontend
FRONTEND_URL=http://localhost:3000
```

## 🗄️ Database Migrations

### Create a new migration:
```bash
alembic revision --autogenerate -m "description of changes"
```

### Apply migrations:
```bash
alembic upgrade head
```

### Rollback one migration:
```bash
alembic downgrade -1
```

### View migration history:
```bash
alembic history
```

## 📚 API Endpoints

### Health Check
- `GET /` - Root endpoint with API info
- `GET /health` - Health check endpoint

### Contacts API (`/api/v1/contacts`)
- `POST /api/v1/contacts/` - Create a new contact
- `GET /api/v1/contacts/` - List all contacts (with pagination)
- `GET /api/v1/contacts/{id}` - Get a specific contact
- `PATCH /api/v1/contacts/{id}` - Update contact status
- `DELETE /api/v1/contacts/{id}` - Delete a contact

### Query Parameters for List
- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 10, max: 100)
- `is_read` - Filter by read status (optional)
- `is_replied` - Filter by replied status (optional)

## 📖 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🧪 Testing

Run tests (to be implemented):
```bash
pytest
```

With coverage:
```bash
pytest --cov=app tests/
```

## 🚢 Deployment

### Production Environment Variables

Update `.env` for production:
```env
APP_ENV=production
DEBUG=False
SECRET_KEY=<strong-secret-key>
POSTGRES_PASSWORD=<strong-password>
CORS_ORIGINS=["https://yourfrontend.com"]
```

### Docker Production Build

```bash
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

### Health Check

Monitor the application health:
```bash
curl http://localhost:8000/health
```

## 📦 Adding New Endpoints

1. **Create a model** in `app/models/`
2. **Create schemas** in `app/schemas/`
3. **Create endpoint** in `app/api/v1/endpoints/`
4. **Register router** in `app/api/v1/api.py`
5. **Create migration**: `alembic revision --autogenerate -m "description"`
6. **Apply migration**: `alembic upgrade head`

## 🔐 Security

- Change `SECRET_KEY` in production
- Use strong database passwords
- Enable HTTPS in production
- Keep dependencies updated
- Review CORS settings

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Create a pull request

## 📝 License

[Your License Here]

## 📧 Contact

For questions or support, please contact the development team.

## 🙏 Acknowledgments

- FastAPI - Modern web framework
- SQLAlchemy - ORM library
- Alembic - Database migrations
- Pydantic - Data validation
