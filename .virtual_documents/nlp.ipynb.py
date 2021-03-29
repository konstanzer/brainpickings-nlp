# Auto Reload
get_ipython().run_line_magic("load_ext", " autoreload")
get_ipython().run_line_magic("autoreload", " 2")


# Import Modules
from collections import Counter
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json
from pprint import pprint
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from math import log


# NLTK Modules
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords


import seaborn as sns
import matplotlib.pyplot as plt


# Import Data
df = pd.read_csv('data/articles.csv', index_col='index')


df.date = pd.to_datetime(df.date)


df.tail()


word_count = sum(df["words"])
art_count = len(df["title"])
#print(df.date[-1:] - df.date[1])
print("Maria Popova has published " + str(word_count) + " words & " + str(art_count) + " articlesget_ipython().getoutput("")")
print("The average article length is " + str(int(word_count/art_count)) + " words.")
print("The articles span " + str(round(4959/365.25, 1)) + " years.")
print("Over that time, she has published an article every " + str(round(4959*24/art_count)) + " hoursget_ipython().getoutput("")")


#Outlander
283910 + 338430 + 380770 + 390050 + 482850 + 502860 + 400055 + 391500


words = dict(Bible=783000, Proust=1270000, Martin=1740000, Gabaldon=3170000, Popova=5080000)
ax =sns.barplot(x=list(words.keys()), y=list(words.values()), palette="mako")
ax.set(ylabel='total words (millions)');


year_counts = df.date.groupby(df.date.dt.year).agg("count")


ax = sns.barplot(x=year_counts.index, y=year_counts.values, color="yellow")
ax.set(xlabel='year', ylabel='articles published')
plt.xticks(rotation=34);


# Create Documents
documents = df['content'][:100] #first 


documents[33]


# Set Stop Words
stop = set(stopwords.words('english'))
# Set Stop Punctuations
puncs = set(string.punctuation)
# Merge Stops
full_stop = stop.union(puncs)
# full_stop


# Tokenize Words from Documents
tokens = [word_tokenize(doc.lower()) for doc in documents]

# Filter each token for stop words
#doc_filter = [filter_tokens(token, full_stop) for token in tokens]


porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()

docs_porter = [[porter.stem(word) for word in words]
               for words in doc_filter]
docs_snowball = [[snowball.stem(word) for word in words]
                 for words in doc_filter]
docs_wordnet = [[wordnet.lemmatize(word) for word in words]
                for words in doc_filter]


## Print the stemmed and lemmatized words from the first document
print("get_ipython().run_line_magic("16s", " | %16s | %16s | %16s |\" % (\"WORD\", \"PORTER\", \"SNOWBALL\", \"LEMMATIZER\"))")
for i in range(min(len(docs_porter[0]), len(docs_snowball[0]), len(docs_wordnet[0]))):
    p, s, w = docs_porter[0][i], docs_snowball[0][i], docs_wordnet[0][i]
    if len(set((p, s, w))) get_ipython().getoutput("= 1:")
        print("get_ipython().run_line_magic("16s", " | %16s | %16s | %16s |\" % (doc_filter[0][i], p, s, w))")


# Stem Words in Each Document
clean_tokens = [list(map(snowball.stem, sent)) for sent in doc_filter]
# clean_tokens


# Check for stray tokens (ones with weird puncs, not alphabetical strings)
strays = []
for i in range(len(clean_tokens)):
#     print("--- sentence tokens (lemmatize): {}".format(tokens_lemmatize[i]))
    for word in clean_tokens[i]:
        if not word.isalpha():
            strays.append(word)
set(strays)


# Documents to series
document_series = pd.Series([" ".join(x) for x in clean_tokens])


documents[0]


document_series[0]


# term occurence = counting distinct words in each bag
term_occ = [Counter(doc) for doc in clean_tokens]
# term_occ


term_freq = list()
for i in range(len(clean_tokens)):
    term_freq.append( {k: (v / float(len(clean_tokens[i])))
                       for k, v in term_occ[i].items()} )
term_freq[0]


doc_occ = Counter( [word for token in clean_tokens for word in set(token)] )

doc_freq = {k: (v / float(len(clean_tokens)))
            for k, v in doc_occ.items()}

# doc_freq


# See words with a high frequency threshhold 50%
thresh = 0.5
for word, freq in doc_freq.items():
    if freq >= thresh:
        print(f"{word}:  {freq}")


# the minimum document frequency (in proportion of the length of the corpus)
min_df = 0.5

# filtering items to obtain the vocabulary
vocabulary = [ k for k,v in doc_freq.items() if v >= min_df ]

# print vocabulary
print ("-- vocabulary (len={}): {}".format(len(vocabulary),vocabulary))


# Plot Minimum Document Frequency Threshold
x = np.arange(0.1, 1.1, 0.1)
vocab_y = [len([ k for k,v in doc_freq.items() if v >= thresh ]) for thresh in x]

fig, ax = plt.subplots(figsize=(11, 7))

ax.bar(x, vocab_y, width=0.1)

ax.set_xlim([0,1])
ax.set_title("Minimum Document Frequency Thresholds")

ax.set_xticks(x)

ax.set_xlabel("DF Threshold")
ax.set_ylabel("Length of Vocabulary")

for i, j in zip(x, vocab_y):
    ax.axhline(j, color='r')

x, vocab_y


all_vocabs = [[ k for k,v in doc_freq.items() if v >= thresh ] for thresh in x]
for vocab in all_vocabs:
    print("-- vocabulary (len={}): {}".format(len(vocab),vocab))


state_df = clean_df.groupby('state')["content"]


tf = CountVectorizer()

document_tf_matrix = tf.fit_transform(document_series).todense()

#print(tf.vocabulary_)
#print(document_tf_matrix)


def idf(frequency_matrix):
    df =  float(len(document_tf_matrix)) / sum(frequency_matrix > 0)
    return [log(i) for i in df.getA()[0]]
#print(sorted(tf.vocabulary_))
#print(idf(document_tf_matrix))


tfidf = TfidfVectorizer()
document_tfidf_matrix = tfidf.fit_transform(document_series)
print(sorted(tfidf.vocabulary_))
print(document_tfidf_matrix.todense())



