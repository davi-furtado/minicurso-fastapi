<div align="center">

# FastAPI

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

_Construindo uma API REST na prática_

</div>

Este repositório contém os arquivos utilizados no minicurso de introdução ao **FastAPI**, ministrado por **Davi Reis Furtado** e **Gabriel de Almeida Dias**. O objetivo é introduzir os conceitos de **API REST**, **HTTP**, **JSON** e **FastAPI** de forma prática, construindo uma API de tarefas.

## 👨🏽‍💻 Pré-requisitos

Antes de iniciar o minicurso, é necessário ter instalado as seguintes ferramentas.

### 🧰 Ferramentas

- Python
- Visual Studio Code

### 🧩 Extensões para VS Code

- Python

### 📦 Bibliotecas Python

- `fastapi[standard]`
- `requests`

As bibliotecas podem ser instaladas utilizando:

```bash
pip install -r requirements.txt
```

---

## 📚 Conteúdo do Minicurso

### 1. O que é uma API

- O que é uma API
- Como aplicações se comunicam
- Cliente e servidor
- Requisição e resposta
- Endpoints
- URLs
- HTTP
- JSON
- Métodos HTTP

Uma API permite que diferentes sistemas se comuniquem através de regras e formatos definidos.

Um exemplo simples de requisição:

```http
GET /tarefas
```

E uma possível resposta:

```json
[
  {
    "id": 1,
    "titulo": "Estudar FastAPI",
    "concluida": false
  }
]
```

### 2. Consumindo uma API externa

Antes de criar nossa própria API, vamos consumir uma API já existente.

Neste exemplo será utilizada a **[BrasilAPI](https://brasilapi.com.br)**, consultando cotações de moedas.

Arquivo:

```text
example.py
```

Com esse exemplo podemos observar conceitos importantes:

- Fazer uma requisição HTTP
- Utilizar o método `GET`
- Enviar uma requisição para uma URL
- Receber uma resposta
- Verificar o status HTTP
- Converter uma resposta JSON para Python

Depois de consumir uma API externa, vamos fazer o contrário: **criar nossa própria API utilizando FastAPI**.

### 3. Conhecendo o FastAPI

- O que é FastAPI
- Python e FastAPI
- Criação de uma aplicação
- Servidor de desenvolvimento
- Uvicorn
- Rotas

Uma aplicação mínima:

```python
from fastapi import FastAPI

app = FastAPI()
```

Uma rota:

```python
@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}
```

Para executar a aplicação:

```bash
fastapi dev main.py
```

### 4. Criando nossa primeira API

Durante o minicurso será construída uma API de tarefas.

Inicialmente teremos uma lista em memória:

```python
tarefas = []
```

Depois criaremos nosso primeiro endpoint:

```python
@app.get("/tarefas")
def listar_tarefas():
    return tarefas
```

A rota poderá ser acessada através de:

```http
GET /tarefas
```

### 5. Criando modelos com Pydantic

Para definir e validar os dados recebidos pela API, utilizaremos o Pydantic.

```python
from pydantic import BaseModel
```

Criando o modelo de uma tarefa:

```python
class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False
```

Agora podemos utilizar esse modelo para receber dados:

```python
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    return tarefa
```

Exemplo de JSON enviado:

```json
{
  "titulo": "Estudar FastAPI",
  "concluida": false
}
```

### 6. Parâmetros de rota

Também podemos receber informações diretamente pela URL.

Exemplo:

```http
GET /tarefas/1
```

No FastAPI:

```python
@app.get("/tarefas/{id}")
def buscar_tarefa(id: int): ...
```

O FastAPI utiliza a anotação `int` para entender que o parâmetro `id` deve ser um número inteiro.

### 7. CRUD de tarefas

Depois dos conceitos iniciais, vamos implementar as principais operações da API.

#### Listar tarefas

```http
GET /tarefas
```

```python
@app.get("/tarefas")
def listar_tarefas():
    return tarefas
```

#### Buscar uma tarefa

```http
GET /tarefas/{id}
```

```python
@app.get("/tarefas/{id}")
def buscar_tarefa(id: int): ...
```

#### Criar uma tarefa

```http
POST /tarefas
```

```python
@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa): ...
```

#### Atualizar uma tarefa

```http
PATCH /tarefas/{id}
```

O `PATCH` será utilizado para atualizar parcialmente uma tarefa.

Exemplo:

```json
{
  "concluida": true
}
```

Modelo:

```python
class TarefaPatch(BaseModel):
    titulo: str | None = None
    concluida: bool | None = None
```

Endpoint:

```python
@app.patch("/tarefas/{id}")
def atualizar_tarefa(id: int, dados: TarefaPatch): ...
```

#### Excluir uma tarefa

```http
DELETE /tarefas/{id}
```

```python
@app.delete("/tarefas/{id}", status_code=204)
def excluir_tarefa(id: int): ...
```

### 8. Status HTTP e tratamento de erros

Durante a implementação do CRUD serão apresentados alguns dos principais códigos de status HTTP.

- `200` — OK
- `201` — Created
- `204` — No Content
- `404` — Not Found

Para informar que uma tarefa não foi encontrada, utilizaremos `HTTPException`:

```python
from fastapi import HTTPException
```

Exemplo:

```python
raise HTTPException(status_code=404, detail="Tarefa não encontrada")
```

### 9. Documentação automática

Uma das principais características do FastAPI é a geração automática da documentação da API.

Depois de executar o servidor, podemos acessar:

```text
/docs
```

A interface **Swagger UI** permite visualizar e testar os endpoints diretamente pelo navegador.

Também temos:

```text
/redoc
```

que disponibiliza uma segunda interface de documentação.

### 10. Testando a API

Durante o minicurso, os endpoints poderão ser testados através da documentação automática do FastAPI.

Também será disponibilizado o arquivo:

```text
tarefas.py
```

Ele contém uma pequena interface de terminal que consome a API.

Com ele será possível:

- Listar tarefas
- Criar tarefas
- Buscar tarefas
- Atualizar tarefas
- Excluir tarefas

Para executar:

```bash
python tarefas.py
```

A API precisa estar executando em outro terminal.

### 11. Estrutura do projeto

```text
minicurso-fastapi/
├── .gitignore
├── example.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── tarefas.json
├── tarefas.py
└── gabarito/
    └── main.py
```

### 12. O que aprendemos

Ao final do minicurso, teremos visto:

- O que é uma API
- Cliente e servidor
- HTTP
- JSON
- Endpoints
- Métodos HTTP
- Como consumir uma API
- FastAPI
- Rotas
- Parâmetros de rota
- Pydantic
- Validação de dados
- CRUD
- `GET`
- `POST`
- `PATCH`
- `DELETE`
- Status HTTP
- Tratamento de erros
- Swagger
- ReDoc

---

## 🔜 Próximos passos

Depois de aprender os fundamentos, uma API pode evoluir para projetos maiores utilizando recursos como:

- Banco de dados
- SQLAlchemy
- PostgreSQL
- Autenticação
- JWT
- Docker
- Deploy

Esses assuntos ficam fora do escopo deste minicurso.

---

## 📄 Arquivos

| Arquivo | Descrição |
| --- | --- |
| `example.py` | Exemplo de consumo de uma API externa |
| `tarefas.py` | Interface de terminal para consumir a API de tarefas |
| `tarefas.json` | Arquivo de armazenamento das tarefas |
| `main.py` | Arquivo vazio para iniciar o desenvolvimento da API |
| `gabarito/main.py` | API completa desenvolvida durante o minicurso |
| `requirements.txt` | Dependências do projeto |

---

## 📜 Licença

Este projeto está sob a licença _MIT_. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).
