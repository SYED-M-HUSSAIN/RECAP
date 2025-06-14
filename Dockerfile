FROM python:3.11-slim

WORKDIR /app

# Install pip and build tools
RUN apt-get update && apt-get install -y build-essential && \
    pip install --upgrade pip setuptools

# Copy project metadata
COPY pyproject.toml ./

# Install dependencies (without needing requirements.txt or uv)
RUN pip install .

# Copy app code
COPY . .

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
