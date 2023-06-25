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

xml_incomplete = """
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>0</index>
    <preco>10.0</preco>
    <quantidade>100</quantidade>
  </row>
</data>
"""

xml_invalid = ""

game_df = pd.DataFrame(game_data)

def test_game_to_xml():
    result = game_to_xml(game_df)
    expected = xml_data
    assert isinstance(result, str)
    assert result.strip().replace('\n', '') == expected.strip().replace('\n', '')

def test_xml_to_game():
    result = xml_to_game(xml_data.strip().replace('\n', ''))
    assert isinstance(result, pd.DataFrame)
    expected = game_df
    assert result.equals(expected)
    
def test_xml_to_game_incomplete():
    expected = xml_incomplete
    result = xml_to_game(expected.strip().replace('\n', '')) 
    assert result is None or result.empty

def test_xml_to_game_invalid():
  expected = None
  result = xml_to_game(xml_invalid.strip().replace('\n', '')) 
  assert result is expected
    