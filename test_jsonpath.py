import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes')

# com o JsonPath eu consigo de forma fácil pegar a lista de todos os nomes que avaliaram. Ele devolve uma lista
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(resultados)

avaliacao = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(avaliacao)