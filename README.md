# QA API Tests

Projeto de automação de testes de API desenvolvido com Pytest e Requests.

## Objetivo

Automatizar testes de API REST validando status codes, estrutura de resposta e comportamento de erro.

## Tecnologias

- Python 3.9
- Pytest
- Requests
- pytest-html

## Estrutura do projeto

    qa-api-tests/
    ├── tests/
    │   └── test_posts.py
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## Como rodar localmente

1. Clone o repositório

        git clone https://github.com/matheuszw-tech/qa-api-tests.git
        cd qa-api-tests

2. Instale as dependências

        pip install -r requirements.txt

3. Execute os testes

        python3 -m pytest tests/ -v

4. Gere o relatório HTML

        python3 -m pytest tests/ -v --html=report.html

## Cenários testados

| Cenário | Método | Endpoint |
|---|---|---|
| Listar posts retorna status 200 | GET | /posts |
| Listar posts retorna lista válida | GET | /posts |
| Buscar post por ID válido | GET | /posts/1 |
| Criar novo post | POST | /posts |
| Buscar post inexistente retorna 404 | GET | /posts/99999 |

## API utilizada

JSONPlaceholder - https://jsonplaceholder.typicode.com