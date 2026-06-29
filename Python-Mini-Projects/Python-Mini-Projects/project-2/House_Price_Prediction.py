# ==========================================
#         HOUSE PRICE PREDICTION
# ==========================================

print("========== House Price Prediction ==========\n")

# Input Section
house_size = float(input("Enter House Size (sq.ft)    : "))
bedrooms = int(input("Enter Number of Bedrooms    : "))
house_age = int(input("Enter House Age (Years)     : "))
location = input("Enter Location (City/Village): ")

# Processing Section
if house_size >= 1800 and bedrooms >= 3 and house_age <= 5 and location.lower() == "city":
    result = "Premium House"

elif house_size >= 1000 and bedrooms >= 2 and house_age <= 15:
    result = "Standard House"

else:
    result = "Budget House"

# Output Section
print("\n========== Prediction Result ==========")
print("House Category :", result)
print("=======================================")