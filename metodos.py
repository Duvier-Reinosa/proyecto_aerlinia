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

def registra_tiquetes(lista):
    with open("archivos/tiquetes.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)

def registra_vuelos(lista):
    with open("archivos/vuelos.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)

def registar_tiquetes(lista):
    with open("archivos/tiquetes.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)

def registrar_pagos(lista):
    with open("archivos/pagos.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)
        
#-----------lectura--------------
def leer_aviones():
     with open("archivos/aviones.pickle", "rb") as archivo:
        aviones = pickle.load(archivo)
        return aviones

def leer_tiquetes():
     with open("archivos/tiquetes.pickle", "rb") as archivo:
        tiquetes= pickle.load(archivo)
        return tiquetes
def leer_usuarios():
     with open("archivos/usuario.pickle", "rb") as archivo:
        usuario= pickle.load(archivo)
        return usuario

def leer_vuelos():
        with open("archivos/vuelos.pickle", "rb") as archivo:
            vuelos = pickle.load(archivo)
            return vuelos
        
def leer_pagos():
        with open("archivos/pagos.pickle", "rb") as archivo:
            pagos = pickle.load(archivo)
            return pagos

def leer_tiquetes():
        with open("archivos/tiquetes.pickle", "rb") as archivo:
            tiquetes = pickle.load(archivo)
            return tiquetes
        
#-----------verificaciones--------------
def verificar_matricula(aviones,matricula):
    if os.path.exists("archivos/aviones.pickle"): ### reviso si el archivo esta creado para obtener los datos
        aviones=leer_aviones()
    ver=True
    while ver:
        cant_aviones=len(aviones)
        con_avi=0
        if cant_aviones>0:
            for m in aviones:
                if m.matricula==matricula:
                    print("La matricula ya existe")
                    return False
                con_avi+=1
                if con_avi==cant_aviones:
                    ver=False
                    return True
        else:
            ver=False
            return True
            
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
            return True
            
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
                if c.numero_vuelo==codigo:
                    print("El codigo ya existe")
                    return False
                con_vuelo+=1
                if con_vuelo==cant_vuelos:
                    ver=False
                    return True
        else:
            ver=False
            return True
            
    return codigo


#------------registrar ----------------
def registrar_aviones(aviones,matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla):
    if os.path.exists("archivos/aviones.pickle"): ### reviso si el archivo esta creado para obtener los datos
        aviones=leer_aviones()
    matric = verificar_matricula(aviones,matricula)  

    if matric:
        avion= clases.Avion(matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla)
        aviones.append(avion)
        registra_avion(aviones)
        return True
    else:
        return False

    

def registrar_usuarios(usuarios,identificacion,nombre,celular,correo,contrasena,millas):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    usu=verificar_identificacion(usuarios,identificacion)
    if usu:
        usuario= clases.Pasajero(identificacion,nombre,celular,correo,contrasena,millas)
        usuarios.append(usuario)
        registra_usuario(usuarios)
        return True
    else:
        return False
    #mostrar(usuarios)


def registrar_vuelos(vuelos,codigo,tipo_vuelo,tipo_tarifa,origen,destino,fecha,hora_ida,hora_llegada, capacidad_silla):
    if os.path.exists("archivos/vuelos.pickle"): ### reviso si el archivo esta creado para obtener los datos
        vuelos=leer_vuelos()
    vuelo = clases.Vuelo(codigo, tipo_vuelo, tipo_tarifa, origen, destino, fecha, hora_ida, hora_llegada, int(capacidad_silla))
    vuelo.set_capacidad()
    vuelos.append(vuelo)
    registra_vuelos(vuelos)
    return True
    
def registrar_tiquetes(tiquetes,codigo,tipo_vuelo,tipo_tarifa,tipo_valor,c_origen,c_destino,fecha,hora_ida,hora_llegada,identificacion,nombre,celular,correo,valor,silla)  :
    if os.path.exists("archivos/tiquetes.pickle"): ### reviso si el archivo esta creado para obtener los datos
        tiquetes=leer_vuelos()
    valor=tipo_valor
    tiquete= clases.tiquete(codigo,tipo_vuelo,tipo_tarifa,tipo_valor,c_origen,c_destino,fecha,hora_ida,hora_llegada,identificacion,nombre,celular,correo,valor,silla)     
    tiquete.activar_equipa_bodega()
    tiquetes.append(tiquete)
    registra_tiquetes(tiquetes)
    

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


##----------verificar usuario--------
def verificar_ingreso_usuario(usuarios,identificacion,contraseña):
    if os.path.exists("archivos/usuario.pickle"): ### reviso si el archivo esta creado para obtener los datos
        usuarios=leer_usuarios()
    ver=True
    while ver:
        cant_usuarios=len(usuarios)
        con_usu=0
        if cant_usuarios>0:
            for c in usuarios:
                if c.identifica==identificacion and contraseña==c.contrasena:
                    #ver=False
                    return True
                    
                con_usu+=1
                if con_usu==cant_usuarios:
                    print("La identificacion o contraseña erronea")
                    return False
                    
        else:
            print("No hay usuarios registrados")
            return False
            
def listOneVuelo(numeroVuelo):
    vuelosFile = leer_vuelos()
    for vuelo in vuelosFile:
        if vuelo.numero_vuelo == numeroVuelo:
            return {
                "origen": vuelo.origen,
                "destino": vuelo.destino,
                "fechaVuelo": vuelo.fecha_ida,
                "horaSalida": vuelo.hora_ida,
                "horaLlegada": vuelo.hora_llegada,
                "tipoVuelo": vuelo.tipo_vuelo,
                "precio": vuelo.precio_vuelo,
                "numeroVuelo": vuelo.numero_vuelo,
                "capacidadSillas": vuelo.capacidad_silla,
                "sillasTuristas": vuelo.sillas_turista,
                "sillasEjecutivas": vuelo.sillas_ejecutiva,
                "tipoTarifa": vuelo.tipo_tarifa,
            }
    return {}

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
            "precio": vuelo.precio_vuelo,
            "numeroVuelo": vuelo.numero_vuelo,
        })
    return json.dumps(vuelos)

def listarMatriculasAvion():
    avionesFile = leer_aviones()
    aviones = []
    for avion in avionesFile:
        aviones.append({
            "matricula": avion.matricula,
        })
    return json.dumps(aviones)

def getUser(id):
    usersFile = leer_usuarios()
    for user in usersFile:
        if user.identifica == id:
            return user.showData()
    return {}


def pagarTiquete(data):
    vuelo = listOneVuelo(data['numeroVuelo'])
    vuelosFile = leer_vuelos()
    tiquetesFile = leer_tiquetes()
    pagosFile = leer_pagos()
    newVuelos = []
    vueloSingle = {}

    for vuelo1 in vuelosFile:
        if vuelo1.numero_vuelo == data['numeroVuelo']:
            vueloSingle = vuelo1
        else:
            newVuelos.append(vuelo)

    user = getUser(data["identificacionUsuario"])
    if len(data['numeroTarjeta']) > 0:
        if data['claseVuelo'] == 'ejecutiva':
            vueloSingle.vender_tiquete_ejecutivo()
        else:
            vueloSingle.vender_tiquete_turista()
                                #   numero_vuelo,               tipo_vuelo,   tipo_tarifa,             tipo_valor,         origen,          destino,              fecha_ida,        hora_ida,             hora_llegada,             identificacion,                 nombre,        celular,          correo,        valor,           silla,              capacidad_silla
        tiquete = clases.Tiquete(data['numeroVuelo'], vueloSingle.tipo_vuelo, vueloSingle.tipo_tarifa, data['claseVuelo'], vuelo['origen'], vuelo['destino'], vueloSingle.fecha_ida, vueloSingle.hora_ida, vueloSingle.hora_llegada, data['identificacionUsuario'], user['nombre'], user['celular'], user['correo'], data['precio'], data['claseVuelo'], vuelo['capacidadSillas'])
        pago = clases.Pago(data['numeroTarjeta'])
        pago.setTiquete(tiquete)
        pago.setIdentificacionUsuario(data['identificacionUsuario'])
        tiquetesFile.append(tiquete)

    registar_tiquetes(tiquetesFile)
    newVuelos.append(vueloSingle)
    registra_vuelos(newVuelos)
    pagosFile.append(pago)
    registrar_pagos(pagosFile)
    return True
