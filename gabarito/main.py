from json import dump, load

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciamento de tarefas.",
    version="1.0.0",
)


class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


def carregar_tarefas():
    try:
        with open("../tarefas.json", "r") as arquivo:
            return load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open("../tarefas.json", "w") as arquivo:
        dump(tarefas, arquivo, indent=2, ensure_ascii=False)


@app.get("/")
def inicio():
    return {"mensagem": "API de tarefas funcionando!"}


@app.get("/tarefas")
def listar_tarefas():
    return carregar_tarefas()


@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    for tarefa in carregar_tarefas():
        if tarefa["id"] == id:
            return tarefa

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada",
    )


@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
    tarefas = carregar_tarefas()
    novo_id = max((tarefa["id"] for tarefa in tarefas), default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": tarefa.titulo,
        "concluida": tarefa.concluida,
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    return nova_tarefa


class TarefaPatch(BaseModel):
    titulo: str | None = None
    concluida: bool | None = None


@app.patch("/tarefas/{id}")
def atualizar_tarefa(id: int, dados: TarefaPatch):
    tarefas = carregar_tarefas()
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            if dados.titulo is not None:
                tarefas[indice]["titulo"] = dados.titulo

            if dados.concluida is not None:
                tarefas[indice]["concluida"] = dados.concluida

            return tarefa

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada",
    )


@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
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
