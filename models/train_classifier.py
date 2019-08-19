import sys
import pandas as pd
import numpy as np
import re 
import nltk
import warnings
import random 
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize, WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
#from sklearn.multiclass import OneVsRestClassifier
#from sklearn.externals import joblib
from sklearn.svm import LinearSVC
import pickle
nltk.download(['punkt', 'wordnet'])
warnings.filterwarnings("ignore")

def load_data(database_filepath):
    x = 'sqlite:///'+ database_filepath
    engine = create_engine(x)
    df = pd.read_sql_table('MSG', engine)
    X = df['message']
    Y = df.iloc[:, 4:]
    cate = Y.columns
    return X, Y, cate

def tokenize(text):
     #lets get tokens
    token = WhitespaceTokenizer().tokenize(text)
    #token = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    # lets clean tokens and return them
    cleaned_tk = []
    for i in token:
        i = lemmatizer.lemmatize(i).lower().strip('!@#$%^&*()"/+=[\\]_-{|}~\'`,;.:<>?')
        i  = re.sub(r'\[[^,.;:]*\]' , '' , i )
        if i != '':
            cleaned_tk.append(i)
            
    return cleaned_tk


def build_model():
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf',TfidfTransformer() ),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))])
    parameters = {'clf__estimator__max_depth': [10, 50, None],
              'clf__estimator__min_samples_leaf':[2, 5, 10]}
    cv =  GridSearchCV(pipeline, param_grid= parameters)
    return cv 


def evaluate_model(model, X_test, y_test, category_names):
    y_pred = model.predict(X_test)
    print(classification_report(y_test.iloc[:,1:].values, np.array([x[1:] for x in y_pred]), target_names= category_names))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath,'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()