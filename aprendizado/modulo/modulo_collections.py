from collections import Counter, namedtuple, deque
from operator import itemgetter

line = "*"
print(line*150)

# Lista de frutas (contagem)
fruits = ["Maça", "Uva", "Pêra", "Laranja", "Maça", "Banana", "Abacaxi", "Uva", "Pêssego", "Cereja", "Melão", "Banana", "Manga", "Limão", "Morango", "Uva"]
print(fruits)
print(Counter(fruits))
print(line*150)

# Utilizar tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game('Resident Evil 4 Remake', 300, 10.0)
print(g1)
print(g2)
print(line*150)

# Ordenar dicionário por chave ou por valor
students = {"Pedro": 23, "Ana": 22, "Ronaldo": 26, "Janaína": 25, "Bruna": 20}
a = sorted(students.items(), key = itemgetter(0))
print(a)
b = sorted(students.items(), key = itemgetter(1))
print(b)
print(line*150)

# Utilizar fila em ambas extremidades
deq = deque([20, 30, 40, 50, 60])
print(deq)
deq.appendleft(10)
print(deq)
deq.append(70)
print(deq)
deq.popleft()
deq.pop
print(deq)
print(line*150)





