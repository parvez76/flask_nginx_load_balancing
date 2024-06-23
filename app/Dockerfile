FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment in the container
RUN python3 -m venv venv

# Upgrade pip using the virtual environment's pip
RUN venv/bin/pip install --upgrade pip

# Install Flask using the virtual environment's pip
RUN venv/bin/pip install flask

# Make port 5000 available to the world outside this container
EXPOSE 5000/tcp

# Define the command to run the application using the virtual environment's python
CMD ["venv/bin/python", "main.py"]
