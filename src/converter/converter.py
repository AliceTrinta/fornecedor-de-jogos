import pandas as pd

def game_to_xml(game_data: pd.DataFrame) -> str:
    xml_data = game_data.to_xml(root_name='data', row_name='row') 
    return xml_data

def xml_to_game(xml_file: str) -> pd.DataFrame:
    game_data = pd.read_xml(xml_file)
    return game_data

