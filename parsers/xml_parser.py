import xml.etree.ElementTree as ET

class XMLParser:
    xml_content = None

    def __init__(self, file_path):
        self.xml_content = ET.parse(open(file_path, 'rb'))

    def parse(self):
        root = self.xml_content.getroot()
        return ' '.join(root.itertext())

    def parse_to_text(self, output_file = 'output/output-xml.txt'):
        with open(output_file, 'w') as f:
            root = self.xml_content.getroot()
            for element in root.iter():
                tag = element.tag
                text = element.text.strip() if element.text else ''
                if text:
                    f.write(f"{tag} {text} ")

if __name__ == '__main__':
    parser = XMLParser('input/xml-sample.xml')
    parser.parse_to_text('output/output-xml.txt')


