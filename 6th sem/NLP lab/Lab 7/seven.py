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


### 2

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


## 3

import nltk
from nltk.tokenize import word_tokenize
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
text = "Lemmatization and stemming are essential for natural language processing tasks."

# Tokenize the text
tokens = word_tokenize(text)

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
