# ---------- Base Image ----------
FROM python:3.11-slim

# ---------- Environment ----------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------- Workdir ----------
WORKDIR /app

# ---------- System deps (optional but useful) ----------
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy project ----------
COPY . /app

# ---------- Install Python deps ----------
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Seed the database at build time ----------
# This will create /app/university.db inside the image
RUN python seed.py

# ---------- Expose port ----------
EXPOSE 8000

# ---------- Run app ----------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
