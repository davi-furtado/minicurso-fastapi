"""
Interface de terminal para nossa API de tarefas.

Execute a API primeiro:

    fastapi dev gabarito/main.py

Depois, em outro terminal:

    python tarefas.py
"""

import requests

API_URL = "http://localhost:8000"


def listar_tarefas():
    response = requests.get(f"{API_URL}/tarefas")

    if response.ok:
        tarefas = response.json()

        print("\n--- Tarefas ---")

        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for tarefa in tarefas:
            status = "✓" if tarefa["concluida"] else " "
            print(f"{tarefa['id']}. [{status}] {tarefa['titulo']}")
    else:
        print("Erro:", response.text)


def criar_tarefa():
    titulo = input("Título da tarefa: ")

    dados = {
        "titulo": titulo,
        "concluida": False,
    }

    response = requests.post(
        f"{API_URL}/tarefas",
        json=dados,
    )

    if response.status_code == 201:
        print("Tarefa criada!")
        print(response.json())
    else:
        print("Erro:", response.text)


def buscar_tarefa():
    id_tarefa = input("ID da tarefa: ")

    response = requests.get(f"{API_URL}/tarefas/{id_tarefa}")

    if response.ok:
        print(response.json())
    else:
        print("Erro:", response.text)


def atualizar_tarefa():
    id_tarefa = input("ID da tarefa: ")

    print("\nO que deseja alterar?")
    print("1 - Título")
    print("2 - Status")
    opcao = input("Opção: ")

    dados = {}

    if opcao == "1":
        dados["titulo"] = input("Novo título: ")

    elif opcao == "2":
        concluida = input("Concluída? (s/n): ").lower()
        dados["concluida"] = concluida == "s"

    else:
        print("Opção inválida.")
        return

    response = requests.patch(
        f"{API_URL}/tarefas/{id_tarefa}",
        json=dados,
    )

    if response.ok:
        print("Tarefa atualizada!")
        print(response.json())
    else:
        print("Erro:", response.text)


def excluir_tarefa():
    id_tarefa = input("ID da tarefa: ")

    response = requests.delete(f"{API_URL}/tarefas/{id_tarefa}")

    if response.status_code == 204:
        print("Tarefa excluída!")
    else:
        print("Erro:", response.text)


def menu():
    while True:
        print("\n===== API DE TAREFAS =====")
        print("1 - Listar tarefas")
        print("2 - Criar tarefa")
        print("3 - Buscar tarefa")
        print("4 - Atualizar tarefa")
        print("5 - Excluir tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_tarefas()
            case "2":
                criar_tarefa()
            case "3":
                buscar_tarefa()
            case "4":
                atualizar_tarefa()
            case "5":
                excluir_tarefa()
            case "0":
                print("Até mais!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    menu()
