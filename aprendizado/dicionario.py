filmInception = {
    "title" : "Inception",
    "yearRelease" : 2010,
    "imdbRating" : 8.8,
    "genre" : ["Sci-fi", "Action", "Thriller"],
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# Recuperar elemento do dicionário - jeito 1
print(filmInception["title"])
print(filmInception["genre"])

# Recuperar elemento do dicionário - jeito 2
print(filmInception.get("title"))
print(filmInception.get("imdbRating"))

# Buscar todas e somente as chaves do dicionário
print(filmInception.keys())

# Buscar todos e somente os valores do dicionário
print(filmInception.values())

# Buscar chave e valor 
print(filmInception.items())

# Adicionar itens no dicionário
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# Adicionar itens
filmInception.update({"imdbRating" : 8.7})
print(filmInception)

# Remover item
filmInception.pop("director")
print(filmInception)


