# classe
class Contador:
    contador_global = 0  # atributo da classe


@classmethod
def incrementar_global(cls):  # metodo (funcao) increment
    cls.contador_global += 1


@staticmethod
def ober_global():
    return Contador.contador_global

# usando a class Contador
