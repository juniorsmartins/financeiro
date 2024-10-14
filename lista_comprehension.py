# listar valores de 0 a 10, que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Zorro", "Superman"]

# Imprimir filmes com a letra 'e' no título
moviesWhithE = [movie for movie in moviesList if 'e' in movie.lower()]
print(moviesWhithE)

# Listar filme que assisti
moviesWatched = [movie for movie in moviesList if movie != "Jurassic Park"]
print(moviesWatched)

# Encontrar filme pelo nome
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar): ")
    if searchName.lower() == "sair":
        print("Programa Encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado com o nome: {searchName}")
    else:
        print(f"Nenhum filme encontrado com o nome: {searchName}")
    


