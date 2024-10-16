import statistics

# Média de números
print(statistics.mean([3, 4, 5, 4, 5, 3, 2, 6]))

# Mediana 
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))

# Moda (valor que mais se repete)
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6, 3, 3]))

# Desvio padrão (quanto mais próximo de zero for o desvio padrão, significa que os dados estão menos dispersos)
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))




