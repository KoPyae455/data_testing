import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.array([0,1,2,3,4,5])
y1 = 2*x+2
y2 = 2*x

plt.scatter(x, y1, color = "black")
plt.scatter(x, y2, color = "black")
plt.plot(x, y1, color = "red", label="y2x+2", linewidth=3)
plt.plot(x, y2, color = "green", label="y2x", linewidth=3)
plt.xlabel("x = independent")
plt.ylabel("x = dependent")
plt.text(2, 2,'a is line of slope\n b is line of intercept',
         rotation = 2,
         horizontalalignment="center",
         verticalalignment="top",
         multalignment="center")


from sklearn import linear_model
from sklearn.matrics import mean_squared_error, r2_score
x = np.array([1,2,3,4,5])
y = np.array([3,2,3,5,4])
reg = linear_model.LinearRegression()
reg.fit(x,y)



y_pred = reg.predict(x)
reg.intercept_
#reg.coef



x = np.array([1,2,3,4,5])
y = np.array([3,2,3,5,4])
plt.scatter(x, y, color = "red")
plt.xlabel("independent varible")
plt.ylabel("target (dependent)")
plt.mergins(0.1,0.5)



y1 = 0.5*x+1.9
plt.scatter(x, y1, color = "black")
plt.plot(x, y1, linewidth=3)



x = np.array([1,2,3,4,5])
y = np.array([3,2,3,4,5])

plt.scatter(x, y, color = "red")
plt.xlabel("independent varible")
plt.ylabel("target (dependent)")
plt.mergins(0.1,0.5)
y1 = 0.5*x+1.9
plt.scatter(x, y1, color = "black")
plt.plot(x, y1, linewidth=2)


r2_score(y, y_pred)

##

mean_squared_error(y, y_pred)

##

import statistics
mse = statistics.variance(y)
mse

##

x = np.array([1,2,3,4,5])
y = np.array([3,2,3,4,5])

plt.scatter(x, y, color = "red")
plt.xlabel("independent varible")
plt.ylabel("target (dependent)")
plt.mergins(0.1,0.5)
plt.grid(True)
i = np.arange(0.1,1,0.1)
for value in i:
    y1 = value*x+1.9
    plt.scatter(x, y1 , color = "black")
    plt.plot(x, y1, linewidth=2)
    plt.text(2,8,
             "y = ax (n=0.1,1,0.1)",rotation=0)
    plt.show()


