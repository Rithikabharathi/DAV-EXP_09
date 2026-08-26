import pandas as pd

comparison = pd.DataFrame({
    'Metric':['Glucose Mean','BMI Mean','Linear Regression R²','Logistic Accuracy'],
    'UCI Diabetes':[137.36,30.99,0.78,82.4],
    'Pima Indians Diabetes':[136.62,32.48,0.72,79.1]
})
print('Comparison of Analysis Results:\n')
print(comparison.to_string(index=False))
print('\nInterpretation: The UCI values show higher example regression and classification performance, while BMI mean is higher in the Pima dataset.')
