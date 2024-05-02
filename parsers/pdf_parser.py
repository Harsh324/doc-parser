import PyPDF2
from parsers.utils import process_text

class PDFParser:
    pdf_content = None

    def __init__(self, file_path):
        self.pdf_content = PyPDF2.PdfReader(open(file_path, 'rb'))

    def get_metadata(self):
        return self.pdf_content.metadata
    
    def get_num_pages(self):
        return len(self.pdf_content.pages)

    def get_text(self):
        text = ''
        total_pages = self.get_num_pages()
        for i in range(total_pages):
            page = self.pdf_content.pages[i]
            text += page.extract_text()

        return text

    def process_text(self):
        raw_text = self.get_text()
        processed_text = process_text(raw_text)
        return processed_text

    def parse_to_text(self, output_file = 'output/output-pdf.txt'):
        text = self.process_text()
        with open(output_file, 'w') as file:
            file.write(text)
        file.close()

if __name__ == '__main__':
    parser = PDFParser('input/pdf-sample.pdf')

    print(parser.get_metadata())
    print(parser.get_num_pages())
    # parser.get_text()
    print(parser.process_text())
    parser.parse_to_text('output/output-pdf.txt')
    #print(parser.parse('input/BT20CSE040-Harsh-Tripathi.pdf'))
