"""import pandas as pd
from src.converter.converter import *
from src.game.game import *


def test_game_to_xml():
    game_data = [
        {'id': 1, 'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100},
        {'id': 2, 'nome': 'Jogo 2', 'preco': 20.0, 'quantidade': 200},
        {'id': 3, 'nome': 'Jogo 3', 'preco': 30.0, 'quantidade': 300},
    ]

    game_df = create_game_df(game_data)
    game_to_xml(game_df)   # tem ainda que checar se o arquivo xml foi feito


def test_xml_to_game():
    game_df = xml_to_game('game_data.xml')
    assert isinstance(game_df, pd.DataFrame)
    assert len(game_df) == 3
    assert game_df.loc[1, 'nome'] == 'Jogo 1'
    assert game_df.loc[2, 'nome'] == 'Jogo 2'
    assert game_df.loc[3, 'nome'] == 'Jogo 3'
"""
