import re 
import pandas as pd 
import nltk 

def getFaceValue(string):
    finder = re.findall(r"\d+(?:\.\d+)?\¢|save +\$+(?:\.\d+)?\d+(?:\.\d+)?|\$+(?:\.\d+)?\d+(?:\.\d+)? off|max savings \$+(?:\.\d+)?\d+(?:\.\d+)?", string.lower())
    value = finder[0].replace('save','').replace('off','').replace('max savings','').strip() if len(finder) > 0 else ''
    if '¢' in value:
        new_value = float(value.replace('¢',''))/100
        value = '$'+str(new_value)
        
    return value

print(getFaceValue("SAVE $1.00 ON TWO when you buy TWO BOXES (8.9 - 15.2 OZ. EXCLUDES LARGE SIZE) any flavor/variety General Mills cereal listed: *"))
