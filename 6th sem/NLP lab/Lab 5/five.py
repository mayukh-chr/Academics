#WRITE A PROGRAM TO REMOVE DIGITS FROM A GIVEN SENTENCE USING GREEDY TOKENIZER

import re

def remove_digits(sentence):
    # Greedy tokenizer to remove digits
    result = re.sub(r'\d+', '', sentence)
    return result

sentence = "I have 2 apples and 3 oranges."
print(remove_digits(sentence))

#Write a program to count how many digits are present in a given sentence

import re

def count_digits(sentence):
    # Find all digit occurrences
    digits = re.findall(r'\d', sentence)
    return len(digits)

sentence = "I have 2 apples and 3 oranges."
print(count_digits(sentence))

#Write a program to extract and print all digits from a sentence using a greedy tokenizer.

import re

def extract_digits(sentence):
    # Greedy tokenizer to find all digits
    digits = re.findall(r'\d+', sentence)
    return digits

sentence = "I have 2 apples and 3 oranges."
print(extract_digits(sentence))

#Write a program that greedily tokenizes a sentence but prioritizes specific patterns, such as dates (\d{1,2}/\d{1,2}/\d{2,4}) and email addresses ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}), over general tokens.
import re

def tokenize_prioritize_patterns(sentence):
    # Prioritize dates and email addresses over general tokens
    date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    digit_pattern = r'\d+'
    
    # Combine all patterns
    combined_pattern = f'({date_pattern})|({email_pattern})|({digit_pattern})'
    
    tokens = re.findall(combined_pattern, sentence)
    # Flatten the list of tuples and filter out empty strings
    tokens = [token for group in tokens for token in group if token]
    
    return tokens

sentence = "Contact me at john.doe@example.com or on 12/04/2023."
print(tokenize_prioritize_patterns(sentence))
