# Import necessary modules from Flask and socket
from flask import Flask
import socket

# Get the IP address of the current machine
ip = socket.gethostbyname(socket.gethostname())

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    # Create an output string with a welcome message and the server's IP address
    out = (
        f'Welcome to docker flask<br/>'
        f'The ip address of this server is {ip}'
    )
    return out

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
