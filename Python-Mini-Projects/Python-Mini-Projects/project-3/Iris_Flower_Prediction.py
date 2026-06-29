# ==========================================
#        IRIS FLOWER PREDICTION
# ==========================================

print("========== Iris Flower Prediction ==========\n")

# Input Section
petal_length = float(input("Enter Petal Length (cm) : "))
petal_width = float(input("Enter Petal Width (cm)  : "))
sepal_length = float(input("Enter Sepal Length (cm) : "))
sepal_width = float(input("Enter Sepal Width (cm)  : "))

# Processing Section
if petal_length < 2 and petal_width < 1 and sepal_length < 6 and sepal_width >= 3:
    result = "Iris Setosa"

elif petal_length < 5 and petal_width < 2 and sepal_length < 7 and sepal_width >= 2:
    result = "Iris Versicolor"

else:
    result = "Iris Virginica"

# Output Section
print("\n========== Prediction Result ==========")
print("Flower Species :", result)
print("=======================================")