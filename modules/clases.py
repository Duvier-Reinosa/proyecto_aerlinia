class Aerolinea:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f"{self.nombre} - {self.pais}"




class persona:
    def __init__(self,identifica,nombre,celular,correo,contrasena):
        self.identifica=identifica
        self.nombre=nombre
        self.correo=correo
        self.celular=celular
        self.contrasena=contrasena
    def mostrar(self):
        print("Identificacion: ",self.identifica)
        print("Nombre: ",self.nombre)
        print("Correo: ",self.correo)

class Pasajero(persona):
    def __init__(self,identifica,nombre,celular,correo,contrasena,numero_millas):
        super().__init__(identifica,nombre,celular,correo,contrasena)
        self.numero_millas=numero_millas
    
    def mostrar(self):
        super().mostrar()
        print("Numero de millas: ",self.numero_millas)



class Avion:
    def __init__(self,matricula,modelo,marca,anio,aerolinea,horas_vuelo,capacida_silla):
        self.matricula=matricula
        self.modelo=modelo
        self.marca=marca
        self.anio=anio
        self.aerolinea=aerolinea
        self.capacidad_silla=capacida_silla
        self.horas_vuelo=horas_vuelo
        self.capacidad_pasajeros=[]

    def mostrar(self):
        print("Matricula: ",self.matricula)
        print("Modelo: ",self.modelo)
        print("Marca: ",self.marca)
        print("Año: ",self.anio)
        print("Horas de vuelo: ",self.horas_vuelo)

class Vuelo:
    def __init__(self,numero_vuelo,tipo_vuelo,tipo_tarifa,origen,destino,fecha_ida,hora_ida,hora_llegada,capacidad_silla):
        self.numero_vuelo=numero_vuelo
        self.origen=origen
        self.tipo_tarifa=tipo_tarifa
        self.destino=destino
        self.fecha_ida=fecha_ida
        self.hora_ida=hora_ida
        self.hora_llegada=hora_llegada
        self.tipo_vuelo=tipo_vuelo
        self.precio_vuelo= [100, 400]
        self.matricula_avion = None
        self.identifica_piloto=None
        self.identifica_tripulacion=[]
        self.capacidad_silla = capacidad_silla
        self.sillas_turista = 0
        self.sillas_ejecutiva = 0
    def valor_tiquete(self):
        if self.tipo_tarifa=="viajero":
            self.valor=500
    def set_capacidad(self):
        self.sillas_turista = self.capacidad_silla * 0.8
        self.sillas_ejecutiva = self.capacidad_silla * 0.2
    def vender_tiquete_turista(self):
        if self.sillas_turista > 0:
            self.sillas_turista -= 1
            return True
        else:
            return False
    def vender_tiquete_ejecutivo(self):
        if self.sillas_ejecutiva > 0:
            self.sillas_ejecutiva -= 1
            return True
        else:
            return False    

class tiquete(Vuelo):
    def __init__(self, numero_vuelo, tipo_vuelo,tipo_tarifa,tipo_valor, origen, destino, fecha_ida, hora_ida, hora_llegada,identificacion,nombre,celular,correo,valor,silla):
        Vuelo.__init__(numero_vuelo, tipo_vuelo,tipo_tarifa,tipo_valor, origen, destino, fecha_ida, hora_ida, hora_llegada)
        self.identificacion=identificacion
        self.nombre=nombre
        self.celular=celular
        self.correo=correo
        self.valor=valor
        self.silla=silla
        self.equipaje_mano=True
        self.equipaje_bodega=None
    def activar_equipa_bodega(self):
        if self.tipo_tarifa=="preferencial" or self.tipo_tarifa=="premium":
            self.equipaje_bodega=True
        else:
            self.equipaje_bodega=False
            
class pago():
    def __init__(self,numero_tarjeta,fecha_vencimiento,codigo_seguridad):
        self.numero_tarjeta=numero_tarjeta
        self.fecha_vencimiento=fecha_vencimiento
        self.codigo_seguridad=codigo_seguridad

        
        
        

    def mostrar(self):
        print("Numero de vuelo: ",self.numero_vuelo)
        print("Tipo de vuelo: ",self.tipo_vuelo)
        print("Origen: ",self.origen)
        print("Destino: ",self.destino)
        print("Fecha: ",self.fecha_ida)
        print("Hora: ",self.hora_ida)

# class Vuelo_comercial(Vuelo):
#     def __init__(self,numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso,numero_pasajeros,precio):
#         super().__init__(numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso)
#         self.numero_pasajeros=numero_pasajeros
#         self.precio=precio
#         self.capidad_equipaje=0
#     def mostrar(self):
#         super().mostrar()
#         print("Numero de pasajeros: ",self.numero_pasajeros)


# class Vuelo_privado(Vuelo):
#     def __init__(self,numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso,numero_pasajeros,precio):
#         super().__init__(numero_vuelo,tipo_vuelo,origen,destino,fecha_ida,fecha_regreso,hora_ida,hora_regreso)
#         self.numero_pasajeros=numero_pasajeros
#         self.precio=precio
#     def mostrar(self):
#         super().mostrar()
#         print("Numero de pasajeros: ",self.numero_pasajeros)


