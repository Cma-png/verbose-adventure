import re

class TextCleaner:
    @staticmethod
    def clean(text: str):
        # Simple text cleaning logic
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text