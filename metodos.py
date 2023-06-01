import pickle
import os
from  modules import clases

def listarVuelos():
    vuelos = []
    #abrir el archivo donde está la lista de vuelos
    #formatearlos en una lista[]
    #retornar la lista
    return vuelos

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
            vuelos= pickle.load(archivo)
            return vuelos
        
#-----------verificaciones--------------
def verificar_matricula(aviones,matricula):
    ver=True
    while ver:
        matricula=input("Digite la matricula: ")
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
    ver=True
    while ver:
        cedula=input("Digite la identificacion: ")
        cant_usuarios=len(usuarios)
        con_usu=0
        if cant_usuarios>0:
            for c in usuarios:
                if c.identifica==cedula:
                    print("La cedula ya existe")
                    break
                con_usu+=1
                if con_usu==cant_usuarios:
                    ver=False
        else:
            ver=False
            
    return cedula 
def verificar_vuelo(vuelos,codigo):
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
def verificar_tiquete(tiquetes,codigo):
    ver=True
    while ver:
        codigo=input("Digite el codigo: ")
        cant_tiquetes=len(tiquetes)
        con_tiquete=0
        if cant_tiquetes>0:
            for c in tiquetes:
                if c.codigo==codigo:
                    print("El codigo ya existe")
                    break
                con_tiquete+=1
                if con_tiquete==cant_tiquetes:
                    ver=False
        else:
            ver=False
            
    return codigo


def registrar_aviones(aviones,matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla):
    if os.path.exists("archivos/aviones.pickle"): ### reviso si el archivo esta creado para obtener los datos
        aviones=leer_aviones()
    matricula=verificar_matricula(aviones,matricula)         
    modelo=input("Modelo avion: ")
    marca=input ("Marca del avion: ")
    anio= input("Año del avion: ")
    aerolinea=input("Aerolinea: ")
    horas_vuelo=input("Horas de vuelo: ")
    capacida_silla=input("Capacidad de sillas: ")
    avion= clases.Avion(matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla)
    aviones.append(avion)
    registra_avion(aviones)

def registrar_usuarios(usuarios,identificacion,nombre,celular,correo,contrasena,millas):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    identificacion=verificar_identificacion(usuarios,identificacion)         
    nombre=input("Nombre: ")
    celular=input ("celular: ")
    correo= input("correo: ")
    contrasena=input("contraseña: ")
    usuario= clases.Pasajero(identificacion,nombre,celular,correo,contrasena,millas)
    usuarios.append(usuario)
    registra_usuario(usuarios)
    #mostrar(usuarios)

def registrar_funcionario(funcionario,identificacion,nombre,edad,celular,correo,contrasena,funcion):
    if os.path.exists("archivos/funcionario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        funcionario=leer_funcionario()
    identificacion=verificar_identificacion(funcionario,identificacion)         
    nombre=input("Nombre: ")
    celular=input ("celular: ")
    correo= input("correo: ")
    contrasena=input("contraseña: ")
    funcion=input("funcion: ")
    
    funcionari= clases.Tripulacion(identificacion,nombre,edad,celular,correo,contrasena,funcion)
    funcionario.append(funcionari)
    registra_funcionario(funcionario)

def registrar_piloto(piloto,identificacion,nombre,celular,edad,correo,contrasena,rango,licencia,hora_vuelo):
    if os.path.exists("archivos/pilotos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        piloto=leer_pilotos()
    identificacion=verificar_identificacion(piloto,identificacion)         
    nombre=input("Nombre: ")
    edad=input ("edad: ")
    correo= input("correo: ")
    contrasena=input("contraseña: ")
    rango=input("rango: ")
    hora_vuelo=input("hora de vuelo: ")
    pilot= clases.Piloto(identificacion,nombre,celular,correo,contrasena,edad,licencia,rango,hora_vuelo)
    piloto.append(pilot)
    registra_pilotos(piloto)

def registrar_vuelos(vuelos,codigo,origen,destino,fecha,hora,valor,avion):
    if os.path.exists("archivos/vuelos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        vuelos=leer_vuelos()
    codigo=input("codigo: ")       
    origen=input("origen: ")
    destino=input ("destino: ")
    fecha= input("fecha: ")
    hora=input("hora: ")
    valor=input("valor: ")
    avion=input("avion: ")
    vuelo= clases.Vuelo(codigo,origen,destino,fecha,hora,valor,avion)
    vuelos.append(vuelo)
    registra_vuelos(vuelos)
#registrar_vuelos([],None,None,None,None,None,None,None)
#registrar_piloto([],None,None,None,None,None,None,None,None,None)
#registrar_funcionario([],None,None,None,None,None,None,None)
##registrar_usuarios([],None,None,None,None,None,None)
#registrar_aviones([],None,None,None,None,None,None,None)