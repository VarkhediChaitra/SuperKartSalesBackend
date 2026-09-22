# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app/backend_sources

# Copy backend sources (Python files, requirements, model) into the container
COPY backend_sources/ /app/backend_sources/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the backend port
EXPOSE 7860

# Start the application with Gunicorn
# -w 4 : 4 worker processes
# -b 0.0.0.0:7860 : bind to all interfaces on port 7860
# superkart_sales_app:app : run the Flask app object named "app" in superkart_sales_app.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "superkart_sales_app:app"]
==
