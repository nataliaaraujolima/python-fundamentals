from collections import Counter

def filtrar_letras_repetidas(string):
    total_strings = Counter(string)
    
    filtra_letras_repetidas = filter(lambda item: item[1] > 1, total_strings.items())
    letras_repetidas = dict(filtra_letras_repetidas)
    
    def substituir_proxima(letra):
        if letra in letras_repetidas:
            letras_repetidas.pop(letra)
            return '*'
        return letra
    
    string_modificada = ''.join(map(substituir_proxima, string))
    
    return string_modificada

gameName = "fifa 23"
print(filtrar_letras_repetidas(gameName))
