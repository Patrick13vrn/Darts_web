from MainApp.darts.game import Game
from MainApp.darts.functions import whose_turn

player_1 = 'Алексей'
player_2 = 'Дмитрий'
game_type = 501

turn = whose_turn(player_1, player_2)

new_game = Game(game_type, player_1, player_2, turn)
new_game.start()
