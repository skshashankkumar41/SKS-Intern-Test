# SKS-Intern-Test

## Exercise 1 
* **Files and Usage**
getFaceValue.py - A function getFaceValue that takes string as parameter and return its extracted facevalue, 

    ```
     python exercise-1/getFaceValue.py --text "Your Text With Facevalue"
    ```
    checkPerformance.py - It has 3 functions to calculate performance of faceValue extraction based on dollor signs, "save/off" keywords etc. It will print all 3 perfomance metrics.
    
    ```
     python exercise-1/checkPerformance.py 
    ```

## Exercise 2
* **Files and Usage**
ner-data-creator.py - It creates data in the format required by spacy by extracting nouns from the coupons corpus [will be entity] and after doing some preprocessing.
    ```
     python exercise-2/ner_data_creator.py 
    ```
    train-ner.py - It trains the ner data created by ner-data-creator.py using spacy and saves the ner model in the same directory.
    ```
     python exercise-2/train_ner.py 
    ```
    get-entity.py - It takes a string as arguement and returns the dictonary with keys as entity type and value as entity
    ```
     python exercise-2/getEntity.py --text "Text containing Entities" 
    ```
    entityOnAllData.py - It just creates the dataframe showing actual and predicted entities on our created ner dataset
    ```
     python exercise-2/entityOnAllData.py 
    ```

