from src.server.server import *
import pytest

game_dict_list = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
game_df = pd.DataFrame(game_dict_list)

storage_dict_list_with_game = [{'nome': 'Jogo 3', 'preco': 10.0, 'quantidade': 100}]
storage_with_game_df = pd.DataFrame(storage_dict_list_with_game)

@pytest.mark.skip
def test_new_game_when_order_is_empty_or_invalid():
    """
    Test for the new_game function
    When receiving an empty/invalid order string
    Should return an error message
    """
    expected = 'Solicitação inválida: Sua solicitação é vazia ou seu pedido tem formato invalido'
    result = new_game('', '')
    assert expected == result

@pytest.mark.skip
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
    result = new_game('', '')
    assert expected == result


def test_new_game_when_game_already_exists(mocker):
    """
    Test for the new_game function
    When receiving a valid order
    And the game already exists on storage
    Should return an error message
    """
    mock_scan_from_file_format = mocker.patch('src.server.server.scan_from_file_format')
    mock_scan_from_file_format.side_effect = [game_df, storage_with_game_df]
    mocker.patch('src.game.game.find_game', return_value = game_df)

    expected = 'Jogo já existe no estoque'
    result = new_game('', '')
    assert expected == result
    
