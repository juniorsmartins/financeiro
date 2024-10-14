line = "*"
print(line*75)

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Zorro", "Superman"]
print(moviesList)
print(line*75)

# Iterar valores com While
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

print(line*75)

# Iterar com while e com condição de encerramento
index = 0
while index < len(moviesList):
    if (moviesList[index] == "Jurassic Park"):
        break
    print(moviesList[index])
    index += 1

print(line*75)

# Iterar com while e com condição de avanço
index = 0
while index < len(moviesList):
    if (moviesList[index] == "Jurassic Park"):
        index += 1
        continue
    print(moviesList[index])
    index += 1

print(line*75)

# Avaliações do filme com While
movieName = input("Digite o nome do filme: ")
numberRating = int(input("Digite quantas avaliações quer fazer: "))

total = 0
contador = 0
while contador < numberRating:
    nota = float(input("Digite a nota do filme: "))
    total += nota
    contador += 1

if numberRating > 0:
    media = total / numberRating
else:
    media = 0

print(f"Média de avaliação do filme {movieName} é: {media:.2f}")



print(line*75)