# This just to see how lambda expressions really work

# create the lambda, with w and h as parameters
bmi = lambda w, h: w/(h**2)

# collect values from user
weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))

# calculate result
result = bmi(weight,height)

# show result
print(f"Your bmi is {result}")