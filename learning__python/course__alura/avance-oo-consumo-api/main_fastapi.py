import requests
from fastapi import FastAPI, Query

app = FastAPI()

'''
FastAPI possui decorators próprios
Aqui, vamos configurar nossa rota get
'''
@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    '''
    return {'Hello':'World'}

'''
No parametro, passamos que será uma str e o valor default dele
será uma Query(None)
Sendo que Query é uma função específica do FastAPI
'''
@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        # Se variável restaurante for nada, realize ação
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []

        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'preco': item['price'],
                    'descricao': item['description']
                })
        
        return {
            'Restaurante': restaurante,
            'Cardapio': dados_restaurante
        }
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}