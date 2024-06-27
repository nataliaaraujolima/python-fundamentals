from collections import namedtuple

# dois argumentos: o nome da nova classe e uma lista de nomes de campo
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # Saída: 1 2
