import pandas as pd
import src.server

def process_buy_game(path: str) -> None:
    """
    Calls buy_game passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")


    match buy_game(xml):
        case 0:
            print("Jogo comprado com sucesso")
        case 1:
            print("Jogo não existe no estoque")
        case 2:
            print("Jogo não possui quantidade necessária")


def process_new_game(path: str) -> None:
    """
    Calls new_game passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")


    match new_game(xml):
        case 0:
            print("Solicitação de compra feita com sucesso")
        case 1:
            print("Jogo já existe no estoque")


def process_scan_storage(path: str) -> None:
    """
    Calls scan_storage passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")
    
    print(f"{scan_storage(xml)}")
        

def process_delete_from_storage(path: str) -> None:
    """
    Calls delete_from_storage passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")


    match new_game(xml):
        case 0:
            print("Remoção feita com sucesso")
        case 1:
            print("Jogo não existe no estoque")



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


def process_update_from_storage(path: str) -> None:
    """
    Calls update_from_storage passing file path as param
    :param path: str: Path of the xml file 
    """
    try:
        xml = open(path, 'r')
    except FileNotFoundError as exception1:
        print(f"Arquivo não existe\n"f"{exception1}")


    match new_game(xml):
        case 0:
            print("Jogo alterado com sucesso")
        case 1:
            print("Jogo não existe no estoque")

def read_xml:

def write_xml: