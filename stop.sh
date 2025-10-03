#!/bin/bash

# Stop script for Robert Portfolio Backend API

echo "🛑 Stopping Robert Portfolio Backend API..."

# Stop services
docker-compose down

echo "✅ Services stopped successfully!"

