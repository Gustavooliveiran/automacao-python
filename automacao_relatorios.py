import pandas as pd

dados = {
    "Funcionário": ["Carlos", "Ana", "Lucas", "Fernanda"],
    "Vendas": [1500, 3200, 2800, 4100]
}

df = pd.DataFrame(dados)

print("Relatório de vendas")
print(df)

media_vendas = df["Vendas"].mean()
maior_venda = df["Vendas"].max()
menor_venda = df["Vendas"].min()

print("\nResumo Geral")
print(f"Média de vendas: R$ {media_vendas}")
print(f"Maior venda: R$ {maior_venda}")
print(f"Menor venda: R$ {menor_venda}")

acima_media = df[df["Vendas"] > media_vendas]

print("\nFuncionários acima da média:")
print(acima_media)
