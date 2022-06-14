from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
from config import config
from forms import RegistroForm

load_dotenv('.flaskenv')
app = Flask(__name__)
app.config.from_object(config['Desarrollo'])

@app.route('/')
def index():
    return render_template('index_s.html') 

@app.route('/ingresar')
def ingresar():
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('registro.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)










