import pandas as pd
import src.server

def process_buy_game(gamePath, storagePath) -> bool:
    """
    Calls buy_game passing file path as param
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

    print(buy_game(game,storage))
    return True
    

def process_new_game(gamePath, storagePath) -> None:
    """
    Calls new_game passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
    
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")

    print(new_game(game,storage))

        

def process_delete_from_storage(gamePath, storagePath) -> None:
    """
    Calls delete_from_storage passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
    
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")

    print(delete_from_storage(game,storage))



def process_update_from_storage(gamePath, storagePath) -> None:
    """
    Calls update_from_storage passing file path as param
    :param gamePath: Path of the game xml file 
    :param storagePath: Path of the storage xml file 
    """
    try:
        game = open(gamePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
    
    try:
        storage = open(storagePath, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")

    print(update_from_storage(game,storage))
    
'''
def process_save_in_storage(path: str) -> None:
    """
    Calls save_in_storage passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")


    match new_game(xml):
        case 0:
            print("Solicitação feita com sucesso")
        case 1:
            print("Jogos já existem no estoque")
        case 3:
            print("Jogo(s) já existe(m) no estoque")

def process_scan_storage(path: str) -> None:
    """
    Calls scan_storage passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        storage = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
    
    print(f"{scan_storage(xml)}")
'''