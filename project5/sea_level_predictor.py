import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from scipy.stats import linregress

_BASE_DIR = Path(__file__).resolve().parent


def draw_plot():
    # Read data from file
    df = pd.read_csv(_BASE_DIR / 'epa-sea-level.csv')

    # Create scatter plot using the Year column as the x-axis and the
    # CSIRO Adjusted Sea Level column as the y-axis.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=5)

    # Create first line of best fit, using all the data, and extend it
    # through the year 2050 to predict the sea level rise in 2050.
    fit_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(1880, 2051))
    sea_all = fit_all.intercept + fit_all.slope * years_all
    plt.plot(years_all, sea_all, color='red')

    # Create second line of best fit, using only the data from the year
    # 2000 through the most recent year in the dataset, and extend it
    # through the year 2050.
    df_recent = df[df['Year'] >= 2000]
    fit_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent = pd.Series(range(2000, 2051))
    sea_recent = fit_recent.intercept + fit_recent.slope * years_recent
    plt.plot(years_recent, sea_recent, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig(_BASE_DIR / 'sea_level_plot.png')
    return plt.gca()
