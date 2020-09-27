import spacy 
import pandas as pd  

df = pd.read_csv('../coupons_ner_preprocessed.csv')

model = spacy.load('NERModel')

compareEntitity = {'Actual':[],'Prediction':[]}

for i in range(df.shape[0]):
    doc = model(df.iloc[i,0])
    compareEntitity['Actual'].append(df.iloc[i,1])
    compareEntitity['Prediction'].append([ent.text for ent in doc.ents])

compareEntititydf = pd.DataFrame(compareEntitity)

compareEntititydf.to_csv('compareEntity.csv',index=False)


    