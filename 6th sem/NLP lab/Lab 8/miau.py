## prolly need to change things later 
#DEMONSTRATE OBJECT STANDARDIZATION SUCH AS REPLACE SOCIAL MEDIA SLANGS FROM A TEXT.
import re

# Dictionary for common slang words
slang_dict = {
    "u": "you",
    "r": "are",
    "omg": "oh my god",
    "lol": "laugh out loud",
    "idk": "I don't know",
    "btw": "by the way"
}

# Dictionary for common emojis
emoji_dict = {
    ":)": "happy",
    ":-)": "happy",
    ":(": "sad",
    ":-(": "sad",
    ";)": "wink",
    ";-)": "wink",
}

def replace_slang_and_emojis(text):
    # Replace slang words
    words = text.split()
    replaced_text = " ".join([slang_dict.get(word.lower(), word) for word in words])
    
    # Replace emojis
    for emoji, replacement in emoji_dict.items():
        replaced_text = replaced_text.replace(emoji, replacement)
    
    # Normalize spaces and punctuation marks
    replaced_text = re.sub(r'\s+', ' ', replaced_text)  # Remove extra spaces
    replaced_text = re.sub(r'([?!,.])\1+', r'\1', replaced_text)  # Normalize repeated punctuation
    replaced_text = re.sub(r'\s([?!,.])', r'\1', replaced_text)  # Remove space before punctuation
    
    return replaced_text

# Test the function on a variety of text inputs
test_texts = [
    "omg!!! u r amazing :)",
    "idk... what's happening :(",
    "btw, lol u r great ;) :-)",
    "hello!!!    world!!!",
]

for text in test_texts:
    print("Original:", text)
    print("Processed:", replace_slang_and_emojis(text))
    print()
#Create a dictionary for common slangs and another dictionary for emojis. Implement a function that replaces slangs, abbreviations, and emojis with their formal counterparts. Normalize any irregular spaces or punctuation marks (e.g., "hello!!!" -> "hello!"). Test the function on a variety of text inputs containing slangs, emojis, and multiple punctuation.
def standardize_text(text):
    # Replace slang words
    words = text.split()
    standardized_text = " ".join([slang_dict.get(word.lower(), word) for word in words])
    
    # Normalize spaces and punctuation marks
    standardized_text = re.sub(r'\s+', ' ', standardized_text)  # Remove extra spaces
    standardized_text = re.sub(r'([?!,.])\1+', r'\1', standardized_text)  # Normalize repeated punctuation
    standardized_text = re.sub(r'\s([?!,.])', r'\1', standardized_text)  # Remove space before punctuation
    
    # Convert text to lowercase
    standardized_text = standardized_text.lower()
    
    return standardized_text

# Test the function on a sentence with mixed case, slang words, and irregular punctuation
test_sentence = "OMG!!! This is sooo cool!!! BTW, u r amazing :)!!!"
print("Original:", test_sentence)
print("Standardized:", standardize_text(test_sentence))
