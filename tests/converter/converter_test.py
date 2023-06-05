"""import pandas as pd
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
    expected_xml = game_to_xml(game_df)
    assert isinstance(expected_xml, str)
    assert expected_xml.strip().replace('\n', '') == xml_data.strip().replace('\n', '')


def test_xml_to_game():
    expected_df = xml_to_game(xml_data.strip().replace('\n', ''))
    assert isinstance(expected_df, pd.DataFrame)
    assert expected_df.equals(game_df)

