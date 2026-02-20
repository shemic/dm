# 1. Switch to a Debian-based image for glibc compatibility
FROM node:24-bookworm-slim

# 2. Install necessary system dependencies (some opencode tools need these)
RUN apt-get update && apt-get install -y \
    curl \
    bash \
    gosu \
    git \
    && rm -rf /var/lib/apt/lists/*

# 3. Install opencode-ai globally
RUN npm i -g opencode-ai

WORKDIR /app

# 4. Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose the default port
EXPOSE 4096

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Default command runs the server
CMD ["serve"]