# tuplas são estruturas de dados imutáveis e ordenadas, que podem armazenar uma coleção de itens
gameList = (
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
)

print(type(gameList))

''' # Imutabilidade
Se você não precisa modificar os dados depois de criá-los, tuplas são a escolha ideal.
A imutabilidade das tuplas pode ajudar a evitar bugs causados por alterações inesperadas nos dados.'''

''' podemos fazer uma analogia entre desestruturação de valores em Python com React '''

#pyton
def getUser():
    name = "Alucard"
    age=  28

    return name, age

name,age = getUser()

'''
react
const [contador, setContador] = useState(0);

'''
