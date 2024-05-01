import xml.etree.ElementTree as ET

class XMLParser:
    @staticmethod
    def parse(file_path):
        with open(file_path, 'r') as file:
            tree = ET.parse(file)
            root = tree.getroot()
            text = ' '.join(root.itertext())
        return text
