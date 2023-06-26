import pandas as pd
from src.server.server import *

def process_buy_game(gamePath, storagePath):
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
    
    game_string = game.read()

    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False

    storage_string = storage.read()

    retorno = buy_game(game_string, storage_string)
    storage_updated = open("resposta_compra.xml", 'w')
    if type(retorno) == tuple:
        storage_updated.write(retorno[0])
    else:
        storage_updated.write(retorno)

    return True

    

def process_new_game(gamePath, storagePath):
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

    game_string = game.read()

    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False

    storage_string = storage.read()

    retorno = new_game(game_string, storage_string)
    storage_updated = open("resposta_novo.xml", 'w')
    if type(retorno) == tuple:
        storage_updated.write(retorno[0])
    else:
        storage_updated.write(retorno)

    return True
        

def process_delete_from_storage(gamePath, storagePath):
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

    game_string = game.read()

    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False

    storage_string = storage.read()

    retorno = new_game(game_string, storage_string)
    storage_updated = open("resposta_delete.xml", 'w')
    if type(retorno) == tuple:
        storage_updated.write(retorno[0])
    else:
        storage_updated.write(retorno)

   
    return True



def process_update_from_storage(gamePath, storagePath):
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

    game_string = game.read()

    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
        return False

    storage_string = storage.read()

    retorno = update_from_storage(game_string, storage_string)
    storage_updated = open("resposta_update.xml", 'w')
    if type(retorno) == tuple:
        storage_updated.write(retorno[0])
    else:
        storage_updated.write(retorno)

    return True