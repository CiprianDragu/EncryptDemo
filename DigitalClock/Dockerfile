FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the Python script
COPY digital_clock.py .

# Install Python dependencies
RUN pip3 install tk

# Set the display environment variable
ENV DISPLAY=:0

# Run the script
CMD ["python", "digital_clock.py"]