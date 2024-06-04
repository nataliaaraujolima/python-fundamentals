'''
2. **args** quando não temos a certeza de quantos argumentos vamos ter dentro de uma função. Ao utilizá-lo, deixamos essa informação dinâmica e variável. Os argumentos são passados como uma tupla.
3. Utilizamos o ****kwargs** para passar além dos valores, as respectivas chaves para os seus argumentos. Os argumentos são passados como um dicionário.
'''


def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")


print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")
