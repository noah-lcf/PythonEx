# coding: UTF-8
from sklearn import datasets, svm, linear_model
import numpy as np

#classfy iris
iris = datasets.load_iris()
iris_X = iris.data
print "iris shape:"+str(iris_X.shape)
iris_y = iris.target
print iris.target_names
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]
# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
print "iris predict :" + str(knn.predict(iris_X_test))
#array([1, 2, 1, 0, 0, 0, 2, 1, 2, 0])
print "iris actually:" + str(iris_y_test)
#array([1, 1, 1, 0, 0, 0, 2, 1, 2, 0])



#predict digit  
digits=datasets.load_digits()
print "shape of digits:"+str(digits.data.shape)
print "num of target:"+str(len(digits.target))

clf=svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])  
print "digit predict:" + str(clf.predict(digits.data[-1]))
#8 
print "digit actually:" + str(digits.target[-1])
#[8]
import pylab as pl
pl.gray()
pl.matshow(digits.images[-1])
#pl.show()

#regression  diabetes
diabetes = datasets.load_diabetes()
# Use only one feature

print diabetes.data.shape
diabetes_X = diabetes.data[:, np.newaxis]
print diabetes_X.shape
diabetes_X_temp = diabetes_X[:, :, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X_temp[:-20]
diabetes_X_test = diabetes_X_temp[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
pl.scatter(diabetes_X_test, diabetes_y_test,  color='black')
pl.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
        linewidth=3)

pl.xticks(())
pl.yticks(())

pl.show()