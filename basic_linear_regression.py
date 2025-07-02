import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Mock up dummy data
np.random.seed(0) # for reproducibility
X = 2 * np.random.rand(100, 1) # Generate 100 random numbers between 0 and 2
y = 4 + 3 * X + np.random.randn(100, 1) # y = 4 + 3x + noise

print("Dummy Data Generated:")
print("First 5 X values:\n", X[:5].flatten())
print("First 5 y values:\n", y[:5].flatten())

# 2. Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# 3. Print the model's coefficients
print("\nLinear Regression Model Fitted:")
print(f"Intercept (b0): {model.intercept_[0]:.2f}")
print(f"Coefficient (b1): {model.coef_[0][0]:.2f}")

# 4. Make predictions
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)
print("\nPredictions for X = [0, 2]:")
print(y_pred.flatten())

# Optional: Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Dummy Data')
plt.plot(X_new, y_pred, color='red', linewidth=3, label='Regression Line')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Basic Linear Regression")
plt.legend()
plt.grid(True)
plt.show()