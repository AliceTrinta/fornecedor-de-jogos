from src.server.server import *


order = ''
storage = ''
happy_path_storage = ''
less_games_than_requested_storage = ''
same_quantity_storage = ''


def test_buy_game_when_order_is_empty_or_invalid():
    """
    Test for the buy_game function
    When receiving an empty/invalid order string
    Should return an error message
    """
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = buy_game('', storage)
    assert expected == result


def test_buy_game_when_storage_is_empty():
    """
    Test for the buy_game function
    When receiving an empty storage string
    Should return an error message
    """
    expected = 'Estoque vazio.'
    result = buy_game(order, '')
    assert expected == result


def test_buy_game_when_game_does_not_exists_on_storage():
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game does not exists in storage
    Should return an error message
    """
    expected = 'Jogo não encontrado no estoque.'
    result = buy_game(order, storage)
    assert expected == result


def test_buy_game_happy_path():
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game exists in storage
    And there are more games than requested
    Should return a success message
    """
    expected = ('Compra efetuada com sucesso', happy_path_storage)
    result = buy_game(order, storage)
    assert expected == result


def test_buy_game_when_there_is_same_game_quantity_as_requested():
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game exists in storage
    And there is the same quantity as requested
    Then increse game quantity in storage
    Should return an error message
    """
    expected = ('Compra efetuada com sucesso', same_quantity_storage)
    result = buy_game(order, storage)
    assert expected == result


def test_buy_game_when_there_are_less_games_than_requested():
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game exists in storage
    And there are less games than requested
    Then increse game quantity in storage
    Should return an error message
    """
    expected = (
        'Jogo não possui estoque suficiente, tente comprar novamente mais tarde.',
        less_games_than_requested_storage,
    )
    result = buy_game(order, storage)
    assert expected == result
