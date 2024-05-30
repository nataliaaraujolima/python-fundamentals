gameList = [
    "The Legend of Zelda: Breath of the Wild",
    "Super Mario Odyssey",
    "Red Dead Redemption 2",
    "The Witcher 3: Wild Hunt",
    "Minecraft",
    "Fortnite",
    "God of War",
    "Among Us",
    "Animal Crossing: New Horizons",
    "Hades",
    "Cyberpunk 2077",
    "Doom Eternal",
    "Sekiro: Shadows Die Twice",
    "Apex Legends",
    "Call of Duty: Modern Warfare",
    "Genshin Impact",
    "Hollow Knight",
    "Resident Evil 2",
    "Persona 5",
    "Dark Souls III"
]

# descobrir tamanho da lista
tamanhoDaLista = len(gameList)
print(tamanhoDaLista)

# Recuperar item da lista por indice
recuperaIndice = gameList.index("Among Us")
print("index:",recuperaIndice)

# copiar a lista de jogos e add jogo ao fim da lista
listaCopiada = gameList.copy()

listaCopiada.append("Naruto")
print(listaCopiada)

# Ordenar lista
gameList.sort()
print(gameList)

# remover jogo da lista
gameList.remove("Dark Souls III")
print(gameList)

# limpar toda lista
gameList.clear()
print(gameList)
