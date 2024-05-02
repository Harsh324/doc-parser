import docx

class DOCXParser:
    docx_content = None

    def __init__(self, file_path):
        self.docx_content = docx.Document(file_path)


    def process_text(self):
        doc = self.docx_content
        paragraphs = [p.text for p in doc.paragraphs]
        text = '\n'.join(paragraphs)
        return text

    def parse_to_text(self, output_file = 'output/output-docx.txt'):
        text = self.process_text()
        with open(output_file, 'w') as file:
            file.write(text)
        file.close()


if __name__ == '__main__':
    parser = DOCXParser('input/docx-sample.docx')
    parser.parse_to_text('output/output-docx.txt')

