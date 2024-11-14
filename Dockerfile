# Stage 1: Build the React frontend
FROM node:16 AS frontend-build

# Set working directory for the frontend
WORKDIR /app/frontend

# Copy the package.json and package-lock.json files first to leverage Docker cache
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend source code and build the frontend
COPY frontend/ .
RUN npm run build

# Stage 2: Set up the Python backend
FROM python:3.9-slim AS backend

# Set the working directory for the backend
WORKDIR /app/backend

# Copy and install backend dependencies first to cache these layers if requirements don’t change
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy the backend source code
COPY backend/ .

# Copy the built frontend files to backend’s static directory
COPY --from=frontend-build /app/frontend/build /app/backend/static

# Expose the port for Railway
EXPOSE $PORT

# Start the Flask app
CMD ["python", "app.py"]
