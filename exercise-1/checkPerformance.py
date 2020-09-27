from getFaceValue import getFaceValue
import pandas as pd

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


print(reAccuracySave('../coupons_ner.csv'))
print(reAccuracySign('../coupons_ner.csv'))
print(reAccuracyTotal('../coupons_ner.csv'))