# 1. Mock up dummy data
set.seed(0) # for reproducibility
X <- 2 * runif(100, min = 0, max = 1) # Generate 100 random numbers between 0 and 1, then scale to 0 and 2
y <- 4 + 3 * X + rnorm(100) # y = 4 + 3x + noise (rnorm generates standard normal noise)

cat("Dummy Data Generated:\n")
cat("First 5 X values:\n", head(X, 5), "\n")
cat("First 5 y values:\n", head(y, 5), "\n")

# 2. Fit a linear regression model
# In R, we use the lm() function for linear models
model <- lm(y ~ X)

# 3. Print the model\'s coefficients
cat("\nLinear Regression Model Fitted:\n")
cat("Intercept (b0):", coef(model)[["(Intercept)"]], "\n")
cat("Coefficient (b1):", coef(model)[["X"]], "\n")

# 4. Make predictions
X_new <- data.frame(X = c(0, 2)) # Create a data frame for new predictions
y_pred <- predict(model, newdata = X_new)
cat("\nPredictions for X = [0, 2]:\n")
cat(y_pred, "\n")

# Optional: Plot the data and the regression line
plot(X, y,
     main = "Basic Linear Regression",
     xlab = "X",
     ylab = "y",
     col = "blue",
     pch = 19, # Plotting character (solid circle)
     cex = 0.8) # Character expansion (size of points)

abline(model, col = "red", lwd = 3) # Add the regression line

legend("topleft",
       legend = c("Dummy Data", "Regression Line"),
       col = c("blue", "red"),
       lwd = c(NA, 3), # No line for dummy data points
       pch = c(19, NA)) # No point for regression line

grid() # Add a grid
