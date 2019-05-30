import re
import requests
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize



#FUNCTIONS

#Function from https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65
def _score_sentences(sentences, freqTable):
    sentenceValue = dict()
    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]]
    return sentenceValue

#Function from https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65
def _create_frequency_table(text_string):
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable









url = 'https://en.wikipedia.org/wiki/Asthma'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 

paragraph_empty = soup.find('p')
paragraphs=paragraph_empty.find_next('p')

article_text = paragraphs.text
article_text=re.sub('\[\d+\]', "",  article_text)#Removes reference tags
print article_text



# 1 Create the word frequency table
freq_table = _create_frequency_table(article_text)



# 2 Tokenize the sentences
sentence_list = sent_tokenize(article_text)  

# 3 Important Algorithm: score the sentences
sentence_scores = _score_sentences(sentence_list, freq_table)


