from collections import Counter

def filtrarLetrasRepetidas(string):
    totalStrings = Counter(string)

    filtraLetrasRepetidas = filter(lambda item: item[1] > 1, totalStrings.items())

    letrasRepetidas = dict(filtraLetrasRepetidas)

    stringModificada = ''.join(map(lambda letra: "*" if letra in letrasRepetidas else letra, string))


    return stringModificada


gameName = "fifa 23"
print(filtrarLetrasRepetidas(gameName))
