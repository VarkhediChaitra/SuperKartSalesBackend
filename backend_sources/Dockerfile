FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app/backend_sources

# Copy backend sources (Python files, requirements, model) into the container
COPY backend_sources/ /app/backend_sources/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run Gunicorn with 4 workers on port 7860
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "superkart_sales_app:app"]
