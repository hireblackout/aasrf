FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create reports directory
RUN mkdir -p /app/reports

# Set entrypoint
ENTRYPOINT ["python", "aasrf.py"]
CMD ["--help"]
