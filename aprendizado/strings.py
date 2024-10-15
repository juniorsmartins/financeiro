# Case Sensitive

movie1 = "Top Gun"
movie2 = "top Gun"
movie3 = "Top Gun"

print(f"O filme '{movie1}' e o filme '{movie2}' são iguais: {movie1 == movie2}")
print(f"O filme '{movie1}' e o filme '{movie3}' são iguais: {movie1 == movie3}")

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura 
  consagrado na indústria cinematográfica.
"""

print(movieDescription)

# Multiplicação de Strings
line = "*"
print(line*60)
print(movie1)
print(line*30)
print(movieDescription)
print(line*60)


# Procurar palavra dentro de texto
print("Top" in movieDescription)


