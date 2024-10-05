movieName = "Top Gun of Maverick"
movieDescription = """
    Top Gun Maverick - é um filme de aviação e aventura 
  consagrado na indústria cinematográfica. Além disso, foi 
  sucesso de crítica - inclusive, da concorrência.
"""

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize())
print(movieName.title())

# Retorna string centralizada com caracter de preenchimento
print(movieName.center(30, '-'))

# Procura a posição de um caracter específico
print(movieName.find("u"))

# Contar a quantidade de um caracter específico
print(movieName.count("o"))

# Substituir valores
print(movieName.replace("Top", "Matrix"))

# Quebra a string em partes pelo caracter escolhido
print(movieDescription.split("-"))


