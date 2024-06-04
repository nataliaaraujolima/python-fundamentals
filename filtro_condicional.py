'''
1 - crie um array de objetos contendo id, nome do personagem, classe e mensagem
'''
arrayObj = [ 
        {"id": 1,
          "nomePersonagem" : "naruto",
         "classePersonagem" : "Guerreiro",
         "msgClasse": "Você é um Guerreiro valente, forte e corajoso!"
         },
        {"id": 2,
          "nomePersonagem" : "sasuke",
         "classePersonagem" : "Curandeiro",
         "msgClasse": "Você é um Curandeiro benevolente, curando feridos em batalha!"
         }
      ]

# 2 - filtre o array de objetos e compare com cada tipo de classificacao com a mensagem

filtro = list(filter(lambda x: x["nomePersonagem"] == "naruto", arrayObj))
print(filtro)