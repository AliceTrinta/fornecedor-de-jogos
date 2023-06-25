import pandas as pd


# Implementing a wrapper
def game_wrapper(func: callable) -> callable:
    """
    Wrapper for the game functions
    :param func: callable: function to be wrapped
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper for the game functions
        :param args: list: list of arguments
        :param kwargs: dict: dictionary of arguments
        """
        game_df = args[0]
        if not isinstance(game_df, pd.DataFrame):
            return None
        return func(*args, **kwargs)
    return wrapper


def create_game_df(game_data: list) -> pd.DataFrame:
    """
    Creates a dataframe with the game data as a list of dictionaries containing the game data
    :param game_data: list - list of dictionaries with the game data
    """
    game_df = pd.DataFrame(game_data)
    return game_df


@game_wrapper
def find_game(game_df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    Searches for a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param name: str: name of the game to be searched
    """
    if game_df['nome'].isin([name]).any():
        return game_df[game_df['nome'] == name]
    return None


@game_wrapper
def insert_game(game_df: pd.DataFrame, game_dict: dict) -> pd.DataFrame:
    """
    Inserts a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param game_dict: dict: dictionary with the game data
    """
    if game_dict['nome'] in game_df['nome'].values:
        return None
    game_df.loc[
        len(game_df)
    ] = game_dict   # Inserting the game in the dataframe
    return game_df


@game_wrapper
def update_game(game_df: pd.DataFrame, game_dict: dict) -> pd.DataFrame:
    """
    Updates a game in the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param game_dict: dict: dictionary with the game data
    """
    name = game_dict['nome']
    if game_df['nome'].isin([name]).any():
        game_df.loc[
            game_df[game_df['nome'] == game_dict['nome']].index, ['preco']
        ] = game_dict['preco']
        game_df.loc[
            game_df[game_df['nome'] == game_dict['nome']].index, ['quantidade']
        ] = game_dict['quantidade']
        return game_df
    return None


@game_wrapper
def delete_game(game_df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    Removes a game from the dataframe
    :param game_df: pd.DataFrame: dataframe with the game data
    :param name: str: name of the game to be removed
    """
    if name not in game_df['nome'].values:
        return None
    game_df.drop(game_df[game_df['nome'] == name].index, inplace=True)
    return game_df
