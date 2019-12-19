import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

text = "Who is the department chair of the Mathematics and Computer Science Department?"
tokens = nltk.word_tokenize(text)
filtered_tokens = [w for w in tokens if not w in stop_words]
bigrm = nltk.bigrams(filtered_tokens)
print(*map(' '.join, bigrm), sep=', ')

#