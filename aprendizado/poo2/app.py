from modelos.biblioteca import Biblioteca
from modelos.itens.item_biblioteca import ItemBiblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

line="*"

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()

biblioteca_cidade.receber_avaliacao('Fulano', 8.5)
biblioteca_cidade.receber_avaliacao('Sicrano', 9.5)

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
revista1 = Revista("National Geographic", "John Doe", 100.0, "Quinta")
livro2 = Livro("Diário de Holga Weiss", "Holga Weiss", 200.0, "072-5285")

biblioteca_cidade.add_item(livro1)
biblioteca_cidade.add_item(revista1)
biblioteca_cidade.add_item(livro2)


def main():
    Biblioteca.listar_bibliotecas()
    print(line*100)
    print(vars(livro1))
    print(vars(revista1))
    print(line*100)
    biblioteca_cidade.view_itens()

if __name__ == "__main__":
    main()

