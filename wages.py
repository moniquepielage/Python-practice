# Import necessary libraries for machine learning and data visualization
from sklearn.linear_model import LinearRegression  # For creating and training the linear regression model
from sklearn.metrics import mean_absolute_error, r2_score  # For evaluating model performance
import numpy as np  # For numerical operations and array handling
import matplotlib.pyplot as plt  # For creating charts and plots

# Load data from CSV file created in Excel
# np.loadtxt reads the file, uses ';' as delimiter (Excel's default for some regions),
# and skips the first row (header row with column names)
data = np.loadtxt('wages (version 1).xlsb.csv', delimiter=';', skiprows=1)

# Prepare the data for the model
# X is the input feature (experience) - reshaped to be a 2D array as required by sklearn
# y is the target variable (wage) - what we want to predict
X = data[:, 0].reshape(-1, 1)  # Experience column (first column, index 0)
y = data[:, 1]  # Wage column (second column, index 1)

# Split data into training and testing sets
# Using first 3 samples for training, rest for testing
# This is a simple split - in practice, you'd use train_test_split from sklearn
X_train, y_train, X_test, y_test = X[:3], y[:3], X[3:], y[3:]

# Create and train the linear regression model
model = LinearRegression()  # Initialize the model
model.fit(X_train, y_train)  # Train the model using the training data

# Make predictions on the test data
predictions = model.predict(X_test)  # Predict wages for the test experience values

# Calculate model performance metrics
mae = mean_absolute_error(y_test, predictions)  # Mean Absolute Error - average prediction error
r2 = r2_score(y_test, predictions)  # R² Score - how well the model explains the data (0-1, higher is better)

# Display the results
print("Mean Absolute Error:", mae)  # Shows average dollar error in predictions
print("R^2 Score:", r2)  # Shows model fit quality (closer to 1.0 is better)

# Additional model information
print("slope:", model.coef_[0])  # The slope of the regression line (wage increase per year of experience)
print("R^2 score:", r2)  # Repeated for clarity

# Create the visualization chart
plt.scatter(X, y, color='blue', label='Data points')  # Plot all actual data points as blue dots

# Generate smooth line for the regression model
# Create 100 evenly spaced points between min and max experience values
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_plot = model.predict(X_plot)  # Predict wages for these points to draw the line
plt.plot(X_plot, y_plot, color='red', label='Regression line')  # Plot the fitted regression line

# Add chart formatting and labels
plt.xlabel('Experience (years)')  # X-axis label
plt.ylabel('Wage ($)')  # Y-axis label
plt.title('Wage vs Experience: Linear Regression')  # Chart title
plt.legend()  # Show the legend explaining the blue dots and red line
plt.grid(True)  # Add a grid for better readability

# Display the chart in a window
plt.show()  # This will open a window showing your chart