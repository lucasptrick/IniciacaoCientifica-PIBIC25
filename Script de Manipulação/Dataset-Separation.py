import os
import shutil
import pandas as pd
from tqdm import tqdm

# Caminho para o CSV e diretórios
csv_path = 'Data_Entry_2017.csv'
base_dir = 'archive'  # caminho onde estão os diretórios images_001 a images_012
output_dir = 'dataset'  # pasta onde serão copiadas as imagens separadas

# Lê o CSV
df = pd.read_csv(csv_path)
df['Finding Labels'] = df['Finding Labels'].fillna('').astype(str)

# Lista os diretórios de imagem do NIH
image_dirs = [os.path.join(base_dir, f'images_{str(i).zfill(3)}', 'images') for i in range(1, 13)]

# Localiza o caminho da imagem
def find_image_path(filename):
    for image_dir in image_dirs:
        full_path = os.path.join(image_dir, filename)
        if os.path.exists(full_path):
            return full_path
    return None

# Cria pasta de destino se não existir
def ensure_label_dir(label):
    label_dir = os.path.join(output_dir, label)
    os.makedirs(label_dir, exist_ok=True)
    return label_dir

# Processa as imagens com barra de progresso
num_encontradas = 0

print("\n🔄 Iniciando a separação das imagens por rótulo...\n")
for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processando imagens"):
    filename = row['Image Index']
    labels = row['Finding Labels'].split('|')
    source_path = find_image_path(filename)

    if source_path:
        num_encontradas += 1
        for label in labels:
            label = label.strip()
            if not label:
                continue
            dest_dir = ensure_label_dir(label)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy2(source_path, dest_path)

print(f"\n✅ Total de imagens processadas com sucesso: {num_encontradas}")
print(f"📂 As imagens foram copiadas para: {output_dir}")
