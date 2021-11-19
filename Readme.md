Esse projeto é de estudos sobre o DRF - Django Rest Framework. 

Abaixo são apenas anotações para recordar de alguns pontos vistos durante o curso.

A primeira implementação foi feita utilizando o arquivo `Views_olds.py`, onde precisamos declarar para cada view de cada 
Model os métodos dela. Em seguida, na `v1` da API, abandonamos isso e passamos a utilizar `from rest_framework import generics`
que então passou a gerar para nós os métodos de listagem e criação e depois de recuperação, deleção e atualização. No entanto
precisamos montar as rotas manualmente, observar `cursos/urls.py` e `escola/urls.py`. 

Na `v2` da API passamos a utilizar os recursos de `ModelViewSet` e `SimpleRouter`. `ModelViewSet` gera para nós o create, retrieve, update, destroy e list do model e
`SimpleRouter` gera as rotas para os models. Como o `SimpleRouter` gera a rota para um model, precisamos alterar o 
`ModelViewSet` de curso, `CursoViewSet`, para ele suportar retornar as avaliações de um curso quando fosse consultado 
`/api/v1/cursos/1/avaliacoes/`, dessa forma acessando dois recursos (Curso e Avaliações). Se observar dentro de
`CursoViewSet` foi criado a método `avaliacoes(self, request, pk=None)` que habilitou essa consulta a avaliações.

Dentro de `cursos/serializers.py` há estratégias de apresentação de relacionamentos entre objetos, três delas foram 
abordadas `Nested Relationship`, `HyperLinked Related Field` e `Primary Key Related Field`. 

Em `escola/settings.py` há uma parametrização para paginação default de todas as consultas.

```
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
```
No entantato, quando um na URI é acionado dois recuros `/api/v2/cursos/5/avaliacoes/`, é necessário fazer a implementação
da paginação na mão. Um exemplo foi implementado `cursos/views.py >> CursoViewSet >> avaliacoes`

Nas configurações `escola/settings.py` foi definido um `throttle rate` default para toda a API para usuários logados
e não logados na plataforma. O DRF utiliza um recurso padrão `cacheback` para fazer o controle de requisições dos usuários.
Esse uso é OK para ambiente de desenvolvimento, para produção é recomendado utilizar o `redis` para esse controle.


Para roder o serviço localmente, no shel executar:
```
python manage.py runserver 
```