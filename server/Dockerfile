# Base image (choose a suitable Python version for your API)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first for efficient caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy remaining project files
COPY . /app

# Expose the port your API listens on (adjust if needed)
# EXPOSE 6500

# Define the command to start the API server
CMD ["python3", "./app/main.py"]