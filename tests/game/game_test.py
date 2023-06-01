# Defing test functions for the game dataframe
import pandas as pd

from src.game.game import *

def test_create_game_df():
    """
    Test function for the create_game_df function
    """
    game_data = [
        {'id': 1, 'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'id': 2, 'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        {'id': 3, 'nome': 'Jogo 3', 'preco': 30.0, 'quantidade': 300},
    ]
    game_df = create_game_df(game_data)
    assert isinstance(game_df, pd.DataFrame)
    assert len(game_df) == 3
    assert game_df.loc[1, 'nome'] == 'Jogo 1'
    assert game_df.loc[2, 'nome'] == 'Jogo 2'
    assert game_df.loc[3, 'nome'] == 'Jogo 3'


def test_find_game():
    """
    Test function for the find_game function
    """
    game_data = [
        {'id': 1, 'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'id': 2, 'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        {'id': 3, 'nome': 'Jogo 3', 'preco': 30.0, 'quantidade': 300},
    ]
    game_df = create_game_df(game_data)
    game = find_game(game_df, 'Jogo 1')
    assert isinstance(game, pd.DataFrame)
    assert len(game) == 1
    assert game.loc[1, 'nome'] == 'Jogo 1'
    assert game.loc[1, 'preco'] == 10.0


def test_insert_game():
    """
    Test function for the insert_game function
    """
    game_data = [
        {'id': 1, 'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'id': 2, 'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        {'id': 3, 'nome': 'Jogo 3', 'preco': 30.0, 'quantidade': 300},
    ]
    game_df = create_game_df(game_data)
    game_dict = {'id': 4, 'nome': 'Jogo 4', 'preco': 40.0, 'quantidade': 400}
    game_df = insert_game(game_df, game_dict)
    assert isinstance(game_df, pd.DataFrame)
    assert len(game_df) == 4
    assert game_df.loc[4, 'nome'] == 'Jogo 4'
    assert game_df.loc[4, 'preco'] == 40.0


def test_delete_game():
    """
    Test function for the delete_game function
    """
    game_data = [
        {'id': 1, 'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'id': 2, 'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        {'id': 3, 'nome': 'Jogo 3', 'preco': 30.0, 'quantidade': 300},
    ]
    game_df = create_game_df(game_data)
    game_df = delete_game(game_df, 'Jogo 1')
    assert isinstance(game_df, pd.DataFrame)
    assert len(game_df) == 2
    assert game_df.loc[2, 'nome'] == 'Jogo 2'
    assert game_df.loc[3, 'nome'] == 'Jogo 3'


if __name__ == '__main__':
    test_create_game_df()
