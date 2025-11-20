# Use official lightweight Python image
FROM python:3.11-slim

# Create working directory
WORKDIR /app

# Copy dependency files first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port
EXPOSE 8080

# Start the FastAPI server
CMD ["uvicorn", "cloud_main:app", "--host", "0.0.0.0", "--port", "8080"]
