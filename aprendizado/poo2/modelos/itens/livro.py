from modelos.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):

    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self.isbn = isbn


