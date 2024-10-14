line = "*"
print(line*75)

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Zorro", "Superman"]
print(moviesList)
print(line*75)

# Iterar valores da lista
for movie in moviesList:
    print(movie)
print(line*75)

# Iteração de valores da lista com condição de encerramento
for movie in moviesList:
    if (movie == "Jurassic Park"):
        break
    print(movie)
print(line*75)

# Iteração de valores da lista com condição de avanço
for movie in moviesList:
    if (movie == "Inception"):
        continue
    print(movie)
print(line*75)

# Avaliações do filme
movieName = input("Digite o nome do filme: ")
numberRating = int(input("Digite quantas avaliações quer fazer: "))

total = 0
for i in range(numberRating):
    nota = float(input("Digite a nota do filme: "))
    total += nota

if numberRating > 0:
    media = total / numberRating
else:
    media = 0

print(f"Média de avaliação do filme {movieName} é: {media:.2f}")


print(line*75)

