# Body Measures Flask API

REST API built with Flask for a body measurement tracking application.

## Estrutura da API
* Config: inicialização de variáveis de ambiente
* Controllers: funções das rotas. Recebem a requisição, interagem com outros módulos e enviam a resposta
* Middlewares: funções a serem executadas entre a requisição e a chamada das funções das rotas de fato
* Models: modelos criados com pydantic para validação e formatação de dados
* Repositories: funções de interação com banco de dados
* Routes: definição das rotas da api (nome, método http e função)

## Siga os passos abaixo para clonar e executar o projeto localmente:
* 1. Clone o repositório
```
git clone https://github.com/BernardoChamilet/body_measures_flask_api
cd body_measures_flask_api
```
* 2. Crie um ambiente virtual (opcional)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
* 3. Instale as dependências
```
pip install -r requirements.txt
```
* 4. Crie um .env na raiz do projeto contendo
```
SECRET_KEY=sua_chave_secreta
DB_NAME=nome_do_banco_sqlite
DEBUG=True/False
```
* 5. Na raiz do projeto rode
```
cd api
python app.py
```