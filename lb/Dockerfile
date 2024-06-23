# Use the official Nginx image from the Docker Hub
FROM nginx

# Copy the custom nginx.conf file to the Nginx configuration directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080 to the outside world
EXPOSE 8080/tcp

# Run Nginx in the foreground (prevent it from daemonizing)
CMD ["nginx", "-g", "daemon off;"]
