from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv('.flaskenv')
app = Flask(__name__)

@app.route('/')
def index():
    return "anda"

if __name__ == "__main__":
    app.run(debug=True)










