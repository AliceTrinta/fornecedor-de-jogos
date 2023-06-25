from src.server.server import *
import pytest

order = ''
storage = ''

game_dict_list = [{'nome': 'Jogo 3', 'preco': 5.0, 'quantidade': 100}]
game_df = pd.DataFrame(game_dict_list)

storage_dict_list = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}]
storage_df = pd.DataFrame(storage_dict_list)

storage_dict_list_with_game = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
storage_with_game_df = pd.DataFrame(storage_dict_list)

storage_dict_with_game_df_updated = [{'nome': 'Jogo 1', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 2', 'preco': 10.0, 'quantidade': 100}, {'nome': 'Jogo 3', 'preco': 5.0, 'quantidade': 100}]
storage_with_game_df = pd.DataFrame(storage_dict_with_game_df_updated)

# happy_path_delete_storage = game_to_xml(storage_dict_list)
# happy_path_update_storage = game_to_xml(storage_with_game_df_updated)

def test_delete_from_storage_when_order_is_empty_or_invalid(mocker):
    """
    Test for the delete_from_storage function
    When receiving an empty/invalid order string
    Should return an error message
    """
    mocker.patch('src.server.server.scan_from_file_format', return_value = None)
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = delete_from_storage(order, storage)
    assert expected == result

def test_delete_from_storage_when_game_does_not_exists(mocker):
    """
    Test for the delete_from_storage function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_df]
    expected = 'Jogo não existe no estoque'
    result = delete_from_storage(order, storage)
    assert expected == result

def test_delete_from_storage_when_storage_is_empty(mocker):
    """
    Test for the delete_from_storage function
    When receiving an empty storage string
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, None]
    expected = 'Não há estoque. Tente novamente mais tarde'
    result = delete_from_storage('', '')
    assert expected == result

@pytest.mark.skip # Testar depois de mergear converter
def test_delete_from_storage_happy_path():
    """
    Test for the delete_from_storage function
    When receiving a valid order
    And the game exists on storage
    Should return a success message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_dict_list_with_game]
    expected = ('Jogo deletado com sucesso', happy_path_delete_storage)
    result = delete_from_storage('', '')
    assert expected == result

def test_update_from_storage_when_order_is_empty_or_invalid(mocker):
    """
    Test for the update_from_storage function
    When receiving an empty/invalid order string
    Should return an error message
    """
    mocker.patch('src.server.server.scan_from_file_format', return_value = None)
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = update_from_storage('', '')
    assert expected == result

def test_update_from_storage_when_game_does_not_exists(mocker):
    """
    Test for the update_from_storage function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_df]
    expected = 'Jogo não existe no estoque'
    result = update_from_storage('', '')
    assert expected == result

def test_update_from_storage_when_storage_is_empty(mocker):
    """
    Test for the update_from_storage function
    When receiving an empty storage string
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, None]
    expected = 'Não há estoque. Tente novamente mais tarde'
    result = update_from_storage('', '')
    assert expected == result

@pytest.mark.skip # Testar depois de mergear converter
def test_update_from_storage_happy_path():
    """
    Test for the update_from_storage function
    When receiving a valid order
    And the game exists on storage
    Should return a success message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_dict_list_with_game]
    expected = ('Jogo atualizado com sucesso', happy_path_update_storage)
    result = update_from_storage('', '')
    assert expected == result
