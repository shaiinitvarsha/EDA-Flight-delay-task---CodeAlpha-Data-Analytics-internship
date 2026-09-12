# CodeAlpha Data Analytics Internship — Task: Exploratory Data Analysis (EDA)

## 📌 Overview
This project is submitted as part of the **CodeAlpha Data Analytics Internship**.
It performs Exploratory Data Analysis (EDA) on real-world US airline arrival delay
data from 2019, sourced from the Bureau of Transportation Statistics.

## 📊 Dataset
- **File:** `delays_2019.csv`
- **Rows:** 20,946
- **Granularity:** one row per carrier–airport pair, per month of 2019
- **Source:** [nickdcox/learn-airline-delays](https://github.com/nickdcox/learn-airline-delays) (originally from the U.S. Bureau of Transportation Statistics)
- **Columns include:** carrier, airport, number of arriving flights, number delayed
  15+ minutes, cancellations, diversions, and delay minutes broken down by cause
  (carrier, weather, air traffic system, security, late aircraft).

## 🎯 What the analysis covers
- Dataset structure, data types, and missing values
- Duplicate record checks
- Overall delay and cancellation rates
- Delay rate comparison across all 18 carriers
- Breakdown of *why* flights get delayed (which cause contributes most minutes)
- Busiest airports vs. airports with the worst delay rates
- Delay rate trends by month
- Hypothesis test: do summer months (Jun–Aug) see more delays?
- Data quality issues identified and how they were handled

## 🔑 Key findings
- Overall delay rate: **18.72%**; cancellation rate: **1.82%**
- **Hawaiian Airlines** has the best on-time performance (11.4% delay rate);
  **ExpressJet** and **Frontier** are the worst (~25%)
- The single biggest cause of delay minutes is **late aircraft** (39.7%) —
  a knock-on effect from a plane's previous flight running late — not weather
- **Newark (EWR)** and **LaGuardia (LGA)** have the highest delay rates among
  major airports, despite Atlanta (ATL) being the busiest airport overall
- Summer months (Jun–Aug) do have meaningfully higher delay rates (21.6%)
  than the rest of the year (17.7%)

## 🛠 Tools used
- Python
- pandas, numpy — data loading, cleaning, aggregation
- tabulate — formatting tables in the report

## 📂 Project structure
```
.
├── 01_eda_flat.py          # Main EDA script
├── delays_2019.csv         # Raw dataset (input)
├── delays_2019_clean.csv   # Cleaned dataset (generated on run)
├── EDA_report.md           # Full written report (generated on run)
└── README.md
```

## ▶️ How to run
```bash
pip install pandas numpy tabulate
python 01_eda_flat.py
```
This prints the full EDA to the terminal and generates `EDA_report.md` and
`delays_2019_clean.csv` in the same folder.

## 🙋 About
Submitted for the **CodeAlpha Data Analytics Internship**.
[www.codealpha.tech](https://www.codealpha.tech)
