import pickle


def mostrar(lista):
    for a in lista:
        a.mostrar()
def registra_avion(lista):
    with open("archivos/pagos.pickle", "wb") as archivo:
        pickle.dump(lista, archivo)

registra_avion([])