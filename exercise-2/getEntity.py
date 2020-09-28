import spacy 
import argparse

#"SAVE $1.00 ON TWO when you buy TWO BOXES (8.9 - 15.2 OZ. EXCLUDES LARGE SIZE) any flavor/variety General Mills cereal listed: *"

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--text", required = True, help="Input text")
args = vars(ap.parse_args())

def getEntity(text):
    model = spacy.load('exercise-2/NERModel')
    doc = model(text)
    res = {ent.label_:ent.text for ent in doc.ents}
    print(res)
    return res

getEntity(args['text'])