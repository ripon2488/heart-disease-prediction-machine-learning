import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import seaborn as sns
#import matplotlib.pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,auc, plot_roc_curve,roc_auc_score,roc_curve,roc_auc_score,plot_confusion_matrix,plot_precision_recall_curve
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
# Import Different Algorithm
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


import pickle

st.write("""
# Heart disease Prediction App
This app predicts If a patient has a heart disease oe not

""")

st.sidebar.header('User Input Features')



# Collects user input features into dataframe
#thall,cp,caa,thalachh,oldpeak,slp 
def user_input_features():
    
    thal = st.sidebar.selectbox('thal',(0,1,2))
    cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
    ca = st.sidebar.selectbox('number of major vessels caa',(0,1,2,3))
    tha = st.sidebar.number_input('Maximum heart rate achieved thalachh: ')
    old = st.sidebar.number_input('oldpeak: ')
    slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ')


#thall,cp,caa,thalachh,oldpeak,slp 
    data = {'cp': cp,
            'thalachh':tha,
            'oldpeak':old,
            'slp':slope,
            'caa':ca,
            'thall':thal
                }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

# Combines user input features with entire dataset
# This will be useful for the encoding phase
#heart_dataset = pd.read_csv('heart.csv')
#heart_dataset = heart_dataset.drop(columns=['target'])

#df = pd.concat([input_df,heart_dataset],axis=0)

# Encoding of ordinal features
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
#df = pd.get_dummies(df, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])

#df = df[:1] # Selects only the first row (the user input data)

st.write(input_df)
# Reads in saved classification model
#load_clf = pickle.load(open('model_svc.sav', 'rb'))
#-----------
final_model = 'model_svc.sav'
#pickle.dump(final_model_svc, open(final_model, 'wb'))
 
# some time later...
 
# load the model from disk
model = pickle.load(open(final_model, 'rb'))
#------------------

# Apply model to make predictions
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)


st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
