import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("student_data.csv")

print("STUDENT PERFORMANCE PREDICTION")
print("--------------------------------")

# Display dataset
print("\nDataset:")
print(data)

# Input features
X = data[[
    "Hours_Studied",
    "Attendance",
    "Previous_Score",
    "Assignments"
]]

# Target value
y = data["Final_Score"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Results")
print("-------------")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Get student information
print("\nEnter Student Details")

hours = float(input("Hours studied per day: "))
attendance = float(input("Attendance percentage: "))
previous = float(input("Previous exam score: "))
assignments = float(input("Assignment score: "))

# Create input DataFrame
student = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Previous_Score": [previous],
    "Assignments": [assignments]
})

# Predict final score
prediction = model.predict(student)[0]

print("\nPredicted Final Score:", round(prediction, 2))

# Performance category
if prediction >= 75:
    print("Performance: Excellent")
elif prediction >= 60:
    print("Performance: Good")
elif prediction >= 50:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")