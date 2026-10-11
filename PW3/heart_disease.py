import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

columns = [
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

df = pd.read_csv('processed.cleveland.data', names=columns, na_values='?')

print(f'Dataset shape (rows, columns): {df.shape}')
print('\nFirst 5 rows:')
print(df.head())

continuous_cols = ['age', 'chol', 'trestbps', 'thalach']
df_continuous = df[continuous_cols]

print('\nIsolated continuous variables:')
print(df_continuous.head())

print('\nSummary statistics for continuous variables:')
print(df_continuous.describe())

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

ax1.hist(df['age'].dropna(), bins=15, edgecolor='black')
ax1.set_title('Age')
ax1.set_xlabel('Years')
ax1.set_ylabel('Frequency')

ax2.hist(df['trestbps'].dropna(), bins=15, edgecolor='black')
ax2.set_title('Resting Blood Pressure (trestbps)')
ax2.set_xlabel('mmHg')
ax2.set_ylabel('Frequency')

ax3.hist(df['chol'].dropna(), bins=15, edgecolor='black')
ax3.set_title('Serum Cholestoral (chol)')
ax3.set_xlabel('mg/dl')
ax3.set_ylabel('Frequency')

ax4.hist(df['thalach'].dropna(), bins=15, edgecolor='black')
ax4.set_title('Max Heart Rate (thalach)')
ax4.set_xlabel('bpm')
ax4.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('continuous_distributions.png')

fig_qq, axes = plt.subplots(2, 2, figsize=(10, 8))
axes_flat = axes.flatten()

for i, col in enumerate(continuous_cols):
  print(f'=== Variable analysis: {col} ===')
  clean_data = df[col].dropna()

  stats.probplot(clean_data, dist='norm', plot=axes_flat[i])
  axes_flat[i].set_title(f'Q-Q Plot: {col}')

  stat, p_val = stats.shapiro(clean_data)
  print(f'Shapiro-Wilk W-statistic = {stat:.5f}')
  print(f'Shapiro-Wilk p-value = {p_val:.5f}')

  if p_val < 0.05:
    print('Conclusion: Distribution IS NOT normal (p < 0.05)\n')
  else:
    print('Conclusion: Distribution IS normal (p >= 0.05)\n')

plt.tight_layout()
plt.savefig('qq_plots.png')

print('=== Session 2 / Part 4: Comparing thalach across groups ===')

df['disease_group'] = df['target'].apply(lambda x: 0 if x == 0 else 1)

healthy_thalach = df[df['disease_group'] == 0]['thalach'].dropna()
disease_thalach = df[df['disease_group'] == 1]['thalach'].dropna()

print(
    f'Healthy group count: {len(healthy_thalach)}, Disease group count:'
    f' {len(disease_thalach)}'
)

u_stat, p_val_mann = stats.mannwhitneyu(
    healthy_thalach, disease_thalach, alternative='two-sided'
)
t_stat, p_val_t = stats.ttest_ind(healthy_thalach, disease_thalach)

print(f'Mann-Whitney U test p-value: {p_val_mann:.5e}')
print(f'Two-sample t-test p-value: {p_val_t:.5e}')

if p_val_mann < 0.05:
  print(
      'Conclusion: Reject H0 -> The two groups genuinely differ in maximum heart'
      ' rate (thalach).\n'
  )
else:
  print(
      'Conclusion: Fail to reject H0 -> No significant difference between'
      ' groups.\n'
  )

mean_h = healthy_thalach.mean()
std_h = healthy_thalach.std(ddof=1)
se_h = std_h / np.sqrt(len(healthy_thalach))
ci_h = 1.96 * se_h

mean_d = disease_thalach.mean()
std_d = disease_thalach.std(ddof=1)
se_d = std_d / np.sqrt(len(disease_thalach))
ci_d = 1.96 * se_d

print('--- Group Statistics ---')
print(
    f'Healthy: Mean = {mean_h:.2f} ± {se_h:.2f} (SE), 95% CI'
    f' [{mean_h - ci_h:.2f}, {mean_h + ci_h:.2f}]'
)
print(
    f'Disease: Mean = {mean_d:.2f} ± {se_d:.2f} (SE), 95% CI'
    f' [{mean_d - ci_d:.2f}, {mean_d + ci_d:.2f}]'
)

groups = ['Healthy', 'Heart Disease']
means = [mean_h, mean_d]
errors = [ci_h, ci_d]

plt.figure(figsize=(6, 5))
plt.bar(
    groups,
    means,
    yerr=errors,
    capsize=5,
    color=['skyblue', 'salmon'],
    edgecolor='black',
)
plt.ylabel('Maximum Heart Rate (thalach)')
plt.title('Comparison of thalach by Health Status (with 95% CI)')
plt.ylim(0, 180)

for i, v in enumerate(means):
  plt.text(
      i,
      v / 2,
      f'{v:.1f}',
      ha='center',
      va='center',
      fontweight='bold',
      fontsize=12,
  )

plt.tight_layout()
plt.savefig('thalach_comparison.png')

print('=== Session 2 / Part 5: Correlation between age and thalach ===')

df_corr = df[['age', 'thalach']].dropna()

r_val, p_val_corr = stats.pearsonr(df_corr['age'], df_corr['thalach'])

print(f'Pearson correlation coefficient r = {r_val:.5f}')
print(f'Correlation p-value = {p_val_corr:.5e}')

if p_val_corr < 0.05:
  print(
      'Conclusion: Reject H0 -> There is a statistically significant'
      ' correlation between age and thalach.\n'
  )
else:
  print(
      'Conclusion: Fail to reject H0 -> No significant correlation found.\n'
  )

plt.figure(figsize=(6, 5))
plt.scatter(
    df_corr['age'],
    df_corr['thalach'],
    alpha=0.6,
    edgecolor='k',
    color='purple',
)
plt.xlabel('Age (years)')
plt.ylabel('Maximum Heart Rate (thalach)')
plt.title(f'Age vs Thalach Correlation (r = {r_val:.2f})')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('age_thalach_correlation.png')
plt.show()