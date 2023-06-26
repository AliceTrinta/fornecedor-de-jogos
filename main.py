import pandas as pd
from src.game.game import *
from src.converter.converter import *
from src.server.server import *
from src.client.client import *


if __name__ == "__main__":
    solicitaçao_path = "solicitacao.xml"
    storage_path = "storage.xml"
    
    process_buy_game(solicitaçao_path, storage_path)
   
def main():
    exit = 0
    while True:
        escolha = input("Escolha uma opção e digite seu numero correspondente: \n1 - Visualizar Estoque\n2 - Atualizar Jogo\n3 - Deletar Jogo\n4 - Ler Compra De Jogo\n5 - Ler adição de Jogo\n6 - sair\n:")
        if escolha == '1':
            print("\nOk\n")
        elif escolha == '2':
            print("\nOk\n")
        elif escolha == '3':
            print("\nOk\n")
        elif escolha == '4':
            print("\nOk\n")
        elif escolha == '5':
            print("\nOk\n")
        elif escolha == '6':
            break
