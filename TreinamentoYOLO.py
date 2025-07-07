from ultralytics import YOLO
from tqdm import tqdm
import os
import time

DATASET_DIR = "yolo_classification_dataset_undersampled"
TEST_IMAGE_PATH = None  # ou substitua por "path/to/image.jpg"
MODEL_TYPE = "yolov8n-cls.pt"
IMAGE_SIZE = 224
EPOCHS = 50


def main():
    print("🔎 Carregando modelo YOLOv8 de classificação...")
    model = YOLO(MODEL_TYPE)

    print(f"\n🚀 Iniciando treinamento no dataset: {DATASET_DIR}")
    print(f"📈 Épocas: {EPOCHS} | Tamanho da imagem: {IMAGE_SIZE}x{IMAGE_SIZE}\n")

    # Executa o treinamento com barra simulada (época a época)
    for epoch in tqdm(range(1, EPOCHS + 1), desc="Treinando"):
        # Treinamento real só ocorre na primeira chamada (com todas as épocas)
        if epoch == 1:
            results = model.train(
                data=DATASET_DIR,
                epochs=EPOCHS,
                imgsz=IMAGE_SIZE,
                verbose=False  # silencia prints extras
            )
        else:
            time.sleep(0.1)  # Simula avanço de época na barra

    print("\n✅ Treinamento concluído!")
    print("📂 Pesos salvos em:", results.save_dir)

    # Previsão opcional
    if TEST_IMAGE_PATH and os.path.exists(TEST_IMAGE_PATH):
        print("\n🧪 Realizando teste com imagem:", TEST_IMAGE_PATH)
        pred = model(TEST_IMAGE_PATH)[0]
        class_id = pred.probs.top1
        confidence = pred.probs.top1conf
        label = model.names[class_id]
        print(f"🔍 Classe prevista: {label} (confiança: {confidence:.2f})")
    else:
        print("\nℹ️ Nenhuma imagem de teste fornecida ou caminho inválido.")


if __name__ == "__main__":
    main()