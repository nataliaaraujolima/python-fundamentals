obj = {
    "nomePersonagem": "naruto",
    "classe": "mago",
}  
''' funcao getNameAndClasseAObject ::
- function que recebe um dic (objeto)
- extrai values das keys
- retorna esses values numa tupla ()
- desestrutura a tupla atribuindo os valores a duas variáveis separadas  nameCharacter e classeCharacter
'''
def getNameAndClasseAObject(array):
  nameCharacter = array.get("nomePersonagem")
  classeCharacter = array.get("classe")
  return nameCharacter, classeCharacter 
  
result = getNameAndClasseAObject(obj)
print(result)

nameCharacter, classeCharacter = result
print(nameCharacter, classeCharacter)


def sayMessageClasse(name, classe):
    if classe.lower() == "guerreiro":
        return f'{name} Você é um Guerreiro valente, forte e corajoso!'
    elif classe.lower() == "mago":
        return f'{name} Você é um Mago sábio, mestre das artes arcanas!'
    elif classe.lower() == "curandeiro":
        return f'{name} Você é um Curandeiro benevolente, curando feridos em batalha!'
    else:
        return 'Classe desconhecida! Você é um personagem misterioso.'
    
result2 = sayMessageClasse(nameCharacter, classeCharacter)
print(result2)