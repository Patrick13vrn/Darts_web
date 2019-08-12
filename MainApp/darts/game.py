from MainApp.darts.player import Player


class Game:
    """
    Initiates new game
    turn == 0 - player_1 starts a game
    turn == 1 - player_2 starts a game
    """

    def __init__(self, game_type, player_1, player_2, turn):
        self.game_type = game_type
        self.end = False
        if turn == 0:
            self.player_1 = player_1
            self.player_2 = player_2
        else:
            self.player_1 = player_2
            self.player_2 = player_1

    def start(self):
        player_1 = Player(self.player_1, self.game_type)
        player_2 = Player(self.player_2, self.game_type)

        while True:
            if not (player_1.end or player_2.end):
                player_1.throws()
            else:
                break

            if not (player_1.end or player_2.end):
                player_2.throws()
            else:
                break
