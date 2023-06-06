from src.server.server import *


order = ''
storage = ''
happy_path_storage = ''


def test_new_game_when_order_is_empty_or_invalid():
    """
    Test for the new_game function
    When receiving an empty/invalid order string
    Should return an error message
    """
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = new_game('', storage)
    assert expected == result


def test_new_game_happy_path():
    """
    Test for the new_game function
    When receiving a valid order
    Should add game in storage with quantity equal 10
    Then return a success message
    """
    expected = (
        'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido',
        happy_path_storage,
    )
    result = new_game(order, storage)
    assert expected == result


def test_new_game_when_game_already_exists():
    """
    Test for the new_game function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    expected = 'Jogo já existe no estoque'
    result = new_game(order, storage)
    assert expected == result
