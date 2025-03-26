# SpendSense: Consumer Credit Card Spending Analysis

A data analysis project examining the relationships between annual income, household size, and credit card spending patterns using statistical methods and regression modeling.

## Project Overview

SpendSense analyzes consumer spending behavior by investigating how annual income and household size influence credit card charges. The project uses statistical analysis and regression modeling to identify significant relationships and predictive factors in consumer spending patterns.

## Key Features

- **Descriptive Statistics**: Calculates means and standard deviations for key variables
- **Data Visualization**: Creates histograms, boxplots, and scatter plots to visualize distributions and relationships
- **Regression Analysis**: Implements simple and multiple linear regression models
- **Statistical Testing**: Evaluates significance of relationships between variables
- **Predictive Modeling**: Develops models to predict credit card charges based on household characteristics

## Data Description

The analysis uses consumer spending data (`consumer.csv`) containing three primary variables:

- **Annual Income**: Household annual income in thousands of dollars
- **Household Size**: Number of individuals in the household
- **Credit Card Charges**: Annual credit card spending in dollars

## Analysis and Findings

### Descriptive Statistics
The analysis begins with basic statistical measures (mean, standard deviation) for all variables to understand their distributions.

### Visualizations
Several visualizations are generated to explore the data:

1. **Distribution Histograms**: Show the frequency distributions of income, household size, and credit card charges
2. **Boxplots**: Identify potential outliers and summarize the central tendency and spread
3. **Scatter Plots**: Visualize relationships between:
   - Annual income and credit card charges
   - Household size and credit card charges
4. **3D Plot**: Demonstrates the combined effect of both income and household size on credit card spending

### Regression Models

The project implements three regression models:

1. **Simple Linear Regression (Income)**: Predicts credit card charges based solely on annual income
2. **Simple Linear Regression (Household Size)**: Predicts credit card charges based solely on household size
3. **Multiple Linear Regression**: Combines both income and household size to predict credit card charges

Each model is evaluated using:
- Coefficient estimates
- P-values for statistical significance
- R-squared values for goodness of fit

## Key Findings

The analysis reveals:

1. A positive correlation between annual income and credit card charges
2. A positive correlation between household size and credit card charges
3. The multiple regression model demonstrates improved predictive power compared to either simple regression model alone
4. Both income and household size are statistically significant predictors of credit card spending

## File Structure

- `code_1.py`: Main Python script containing the complete analysis
- `consumer.csv`: Dataset with consumer spending information
- `annual_income_distribution.png`: Histogram of income distribution
- `household_size_distribution.png`: Histogram of household size distribution
- `credit_card_charges_distribution.png`: Histogram of charges distribution
- `annual_income_boxplot.png`: Boxplot of annual income

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/yourusername/SpendSense.git
   cd SpendSense
   ```

2. Install required packages
   ```
   pip install pandas numpy matplotlib statsmodels
   ```

3. Run the analysis script
   ```
   python code_1.py
   ```

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **Matplotlib**: Data visualization
- **Statsmodels**: Statistical modeling and hypothesis testing

## Future Work

- Incorporate demographic variables (age, education, occupation) for more nuanced analysis
- Segment consumers into clusters based on spending patterns
- Develop interactive visualizations for exploring the data
- Implement machine learning models for improved predictions
- Time series analysis to examine seasonal spending patterns

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Financial institutions for inspiring the analysis of consumer spending patterns
- The Python data science community for their excellent tools and libraries
