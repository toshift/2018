import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import neural_network
from sklearn import svm
from sklearn.metrics import accuracy_score, precision_score, recall_score


data = np.loadtxt('foo.csv', delimiter=',', dtype=float)
labels = data[:, 0:1] # 目的変数を取り出す
features = preprocessing.minmax_scale(data[:, 1:]) # 説明変数を取り出した上でスケーリング
x_train, x_test, y_train, y_test = train_test_split(features, labels.ravel(), test_size=0.3) # トレーニングデータとテストデータに分割

#clf = neural_network.MLPClassifier(activation="relu", alpha=0.0001) # clfはclassificationの略語
clf = svm.SVC(kernel='rbf', C=10, gamma=0.1) # clfはclassificationの略語

clf.fit(x_train, y_train)

predict = clf.predict(x_test)
print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))