'''
múltiplos pares de chave-valor

Exercício: Classificação de Personagens de Anime
Escreva um programa que pergunte ao usuário o nome e a classe de um personagem de um anime. Baseado na classe fornecida,
o programa deve exibir uma mensagem específica sobre o personagem.

Classes e Mensagens:
Guerreiro: "Você é um Guerreiro valente, forte e corajoso!"
Mago: "Você é um Mago sábio, mestre das artes arcanas!"
Curandeiro: "Você é um Curandeiro benevolente, curando feridos em batalha!"
Arqueiro: "Você é um Arqueiro ágil, preciso e letal à distância!"
Qualquer outra entrada: "Classe desconhecida! Você é um personagem misterioso."
'''


nomePersoangem = input("Digire o nome do personagem \n")
classePersonagem = input("Digite a classe do personagem (Guerreiro, Mago, Curandeiro, Arqueiro): ")

if classePersonagem.lower() == "guerreiro":
    print(f'{nomePersoangem} Você é um Guerreiro valente, forte e corajoso!')
elif classePersonagem.lower() == "mago":
    print(f'{nomePersoangem} Você é um Mago sábio, mestre das artes arcanas!')
elif classePersonagem.lower() == "Curandeiro":
    print(f'{nomePersoangem} Você é um Curandeiro benevolente, curando feridos em batalha!')
else:
    print('Classe desconhecida! Você é um personagem misterioso.')