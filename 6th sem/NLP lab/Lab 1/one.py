import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize

def split_text(text):
    # Use regular expression to split text at spaces and punctuation marks
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    return tokens

def extract_dates(text):
    # Regular expression pattern to extract dates in the format DD/MM/YYYY
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(date_pattern, text)
    return dates

def extract_phone_numbers(text):
    # Regular expression pattern to extract phone numbers in the format (XXX) XXX-XXXX or XXX-XXX-XXXX
    phone_pattern = r'\b(?:\(\d{3}\)\s*|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}\b'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

if __name__ == "__main__":
        text = """
        John Doe's phone number is (123) 456-7890. 
        Jane's number is 987-654-3210. 
        We met on 12/05/2021 and planned another meeting on 23/06/2022.
        """

        # Test split_text function
        tokens = split_text(text)
        print("Tokens:", tokens)

        # Test extract_dates function
        dates = extract_dates(text)
        print("Dates:", dates)

        # Test extract_phone_numbers function
        phone_numbers = extract_phone_numbers(text)
        print("Phone Numbers:", phone_numbers)
