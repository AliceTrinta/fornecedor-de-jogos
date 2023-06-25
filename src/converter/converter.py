import pandas as pd
import xml.etree.ElementTree as ET

def game_to_xml(game_data: pd.DataFrame) -> str: 
    xml_data = game_data.to_xml(root_name='data', row_name='row') 
    return xml_data

def xml_to_game(xml_file: str) -> pd.DataFrame:
    try:
        xml_file = xml_file.strip().replace('\n', '') 
        root = ET.fromstring(xml_file)
        
        preco_element = root.find('row/preco')
        quantidade_element = root.find('row/quantidade')
        nome_element = root.find('row/nome')
        
        if preco_element is None or quantidade_element is None or nome_element is None:
            return None
        else:
            game_data = pd.read_xml(xml_file)
            game_data = game_data.drop(columns=['index'])
            return game_data
        
    except ET.ParseError:
        return None

      
      
      
      
      
      
      
      
