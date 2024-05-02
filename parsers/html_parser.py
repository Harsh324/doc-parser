from bs4 import BeautifulSoup

class HTMLParser:
    html_content = None

    def __init__(self, file_path):
        self.html_content = BeautifulSoup(open(file_path, 'rb'), 'html.parser')

    def remove_newline(self, text):
        return text.replace('\n', ' ')

    def process_text(self):
        tag_meta_language = self.html_content.head.find("meta", attrs={"http-equiv": "content-language"})
        if tag_meta_language:
            document_language = tag_meta_language["content"]
            if document_language and document_language not in ["en", "en-us", "en-US"]:
                raise ValueError("Language {} is not english".format(document_language))

        # Get text from the specified tags. Add more tags if necessary.
        TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
        return ' '.join([self.remove_newline(tag.text) for tag in self.html_content.findAll(TAGS)])

    def parse_to_text(self, output_file = 'output/output-html.txt'):
        text = self.process_text()
        with open(output_file, 'w') as file:
            file.write(text)
        file.close()


if __name__ == '__main__':
    parser = HTMLParser('input/html-sample.html')

    # print(parser.get_metadata())
    # print(parser.get_num_pages())
    # parser.get_text()
    # print(parser.process_text())
    parser.parse_to_text('output/output-html.txt')
    #print(parser.parse('input/BT20CSE040-Harsh-Tripathi.pdf'))


