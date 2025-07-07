import os
import matplotlib.pyplot as plt
from collections import Counter

# Dicionário de tradução das doenças para português
traducao_doencas = {
    "No Finding": "Sem Achados",
    "Infiltration": "Infiltração",
    "Atelectasis": "Atelectasia",
    "Effusion": "Derrame Pleural",
    "Consolidation": "Consolidação",
    "Nodule": "Nódulo",
    "Mass": "Massa",
    "Cardiomegaly": "Cardiomegalia",
    "Pneumothorax": "Pneumotórax",
    "Edema": "Edema",
    "Emphysema": "Enfisema",
    "Pleural_Thickening": "Espessamento Pleural",
    "Fibrosis": "Fibrose",
    "Pneumonia": "Pneumonia",
    "Hernia": "Hérnia"
}

pasta_saida = "dataset"
contagem = Counter()

# Conta quantas imagens existem por pasta (doença)
for doenca in os.listdir(pasta_saida):
    caminho_doenca = os.path.join(pasta_saida, doenca)
    if os.path.isdir(caminho_doenca):
        contagem[doenca] = len(os.listdir(caminho_doenca))

# Ordena da maior para a menor quantidade
contagem_ordenada = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

# Traduz os nomes para português e prepara dados para o gráfico
labels = [traducao_doencas.get(doenca, doenca) for doenca, _ in contagem_ordenada]
quantidades = [qtd for _, qtd in contagem_ordenada]

# Gráfico de colunas
plt.figure(figsize=(12, 6))
bars = plt.bar(labels, quantidades, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Quantidade de Imagens")
plt.title("Distribuição das Imagens por Doença (em Português)")

# Adiciona os valores nas barras
for bar, qtd in zip(bars, quantidades):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(qtd),
             ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig("distribuicao_quantidade_doencas_colunas.png")
plt.show()