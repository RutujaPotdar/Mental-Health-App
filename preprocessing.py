import sklearn
import pickle
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from nltk.stem import PorterStemmer

tfidf =  pickle.load(open('tfidf.pkl', 'rb')) 

def preprocess(inp):
    inp = inp.lower()
    inp = inp.replace(r'[^\w\s]+', '')
    inp = [word for word in inp.split() if word not in (stop_words)]

    ps = PorterStemmer()
    inp = ' '.join([ps.stem(i) for i in inp])
    inputToModel = tfidf.transform([inp]).toarray()
    return inputToModel