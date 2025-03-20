# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY README.md ./
COPY main.py ./
COPY memos.py ./

# Install build dependencies
RUN pip install --no-cache-dir setuptools wheel

# Install project dependencies
RUN pip install --no-cache-dir .

# Expose port, if needed (server runs via stdio so not exposed), but gateway logs say port 8080 for WS

# Use python main.py directly as the entrypoint
CMD ["python", "main.py"]
