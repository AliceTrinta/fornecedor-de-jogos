from src.server.server import *


order = ''
storage = ''
happy_path_delete_storage = ''
happy_path_update_storage = ''


def test_delete_from_storage_when_order_is_empty_or_invalid():
    """
    Test for the delete_from_storage function
    When receiving an empty/invalid order string
    Should return an error message
    """
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = delete_from_storage('', storage)
    assert expected == result


def test_delete_from_storage_when_game_does_not_exists():
    """
    Test for the delete_from_storage function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    expected = 'Jogo não existe no estoque'
    result = delete_from_storage(order, storage)
    assert expected == result


def test_delete_from_storage_happy_path():
    """
    Test for the delete_from_storage function
    When receiving a valid order
    And the game exists on storage
    Should return a success message
    """
    expected = ('Jogo deletado com sucesso', happy_path_delete_storage)
    result = delete_from_storage(order, storage)
    assert expected == result


def test_update_from_storage_when_order_is_empty_or_invalid():
    """
    Test for the update_from_storage function
    When receiving an empty/invalid order string
    Should return an error message
    """
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = update_from_storage('', storage)
    assert expected == result


def test_update_from_storage_when_game_does_not_exists():
    """
    Test for the update_from_storage function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    expected = 'Jogo não existe no estoque'
    result = update_from_storage(order, storage)
    assert expected == result


def test_update_from_storage_happy_path():
    """
    Test for the update_from_storage function
    When receiving a valid order
    And the game exists on storage
    Should return a success message
    """
    expected = ('Jogo atualizado com sucesso', happy_path_update_storage)
    result = update_from_storage(order, storage)
    assert expected == result
