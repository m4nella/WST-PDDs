# CODIGO APENAS PARA GERAR O CSV :)
import pandas as pd
from bs4 import BeautifulSoup

caminho_arquivo_html = 'T:/1DS-MB-B/Emanuelle Jesus Silva/FPOO-Formativa-WebScraping_E-commerce.html'

with open(caminho_arquivo_html, 'r', encoding='utf-8') as arquivo:
    info = arquivo.read()
soup = BeautifulSoup(info, 'html.parser')

# encontrar tabelas
tabela = soup.find('table')

# pegando as info da tabela e criando um df
dados = []
for linha in tabela.find_all('tr'):
    colunas = linha.find_all(['td', 'th'])
    colunas = [coluna.text.strip() for coluna in colunas]
    dados.append(colunas)

df = pd.DataFrame(dados[1:], columns=dados[0])

#  o dataframe vai ser salvo em arquivo csv
df.to_csv('tabela.csv', index=False)
print('Os pedidos foram criados em um arquivo CSV: tabela.csv')
