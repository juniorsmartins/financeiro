from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()
biblioteca_cidade.alterna_estado()
Biblioteca.listar_bibliotecas()