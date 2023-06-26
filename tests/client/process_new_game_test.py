import pandas as pd
from src.client.client import *
from src.game.game import *
import pytest


def test_process_new_game_empty_or_invalid(mocker):
    """
    Test for the process_new_game function
    When receiving an empty/invalid path string
    Should return False
    """
    order = ''
    storage = ''

    expected = False
    result = process_new_game(order, storage)
    assert expected == result


def test_process_new_game_happy_path(mocker):
    """
    Test for the process_new_game function
    When receiving an valid path string
    Should return True
    """
    order = '/home/lucalinux/modular/fornecedor-de-jogos/tests/client/order.xml'
    storage = '/home/lucalinux/modular/fornecedor-de-jogos/tests/client/storage.xml'
    expected = True
    mocker.patch('src.server.server.new_game', return_value = [storage])
    result = process_new_game(order, storage)
    assert expected == result