from modelos.itens.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):

    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.edition = edition

    def apply_discount(self):
        return self._price - (self._price * 0.05)

