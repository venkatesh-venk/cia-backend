# Quick Start Guide - Robert Portfolio Backend API

Get your FastAPI backend up and running in minutes! 🚀

## 🎯 Prerequisites

- Docker and Docker Compose installed
- OR Python 3.11+ and PostgreSQL 14+

## ⚡ Quick Start with Docker (Recommended)

### 1. Start Everything
```bash
./start.sh
```

That's it! The script will:
- ✅ Create `.env` if it doesn't exist
- ✅ Start PostgreSQL database
- ✅ Start FastAPI application
- ✅ Run database migrations automatically
- ✅ Set up PgAdmin (optional)

### 2. Access Your API
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 3. Test the API
```bash
# Health check
curl http://localhost:8000/health

# Create a contact
curl -X POST "http://localhost:8000/api/v1/contacts/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Test Message",
    "message": "Hello from the API!"
  }'

# List contacts
curl http://localhost:8000/api/v1/contacts/
```

### 4. Stop Everything
```bash
./stop.sh
```

## 🔧 Manual Setup (Without Docker)

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Database
```bash
# Create PostgreSQL database
createdb robert_portfolio

# Update .env with your database credentials
# Then run migrations
alembic upgrade head
```

### 4. Start Server
```bash
uvicorn app.main:app --reload
```

## 📊 PgAdmin (Database Management)

To start with PgAdmin included:
```bash
docker-compose --profile tools up -d
```

Access PgAdmin at http://localhost:5050
- Email: admin@admin.com
- Password: admin

## 🛠️ Common Commands

### View Logs
```bash
docker-compose logs -f api        # API logs
docker-compose logs -f postgres   # Database logs
```

### Restart Services
```bash
docker-compose restart api
```

### Access Database
```bash
docker-compose exec postgres psql -U postgres -d robert_portfolio
```

### Create Migration
```bash
# Inside the api container
docker-compose exec api alembic revision --autogenerate -m "your description"

# Or locally
alembic revision --autogenerate -m "your description"
```

### Apply Migrations
```bash
docker-compose exec api alembic upgrade head
# Or locally: alembic upgrade head
```

## 🔐 Security Notes

**IMPORTANT**: Before deploying to production:

1. Change `SECRET_KEY` in `.env`:
   ```bash
   # Generate a secure key
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

2. Update database password
3. Set `DEBUG=False`
4. Update `CORS_ORIGINS` with your frontend URL

## 📝 Environment Variables

Edit `.env` to configure:

```env
# Application
APP_NAME=Robert Portfolio API
APP_ENV=development
DEBUG=True

# Database
POSTGRES_HOST=localhost
POSTGRES_DB=robert_portfolio
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Security (CHANGE IN PRODUCTION!)
SECRET_KEY=your-secret-key-here-change-in-production

# CORS (Update with your frontend URL)
CORS_ORIGINS=["http://localhost:3000"]
```

## 🐛 Troubleshooting

### Database Connection Error
```bash
# Restart PostgreSQL
docker-compose restart postgres

# Check if it's running
docker-compose ps
```

### Port Already in Use
```bash
# Change ports in .env
PORT=8001
POSTGRES_PORT=5433
```

### Migration Issues
```bash
# Reset database (⚠️ THIS DELETES ALL DATA)
docker-compose down -v
docker-compose up -d
```

## 📚 Next Steps

1. **Explore API**: Visit http://localhost:8000/docs
2. **Add Models**: Create new models in `app/models/`
3. **Add Endpoints**: Create new endpoints in `app/api/v1/endpoints/`
4. **Connect Frontend**: Update frontend to use `http://localhost:8000/api/v1/`

## 🆘 Need Help?

- Check full documentation in `README.md`
- View logs: `docker-compose logs -f`
- Check API status: http://localhost:8000/health

Happy coding! 🎉

