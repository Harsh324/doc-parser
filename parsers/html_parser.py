from bs4 import BeautifulSoup

class HTMLParser:
    @staticmethod
    def parse(file_path):
        with open(file_path, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text()
        return text
