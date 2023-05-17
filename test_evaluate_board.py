import ai_engine
from Piece import Knight
import ai_engine
from chess_engine import game_state
from enums import Player


def test_evaluate_board():
    ai = ai_engine.chess_ai()
    game = game_state()
    k1 = Knight('n', 3, 4, Player.PLAYER_1)
    k2 = Knight('n', 1, 3, Player.PLAYER_2)
    k3 = Knight('n', 1, 5, Player.PLAYER_1)
    game.init_empty_board()
    game.board[3][4] = k1
    game.board[1][3] = k2
    game.board[1][5] = k3
    assert ai.evaluate_board(game,Player.PLAYER_1) == -30

