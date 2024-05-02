import PyPDF2
from utils import to_lower

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
        lower_case_text = to_lower(raw_text)
        return lower_case_text

if __name__ == '__main__':
    parser = PDFParser('input/BT20CSE040-Harsh-Tripathi.pdf')

    print(parser.get_metadata())
    print(parser.get_num_pages())
    # parser.get_text()
    print(parser.process_text())
    #print(parser.parse('input/BT20CSE040-Harsh-Tripathi.pdf'))
