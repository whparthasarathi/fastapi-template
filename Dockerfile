# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

COPY  requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app/ .

# Expose the port for the API
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "--reload", "main:app", "--host", "0.0.0.0", "--port", "8000"]
