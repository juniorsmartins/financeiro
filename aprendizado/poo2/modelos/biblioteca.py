class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return f"Nome: {self.nome}"

    @classmethod
    def listar_bibliotecas(cls):
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativo" if self._ativo else "inativo"

