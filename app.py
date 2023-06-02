from flask import Flask, render_template, request, url_for, send_from_directory, send_file
import os
from metodos import listarVuelosApi, listarMatriculasAvion

app = Flask(__name__)

app.static_folder = 'static'
app.static_url_path = '/static'

# vistas

@app.route('/')
def index():
    return render_template('vistas/index.html')

@app.route('/vuelo/<id>')
def vuelo(id):
    print(id)
    return render_template('vistas/vuelo.html', id = id)

@app.route('/misVuelos')
def misVuelos():
    return render_template('vistas/misVuelos.html')

@app.route('/pagar')
def pagar():
    return render_template('vistas/pagar.html')

# vistas dashboard
@app.route('/dashboard/agregarVuelo')
def agregarVuelo():
    return render_template('dashboard/agregarVuelo.html')

# api /backend

@app.route('/api/listaVuelos', methods=['GET'])
def login():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listarVuelosApi()
    else:
        return []
    
# api para dashboard
@app.route('/api/dashboard/agregarVuelo', methods=['POST'])
def agregarVueloApi():
    if request.method == 'POST':
        data = request.form 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return []
    else:
        return []
#  
@app.route('/api/dashboard/listarMatriculas', methods=['GET'])
def listasMAtriculas():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listarMatriculasAvion()
    else:
        return []
    

if __name__ == '__main__':
    app.run()