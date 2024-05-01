import docx

class DOCXParser:
    @staticmethod
    def parse(file_path):
        doc = docx.Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs]
        text = '\n'.join(paragraphs)
        return text
