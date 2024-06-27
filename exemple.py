class Carro:  # oque é

    def __init__(self, marca, modelo, ano) -> None: # oque faz
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def descrever_carro(self):
        descricao = f"A marca do carro é {self.marca}, modelo {self.modelo} e o ano {self.ano}"
        return descricao

    def buzinar(self):
        return "Beep beep!"


meu_carro = Carro("Toyota","Corolla",2020) # instancia da classe / como é

print(meu_carro.descrever_carro()) # chamando métodos da instancia / oque fazer
print(meu_carro.buzinar())
