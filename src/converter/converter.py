import pandas as pd


def game_to_xml(game_data: pd.DataFrame):
    game_df = pd.DataFrame(game_data)
    xml_data = game_df.to_xml(root_name='data', row_name='row')

    with open('game_data.xml', 'w') as f:
        f.write(xml_data)


def xml_to_game(xml_file):
    game_df = pd.read_xml(xml_file)
    return game_df
