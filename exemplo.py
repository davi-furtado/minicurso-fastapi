"""Exemplo simples de consumo de uma API externa."""

from datetime import datetime, timedelta
from json import dumps

from httpx import get

moeda = input("Digite o código ISO da moeda (ex: USD, EUR, BGP): ").strip().upper()
data = input(
    "Digite a data de referência [AAAA-MM-DD] ou deixe vazio para data de ontem: "
).strip()
if not data:
    data = (datetime.now().astimezone() - timedelta(days=1)).date()

# Documentação da API: https://brasilapi.com.br/docs
url = f"https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}"

response = get(url)

print("Status HTTP:", response.status_code)

if response.is_success:
    dados = response.json()

    print("\nResposta da API:")
    print(dumps(dados, indent=2, ensure_ascii=False))
    print("\nValores extraídos:")
    print(f"  Moeda: {dados['moeda']}")
    ano, mes, dia = dados["data"].split("-")
    print(f"  Data: {dia}/{mes}/{ano}")
    print(f"  Valor de compra: R$ {dados['cotacoes'][-1]['cotacao_compra']:.2f}")
    print(f"  Valor de venda: R$ {dados['cotacoes'][-1]['cotacao_venda']:.2f}")
else:
    print(f"Erro ao consultar a API:\n{response.text}")
