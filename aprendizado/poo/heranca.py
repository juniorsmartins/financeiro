# Superclasse
class Game:

    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note        

    def __str__(self):
        return f"Nome do Game: {self.name}"
    
    def technical_sheet(self):
        print(f"Nome do Game: {self.name} | Ano de Lançamento: {self.yearLaunch} | Multiplayer: {self.multiplayer} | Nota: {self.note}")

# Subclasse
class SinglePlayerGame(Game):

    def __init__(self, name="", yearLaunch=0, note=0, storyLine=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyLine = storyLine

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyLine}")


# Teste de herança
line = "*"
print(line*100)

mult_game = Game("Fortnite", 2017, True, 8.0)
mult_game.technical_sheet()
print(line*100)

sing_game = SinglePlayerGame("The Last of Us 2", 2020, 9.5, "Emocionante história de sobrevivência entre mortos-vivos")
sing_game.technical_sheet()
print(line*100)

