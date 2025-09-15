# Step 1: Use official Python image
FROM python:3.10-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy requirements first (for caching)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all source code
COPY . .

# Step 6: Set default command (run prediction script)
CMD ["python3", "app.py"]
