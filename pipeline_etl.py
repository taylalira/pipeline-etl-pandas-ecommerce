import pandas as pd

# 1. Extração (Camada Bronze)
vb_pd = pd.read_csv("vendas_brutas.csv")

# 2. Transformação e Limpeza (Camada Silver)
# Padronizando textos e tipos para evitar erros de comparação
vb_pd["produto"] = vb_pd["produto"].fillna("NAO INFORMADO").str.strip().str.upper()
vb_pd["quantidade"] = vb_pd["quantidade"].astype(int)
vb_pd["data_compra"] = pd.to_datetime(vb_pd["data_compra"], format='mixed', dayfirst=True).dt.date

# Removendo duplicados com base nos critérios de negócio
vb_pd = vb_pd.drop_duplicates(subset=["produto", "quantidade", "preco_unitario", "data_compra"])

# Isolando os dados corrompidos na Quarentena (Nulos, Zerados ou Negativos)
vb_pd_quarentena = vb_pd[
    (vb_pd["quantidade"] <= 0) | 
    (vb_pd["produto"] == "NAO INFORMADO") | 
    (vb_pd["preco_unitario"].isna()) | 
    (vb_pd["preco_unitario"] <= 0)
]

# Criando a tabela limpa trazendo APENAS o que passou nas regras.
vb_pd_limpo = vb_pd[
    (vb_pd["quantidade"] > 0) & 
    (vb_pd["produto"] != "NAO INFORMADO") & 
    (vb_pd["preco_unitario"] > 0)
].copy()

# Calculando o faturamento total de forma vetorizada
vb_pd_limpo["faturamento_total"] = vb_pd_limpo["quantidade"] * vb_pd_limpo["preco_unitario"]

# 3. Carregamento (Camada Gold)
relatorio = vb_pd_limpo.groupby("produto")[["quantidade", "faturamento_total"]].sum().reset_index()

# Exportando os resultados finais
relatorio.to_csv("relatorio_faturamento_gold.csv", index=False)
print("Relatório Gold salvo com sucesso!")

vb_pd_limpo.to_parquet("vendas_camada_silver.parquet", index=False)
print("Dados limpos da camada Silver salvos com sucesso!")

vb_pd_quarentena.to_csv("vendas_quarentena.csv", index=False)
print("Quarentena de auditoria salva com sucesso!")
