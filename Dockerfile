
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Expose the port
EXPOSE 8080

# Set the entrypoint
ENTRYPOINT ["poetry", "run", "python", "-m", "deployment.remote"]
