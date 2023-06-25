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

    game_from_storage = find_game(storage, game['nome'])

    if not game_from_storage:
        return 'Jogo não existe no estoque'
    
    name = game.loc[0, 'nome']
    quantity_in_storage = game_from_storage.loc[0, 'quantidade']
    quantity_asked = game.loc[0, 'quantidade']
    price = game_from_storage.loc[0, 'preco']

    if quantity_in_storage < quantity_asked:
        new_quantity = quantity_in_storage + 10
        new_storage = update_game(
            storage,
            {name, game_from_storage.loc[0, 'preco'], new_quantity},
        )
        new_storage_file_format = save_in_file_format(new_storage)
        return (
            'Jogo não possui estoque suficiente, tente comprar novamente mais tarde.',
            new_storage_file_format,
        )

    if quantity_in_storage > quantity_asked:
        new_quantity = quantity_in_storage - quantity_asked
        new_storage = update_game(storage, {name, price, new_quantity})
        new_storage_file_format = save_in_file_format(new_storage)
        return 'Compra efetuada com sucesso', new_storage_file_format

    if quantity_in_storage == quantity_asked:
        new_quantity = 10
        new_storage = update_game(storage, {name, price, new_quantity})
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
    
    game_from_storage = find_game(storage, game['nome'])
    if game_from_storage:
        return 'Jogo já existe no estoque'

    new_storage = insert_game(
        storage, {game.loc[0, 'nome'], game.loc[0, 'preco'], 10}
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
    
    game_from_storage = find_game(storage, game['nome'])

    if not game_from_storage:
        return 'Jogo não existe no estoque'

    new_storage = delete_game(storage, game.loc[0, 'nome'])
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
    
    game_from_storage = find_game(storage, game['nome'])

    if not game_from_storage:
        return 'Jogo não existe no estoque'

    new_storage = update_game(
        storage,
        {game.loc[0, 'nome'], game.loc[0, 'preco'], game.loc[0, 'quantidade']},
    )
    return ('Jogo atualizado com sucesso', save_in_file_format(new_storage))
