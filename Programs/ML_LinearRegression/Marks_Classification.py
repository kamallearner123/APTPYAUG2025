import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

# Step 1: Define the problem
# Features (x): Hours studied
# Target (y): Pass (1) or Fail (0)

# Step 2: Load data
# Sample data: Hours studied vs Pass/Fail
study_vs_pass = {
    "Hours": [30, 20, 25, 15, 10, 5, 12, 18, 22, 28],
    "Pass": [1, 1, 1, 0, 0, 0, 0, 1, 1, 1]  # 1 = Pass, 0 = Fail
}
df = pd.DataFrame(data=study_vs_pass)

# Step 3: Prepare data (no cleaning needed for this synthetic dataset)
X = np.array(df["Hours"]).reshape(-1, 1)
y = np.array(df["Pass"])

# Step 4: Split data (80/20 train-test split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Build model
# Using LogisticRegression for binary classification
model = LogisticRegression()

# Step 6: Train model
model.fit(X_train, y_train)

# Step 7: Evaluate model
y_pred = model.predict(X_test)
for i in range(len(y_test)):
    print(f"Actual: {y_test[i]}, Predicted: {y_pred[i]}")
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

# Step 8: Persist (optional, not implemented here but could use joblib/pickle)
# Step 9: Predict & monitor (example prediction for a new data point)
new_hours = np.array([[22]])  # Example: Predict for 22 hours studied
prediction = model.predict(new_hours)
print(f"Prediction for 22 hours studied: {'Pass' if prediction[0] == 1 else 'Fail'}")