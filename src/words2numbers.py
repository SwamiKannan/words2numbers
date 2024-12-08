# Imports
from text2digits import text2digits
import inflect
import re

# Instantiated both imported classes

p = inflect.engine()
t2d = text2digits.Text2Digits()

def words_to_numbers(input_string):
    """
    Convert a string of number words into a numeric value.
    Handles:
    - Cardinal numbers (e.g., "two hundred and forty seven")
    - Ordinal numbers (e.g., "fifteenth")
    """
    # Preprocess: Clean up 'and' and extra spaces
    clean_input = re.sub(r'\band\b', '', input_string.lower()).strip()
    
    # Handle ordinal numbers manually
    ordinals = {
        "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
        "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
        "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
        "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18,
        "nineteenth": 19, "twentieth": 20, "thirtieth": 30, "fortieth": 40,
        "fiftieth": 50, "sixtieth": 60, "seventieth": 70, "eightieth": 80,
        "ninetieth": 90, "hundredth": 100, "thousandth": 1000
    }
    
    try:
        # First, check for exact matches in the ordinals dictionary
        if clean_input in ordinals:
            return ordinals[clean_input]
        
        # If not an ordinal, process as a cardinal using word2number
        return t2d.convert(clean_input)
    
    except ValueError:
        print(f"Error: '{input_string}' could not be converted into a number.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None