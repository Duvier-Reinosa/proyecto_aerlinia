from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('vistas/index.html')

@app.route('/vuelo')
def index():
    return render_template('vistas/vuelo.html')

@app.route('/misvuelos')
def index():
    return render_template('vistas/index.html')

@app.route('/pagar')
def index():
    return render_template('vistas/index.html')

if __name__ == '__main__':
    app.run()