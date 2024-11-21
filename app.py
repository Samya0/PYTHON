from config.database import get_connection
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Initialize the database connection
db_connection = get_connection()

# Set up a basic route
@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    # Set the port from environment or use default 8080
    port = int(os.getenv("PORT", 8080))
    # Run the Flask app
    app.run(host="0.0.0.0", port=port)
