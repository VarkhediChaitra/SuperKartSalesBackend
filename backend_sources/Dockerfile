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
IyBVc2UgYSBsaWdodHdlaWdodCBQeXRob24gYmFzZSBpbWFnZQpGUk9NIHB5dGhvbjozLjktc2xpbQoKIyBTZXQgd29ya2luZyBkaXJlY3RvcnkgaW5zaWRlIHRoZSBjb250YWluZXIKV09SS0RJUiAvYXBwL2JhY2tlbmRfc291cmNlcwoKIyBDb3B5IGJhY2tlbmQgc291cmNlcyAoUHl0aG9uIGZpbGVzLCByZXF1aXJlbWVudHMsIG1vZGVsKSBpbnRvIHRoZSBjb250YWluZXIKQ09QWSBiYWNrZW5kX3NvdXJjZXMvIC9hcHAvYmFja2VuZF9zb3VyY2VzLwoKIyBJbnN0YWxsIGRlcGVuZGVuY2llcyBmcm9tIHJlcXVpcmVtZW50cy50eHQKUlVOIHBpcCBpbnN0YWxsIC0tbm8tY2FjaGUtZGlyIC0tdXBncmFkZSAtciByZXF1aXJlbWVudHMudHh0CgojIEV4cG9zZSB0aGUgYmFja2VuZCBwb3J0CkVYUE9TRSA3ODYwCgojIFN0YXJ0IHRoZSBhcHBsaWNhdGlvbiB3aXRoIEd1bmljb3JuCiMgLXcgNCA6IDQgd29ya2VyIHByb2Nlc3NlcwojIC1iIDAuMC4wLjA6Nzg2MCA6IGJpbmQgdG8gYWxsIGludGVyZmFjZXMgb24gcG9ydCA3ODYwCiMgc3VwZXJrYXJ0X3NhbGVzX2FwcDphcHAgOiBydW4gdGhlIEZsYXNrIGFwcCBvYmplY3QgbmFtZWQgImFwcCIgaW4gc3VwZXJrYXJ0X3NhbGVzX2FwcC5weQpDTUQgWyJndW5pY29ybiIsICItdyIsICI0IiwgIi1iIiwgIjAuMC4wLjA6Nzg2MCIsICJzdXBlcmthcnRfc2FsZXNfYXBwOmFwcCJdCg==
