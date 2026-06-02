import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# https://www.geeksforgeeks.org/machine-learning/how-to-perform-a-two-way-anova-in-python/

df = pd.read_csv('rpr-1305.csv')
model = ols('Pressure ~ C(Sugar) + C(Weight) + C(Sugar):C(Weight)', data=df).fit()
anova_result = anova_lm(model, typ=2)

# Ostatnia kolumna to p-value - gdy < 0.05 to odrzucamy
print(anova_result)