from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
from model import Document
import easyocr
import cv2

class Main:
    def __init__(self, model_name="TahaDouaji/detr-doc-table-detection", lang="fr"):
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name)
        self.reader = easyocr.Reader([lang])

    def load_image(self, path):
        image = Image.open(path)
        if image.mode not in ["RGB"]:
            image = image.convert("RGB")
        return image

    def detect_document_type(self, text_results):
        for detection in text_results:
            text = detection[1].lower()
            if "bancaire" in text or "banque" in text:
                return Document("Banque")
            elif "facture" in text:
                return Document("Facture")
        return None

    def process_image(self, image):
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        target_sizes = torch.tensor([image.size[::-1]])
        return self.processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    def extract_data_from_image(self, document, cv_image, results):
        data = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            document._set_score(round(score.item(), 3))
            document._set_label(label.item())
            box = [round(i, 2) for i in box.tolist()]
            document._set_box(box)
            if label in [0, 1]:
                xmin, ymin, xmax, ymax = map(int, box)
                cropped = cv_image[ymin:ymax, xmin:xmax]
                table_text = self.reader.readtext(cropped)
                data.extend([detection[1] for detection in table_text])
        document._set_data(data)
        return document

    def process(self, path):
        image = self.load_image(path)
        text_results = self.reader.readtext(path)
        document = self.detect_document_type(text_results)

        if not document:
            raise SystemExit("Cette image n'est pas une facture ou un document bancaire...")

        results = self.process_image(image)
        cv_image = cv2.imread(path)
        document = self.extract_data_from_image(document, cv_image, results)

        return document


if __name__ == "__main__":
    run = Main()
    document = run.process("../documents/releve_banquaire.png")
    print("Lecture du fichier terminée: ")
    print(document)