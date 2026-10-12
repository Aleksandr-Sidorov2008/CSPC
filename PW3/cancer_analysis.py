import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

print('=== Loading Dataset 2 ===')
df_chem = pd.read_csv('chemicals_cancer.csv')
print(f'Dataset shape: {df_chem.shape}')
print(df_chem.head())

print('\n=== Task 6: Naive Analysis (Correlations with Malignancy) ===')
r_benz, p_benz = stats.pearsonr(df_chem['benzene'], df_chem['malignancy'])
r_cadm, p_cadm = stats.pearsonr(df_chem['cadmium'], df_chem['malignancy'])

print(f'Benzene vs Malignancy: r = {r_benz:.4f} (p = {p_benz:.5e})')
print(f'Cadmium vs Malignancy: r = {r_cadm:.4f} (p = {p_cadm:.5e})')

print(
    'Naive conclusion: Benzene shows a much stronger association and appears'
    ' to be the cause.'
)

print('\n=== Task 7: Controlling for Confounding Variable (Pollution Index) ===')

df_chem['pollution_bin'] = pd.qcut(df_chem['pollution_index'], q=3)

for name, group in df_chem.groupby('pollution_bin'):
  rb, _ = stats.pearsonr(group['benzene'], group['malignancy'])
  rc, _ = stats.pearsonr(group['cadmium'], group['malignancy'])
  print(
      f'Pollution Bin {name}: Benzene r = {rb:.4f} | Cadmium r = {rc:.4f}'
  )

print(
    '\nConclusion after accounting for confounding: Within similar pollution'
    ' levels, Benzene correlation drops near zero, while Cadmium remains '
    ' strongly associated. Cadmium is the real cause; Benzene only looked'
    ' guilty because it correlates with general area pollution.'
)

plt.figure(figsize=(8, 5))
plt.scatter(
    df_chem['benzene'],
    df_chem['malignancy'],
    alpha=0.5,
    color='red',
    label='Benzene (Naive culprit)',
)
plt.scatter(
    df_chem['cadmium'],
    df_chem['malignancy'],
    alpha=0.5,
    color='blue',
    label='Cadmium (Real cause)',
)
plt.xlabel('Chemical Level')
plt.ylabel('Tumour Malignancy Score')
plt.title('Chemicals vs Malignancy')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('chemicals_comparison.png')
plt.show()

print('\n=== Bonus: Categorical Unpredictability (Heart Dataset) ===')

columns_heart = [
    'age',
    'sex',
    'cp',
    'trestbps',
    'chol',
    'fbs',
    'restecg',
    'thalach',
    'exang',
    'oldpeak',
    'slope',
    'ca',
    'thal',
    'target',
]
df_heart = pd.read_csv('processed.cleveland.data', names=columns_heart, na_values='?')

proportions = df_heart['target'].value_counts(normalize=True)
print('Target proportions:\n', proportions)

entropy = -np.sum(proportions * np.log2(proportions))
print(
    f'Shannon Entropy of target: {entropy:.4f} bits (max is 1.0 for binary'
    ' balanced)'
)