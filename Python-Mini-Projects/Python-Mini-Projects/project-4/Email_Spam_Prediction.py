# ==========================================
#         EMAIL SPAM PREDICTION
# ==========================================

print("========== Email Spam Prediction ==========\n")

# Input Section
sender = input("Enter Sender Type (Known/Unknown): ")
links = int(input("Enter Number of Links           : "))
spam_words = int(input("Enter Number of Spam Words      : "))
attachments = int(input("Enter Number of Attachments     : "))

# Processing Section
if sender.lower() == "unknown" and links >= 3 and spam_words >= 5 and attachments >= 1:
    result = "Spam Email"

elif links >= 1 and spam_words >= 2:
    result = "Suspicious Email"

else:
    result = "Safe Email"

# Output Section
print("\n========== Prediction Result ==========")
print("Email Status :", result)
print("=======================================")