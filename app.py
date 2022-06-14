from flask import Flask, render_template
from dotenv import load_dotenv
from config import config

load_dotenv('.flaskenv')
app = Flask(__name__)
app.config.from_object(config['Desarrollo'])

@app.route('/')
def index():
    return render_template('index_s.html') 

@app.route('/ingresar')
def ingresar():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)










