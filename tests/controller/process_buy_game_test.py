import pandas as pd
from src.controller.controller import *
from src.server.server import *
from src.game.game import *	
import pytest


order = ''
storage = ''

def test_process_buy_game_empty_or_invalid(mocker):
    """
    Test for the process_buy_game function
    When receiving an empty/invalid path string
    Should return False
    """
    expected = False
    result = process_buy_game(order, storage)
    assert expected == result


def test_process_buy_game_happy_path(mocker):
    """
    Test for the process_buy_game function
    When receiving an valid path string
    Should return True
    """

    expected = True
    mocker.patch('src.server.server.buy_game', return_value = ['Compra efetuada com sucesso', mock_scan_from_file_format])
    result = process_buy_game(order, storage)
    assert expected == result