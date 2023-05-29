class Aerolinea:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f"{self.nombre} - {self.pais}"

class Aviones:
    def __init__(self, modelo, aerolinia, capacidad):
        self.modelo = modelo
        self.aerolinia = aerolinia
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.modelo} - {self.aerolinia} - {self.capacidad}"

class Tripulantes:
    def __init__(self, nombre, apellido, edad, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad} - {self.cargo}"