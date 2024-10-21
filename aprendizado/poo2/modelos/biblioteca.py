class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return f"Nome: {self.nome}"

    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"Nome: {biblioteca.nome} | Ativo: {biblioteca._ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

Biblioteca.listar_bibliotecas()

biblioteca_cidade.alterna_estado()

Biblioteca.listar_bibliotecas()


