from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('vistas/index.html')

@app.route('/vuelo')
def vuelo():
    return render_template('vistas/vuelo.html')

@app.route('/misvuelos')
def misVuelos():
    return render_template('vistas/misVuelos.html')

@app.route('/pagar')
def pagar():
    return render_template('vistas/pagar.html')

@app.route('/listaVuelos', methods=['GET'])
def login():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return []
    else:
        return []

if __name__ == '__main__':
    app.run()