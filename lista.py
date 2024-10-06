film = []
print(type(film))

# Adicionar item no final da lista
film.append("Top")
film.append("Gun")

print(film)


filmMatrix = ["Matrix", 1999, 8.7, True]
print(filmMatrix)


filmList = ["Inception", "Zorro", "The Dark", "Pulp Fiction", "Intocáveis", "Senhor dos Anéis"]

# Buscar os dois primeiros filmes da lista
print(filmList[:2])

# Buscar o último item da lista
print(filmList[-1])

# Buscar filme do índice inicial e até anterior ao índice final
print(filmList[1:3])

# Tamanho de lista
print(len(filmList))

# Recuperar o índice de um item da lista
print(filmList.index("Senhor dos Anéis"))

# Ordenar lista
print(filmList)
filmList.sort()
print(filmList)

# Copiar os itens de uma lista para outra
filmListCopy = filmList.copy()
print(filmListCopy)

# Remover item da lista
filmListCopy.remove("Zorro")
print(filmListCopy)

# Remove todos os itens da lista
filmListCopy.clear()
print(f"Lista vazia: {filmListCopy}")



