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

def reAccuracySign(dfPath):
    df = pd.read_csv(dfPath,header = None)
    actual = 0
    pred = 0
    for i in df.iloc[:,0]:
        if ('$' or '¢') in i.lower():
            actual += 1
            if getFaceValue(i) != '':
                pred += 1

    return pred/actual 

def reAccuracySave(dfPath):
    df = pd.read_csv(dfPath,header = None)
    actual = 0
    pred = 0
    for i in df.iloc[:,0]:
        if ('save' or 'off' or 'max savings') in i.lower():
            actual += 1
            if getFaceValue(i) != '':
                pred += 1

    return pred/actual 

def reAccuracyTotal(dfPath):
    df = pd.read_csv(dfPath,header = None)
    actual = df.shape[0]
    pred = 0
    for i in df.iloc[:,0]:
        if getFaceValue(i) != '':
            pred += 1

    return pred/actual 

print(reAccuracySave('coupons_ner.csv'))
print(reAccuracySign('coupons_ner.csv'))
print(reAccuracyTotal('coupons_ner.csv'))

# print(getFaceValue("SAVE $1.00 ON TWO when you buy TWO BOXES (8.9 - 15.2 OZ. EXCLUDES LARGE SIZE) any flavor/variety General Mills cereal listed: *"))
