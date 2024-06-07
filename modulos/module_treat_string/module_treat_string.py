'''
Escreva um módulo em python para tratar algumas strings
e que possua as seguintes funcionalidades:
1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.
'''


def reverse_string(string):
    result = string[::-1]
    result.strip()
    return result


def even_index(string):
    result = string[::2]
    result.strip()
    return result


def odd_index(string):
    result = string[1::2]
    result.strip()
    return result
