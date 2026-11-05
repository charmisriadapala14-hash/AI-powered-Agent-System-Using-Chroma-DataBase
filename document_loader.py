import os
from pypdf import PdfReader


class DocumentLoader:

    def load_pdf(self, file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError("PDF file not found.")

        reader = PdfReader(file_path)

        documents = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                documents.append(text)

        return documents

    def load_text(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            return [file.read()]
