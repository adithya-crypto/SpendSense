import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


# Load data from CSV file
file_path = "consumer.csv"  # Update to your CSV file name
df = pd.read_csv(file_path)

# Update column names based on the actual names in your CSV file
annual_income_data = df["income"].tolist()
household_size_data = df["Household_Size"].tolist()
credit_card_charges_data = df["Amount_Charged"].tolist()

# Calculate mean and standard deviation for Annual Income
mean_income = np.mean(annual_income_data)
std_dev_income = np.std(annual_income_data)

# Calculate mean and standard deviation for Household Size
mean_household_size = np.mean(household_size_data)
std_dev_household_size = np.std(household_size_data)

# Calculate mean and standard deviation for Credit Card Charges
mean_credit_card_charges = np.mean(credit_card_charges_data)
std_dev_credit_card_charges = np.std(credit_card_charges_data)

# Print the results
print("\nDescriptive Statistics:")
print("• Annual Income:")
print(f"  • Mean: ${mean_income:.2f}")
print(f"  • Standard Deviation: ${std_dev_income:.2f}")
print("• Household Size:")
print(f"  • Mean: {mean_household_size:.2f}")
print(f"  • Standard Deviation: {std_dev_household_size:.2f}")
print("• Credit Card Charges:")
print(f"  • Mean: ${mean_credit_card_charges:.2f}")
print(f"  • Standard Deviation: ${std_dev_credit_card_charges:.2f}")


plt.figure(figsize=(8, 6))
plt.hist(annual_income_data, bins=20, color="skyblue", edgecolor="black")
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income ($1000s)")
plt.ylabel("Frequency")
plt.savefig("annual_income_distribution.png")  # Save the plot as an image
plt.show()

# Household Size Distribution
plt.figure(figsize=(8, 6))
plt.hist(household_size_data, bins=10, color="lightcoral", edgecolor="black")
plt.title("Household Size Distribution")
plt.xlabel("Household Size")
plt.ylabel("Frequency")
plt.savefig("household_size_distribution.png")  # Save the plot as an image
plt.show()

# Credit Card Charges Distribution
plt.figure(figsize=(8, 6))
plt.hist(credit_card_charges_data, bins=20, color="lightgreen", edgecolor="black")
plt.title("Credit Card Charges Distribution")
plt.xlabel("Amount Charged ($)")
plt.ylabel("Frequency")
plt.savefig("credit_card_charges_distribution.png")  # Save the plot as an image
plt.show()

# Annual Income Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(
    annual_income_data,
    vert=False,
    widths=0.7,
    patch_artist=True,
    boxprops=dict(facecolor="pink"),
)
plt.title("Annual Income Boxplot")
plt.xlabel("Annual Income ($1000s)")
plt.savefig("annual_income_boxplot.png")  # Save the plot as an image
plt.show()

X = sm.add_constant(annual_income_data)

# Fit the regression model
model = sm.OLS(credit_card_charges_data, X).fit()

# Print the regression results
print("Regression Equation: Annual Income as Independent Variable\n")
print(model.summary().as_text())

X = sm.add_constant(household_size_data)

# Fit the regression model
model = sm.OLS(credit_card_charges_data, X).fit()

# Print the regression results in a format suitable for copy-pasting into Word
print("Regression Equation: Household Size as Independent Variable\n")
print(model.summary().as_text())

X = sm.add_constant(np.column_stack((annual_income_data, household_size_data)))

# Fit the regression model
model = sm.OLS(credit_card_charges_data, X).fit()

# Print the regression results in a format suitable for copy-pasting into Word
print("Regression Equation: Annual Income and Household Size as Independent Variables\n")
print(model.summary().as_text())

coefficients_income = model_income.params[1]
X_income = sm.add_constant(annual_income_data)
model_income = sm.OLS(credit_card_charges_data, X_income).fit()
coefficients_income = model_income.params
p_value_income = model_income.pvalues[1]

# Fit the regression model with household size as the independent variable
X_size = sm.add_constant(household_size_data)
model_size = sm.OLS(credit_card_charges_data, X_size).fit()
coefficients_size = model_size.params
p_value_size = model_size.pvalues[1]

# Fit the regression model with both annual income and household size as independent variables
X_combined = sm.add_constant(np.column_stack((annual_income_data, household_size_data)))
model_combined = sm.OLS(credit_card_charges_data, X_combined).fit()
coefficients_combined = model_combined.params
p_values_combined = model_combined.pvalues[1:]

# Print the results
print("\nResults for Annual Income as Independent Variable:")
print("Coefficients:", coefficients_income)
print("P-value:", p_value_income)

print("\nResults for Household Size as Independent Variable:")
print("Coefficients:", coefficients_size)
print("P-value:", p_value_size)

print("\nResults for Combined Model (Annual Income + Household Size):")
print("Coefficients:", coefficients_combined)
print("P-values:", p_values_combined) DataFrame format:")
print(results_df)
