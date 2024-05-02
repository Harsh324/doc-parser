from parsers.xml_parser import XMLParser
from parsers.html_parser import HTMLParser
from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser

file_type_map =  {
    1 : 'xml',
    2 : 'html',
    3 : 'pdf',
    4 : 'docx'
}

def main(file_type):
    if file_type == 'xml':
        parser = XMLParser('input/xml-sample.xml')
        parser.parse_to_text()
    elif file_type == 'html':
        parser = HTMLParser('input/html-sample.html')
        parser.parse_to_text()
    elif file_type == 'pdf':
        parser = PDFParser('input/pdf-sample.pdf')
        parser.parse_to_text()
    elif file_type == 'docx':
        parser = DOCXParser('input/docx-sample.docx')
        parser.parse_to_text()

if __name__ == "__main__":
    type = int(input("Enter the File type\n1 : xml\n2 : html\n3 : pdf\n4 : docx\n"))
    main(file_type_map[type])
