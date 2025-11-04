FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first for layer caching
COPY requirements.txt ./

# Install dependencies before copying rest of the code
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose API port
EXPOSE 8000

# Set the entrypoint to start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
