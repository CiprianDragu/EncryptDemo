
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY weather_app.py requirements.txt ./

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "weather_app.py"]