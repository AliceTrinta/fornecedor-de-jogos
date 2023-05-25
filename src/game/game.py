import pandas as pd


def create_game_df(game_data: list) -> pd.DataFrame:
    """
    Creates a dataframe with the game data as a list of dictionaries containing the game data
    :param game_data: list: list of dictionaries with the game data
    """
    game_df = pd.DataFrame(
        game_data
    )   # Creating a dataframe with the game data
    game_df.set_index('id', inplace=True)   # Setting the game id as the index
    return game_df


def find_game(game_df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    Searches for a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param name: str: name of the game to be searched
    """
    if name not in game_df['nome'].values:
        raise Exception('Game not found')
    return game_df[game_df['nome'] == name]


def insert_game(game_df: pd.DataFrame, game_dict: dict) -> pd.DataFrame:
    """
    Inserts a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param game_dict: dict: dictionary with the game data
    """
    if game_dict['nome'] in game_df['nome'].values:
        game_df.drop(
            game_df[game_df['nome'] == game_dict['nome']].index, inplace=True
        )   # Removing the game from the dataframe
    if game_df.empty:
        raise Exception('Empty dataframe')
    game_df.loc[
        len(game_df) + 1
    ] = game_dict   # Inserting the game in the dataframe
    return game_df


def update_game(game_df: pd.DataFrame, game_dict: dict) -> pd.DataFrame:
    """
    Updates a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param game_dict: dict: dictionary with the game data
    """
    if game_dict['nome'] in game_df['nome'].values:
        game_df.replace(
            game_df[game_df['nome'] == game_dict['nome']].index, inplace=True
        )   # Consertar replace
    if game_df.empty:
        raise Exception('Empty dataframe')
    return game_df


def delete_game(game_df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    Removes a game from the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param name: str: name of the game to be removed
    """
    if name not in game_df['nome'].values:
        raise Exception('Game not found')
    game_df.drop(
        game_df[game_df['nome'] == name].index, inplace=True
    )   # Removing the game from the dataframe
    return game_df
