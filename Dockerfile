# Stage 1: Build the React frontend
FROM node:16 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Set up Python backend
FROM python:3.9-slim AS backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .

# Copy built frontend files to backend’s static folder
COPY --from=frontend-build /app/frontend/build /app/backend/static

EXPOSE $PORT
CMD ["python", "app.py"]
