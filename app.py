from flask import Flask, render_template, request
import os
from metodos import listarVuelosApi, listarMatriculasAvion, registrar_vuelos, registrar_aviones,registrar_usuarios,verificar_ingreso_usuario

app = Flask(__name__)

app.static_folder = 'static'
app.static_url_path = '/static'

# vistas------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('vistas/index.html')

@app.route('/vuelo/<id>')
def vuelo(id):
    print(id)
    return render_template('vistas/vuelo.html', id = id)

@app.route('/agregarUsuario')
def agregarUsuario():
    return render_template('vistas/agregarUsuario.html')

@app.route('/iniciarSecion')
def iniciarSecion():
    return render_template('vistas/inciarSecion.html')

@app.route('/misVuelos')
def misVuelos():
    return render_template('vistas/misVuelos.html')

@app.route('/pagar')
def pagar():
    return render_template('vistas/pagar.html')

# vistas dashboard<--------------------------------------------------------

@app.route('/dashboard/home')
def homeDashboard():
    return render_template('dashboard/home.html')


@app.route('/dashboard/agregarVuelo')
def agregarVuelo():
    return render_template('dashboard/agregarVuelo.html')


@app.route('/dashboard/agregarAvion')
def agregarAvion():
    return render_template('dashboard/agregarAvion.html')




# api /backend------------------------------------------------------------

@app.route('/api/listaVuelos', methods=['GET'])
def login():
    if request.method == 'GET':
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        return listarVuelosApi()
    else:
        return []
    
# api para dashboard------------------------------------------------------

@app.route('/api/dashboard/agregarVuelo', methods=['POST'])
def agregarVueloApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_vuelos([], data["numero_vuelo"], data["tipo_vuelo"],["turista","ejecutiva"], data["origen"], data["destino"], data["fecha_ida"], data["hora_ida"],data["hora_regreso"])
        if returned:
            return {"status": "success"}
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
    
@app.route('/api/dashboard/agregarAvion', methods=['POST'])
def agregarAvionApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_aviones([], data["matricula"], data["modelo"], data["marca"], data["anio"], data["aerolinea"], data["horas_vuelo"],data["capacidad_silla"])
        if returned:
            return {"status": "success"}
    else:
        return []
    
@app.route('/api/agregarUsuario', methods=['POST'])
def agregarUsuarioApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  registrar_usuarios([], data["identificacion"], data["nombre"], data["celular"], data["correo"], data["contrasena"],0)
        if returned:
            return {"status": "success"}
    else:
        return []
    
@app.route('/api/iniciarSecion', methods=['POST'])    
def iniciarSecionApi():
    if request.method == 'POST':
        data = request.get_json() 
        print(data)
        # agregar metodo para obtener los vuelos, se pueden guardar en un archivo de texto hacer un metodo en el archivo metodos para obtener los vuelos
        returned =  verificar_ingreso_usuario([], data["identificacion"],data["contrasena"])
        if returned:
            return {"status": "success"}
    else:
        return []
if __name__ == '__main__':
    app.run()