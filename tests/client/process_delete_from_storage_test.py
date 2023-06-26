import pandas as pd
from src.client.client import *
from src.game.game import *	
import pytest


order = ''
storage = ''

def test_process_delete_from_storage_empty_or_invalid(mocker):
    """
    Test for the process_delete_from_storage function
    When receiving an empty/invalid path string
    Should return False
    """
    order = ''
    storage = ''

    expected = False
    result = process_delete_from_storage(order, storage)
    assert expected == result




def test_process_delete_from_storage_happy_path(mocker):
    """
    Test for the process_delete_from_storage function
    When receiving an valid path string
    Should return True
    """
    order = 'solicitacao.xml'
    storage = 'storage.xml'
    
    expected = True
    result = process_delete_from_storage(order, storage)
    assert expected == result
