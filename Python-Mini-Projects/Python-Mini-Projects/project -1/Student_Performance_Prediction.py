# ==========================================
#      STUDENT PERFORMANCE PREDICTION
# ==========================================

print("========== Student Performance Prediction ==========\n")

# Input Section
study_hours = float(input("Enter Study Hours Per Day      : "))
attendance = float(input("Enter Attendance Percentage    : "))
previous_marks = float(input("Enter Previous Marks           : "))
assignment_score = float(input("Enter Assignment Score (100)   : "))

# Processing Section
if study_hours >= 6 and attendance >= 90 and previous_marks >= 85 and assignment_score >= 80:
    result = "Excellent Performer"

elif study_hours >= 4 and attendance >= 75 and previous_marks >= 65 and assignment_score >= 60:
    result = "Good Performer"

else:
    result = "Needs Improvement"

# Output Section
print("\n========== Prediction Result ==========")
print("Student Performance :", result)
print("=======================================")