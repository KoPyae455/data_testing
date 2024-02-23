import pandas as pd
from sklearn.linear_model import LinearRegression

bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv")
model = LinearRegression()
model.fit(bmi_life_data[['BMI']], bmi_life_data['Life expectancy'])
myanmar_life_exp = model.predict([[23.50004]])

print(myanmar_life_exp)
