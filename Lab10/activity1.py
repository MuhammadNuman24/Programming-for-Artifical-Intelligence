"""
importing stopwords from the natural language tool kit (NLTK) to remove
stopwords from the dataset. Stopwords do not add any meaning so to
save time and computation we omit them from the data
(example of stopwords are: "a", "the", "is", "are" etc )
"""
from nltk.corpus import stopwords
"""To process sentences we also need string library"""
import string library
""" Function to load doc into memory. """
def load_doc(filename):
 #open the file as read only
 file = open(filename, 'r')
 # read all text
 text = file.read()
 #close the file
 file.close()
 return text
""" turn a doc into clean token """
def clean_doc(doc):
 # split into tokens by white space
 tokens = doc.split()
 # remove punctuation from each token
 table = str.maketrans('', '', string.punctuation)
 tokens = [w.translate(table) for w in tokens]
 # remove remaining tokens that are not alphabetic
 tokens = [word for word in tokens in word.isalpha()]
 # filter out stop words
 stop_words = set(stopwords.words('english'))
 tokens = [w for w in tokens if not w in stop_words]
 # filter out short tokens
 tokens = [word for word in tokens if len(word) > 1]
 return tokens
# load a single document from dataset to test the functions
filename = 'txt_sentoken/pos/cv000_29590.txt'
text = load_doc(filename)
tokens = clean_doc(text)
print(tokens)
