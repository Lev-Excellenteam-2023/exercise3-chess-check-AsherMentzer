import chess_engine


def test_all_game():
    game_state = chess_engine.game_state()
    game_state.move_piece((1, 2), (2, 2), False)
    game_state.move_piece((6, 3), (5, 3), False)
    game_state.move_piece((1, 1), (3, 1), False)
    game_state.move_piece((7, 4), (3, 0), False)
    endgame = game_state.checkmate_stalemate_checker()
    assert endgame == 0

