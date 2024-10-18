# Classe que será usada na composição de outra
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

# Classe que será composta por Game
class GameStudio:

    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda não lançou jogo.")
        else:
            average_note = total_notes / num_games
            print(f"Avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}")

# Teste
game1 = Game("The Legend of Zelda", 2017, False, 7.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("The Last of Us II", 2020, False, 8.5)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()

