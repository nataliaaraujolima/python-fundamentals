from collections import Counter

def filtrar_letras_repetidas(string):
    total_strings = Counter(string)
    
    # Criar um dicionário para rastrear a contagem de letras repetidas
    contagem_letras_repetidas = {letra: total_strings[letra] - 1 for letra in total_strings if total_strings[letra] > 1}
    
    # Substituir apenas a próxima ocorrência de cada letra repetida por '*'
    nova_string = ''
    for letra in string:
        if letra in contagem_letras_repetidas and contagem_letras_repetidas[letra] > 0:
            nova_string += '*'
            contagem_letras_repetidas[letra] -= 1
        else:
            nova_string += letra
    
    return nova_string

gameName = "fifa 23"
print(filtrar_letras_repetidas(gameName))
