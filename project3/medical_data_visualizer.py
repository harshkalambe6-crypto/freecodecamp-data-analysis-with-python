import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path

_BASE_DIR = Path(__file__).resolve().parent

# Import data
df = pd.read_csv(_BASE_DIR / 'medical_examination.csv')

# Add 'overweight' column: BMI = weight (kg) / height (m)^2;
# overweight is 1 when BMI > 25, otherwise 0.
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(
    lambda bmi: 1 if bmi > 25 else 0
)

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0.
# If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active',
                    'overweight'],
    )

    # Group and reformat the data to split it by 'cardio'.
    # Show the counts of each feature.
    df_cat = df_cat.groupby(
        ['cardio', 'variable', 'value'], as_index=False
    ).size()
    df_cat = df_cat.rename(columns={'size': 'total'})

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        data=df_cat, x='variable', y='total', hue='value', col='cardio',
        kind='bar',
    )

    # Do not modify the next two lines
    fig.savefig(_BASE_DIR / 'catplot.png')
    return fig.fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr, mask=mask, vmax=0.3, center=0, square=True, linewidths=0.5,
        cbar_kws={'shrink': 0.5}, annot=True, fmt='.1f', ax=ax,
    )

    # Do not modify the next two lines
    fig.savefig(_BASE_DIR / 'heatmap.png')
    return fig
