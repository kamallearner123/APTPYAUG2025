# Simple regression example
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: Hours studied vs Performance
study_vs_perf = {"Hours":[30, 20, 25, 15, 10, 5, 12, 18, 22, 28],
                 "Performance":[85, 70, 75, 60, 50, 30, 55, 65, 72, 80] }
df = pd.DataFrame(data = study_vs_perf)

# Prepare data
X = np.array(df["Hours"]).reshape(-1, 1)
y = np.array(df["Performance"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
for i in range(len(y_test)):
    print(f"Actual: {y_test[i]}, Predicted: {y_pred[i]:.2f}")
mse = np.mean((y_test - y_pred) ** 2)
print(f"Mean Squared Error: {mse:.2f}")

# Plotting (optional)
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.plot(X_test, y_pred, 'go')  # Predictions on test set
plt.plot(X_test, y_test, 'yx')  # Actual values on test set
plt.xlabel('Hours Studied')
plt.ylabel('Performance')
plt.title('Hours Studied vs Performance')
plt.savefig("regression_plot.png")

