# Use the uv Alpine image as the base
FROM ghcr.io/astral-sh/uv:python3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies using uv
RUN uv sync --frozen

# Run the script
CMD ["uv", "run", "star-and-toot.py"]