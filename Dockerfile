# Use CircleCI's Python image for compatibility
FROM cimg/python:3.9

# Set working directory
WORKDIR /app

# Copy all project files except best.pt
COPY . /app/

# Remove best.pt if it exists
RUN rm -f /app/best.pt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for web access (e.g., Flask/FastAPI)
EXPOSE 5000

# Set the default command to run the application
CMD ["python", "app.py"]
