from parsers.xml_parser import XMLParser
from parsers.html_parser import HTMLParser
from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser

def main():
    file_path = 'path/to/your/document.xml'
    parser = XMLParser()
    text = parser.parse(file_path)
    print(text)

if __name__ == "__main__":
    main()
