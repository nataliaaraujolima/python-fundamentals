'''
dic -> colecao de pares e chaves
meu_dict = {
    "nome": "Alice",
    "idade": 30,
    "profissao": "Engenheira"
}
METÓDOS:
    - keys(): Retorna uma visão das chaves.
    - values(): Retorna uma visão dos valores.
    - items(): Retorna uma visão dos pares chave-valor.
    - get(): Retorna o valor para uma chave, ou None se a chave não existir.
    - update(): Atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares.
'''
# 1 forma de escrever dict
obj_dic = {
    "name": "alucard",
    "age": 28,
    "food": ["pizza","sushi"]
}

# 2 forma de escrever dic -> function dict()
my_obj_dic = dict(name="alucard", age="28", food= ["pizza","sushi"])
print(my_obj_dic)
print(my_obj_dic["name"]) #acessar valor por []
my_obj_dic["name"] = "bestial" #alterar name
print(my_obj_dic["name"])
print(my_obj_dic.keys()) #retorna keys
print(my_obj_dic.values()) #reotrna values
print(my_obj_dic.items()) #retorna tupla com keys e values
print(my_obj_dic.get("age")) #reotrna values dde uma key especifica
