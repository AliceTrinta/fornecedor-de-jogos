import pandas as pd
from src.converter.converter import *
from src.game.game import *

game_data = [
        {'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}
    ]

xml_data = """
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>0</index>
    <nome>Jogo 1</nome>
    <preco>10.0</preco>
    <quantidade>100</quantidade>
  </row>
</data>
"""
game_df = pd.DataFrame(game_data)

def test_game_to_xml():
    xml_str = game_to_xml(game_df)
    assert isinstance(xml_str, str)
    assert xml_str.strip().replace('\n', '') == xml_data.strip().replace('\n', '')


def test_xml_to_game():
    game_df = xml_to_game(xml_data.strip().replace('\n', ''))
    
    assert isinstance(game_df, pd.DataFrame)
    assert game_df.equals(game_df)

    
