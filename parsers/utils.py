import re
import string
import nltk
from nltk.corpus import stopwords, brown
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from autocorrect import spell, Speller


def to_lower(text):

    spell  = Speller(lang='en')
    texts = spell(text)
    return ' '.join([w.lower() for w in word_tokenize(text)])

def process_text(text):
    spell  = Speller(lang='en')
    text = spell(text)
    lower_case = ' '.join([w.lower() for w in word_tokenize(text)])

    words  = nltk.word_tokenize(lower_case)
    punctuations = ['.', ',', '/', '!', '?', ';', ':', '(',')', '[',']', '-', '_', '%']
    punctuations = re.sub(r'\W', ' ', str(lower_case))
    
    # Initialize the stopwords variable, which is a list of words ('and', 'the', 'i', 'yourself', 'is') that do not hold much values as key words
    stop_words  = stopwords.words('english')
    
    # Getting rid of all the words that contain numbers in them
    w_num = re.sub('\w*\d\w*', '', lower_case).strip()
            
    # Removing non-english characters
    lower_case = re.sub(r'^b\s+', '', lower_case)
    
    # Return keywords which are not in stop words 
    keywords = [word for word in words if not word in stop_words  and word in punctuations and  word in w_num]
    
    wordnet_lemmatizer = WordNetLemmatizer()

    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in keywords]

    # lets print out the output from our function above and see how the data looks like
    clean_data = ' '.join(lemmatized_word)

    return clean_data