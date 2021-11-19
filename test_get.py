import requests

headers = {'Authorization': 'Token a10340ca41ae396da49b97e6d7d6ca933a400382'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())
assert resultado.status_code == 200

