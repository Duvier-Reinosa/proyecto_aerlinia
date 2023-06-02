import pickle
import os
from  modules import clases
import json


def mostrar(lista):
    for a in lista:
        a.mostrar()
def registra_avion(lista):
    with open("archivos/aviones.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
def registra_usuario(lista):
    with open("archivos/usuario.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
def registra_funcionario(lista):
    with open("archivos/funcionario.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
def registra_tiquetes(lista):
    with open("archivos/tiquetes.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
def registra_pilotos(lista):
    with open("archivos/pilotos.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)

def registra_vuelos(lista):
    with open("archivos/vuelos.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
        
#-----------lectura--------------
def leer_aviones():
     with open("archivos/aviones.pickle", "rb") as archivo:
        aviones = pickle.load(archivo)
        return aviones
def leer_funcionario():
     with open("archivos/funcionario.pickle", "rb") as archivo:
        funcionario = pickle.load(archivo)
        return funcionario
def leer_tiquetes():
     with open("archivos/tiquetes.pickle", "rb") as archivo:
        tiquetes= pickle.load(archivo)
        return tiquetes
def leer_usuarios():
     with open("archivos/usuario.pickle", "rb") as archivo:
        usuario= pickle.load(archivo)
        return usuario
def leer_pilotos():
        with open("archivos/pilotos.pickle", "rb") as archivo:
            pilotos= pickle.load(archivo)
            return pilotos
def leer_vuelos():
        with open("archivos/vuelos.pickle", "rb") as archivo:
            vuelos = pickle.load(archivo)
            return vuelos
        
#-----------verificaciones--------------
def verificar_matricula(aviones,matricula):
    if os.path.exists("archivos/aviones.pickle"): ### reviso si el archivo esta creado para obtener los datos
        aviones=leer_usuarios()
    ver=True
    while ver:
        cant_aviones=len(aviones)
        con_avi=0
        if cant_aviones>0:
            for m in aviones:
                if m.matricula==matricula:
                    print("La matricula ya existe")
                    break
                con_avi+=1
                if con_avi==cant_aviones:
                    ver=False
        else:
            ver=False
            
    return matricula
def verificar_identificacion(usuarios,cedula):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    ver=True
    while ver:
        
        cant_usuarios=len(usuarios)
        con_usu=0
        if cant_usuarios>0:
            for c in usuarios:
                if c.identifica==cedula:
                    print("El usuario ya esta registrado")
                    return False
                con_usu+=1
                if con_usu==cant_usuarios:
                    ver=False
                    return True
        else:
            ver=False
            return False
            
def verificar_vuelo(vuelos,codigo):
    if os.path.exists("archivos/vuelos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        vuelos=leer_usuarios()
    ver=True
    while ver:
        codigo=input("Digite el codigo: ")
        cant_vuelos=len(vuelos)
        con_vuelo=0
        if cant_vuelos>0:
            for c in vuelos:
                if c.codigo==codigo:
                    print("El codigo ya existe")
                    break
                con_vuelo+=1
                if con_vuelo==cant_vuelos:
                    ver=False
        else:
            ver=False
            
    return codigo



def registrar_aviones(aviones,matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla):
    if os.path.exists("archivos/aviones.pickle"): ### reviso si el archivo esta creado para obtener los datos
        aviones=leer_aviones()
    matric=verificar_matricula(aviones,matricula)         
    
    avion= clases.Avion(matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla)
    aviones.append(avion)
    registra_avion(aviones)

def registrar_usuarios(usuarios,identificacion,nombre,celular,correo,contrasena,millas):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    usuario= clases.Pasajero(identificacion,nombre,celular,correo,contrasena,millas)
    usuarios.append(usuario)
    registra_usuario(usuarios)
    #mostrar(usuarios)

def registrar_funcionario(funcionario,identificacion,nombre,edad,celular,correo,contrasena,funcion):
    if os.path.exists("archivos/funcionario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        funcionario=leer_funcionario()        
    funcionari= clases.Tripulacion(identificacion,nombre,edad,celular,correo,contrasena,funcion)
    funcionario.append(funcionari)
    registra_funcionario(funcionario)

def registrar_piloto(piloto,identificacion,nombre,celular,edad,correo,contrasena,rango,licencia,hora_vuelo):
    if os.path.exists("archivos/pilotos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        piloto=leer_pilotos()     
    pilot= clases.Piloto(identificacion,nombre,celular,correo,contrasena,edad,licencia,rango,hora_vuelo)
    piloto.append(pilot)
    registra_pilotos(piloto)

def registrar_vuelos(vuelos,codigo,tipo_vuelo,tipo_tarifa,origen,destino,fecha,hora_ida,hora_llegada,valor_vuelo):
    if os.path.exists("archivos/vuelos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        vuelos=leer_vuelos()
    vuelo= clases.Vuelo(codigo,tipo_vuelo,tipo_tarifa,valor_vuelo,origen,destino,fecha,hora_ida,hora_llegada)
    vuelos.append(vuelo)
    registra_vuelos(vuelos)


##---consultar vuelos----
def consultar_vuelos(vuelos,c_origen,c_destino,fecha):
    if os.path.exists("archivos/vuelos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        vuelos=leer_vuelos()
    cant_vuelos=len(vuelos)
    cont_vuelos=0
    for vuel in vuelos:
        if vuel.origen==c_origen and vuel.destino==c_destino and vuel.fecha_ida==fecha:
            return True
        cont_vuelos+=1
        if cant_vuelos==cont_vuelos:
            return False

def registrar_tiquetes(tiquetes,codigo,tipo_vuelo,tipo_tarifa,c_origen,c_destino,fecha,hora_ida,hora_llegada)  :
    pass     
##----------verificar usuario--------
def verificar_ingreso_usuario(usuarios,identificacion,contraseña):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    ver=True
    while ver:
        identificacion=input("Digite la identificacion: ")
        contraseña=input("contraseña ")
        cant_usuarios=len(usuarios)
        con_usu=0
        if cant_usuarios>0:
            for c in usuarios:
                if c.identifica==identificacion and contraseña==c.contrasena:
                    ver=False
                    return True
                    break
                con_usu+=1
                if con_usu==cant_usuarios:
                    print("La identificacion o contraseña erronea")
                    return False
                    break
        else:
            print("No hay usuarios registrados")
            return False
            break
            
##----------verificar funcionario--------
def verificar_ingreso_funcionario(funcionario,identificacion,contraseña):
    if os.path.exists("archivos/funcionario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        funcionario=leer_funcionario()
    ver=True
    while ver:
        cant_funcionario=len(funcionario)
        con_funcionario=0
        if cant_funcionario>0:
            for c in funcionario:
                if c.identifica==identificacion and contraseña==c.contrasena:
                    ver=False
                    return True
                    break
                con_funcionario+=1
                if con_funcionario==cant_funcionario:
                    print("La identificacion o contraseña erronea")
                    return False
                    break
        else:
            print("No hay funcionario registrados")
            return False
            break

##----------verificar piloto--------
def verificar_ingreso_piloto(piloto,identificacion,contraseña):
    if os.path.exists("archivos/pilotos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        piloto=leer_pilotos()
    ver=True
    while ver:
        cant_piloto=len(piloto)
        con_piloto=0
        if cant_piloto>0:
            for c in piloto:
                if c.identifica==identificacion and contraseña==c.contrasena:
                    ver=False
                    return True
                    break
                con_piloto+=1
                if con_piloto==cant_piloto:
                    print("La identificacion o contraseña erronea")
                    return False
                    break
        else:
            print("No hay piloto registrados")
            return False
            break


def listarVuelosApi():
    vuelosFile = leer_vuelos()
    vuelos = []
    for vuelo in vuelosFile:
        vuelos.append({
            "origen": vuelo.origen,
            "destino": vuelo.destino,
            "fechaVuelo": vuelo.fecha_ida,
            "horaSalida": vuelo.hora_ida,
            "horaLlegada": vuelo.hora_llegada,
            "tipoVuelo": vuelo.tipo_vuelo,
            "precio": vuelo.tipo_valor
        })
    return json.dumps(vuelos)

def listarMatriculasAvion():
    avionesFile = leer_aviones()
    aviones = []
    for avion in avionesFile:
        aviones.append({
            "matricula": avion.matricula,
        })
    return aviones



##----------verificar vuelos  programados---


# registrar_vuelos([],"1","comercial",["viajero","preferencia","premium"],"perira","cali","15-7-2023","13:00","15:00",[200.000,300.000,400,000])
# registrar_piloto([],"11182","carlo angola","31233564","25","agola@sa.com","32545","comandante","32sa","300")
# #registrar_funcionario([],None,None,None,None,None,None,None)
# #registrar_usuarios([],None,None,None,None,None,None)
# print(consultar_vuelos([],"bogota","cali","12-6-2023"))
# registrar_vuelos([],None,None,None,None,None,None,None,None)
# #print(verificar_ingreso_usuario([],None,None))
# #registrar_aviones([],None,None,None,None,None,None,None)
# listarVuelosApi()
