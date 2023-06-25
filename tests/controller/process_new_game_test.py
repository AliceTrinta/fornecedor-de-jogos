import pandas as pd
from src.controller.controller import *
from src.game.game import *
import pytest


order = './order.xml'
storage = './storage.xml'

def test_process_new_game_empty_or_invalid(mocker):
    """
    Test for the process_new_game function
    When receiving an empty/invalid path string
    Should return False
    """
    expected = False
    result = process_new_game(order, storage)
    assert expected == result


def test_process_new_game_happy_path(mocker):
    """
    Test for the process_new_game function
    When receiving an valid path string
    Should return True
    """

    expected = True
    mocker.patch('src.server.server.new_game', return_value = [mock])
    result = process_new_game(order, storage)
    assert expected == result