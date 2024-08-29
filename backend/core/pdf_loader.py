import PyPDF2

class PDFLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text