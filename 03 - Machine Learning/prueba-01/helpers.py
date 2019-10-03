import nltk
from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
        self.tknzr = TweetTokenizer()

    def __call__(self, sentences):
        return [self.wnl.lemmatize(t) for t in self.tknzr.tokenize(sentences)]

def most_common_words(serie):
    count_vectorizer = CountVectorizer(stop_words='english')
    lyrics_count = count_vectorizer.fit_transform(serie)
    words = count_vectorizer.get_feature_names()
    words_freq = lyrics_count.toarray().sum(axis=0)
    return pd.DataFrame({ 'freq': words_freq }, index=words).sort_values(by='freq', ascending=False)[:100]
