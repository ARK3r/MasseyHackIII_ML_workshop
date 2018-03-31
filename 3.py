####				BASIC SCIKIT-LEARN (LINEAR REGRESSION)              ####
#### Source: http://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

# linear regression: finding a line of best fit to represent the current and future values

from sklearn import linear_model
# model: Y[i] = X[i] * 4 + 3
X = [[0], [1], [2], [3]]
Y = [3, 7, 11, 15]


reg = linear_model.LinearRegression()
reg.fit(X, Y)
print "\n\n\tfor input array:", X, "and output array:", Y
print "\n\n\tthe set of coefficients respective to features are:", reg.coef_
print "\tand the intercept (constant) is", reg.intercept_

X_ = [[4], [5], [10], [100]]
print "\n\n\tfor input array:", X_, "the predictions are:", reg.predict(X_), "\n\n"
