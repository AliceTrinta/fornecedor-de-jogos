import pandas as pd
from src.game.game import *
from src.converter.converter import *
from src.server.server import *
from src.client.client import *


if __name__ == "__main__":
    solicitaçao_path = "solicitacao.xml"
    storage_path = "storage.xml"
    
    process_buy_game(solicitaçao_path, storage_path)
   
