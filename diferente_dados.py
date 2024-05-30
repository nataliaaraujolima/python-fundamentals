# diferença entre listas, tuplas e sets ->  armazenar múltiplos itens

'''
array [] :
   - Ordenada, mutável, elementos duplicados
   - METÓDOS : append(), remove(), pop(), sort(), reverse()
'''
#array
lista = [1, 2, 3, 4, 5]
lista.append(6)  # Adiciona um elemento
lista[0] = 10    # Modifica um elemento
print(lista)     # Saída: [10, 2, 3, 4, 5, 6]

'''
tupla (1,2) :
  - Ordenada, Imutável, elementos duplicados, + de 1 elemento
  - METÓDOS : count(), index()
'''
#dupla
tupla = (1, 2, 3, 4, 5)
# tupla[0] = 10  # Isso causará um erro, pois tuplas são imutáveis
print(tupla)     # Saída: (1, 2, 3, 4, 5)


'''
set {} :
 - Não ordenada, mutável, elementos não duplicados
 - METÓDOS : add(), remove(), union(), intersection(), difference()
'''
#objeto
objeto = {1,2,3,4}
objeto.add(4) #add elemento, será ignorado pois ja existe um n 4
print("4 ignorado",objeto)
