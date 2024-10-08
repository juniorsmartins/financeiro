filmsSet = {"Inception", "Zorro", "The Dark", "Pulp Fiction", "Intocáveis", "Senhor dos Anéis"}

print(type(filmsSet))

# Buscar tamanho do Set
print(len(filmsSet))

# True e 1 são considerados o mesmo valor
exempleSet = {"Inception", True, 1, 8.7}
print(exempleSet)

# Adicionar itens de um set em outro set
filmsSet.update(exempleSet)
print(filmsSet)

# Remover item do Set
filmsSet.remove(8.7)
print(filmsSet)



