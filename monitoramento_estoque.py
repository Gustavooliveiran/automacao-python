import pandas as pd

produtos = {
    "Produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "Estoque": [5, 50, 12, 3],
    "Preço": [3500, 80, 150, 1200]
}

df = pd.DataFrame(produtos)

print("Controle de Estoque")
print(df)

print("\nProdutos com estoque baixo:")

estoque_baixo = df[df["Estoque"] < 10]

print(estoque_baixo)

valor_total = (df["Estoque"] * df["Preço"]).sum()

print(f"\nValor total do estoque: R$ {valor_total}")
