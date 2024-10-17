class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

    def __str__(self):
        return f"Nome do Game: {self.name}"
    
    def technical_sheet(self):
        return f"Nome do Game: {self.name} | Ano de Lançamento: {self.yearLaunch} | Multiplayer: {self.multiplayer} | Nota: {self.note}"

# Primeiro Jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

print(game1)
print(game1.technical_sheet())



