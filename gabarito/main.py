from json import JSONDecodeError, dump, load

from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciamento de tarefas.",
    version="1.0.0",
)


def carregar_tarefas():
    try:
        with open("../tarefas.json", "r", encoding="utf-8") as arquivo:
            return load(arquivo)
    except (FileNotFoundError, JSONDecodeError):
        return []


def salvar_tarefas(tarefas):
    with open("../tarefas.json", "w", encoding="utf-8") as arquivo:
        dump(tarefas, arquivo, indent=2, ensure_ascii=False)


@app.get(
    "/",
    summary="Início",
    description="Retorna uma mensagem de boas-vindas.",
    response_description="Mensagem de boas-vindas",
)
def inicio():
    return {"mensagem": "API de tarefas funcionando!"}


@app.get(
    "/tarefas",
    description="Retorna uma lista de todas as tarefas.",
    response_description="Lista de tarefas",
)
def listar_tarefas():
    return carregar_tarefas()


@app.get(
    "/tarefas/{id}",
    description="Retorna uma tarefa pelo ID.",
    response_description="Tarefa encontrada",
)
def buscar_tarefa(id: int):
    for tarefa in carregar_tarefas():
        if tarefa["id"] == id:
            return tarefa

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada",
    )


@app.post(
    "/tarefas",
    status_code=status.HTTP_201_CREATED,
    description="Cria uma nova tarefa.",
    response_description="Tarefa criada",
)
def criar_tarefa(titulo: str, concluida: bool = False):
    tarefas = carregar_tarefas()
    novo_id = max((tarefa["id"] for tarefa in tarefas), default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "concluida": concluida,
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    return nova_tarefa


@app.patch(
    "/tarefas/{id}",
    description="Atualiza uma tarefa existente.",
    response_description="Tarefa atualizada",
)
def atualizar_tarefa(id: int, titulo: str | None = None, concluida: bool | None = None):
    tarefas = carregar_tarefas()
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            if titulo is not None:
                tarefas[indice]["titulo"] = titulo

            if concluida is not None:
                tarefas[indice]["concluida"] = concluida

            # Salva no arquivo antes de retornar
            salvar_tarefas(tarefas)
            return tarefa

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada",
    )


@app.delete(
    "/tarefas/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Exclui uma tarefa existente.",
    response_description="Tarefa excluída",
)
def excluir_tarefa(id: int):
    tarefas = carregar_tarefas()
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada",
    )


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", host="0.0.0.0", reload=True)
