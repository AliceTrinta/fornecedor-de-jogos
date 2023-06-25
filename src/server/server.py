from src.converter.converter import *
from src.game.game import *

def scan_from_file_format(file_format_string):
    return xml_to_game(file_format_string)


def save_in_file_format(game_dataframe):
    return game_to_xml(game_dataframe)


def buy_game(game_str, storage_str):
    """
    Sells a game, updating storage according to the order received
    :param game_str: str: order file content string
    :param storage_str: str: storage file content string
    """
    game = scan_from_file_format(game_str)
    if game is None:
        return 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'

    storage = scan_from_file_format(storage_str)
    if storage is None:
        return 'Não há estoque. Tente novamente mais tarde'

    game_from_storage = find_game(storage, game['nome'].iloc[0])

    if game_from_storage is None:
        return 'Jogo não existe no estoque'
    
    name = game['nome'].iloc[0]
    quantity_in_storage = game_from_storage['quantidade'].iloc[0]
    quantity_asked = game_from_storage['quantidade'].iloc[0]
    price = game_from_storage['preco'].iloc[0]

    if quantity_in_storage < quantity_asked:
        new_quantity = quantity_in_storage + 10
        new_storage = update_game(
            storage,
            {'nome': name, 'preco': price, 'quantidade': new_quantity}
        )
        new_storage_file_format = save_in_file_format(new_storage)
        return (
            'Jogo não possui estoque suficiente, tente comprar novamente mais tarde.',
            new_storage_file_format,
        )

    if quantity_in_storage > quantity_asked:
        new_quantity = quantity_in_storage - quantity_asked
        new_storage = update_game(storage,  {'nome': name, 'preco': price, 'quantidade': new_quantity})
        new_storage_file_format = save_in_file_format(new_storage)
        return 'Compra efetuada com sucesso', new_storage_file_format

    if quantity_in_storage == quantity_asked:
        new_quantity = 10
        new_storage = update_game(storage,  {'nome': name, 'preco': price, 'quantidade': new_quantity})
        new_storage_file_format = save_in_file_format(new_storage)
        return 'Compra efetuada com sucesso', new_storage_file_format


def new_game(game_str, storage_str):
    """
    Register a new game on storage according to the order received
    :param game_str: str: order file content string
    :param storage_str: str: storage file content string
    """
    game = scan_from_file_format(game_str)
    if game is None:
        return 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'

    storage = scan_from_file_format(storage_str)
    if storage is None:
        return 'Não há estoque. Tente novamente mais tarde'
    
<<<<<<< HEAD
    game_from_storage = find_game(storage, game['nome'])
=======
    game_from_storage = find_game(storage, game['nome'].iloc[0])
>>>>>>> 1ae278e (Fix)
    if game_from_storage:
        return 'Jogo já existe no estoque'

    new_storage = insert_game(
<<<<<<< HEAD
        storage, {game.loc[0, 'nome'], game.loc[0, 'preco'], 10}
=======
        storage, {'nome': game['nome'].iloc[0], 'preco': game['preco'].iloc[0], 'quantidade': 10}
>>>>>>> 1ae278e (Fix)
    )
    return save_in_file_format(new_storage)


def delete_from_storage(game_str, storage_str):
    """
    :param game_str: str: order file content string
    :param storage_str: str: storage file content string
    """
    game = scan_from_file_format(game_str)
    if game is None:
        return 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'

    storage = scan_from_file_format(storage_str)
    if storage is None:
        return 'Não há estoque. Tente novamente mais tarde'
    
<<<<<<< HEAD
    game_from_storage = find_game(storage, game['nome'])
=======
    game_from_storage = find_game(storage, game['nome'].iloc[0])
>>>>>>> 1ae278e (Fix)

    if game_from_storage is None:
        return 'Jogo não existe no estoque'

<<<<<<< HEAD
    new_storage = delete_game(storage, game.loc[0, 'nome'])
=======
    new_storage = delete_game(storage, game['nome'].iloc[0])
>>>>>>> 1ae278e (Fix)
    return ('Jogo deletado com sucesso', save_in_file_format(new_storage))


def update_from_storage(game_str, storage_str):
    """
    :param game_str: str: order file content string
    :param storage_str: str: storage file content string
    """
    game = scan_from_file_format(game_str)
    if game is None:
        return 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'

    storage = scan_from_file_format(storage_str)
    if storage is None:
        return 'Não há estoque. Tente novamente mais tarde'
    
<<<<<<< HEAD
    game_from_storage = find_game(storage, game['nome'])
=======
    game_from_storage = find_game(storage, game['nome'].iloc[0])
>>>>>>> 1ae278e (Fix)

    if not game_from_storage:
        return 'Jogo não existe no estoque'

    new_storage = update_game(
        storage,
<<<<<<< HEAD
        {game.loc[0, 'nome'], game.loc[0, 'preco'], game.loc[0, 'quantidade']},
=======
        {'nome': game['nome'].iloc[0], 'preco': game['preco'].iloc[0], 'quantidade': game['nome'].iloc[0]},
>>>>>>> 1ae278e (Fix)
    )
    return ('Jogo atualizado com sucesso', save_in_file_format(new_storage))