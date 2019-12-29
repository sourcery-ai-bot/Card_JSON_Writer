import json
import os

file = open(os.path.dirname(os.path.realpath(__file__)) + '\path_config.txt', 'r')
arquivo_caminho = file.read()

r = input('Se o arquivo for novo digite n se ja existir dados digite a: ')
if r == 'n':
    data = {}
    data['Carta'] = []
else:
    with open(arquivo_caminho) as data_file:    
        data = json.load(data_file)

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

with open(arquivo_caminho, 'w') as outfile:
    json.dump(data, outfile)