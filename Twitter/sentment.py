import pandas as pd
import string

#importing nltk modules for sentment analysis
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def analyse_text(x):
    # lower casing all text
    lower_case = x.lower()

    # removing punctuators from text
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # tokenizeing sentense to words,Using word_tokenize because it's faster than split()
    tokenized_words = word_tokenize(cleaned_text, "english")

    # analysing the score
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    
    #score will return a dictionary keys are 'neg','neu','pos' and 'combined'
    return score
    
