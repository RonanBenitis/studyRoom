import json
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        '''
        Para acessar o atributo do json, deve-se respeitar
        exatamente o formato que se está escrito
        '''
        nome_restaurante = item['Company']

        '''
        Se nome_restaurante não estive em dados_restaurante
        crie uma nova lista vazia.
        '''
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        '''
        Tudo que for do restaurante X, acrescente os dados a ele
        Dar-se-á .append porque dados_restaurante[nome_restaurante] é uma lista
        '''
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'preco': item['price'],
            'descricao': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'

    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, indent=4)