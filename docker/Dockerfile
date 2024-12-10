# -------------------------------------------------------
# Step 1: Base image (lightweight Python 3.11)
# -------------------------------------------------------
FROM python:3.11-slim

# -------------------------------------------------------
# Step 2: Set environment variables to avoid .pyc files and enable live logging
# -------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# -------------------------------------------------------
# Step 3: Set the working directory for the app
# -------------------------------------------------------
WORKDIR /usr/src/app

# -------------------------------------------------------
# Step 4: Copy only the relevant files (requirements.txt first to use Docker cache)
# -------------------------------------------------------
COPY ../requirements.txt /usr/src/app/

# -------------------------------------------------------
# Step 5: Install dependencies (system dependencies + Python dependencies)
# -------------------------------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# -------------------------------------------------------
# Step 6: Copy the entire source code (kept clean to avoid copying unnecessary files)
# -------------------------------------------------------
COPY ../src /usr/src/app

# -------------------------------------------------------
# Step 7: Expose ports used by Django and FastAPI
# -------------------------------------------------------
EXPOSE 8000
EXPOSE 8001

# -------------------------------------------------------
# Step 8: Run database migrations and collect static files (Django setup tasks)
# -------------------------------------------------------
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput

# -------------------------------------------------------
# Step 9: Run both Django and FastAPI simultaneously
# -------------------------------------------------------
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 & uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8001 --reload"]
