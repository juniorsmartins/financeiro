from modelos.itens.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):

    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.edition = edition

