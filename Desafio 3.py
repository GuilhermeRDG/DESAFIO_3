import requests
import pandas as pd

ACCESS_TOKEN = "APP_USR-4207752727981094-031400-5650e977a5dfda4ba1066c81c03de301-288368966"
# Função para buscar itens de um termo de pesquisa
def buscar_produtos(termo_busca, limite=50):
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={termo_busca}&limit={limite}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return []

# Função para obter detalhes de cada produto
def obter_detalhes_produto(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

# Função para salvar os dados em um arquivo CSV
def salvar_dados_em_csv(dados, nome_arquivo):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False, sep=',', encoding='utf-8')

# Lista de termos de busca
termos_busca = ['chromecast', 'google home', 'apple tv', 'amazon fire tv']

# Lista para armazenar os dados de todos os produtos
todos_dados = []

# Loop para buscar e obter detalhes de cada produto
for termo in termos_busca:
    print(f"Buscando por: {termo}")
    
    # Buscar os produtos
    produtos = buscar_produtos(termo)
    
    for produto in produtos:
        item_id = produto['id']
        detalhes = obter_detalhes_produto(item_id)
        
        # Criar um dicionário com as informações do produto
        dados_produto = {
            'Item_Id': item_id,
            'Nome': produto.get('title', ''),
            'Preço': produto.get('price', ''),
            'Moeda': produto.get('currency_id', ''),
            'Categoria': produto.get('category_id', ''),
            'Marca': produto.get('attributes', [{'name': 'Marca', 'value_name': ''}])[0].get('value_name', ''),
            'Quantidade': produto.get('available_quantity', ''),
            'Link': produto.get('permalink', ''),
            'Detalhes_Imagem': produto.get('thumbnail', ''),
            'Descrição': detalhes.get('description', ''),
            'Condicao': produto.get('condition', ''),
            'Estado': produto.get('address', {}).get('state_name', ''),
        }
        
        # Adicionar os dados ao conjunto de todos os produtos
        todos_dados.append(dados_produto)

# Salvar os dados em um arquivo CSV
salvar_dados_em_csv(todos_dados, r'D:\Desafio ML\3\mercadolibre_produtos.csv')

print("Análise concluída e dados salvos em 'mercadolibre_produtos.csv'.")
