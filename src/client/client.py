import pandas as pd
from src.server.server import *

def process_buy_game(gamePath, storagePath) -> bool:
    """
    Calls buy_game passing file path cont as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False


    print(buy_game(gamePath, storagePath))
    return True
    

def process_new_game(gamePath, storagePath) -> bool:
    """
    Calls new_game passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False


    print(new_game(gamePath, storagePath))
    return True
        

def process_delete_from_storage(gamePath, storagePath) -> bool:
    """
    Calls delete_from_storage passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False


    print(delete_from_storage(gamePath, storagePath))
    return True



def process_update_from_storage(gamePath, storagePath) -> bool:
    """
    Calls update_from_storage passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False

    print(update_from_storage(gamePath, storagePath))
    return True