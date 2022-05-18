from sklearn import linear_model
# from sklearn.linear_model.base import LinearRegression 
reg = linear_model.LinearRegression()

reg.fit( [[0, 0], [1, 1], [2, 2]], [0, 1, 2])

