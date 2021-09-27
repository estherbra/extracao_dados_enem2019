##Extração de dados do Enem 2019
#Importar bibliotecas necessárias
import pandas as pd
import numpy as np
import zipfile
import requests
from io import BytesIO
import os

#Criar diretórios para armazenamento do conteúdo
os.makedirs('./enem2019', exist_ok=True)

#Define a URL
url= "https://download.inep.gov.br/microdados/microdados_enem_2019.zip"

#Faz download do conteúdo
filebytes = BytesIO(
    requests.get(url).content
)

#Extrai o conteúdo do arquivo zip
myzip = zipfile.ZipFile(filebytes)
myzip.extractall('./enem2019')

##Verifica os itens baixados
enem = pd.read_csv(
    './enem2019/DADOS/MICRODADOS_ENEM_2019.csv' , engine = 'python' , sep = ';' , decimal = ','
)
