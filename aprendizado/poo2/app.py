from modelos.biblioteca import Biblioteca
from modelos.itens.item_biblioteca import ItemBiblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

line="*"
print(line*100)

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()

biblioteca_cidade.receber_avaliacao('Fulano', 8.5)
biblioteca_cidade.receber_avaliacao('Sicrano', 9.5)

print(line*100)

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")


def main():
    Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))

if __name__ == "__main__":
    main()

