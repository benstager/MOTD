FROM python:3.11.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y ca-certificates curl && rm -rf /var/lib/apt/lists/*

# Copy the local tectonic binary into the image
COPY tectonic /usr/local/bin/tectonic
RUN chmod +x /usr/local/bin/tectonic

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose port 8080 (for DigitalOcean)
EXPOSE 8080

# Run Uvicorn on port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
