class Carro:  # oque é um carro ?

    # construtor - oque precisa para construir um novo carro
    def __init__(self, marca, modelo, ano) -> None:  # atributos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # oque um carro faz ?
    def descrever_carro(self):
        descricao = f"A marca do carro é {self.marca}, modelo {self.modelo} e o ano {self.ano}"
        return descricao

    def buzinar(self):
        return "Beep beep!"


# instancia - > como é o seu carro ?
meu_carro = Carro("Toyota", "Corolla", 2020)

# chamando métodos da instancia / oque fazer com esse carro ?
print(meu_carro.descrever_carro())
print(meu_carro.buzinar())
