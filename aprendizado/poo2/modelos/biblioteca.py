from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
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

