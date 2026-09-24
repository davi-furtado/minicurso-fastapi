# ==============================================================================
# 1. IMPORTAÇÕES
# Importe JSONDecodeError, dump e load da biblioteca json
# Importe FastAPI, HTTPException e status do framework fastapi
# ==============================================================================


# ==============================================================================
# 2. INICIALIZAÇÃO DA API
# Crie a instância do FastAPI e defina title, description e version
# ==============================================================================

# app =


# ==============================================================================
# 3. FUNÇÕES AUXILIARES DE PERSISTÊNCIA (LEITURA E ESCRITA)
# ==============================================================================
LOCAL_JSON = "tarefas.json"


def carregar_tarefas():
    # Abra o arquivo LOCAL_JSON em modo de leitura com encoding="utf-8"
    # Trate com try/except as exceções FileNotFoundError e JSONDecodeError
    # Se o arquivo for lido com sucesso, retorne o JSON carregado (load)
    # Se der erro, retorne uma lista vazia []
    pass


def salvar_tarefas(tarefas):
    # Abra o arquivo LOCAL_JSON em modo de escrita ("w") com encoding="utf-8"
    # Use o dump para salvar a lista de tarefas no arquivo (com indent=2 e ensure_ascii=False)
    pass


# ==============================================================================
# 4. ROTAS / ENDPOINTS
# ==============================================================================


# Rota RIZ (Boas-vindas)
# Crie um decorator @app.get("/") com summary, description e response_description
def inicio():
    # Retorne um dicionário com uma mensagem de boas-vindas
    pass


# Rota LISTAR TAREFAS
# Crie um decorator @app.get("/tarefas")
def listar_tarefas():
    # Retorne o resultado da função carregar_tarefas()
    pass


# Rota BUSCAR TAREFA POR ID
# Crie um decorator @app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    # Percorra as tarefas carregadas
    # Se encontrar a tarefa com o ID correto, retorne-a
    # Se não encontrar no final do loop, lance um HTTPException 404
    pass


# Rota CRIAR TAREFA
# Crie um decorator @app.post("/tarefas") com status_code=status.HTTP_201_CREATED
def criar_tarefa(titulo: str, concluida: bool = False):
    # Carregue as tarefas existentes
    # Calcule o novo ID (dica: max(...) + 1, com default=0)
    # Monte o dicionário da nova tarefa
    # Adicione à lista de tarefas e chame salvar_tarefas()
    # Retorne a nova tarefa criada
    pass


# Rota ATUALIZAR TAREFA (PATCH)
# Crie um decorator @app.patch("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str | None = None, concluida: bool | None = None):
    # Carregue as tarefas
    # Procure a tarefa pelo ID usando o enumerate para saber o índice
    # Se titulo não for None, atualize o título
    # Se concluida não for None, atualize o status
    # Salve as tarefas no arquivo e retorne a tarefa atualizada
    # Se não encontrar a tarefa, lance um HTTPException 404
    pass


# Rota EXCLUIR TAREFA
# Crie um decorator @app.delete("/tarefas/{id}") com status_code=status.HTTP_204_NO_CONTENT
def excluir_tarefa(id: int):
    # Carregue as tarefas
    # Procure a tarefa pelo ID
    # Remova a tarefa da lista (use pop ou remove)
    # Salve as alterações no arquivo e dê return
    # Se não encontrar a tarefa, lance um HTTPException 404
    pass


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", host="0.0.0.0", reload=True)
