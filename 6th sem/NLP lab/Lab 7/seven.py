##1 PERFORM LEMMATIZATION AND STEMMING USING PYTHON LIBRARY NLTK
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize the stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Example text
text = "Here's an example text with #hashtags, @mentions, URLs like https://example.com, and punctuation!"

# Custom tokenizer to remove noise
def custom_tokenizer(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)

# Tokenize the text
tokens = custom_tokenizer(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Apply stemming and lemmatization
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# Output the results
print("Original Tokens:", tokens)
print("Filtered Tokens (without stopwords):", filtered_tokens)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)

### 2 1.	Write a python program to design a custom tokenizer that can handle multiple types of noise (hashtags, mentions, URLs, punctuation, etc.) and then apply stemming and lemmatization.
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def process_text(text):
    text = re.sub(r'http\S+|www\.\S+|@\w+|#\w+|[^a-zA-Z\s]', '', text)
    tokens = [w for w in word_tokenize(text) if w.lower() not in stopwords.words('english')]
    stemmer, lemmatizer = PorterStemmer(), WordNetLemmatizer()
    return [(w, stemmer.stem(w), lemmatizer.lemmatize(w, wordnet.NOUN)) for w in tokens]

def main():
    text = "Check out my blog at https://example.com! @user #PythonCoding is awesome."
    print("Original | Stemmed | Lemmatized")
    print("-" * 30)
    for w, s, l in process_text(text):
        print(f"{w:10} | {s:10} | {l}")

if __name__ == "__main__":
    main()



### 3 Write a python program to create a Named Entity Recognition (NER) system to identify entities (like people, organizations, dates) and perform text normalization (remove or standardize text such as dates, monetary values, and numbers).

import nltk
import re
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Example text
text = "Barack Obama was born on August 4, 1961. He was the 44th President of the USA. He was born in Honolulu, Hawaii. His net worth is $70 million."

# Named Entity Recognition (NER)
def perform_ner(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    return named_entities

# Text normalization (e.g., remove or standardize dates, monetary values)
def normalize_text(text):
    # Standardize dates
    text = re.sub(r'\b\d{1,2}[\/\-\s]\d{1,2}[\/\-\s]\d{2,4}\b', 'DATE', text)
    text = re.sub(r'\b\d{4}\b', 'YEAR', text)
    text = re.sub(r'\b[A-Z][a-z]+ \d{1,2}, \d{4}\b', 'DATE', text)
    
    # Standardize monetary values
    text = re.sub(r'\$\d+(\.\d{1,2})?', 'MONEY', text)
    
    # Standardize numbers
    text = re.sub(r'\b\d+\b', 'NUMBER', text)
    
    return text

# Perform NER
named_entities = perform_ner(text)

# Normalize text
normalized_text = normalize_text(text)

# Output the results
print("Named Entities:", named_entities)
print("Normalized Text:", normalized_text)

