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
    def showData(self):
        return {
            "identifica": self.identifica,
            "nombre": self.nombre,
            "celular": self.celular,
            "correo": self.correo,
            "numero_millas": self.numero_millas
        }



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

class Tiquete(Vuelo):
    def __init__(self, numero_vuelo, tipo_vuelo,tipo_tarifa,tipo_valor, origen, destino, fecha_ida, hora_ida, hora_llegada,identificacion,nombre,celular,correo,valor,silla):
        Vuelo.__init__(numero_vuelo, tipo_vuelo,tipo_tarifa,tipo_valor, origen, destino, fecha_ida, hora_ida, hora_llegada)
        self.identificacion=identificacion
        self.nombre=nombre
        self.celular=celular
        self.correo=correo
        self.valor=valor
        self.silla=silla
        self.equipaje_mano=True
    def showData(self):
        return {
            "numero_vuelo": self.numero_vuelo,
            "tipo_vuelo": self.tipo_vuelo,
            "tipo_tarifa": self.tipo_tarifa,
            "tipo_valor": self.tipo_valor,
            "origen": self.origen,
            "destino": self.destino,
            "fecha_ida": self.fecha_ida,
            "hora_ida": self.hora_ida,
            "hora_llegada": self.hora_llegada,
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "celular": self.celular,
            "correo": self.correo,
            "valor": self.valor,
            "silla": self.silla,
            "equipaje_mano": self.equipaje_mano,
        }
            
class Pago():
    def __init__(self,numero_tarjeta):
        self.numero_tarjeta=numero_tarjeta
        self.identificacionUsuario=None
        self.tiquete = None
    def setIdentificacionUsuario(self, identificacionUsuario):
        self.identificacionUsuario = identificacionUsuario
    def setTiquete(self, tiquete):
        self.tiquete = tiquete
    def showData(self):
        return {
            "numero_tarjeta": self.numero_tarjeta,
            "identificacionUsuario": self.identificacionUsuario,
            "tiquete": self.tiquete
        }



