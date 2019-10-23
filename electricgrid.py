import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import seaborn as sn


df = pd.read_csv('data.csv')


print('COLUMNS : ', df.columns)

print('shape of dataframe : ', df.shape)


labels = df['stabf']
df.drop(columns='stabf', inplace=True)
#print('features sample : ', df.head())


labels = labels.map({'unstable':0, 'stable':1})
#print('Labels sample : ', labels.head())


x_train, x_test, y_train, y_test = train_test_split(df, labels, test_size=0.25, random_state=42)

print('train_features : {}, train_labels : {}'.format(x_train.shape, y_train.shape))
print('test_features : {}, test_labels : {}'.format(x_test.shape, y_test.shape))


clf = SVC(kernel = 'linear', C=75, gamma='auto')
clf.fit(x_train, y_train)
pred = clf.predict(x_test)
print('accuracy : ', accuracy_score(pred, y_test))