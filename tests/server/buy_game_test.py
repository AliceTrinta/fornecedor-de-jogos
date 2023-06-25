from src.server.server import *
import pytest
import logging


order = ''
storage = ''
happy_path_storage = ''
same_quantity_storage = ''

game_dict_list = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 20}]
game_df = pd.DataFrame(game_dict_list)

game_dict_updated = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 80}]
game_df_updated = pd.DataFrame(game_dict_updated)

storage_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}]
storage_df = pd.DataFrame(storage_dict_list)

storage_dict_list_with_game = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
storage_with_game_df = pd.DataFrame(storage_dict_list_with_game)

game_dict_list_same_quantity = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
game_dict_list_same_quantity_df = pd.DataFrame(game_dict_list_same_quantity)

game_dict_list_same_quantity_updated = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
game_dict_list_same_quantity_updated_df = pd.DataFrame(game_dict_list_same_quantity)

less_games_than_requested_storage_dict = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 110}]
less_games_than_requested_storage_df = pd.DataFrame(less_games_than_requested_storage_dict) 

def test_buy_game_when_order_is_empty_or_invalid(mocker):
    """
    Test for the buy_game function
    When receiving an empty/invalid order string
    Should return an error message
    """
    mocker.patch('src.server.server.scan_from_file_format', return_value = None)
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = buy_game('', '')
    assert expected == result

def test_buy_game_when_storage_is_empty(mocker):
    """
    Test for the buy_game function
    When receiving an empty storage string
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, None]
    expected = 'Não há estoque. Tente novamente mais tarde'
    result = buy_game('', '')
    assert expected == result


def test_buy_game_when_game_does_not_exists_on_storage(mocker):
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game does not exists in storage
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_df]
    expected = 'Jogo não existe no estoque'
    result = buy_game('', '')
    assert expected == result

@pytest.mark.skip
def test_buy_game_happy_path(mocker):
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game exists in storage
    And there are more games than requested
    Should return a success message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_with_game_df]
    mocker.patch('src.game.game.update_game', return_value = game_df_updated)
    expected = ('Compra efetuada com sucesso', happy_path_storage)
    result = buy_game('', '')
    assert expected == result

@pytest.mark.skip #Mergear converter
def test_buy_game_when_there_is_same_game_quantity_as_requested():
    """
    Test for the buy_game function
    When receiving a valid and not empty order string
    And receiving a not empty storage string
    And game exists in storage
    And there is the same quantity as requested
    Then increse game quantity in storage
    Should return a success message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_with_game_df]
    mocker.patch('src.game.game.update_game', return_value = game_df_updated)
    expected = ('Compra efetuada com sucesso', same_quantity_storage)
    result = buy_game('', '')
    assert expected == result

@pytest.mark.skip #Mergear converter
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
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_dict_list_same_quantity_df, storage_with_game_df]
    mocker.patch('src.game.game.update_game', return_value = game_dict_list_same_quantity_updated_df)
    expected = (
        'Jogo não possui estoque suficiente, tente comprar novamente mais tarde.',
        less_games_than_requested_storage,
    )
    result = buy_game('', '')
    assert expected == result

def test():
    game = game_to_xml(game_df).strip().replace('\n', '')
    storage = game_to_xml(storage_with_game_df).strip().replace('\n', '')
    logging.info(game)
    logging.info(storage)
    result = buy_game(game, storage)
    assert result == None