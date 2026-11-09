# Data Analysis with Python — freeCodeCamp

Data Analysis with Python certification projects from freeCodeCamp, by Harsh Ganesh Kalambe, B.Sc. Data Science student at KES Shroff College, Kandivali, Mumbai.

**Status: in progress — certificate not earned yet.** All five projects below are practice builds, tested locally. Nothing here claims a completed certificate.

## Tools
NumPy, Pandas, Matplotlib, Seaborn, Python.

## Projects

### Project 1 — Mean-Variance-Standard Deviation Calculator
`project1/mean_var_std.py`

`calculate()` takes a list of 9 numbers, turns it into a 3×3 NumPy array, and returns the mean, variance, standard deviation, max, min and sum — for the columns, the rows, and the whole matrix. A list with fewer than 9 numbers raises `ValueError: "List must contain nine numbers."`

Checked against freeCodeCamp's example: `calculate([0,1,2,3,4,5,6,7,8])` gives whole-matrix mean 4.0, sum 36, max 8, min 0.

### Project 2 — Demographic Data Analyzer
`project2/demographic_data_analyzer.py` — data in `project2/adult.data.csv` (1994 Census data, UCI Machine Learning Repository)

`calculate_demographic_data()` answers 9 questions with Pandas, including:
- Average age of men: 39.4
- People with a Bachelors degree: 16.4%
- Advanced education earning >50K: 46.5%, without advanced education: 17.4%
- Minimum hours worked per week: 1; of those workers, 10% earn >50K
- Highest-earning country: Iran, 41.9%
- Top occupation for >50K earners in India: Prof-specialty

All 9 answers match freeCodeCamp's expected values.

### Project 3 — Medical Data Visualizer
`project3/medical_data_visualizer.py` — data in `project3/medical_examination.csv` (70,000 rows)

Adds an `overweight` column from BMI (weight / height², 1 when BMI > 25), normalises `cholesterol` and `gluc` so 0 is always good and 1 is always bad, then draws two charts:
- `draw_cat_plot()` — counts of cholesterol, gluc, smoke, alcohol, activity and overweight, split by cardio disease (saved as `catplot.png`)
- `draw_heat_map()` — correlation heatmap after cleaning (ap_lo ≤ ap_hi, height and weight within the 2.5th–97.5th percentiles), upper triangle masked (saved as `heatmap.png`)

Tested 2026-11-08 with freeCodeCamp's own `test_module.py`: **all 4 tests pass** (cat-plot labels, 13 bars, heatmap labels and heatmap values). Strongest correlations in the cleaned data: overweight–weight 0.7, height–sex 0.5, cholesterol–gluc 0.4.

### Project 4 — Page View Time Series Visualizer
`project4/time_series_visualizer.py` — data in `project4/fcc-forum-pageviews.csv` (1,304 daily page-view counts, 9 May 2016 – 3 Dec 2019)

Cleans the data by dropping days in the top and bottom 2.5% of page views (1,304 → 1,238 rows), then draws three charts:
- `draw_line_plot()` — daily page views over time (`line_plot.png`)
- `draw_bar_plot()` — average monthly page views grouped by year (`bar_plot.png`)
- `draw_box_plot()` — year-wise box plot (trend) and month-wise box plot (seasonality) (`box_plot.png`)

Tested 2026-11-08 with freeCodeCamp's own `test_module.py`: **all 11 tests pass** (data cleaning, line-plot title/labels/1,238 points, bar-plot legend/labels/49 bars, box-plot labels/titles/4 year boxes and 12 month boxes). Median daily page views in the cleaned data: 57,197; highest monthly average: December 2019 (~150,734/day).

### Project 5 — Sea Level Predictor
`project5/sea_level_predictor.py` — data in `project5/epa-sea-level.csv` (134 yearly records, 1880–2013, CSIRO Adjusted Sea Level in inches)

`draw_plot()` draws a scatter plot of sea level against year, then two lines of best fit (SciPy `linregress`), both extended to 2050:
- All data (1880–2013): about 0.063 inches/year, predicting about 10.18 inches above the 1880 level by 2050 (saved as `sea_level_plot.png`, red line)
- Data from 2000 onwards only: about 0.166 inches/year — the rise is faster in recent decades — predicting about 15.38 inches by 2050 (green line)

The practice copy of the CSV carries the two columns this project uses (Year and CSIRO Adjusted Sea Level), with freeCodeCamp's frozen boilerplate values; the full EPA file also has Lower/Upper Error Bound and NOAA Adjusted Sea Level columns, and the live copy of that file has since revised the 1990–2013 values.

Tested 2026-11-09 with freeCodeCamp's own `test_module.py` (from the boilerplate-sea-level-predictor repo): **all 4 tests pass** (title, labels including x-ticks, 134 scatter points, both fit lines — 171 and 51 values). The authoritative check is still freeCodeCamp's own test runner when the project is submitted there.

## How to run
```bash
python3 project1/mean_var_std.py
python3 project2/demographic_data_analyzer.py
python3 project3/main.py
python3 project4/main.py
python3 project5/main.py
```
