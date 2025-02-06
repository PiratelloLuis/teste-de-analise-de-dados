import pandas as pd
import openpyxl

tabela = pd.read_excel("Pandas/Vendas.xlsx")
print(tabela)

faturamento_total = tabela["Valor Final"].sum()
print(f"{faturamento_total},00 Reais")

faturamento_por_loja = tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

faturamento_por_produto = tabela[["ID Loja", "Produto" ,"Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)

print("A loja em Iguatemi Campinas ")