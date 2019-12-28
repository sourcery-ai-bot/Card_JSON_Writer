import json
import os

file = open(os.path.dirname(os.path.realpath(__file__)) + '\path_config.txt', 'r')
arquivo_caminho = file.read()

#Os comentarios são testes para usar os dados antigos ao inves de sobrescrever
"""
with open(arquivo_caminho) as data_file:    
    data_old = json.load(data_file)
"""

data = {}
data['Carta'] = []

i = 0
while i == 0: 
    data['Carta'].append({
        'NOME_CRIATURA': input('Nome da Criatura: '),
        'HP': input('HP: '),
        'MP': input('MP: '),
        'LC': input('LC: '),
        'SC': input('SC: '),
        'BP': input('BP: '),
        'ATK_FORCA': input('Forca do Ataque: '),
        'ATK_CUSTO': input('Custo do Ataque: '),
        'DEF_FORCA': input('Forca da Defesa: '),
        'DEF_CUSTO': input('Custo da Defesa: '),
        'ZONA_ATK': input('Zona de Ataque: '),
        'ZONA_DEFESA': input('Zona de Defesa: '),
        'TIPO': input('Tipo: '),
        'CLASSE': input('Classe: '),
        'MOVIMENTO': input('Movimento: '),
        'HABILIDADES': input('Habilidades: ')    
    })
    try:
        i = int(input('Se deseja continuar digite 0, se nao digite 1: '))
    except:
        i = 1
"""
data = data_old + data
"""

with open(arquivo_caminho, 'w') as outfile:
    json.dump(data, outfile)