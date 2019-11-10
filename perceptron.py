import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
""""from sklearn.linear_model import Perceptron"""
import pickle
class Perceptron(object):
        def __init__(self, eta, n_iter):
                self.eta = eta
                self.n_iter = n_iter
        def fit(self, X, y):
                self.w_ = np.zeros(1 + X.shape[1])
                self.errors_=[]
                plot_X=[]
                plot_y=[]
                for _ in range(self.n_iter):
                        errors=0
                        for xi, target in zip(X, y):
                                plot_X.append(xi)
                                plot_y.append(self.predict(xi))
                                error = target - self.predict(xi)
                                if error != 0:
                                        update = self.eta * error
                                        self.w_[1:] += update * xi
                                        self.w_[0] += update
                                        errors+=int(update!=0.0)
                        self.errors_.append(errors)
                return self
        def net_input(self, X):
                return np.dot(X, self.w_[1:]) + self.w_[0]
        def predict(self, X):
                return np.where(self.net_input(X) >= 0.0, 1, -1)
def main():
        data=pd.read_csv('Data_for_UCI_named.csv')
        print(data.head())
        y=data['stabf'].values
        print(y)
        X=data.drop(['stabf'],axis=1).values
        y=np.where(y=='stable',1,-1)
        print(y)
        from sklearn.preprocessing import StandardScaler
        scaler=StandardScaler().fit(X)
        rescaledX=scaler.transform(X)
        rescaledX[0:5,:]
        X_train,X_test,y_train,y_test=train_test_split(
                rescaledX,y,test_size=0.2,random_state=0)
        ppn=Perceptron(n_iter=400, eta=0.4)
        print(X_train)
        ppn.fit(X_train, y_train)
        y_pred=ppn.predict(X_test)
        print('misclassified samples: %d'%(y_test!=y_pred).sum())
        from sklearn.metrics import accuracy_score
        print('Predicting Accuracy:%.2f'%accuracy_score(y_test,y_pred))
        plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
        plt.show()
        with open("final.pkl","wb") as f:
                pickle.dump(ppn,f)

if __name__=='__main__':
    main()

