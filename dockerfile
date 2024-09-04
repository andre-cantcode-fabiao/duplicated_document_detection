# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt if you have one (optional step if you decide to keep dependencies separate)
COPY requirements.txt .

# Install required Python packages
RUN pip install -r requirements.txt

# Copy the FastAPI app into the container
COPY . .

# Expose the port that Uvicorn will run on
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]