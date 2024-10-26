from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return f"Nome: {self.nome}"

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da Biblioteca'.ljust(25)} | {'Nota Média'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes).ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativo" if self._ativo else "inativo"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = soma / len(self._avaliacao)
        media_arredondada = round(media, 1)
        return media_arredondada

    def add_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def view_itens(self):
        print(f"Library Itens: {self.nome}\n")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "isbn"):
                msg_livro = f"Livro - {i}. Title: {item._title} | Author: {item._author} | Price: {item._price} and Discounted Price: {item.apply_discount()} | ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"Revista - {i}. Title: {item._title} | Author: {item._author} | Price: {item._price} and Discounted Price: {item.apply_discount()} | Edition: {item.edition}"
                print(msg_revista)


