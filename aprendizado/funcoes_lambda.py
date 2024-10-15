# Função de potência de um número
power = lambda num: num ** 2

print(power(5))
print(power(9))

# Função para verificar se número é par
is_even = lambda x: x % 2 == 0

print(is_even(27))
print(is_even(30))

# Função para dividir um número por outro
div_num = lambda x, y: x / y

print(div_num(5, 2))
print(div_num(12, 3))
print(f"{div_num(10, 3):.2f}")

# Função para inverter string
reverse_string = lambda s: s[::-1]

print(reverse_string("Python"))


# Funcionalidades
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 8.0],
    "The Godfather": [9.5, 9.8, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.0],
    "Matrix": [8.8, 9.2, 8.5],
}

# Função para calcular a média de notas de um filme
average_ratings = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f"A média de avaliação do filme Matrix: {average_ratings("Matrix"):.2f}")

# Função para verificar se filme está na lista
check_movie = lambda movie_name: movie_name in moviesList

print(f"Inception está na lista? {check_movie("Inception")}")

# Função para recomendar filme com média de avaliação
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_ratings(movie_name):.2f}"

print(f"{recommend_movie("Titanic")}")


