from Piece import Knight
from chess_engine import game_state
from enums import Player


def test_get_valid_peaceful_moves_middle() -> None:
    game = game_state()
    k = Knight('n', 3, 4, Player.PLAYER_1)
    game.board = board = [
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY]
    ]
    game.board[3][4] = k
    assert sorted(k.get_valid_peaceful_moves(game)) == [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]


def test_get_valid_peaceful_moves_corner() -> None:
    game = game_state()
    k = Knight('n', 0, 0, Player.PLAYER_1)
    game.board = board = [
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY]
    ]
    game.board[0][0] = k
    assert sorted(k.get_valid_peaceful_moves(game)) == [(1, 2), (2, 1)]


def test_get_valid_peaceful_moves_with_other_pieces() -> None:
    game = game_state()
    k1 = Knight('n', 3, 4, Player.PLAYER_1)
    k2 = Knight('n', 1, 3, Player.PLAYER_1)
    game.board = board = [
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY]
    ]
    game.board[3][4] = k1
    game.board[1][3] = k2
    assert sorted(k1.get_valid_peaceful_moves(game)) == [(1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]


