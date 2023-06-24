# Defing test functions for the game dataframe
import pandas as pd
import pytest
from src.game.game import *


def test_create_game_df():
    """
    Test for the create_game_df function
    When receiving a list of dict with games
    Should return a DataFrame with the list content
    """
    game_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}]
    game_df = pd.DataFrame(game_dict_list)
    expected = game_df
    result = create_game_df(game_dict_list)
    assert expected.loc[0, 'nome'] == result.loc[0, 'nome']
    assert expected.loc[0, 'preco'] == result.loc[0, 'preco']
    assert expected.loc[0, 'quantidade'] == result.loc[0, 'quantidade']


def test_find_game():
    """
    Test for the find_game function
    When receiving a DataFrame and a name of a game
    Should return the DataFrame with the game
    """
    game_df = pd.DataFrame(
        [
            {'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
            {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        ]
    )
    expected = pd.DataFrame(
        [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}]
    )
    result = find_game(game_df, 'Jogo 1')
    assert len(result) == len(expected)
    assert expected.loc[0, 'nome'] == result.loc[0, 'nome']
    assert expected.loc[0, 'preco'] == result.loc[0, 'preco']
    assert expected.loc[0, 'quantidade'] == result.loc[0, 'quantidade']


def test_insert_game():
    """
    Test for the insert_game function
    When receiving a DataFrame and a dict of a game
    Should return the DataFrame with the dict of the game appended
    """
    game_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}]
    game_df = pd.DataFrame(game_dict_list)
    expected = pd.DataFrame(
        [
            {'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
            {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        ]
    )
    result = insert_game(
        game_df, {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200}
    )
    assert len(result) == len(expected)
    assert expected.loc[1, 'nome'] == result.loc[1, 'nome']
    assert expected.loc[0, 'preco'] == result.loc[0, 'preco']
    assert expected.loc[0, 'quantidade'] == result.loc[0, 'quantidade']


def test_update_game():
    """
    Test for the update_game function
    When receiving a DataFrame and a dict of a game
    Should return the DataFrame with the dict modified
    """
    game_dict_list = [
        {'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
    ]
    game_df = pd.DataFrame(game_dict_list)
    result = update_game(
        game_df, {'nome': 'Jogo 1', 'preco': 20.0, 'quantidade': 200}
    )
    expected = pd.DataFrame(
        [
            {'nome': 'Jogo 1', 'preco': 20.0, 'quantidade': 200},
            {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        ]
    )
    assert len(result) == len(expected)
    assert expected.loc[0, 'nome'] == result.loc[0, 'nome']
    assert expected.loc[0, 'preco'] == result.loc[0, 'preco']
    assert expected.loc[0, 'quantidade'] == result.loc[0, 'quantidade']


def test_delete_game():
    """
    Test for the delete_game function
    When receiving a DataFrame and a name of a game
    Should return the DataFrame without the dict of the game
    """
    game_dict_list = [
        {'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
    ]
    new_game_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}]
    new_game_df = pd.DataFrame(new_game_dict_list)
    game_df = pd.DataFrame(game_dict_list)
    result = delete_game(game_df, 'Jogo 2')
    expected = new_game_df
    assert len(result) == len(expected)
    assert expected.loc[0, 'nome'] == result.loc[0, 'nome']
    assert expected.loc[0, 'preco'] == result.loc[0, 'preco']
    assert expected.loc[0, 'quantidade'] == result.loc[0, 'quantidade']


def test_wrapper():
    """
    Test for the wrapper function
    When running a function, if game_df is not a DataFrame it should raise a TypeError
    """
    game_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
                      {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200}]
    expected = TypeError
    
    with pytest.raises(expected):
        find_game(game_dict_list, 'Jogo 1')
        insert_game(game_dict_list, {'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200})
        update_game(game_dict_list, {'nome': 'Jogo 1', 'preco': 20.0, 'quantidade': 200})
        delete_game(game_dict_list, 'Jogo 2')
