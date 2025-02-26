import spacy
from spacy import displacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# 1. Part of Speech (POS) Tagging
def pos_tagging(text):
    return [(token.text, token.pos_) for token in nlp(text)]

# 2. Syntactic Analysis and Named Entity Recognition (NER)
def analyze_text(text):
    doc = nlp(text)
    return {
        "pos_tags": [(token.text, token.pos_) for token in doc],
        "dependencies": [(token.text, token.dep_, token.head.text) for token in doc],
        "noun_phrases": [chunk.text for chunk in doc.noun_chunks],
        "named_entities": [(ent.text, ent.label_) for ent in doc.ents]
    }

# 2. Visualization of Dependency Tree
def visualize_dependencies(text):
    doc = nlp(text)
    displacy.serve(doc, style="dep")

# 3. Improved Noun Phrase Extraction using Chunking
def chunking_noun_phrases(text):
    doc = nlp(text)
    return [" ".join([token.text for token in chunk]) for chunk in doc.noun_chunks]

# 4. Multilingual Support for POS Tagging
def multilingual_analysis(text, lang="en_core_web_sm"):
    model = spacy.load(lang)
    doc = model(text)
    return [(token.text, token.pos_) for token in doc]

# Example usage
text = "Apple is looking at buying U.K. startup for $1 billion."
print(analyze_text(text))
visualize_dependencies(text)
