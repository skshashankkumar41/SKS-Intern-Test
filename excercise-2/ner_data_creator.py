import pandas as pd
import re
import nltk
from textblob import TextBlob
from tqdm import tqdm
import pickle

nltk.download('brown')
nltk.download('punkt')

def prod(txt):

    txt = txt.lower()
    txt = re.sub('packs','', txt)
    txt = re.sub('trial','', txt)
    txt = re.sub('travel','', txt)
    txt = re.sub('size','', txt)
    txt = re.sub('save','', txt)
    txt = re.sub('excludes','', txt)  
    blob = TextBlob(txt)
    return blob.noun_phrases

df = pd.read_csv('../coupons_ner.csv',names = ['OfferDetails'])

df['Products'] = df['OfferDetails'].map(prod)

# https://towardsdatascience.com/train-ner-with-custom-training-data-using-spacy-525ce748fab7
# creating data based on requirement of spacy library
train_data = []

for i in tqdm(range(df.shape[0])):
    string = df.iloc[i,0].lower()
    products = df.iloc[i,1]
    entity = []
    loc = []
    for product in set(products):
        product = product.replace(' ’','’').replace('’ ','’').replace(' \'','\'').replace('\' ','\'').replace('...','').replace('$','').strip().lower()
        app = True
        if string.find(product) != -1:
            start = string.find(product)
            end = string.find(product)+len(product)
            for l in loc:
                if start < l[1] and end > l[0]:
                    app = False
                    break

            if app:
                loc.append([start,end])
                entity.append((start,end,'Product'))
    
    train_data.append((string,{'entities':entity}))


with open('excercise-2/train_data.pkl', 'wb') as f:
    pickle.dump(train_data, f)


    