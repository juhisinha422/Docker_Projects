<<<<<<< HEAD
import psycopg2
=======
>>>>>>> 296ad6650222a786eb98c7a05bbf7e7ed03bd999
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
conn = psycopg2.connect(
    host="db",
    database="mydb",
    user="user",
    password="password"
)

@app.route("/")
def home():
    return "Connected to PostgreSQL successfully!"

app.run(host="0.0.0.0", port=5000)
=======
@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 296ad6650222a786eb98c7a05bbf7e7ed03bd999

