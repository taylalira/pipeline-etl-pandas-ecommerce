# Pipeline de ETL - Engenharia de Dados com Pandas (E-commerce)

Este projeto simula um pipeline de dados real de um e-commerce, aplicando conceitos fundamentais de Engenharia de Dados para limpar, transformar e consolidar dados de vendas brutos (Camada Bronze) em dados prontos para análise (Camadas Silver e Gold).

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **Pandas** (Tratamento, filtros e transformações de dados)
* **NumPy** (Operações lógicas vetorizadas de alta performance)
* **Formatos de saída:** CSV, e Parquet

## 📐 Arquitetura e Regras de Negócio Aplicadas
* **Camada Bronze (Raw):** Consumo de dados brutos simulando um dump diário de banco transacional contendo anomalias.
* **Camada Silver (Cleaned):** 
  * Padronização de strings de produtos (remoção de espaços e caixa alta).
  * Conversão de tipos de dados (`object` para `int` e `datetime`).
  * Tratamento de formatos de datas mistos (padrão internacional e brasileiro) sem quebra de pipeline.
  * Remoção de registros duplicados com base em subconjuntos críticos.
  * **Tratamento de Exceções (Quarentena):** Isolamento de registros corrompidos com preços ou quantidades negativas/zeradas para auditoria de TI, garantindo a integridade dos cálculos financeiros.
* **Camada Gold (Analytical):** Geração de relatórios agregados contendo faturamento total e volumetria por produto para o time de negócios.
