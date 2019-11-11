import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import seaborn as sn
import pickle
import glob
import seaborn as sns
import pickle

data_set = glob.glob('*.csv')

df = pd.read_csv(data_set[0])
print(df.isnull().sum())

print('COLUMNS : ', df.columns)
print('shape of dataframe : ', df.shape)
labels = df['stabf']
df.drop(columns='stabf', inplace=True)
labels = labels.map({'unstable':0, 'stable':1})
df['labels'] = labels
corr = df.corr()
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns)

x_train, x_test, y_train, y_test = train_test_split(df[df.columns[0:13]], labels, test_size=0.25, random_state=42)
with open('lists.pkl', 'wb') as file:
    pickle.dump([x_test, y_test], file)
print('train_features : {}, train_labels : {}'.format(x_train.shape, y_train.shape))
print('test_features : {}, test_labels : {}'.format(x_test.shape, y_test.shape))

try:
    with open('svm.pkl', 'rb') as file:
        saved_model = pickle.load(file)
except:
    clf = SVC(kernel = 'linear', C=75, gamma='auto')
    clf.fit(x_train, y_train)
    with open('svm.pkl', 'wb') as file:
        pickle.dump(clf, file)
    with open('svm.pkl', 'rb') as file:
        saved_model = pickle.load(file)


pred = saved_model.predict(x_test)
print('accuracy : ', accuracy_score(pred, y_test))
