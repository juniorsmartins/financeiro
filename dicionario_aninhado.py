import pprint

filmsDict = {
    "Inception" : {
        "yearRelease" : 2010,
        "imdbRating" : 8.9,
        "genre" : ["Sci-fi", "Action", "Thriller"]
    },
    "Interstellar" : {
        "yearRelease" : 2014,
        "imdbRating" : 8.6,
        "genre" : ["Sci-fi", "Drama"]
    },
    "The Dark Knight" : {
        "yearRelease" : 2008,
        "imdbRating" : 9.0,
        "genre" : ["Action", "Drama", "Crime"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# Buscar informação dentro de dicionário aninhado
print(filmsDict["Interstellar"]["genre"])

# Adicionar novo item
filmsDict["Inception"]["director"] = "Christopher Nolan"
print(filmsDict["Inception"])

# Excluir item do dicionário
del filmsDict["The Dark Knight"]
pp.pprint(filmsDict)

