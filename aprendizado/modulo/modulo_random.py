import random

line = "*"
print(line*100)

# Selecionar valor aleatório de lista
list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))
print(line*100)

# Gerar número aleatório em intervalo de valores
r1 = random.randint(5, 15)
print(r1)
print(line*100)

# Selecionar caracter aleatório de string
name = "Curso Python"
r2 = random.choice(name)
print(r2)
print(line*100)

# Selecionar mais de um valor aleatório
# random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))

s = "Olá, mundo!"
print(random.sample(s, 2))

print(line*100)

    


