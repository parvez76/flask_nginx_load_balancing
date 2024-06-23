Docker Compose Flask App with Nginx Load Balancing

This project demonstrates setting up a Flask web application with Nginx load balancing using Docker Compose.

Prerequisites:
Docker
Docker Compose

How to Use:
Clone the Repository
git clone <repository-url>
cd <repository-name>


Build and Run Containers:

docker-compose up --build
Access the Application

Open your web browser and go to http://localhost:8080.
Refresh the page multiple times to observe load balancing between Flask application instances (flask-app1 and flask-app2).


Monitoring Logs:

Check logs for Nginx and Flask applications

docker-compose logs nginx  # Nginx logs
docker-compose logs flask-app1  # Flask app 1 logs
docker-compose logs flask-app2  # Flask app 2 logs

Notes:
Flask applications (flask-app1 and flask-app2) run on ports 5000 internally.
Nginx balances requests between flask-app1 and flask-app2 based on the nginx.conf configuration.
For production use, consider using a production-ready WSGI server instead of Flask's built-in server.
