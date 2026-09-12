"""
CodeAlpha Data Analytics Internship — Task : Exploratory Data Analysis (EDA)
Dataset: US Airline Arrival Delays (2019)
Source: Bureau of Transportation Statistics (via nickdcox/learn-airline-delays on GitHub)

Each row = one carrier-airport pair for one month of 2019, with counts of
on-time vs delayed/cancelled/diverted arrivals and delay minutes broken down
by cause (carrier, weather, NAS/air-traffic-system, security, late aircraft).

This script:
1. Loads and inspects the raw dataset
2. Checks data types, missing values and duplicates
3. Explores delay rates, cancellations, and causes of delay
4. Compares carriers and airports against each other
5. Tests a couple of simple hypotheses about the data
6. Flags data quality issues to handle before further analysis
7. Saves a cleaned version of the dataset for later tasks
"""

import pandas as pd
import numpy as np

pd.set_option("display.width", 120)

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
df = pd.read_csv("../data/delays_2019.csv")

report_lines = []


def log(line=""):
    print(line)
    report_lines.append(str(line))


log("# EDA Report — US Airline Arrival Delays (2019)\n")
log(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

# ---------------------------------------------------------------------------
# 2. Structure & data types
# ---------------------------------------------------------------------------
log("## 1. Column overview\n")
log("| Column | Dtype | Non-null | Missing % |")
log("|---|---|---|---|")
for col in df.columns:
    non_null = df[col].notnull().sum()
    missing_pct = round(100 * (1 - non_null / len(df)), 2)
    log(f"| {col} | {df[col].dtype} | {non_null} | {missing_pct}% |")

# ---------------------------------------------------------------------------
# 3. Duplicates
# ---------------------------------------------------------------------------
dupes = df.duplicated(subset=["date", "carrier", "airport"]).sum()
log(f"\n**Duplicate (date, carrier, airport) rows:** {dupes}")

# ---------------------------------------------------------------------------
# 4. Rows with missing core metrics — inspect and decide how to handle
# ---------------------------------------------------------------------------
missing_rows = df[df["arr_flights"].isnull()]
log(f"\n**Rows missing core flight-count data:** {len(missing_rows)} "
    f"(dropped for numeric analysis — no usable data in those rows).")

df_num = df.dropna(subset=["arr_flights"]).copy()

# ---------------------------------------------------------------------------
# 5. Overall scale
# ---------------------------------------------------------------------------
log("\n## 2. Overall scale\n")
log(f"- Total scheduled arrivals recorded: {int(df_num['arr_flights'].sum()):,}")
log(f"- Total delayed arrivals (15+ min): {int(df_num['arr_del15'].sum()):,}")
log(f"- Total cancelled arrivals: {int(df_num['arr_cancelled'].sum()):,}")
log(f"- Total diverted arrivals: {int(df_num['arr_diverted'].sum()):,}")
log(f"- Carriers covered: {df_num['carrier_name'].nunique()}")
log(f"- Airports covered: {df_num['airport'].nunique()}")
log(f"- Months covered: {sorted(df_num['date'].unique())}")

# ---------------------------------------------------------------------------
# 6. Delay rate
# ---------------------------------------------------------------------------
overall_delay_rate = df_num["arr_del15"].sum() / df_num["arr_flights"].sum() * 100
overall_cancel_rate = df_num["arr_cancelled"].sum() / df_num["arr_flights"].sum() * 100
log("\n## 3. Delay and cancellation rates\n")
log(f"- Overall delay rate (15+ min late): {overall_delay_rate:.2f}%")
log(f"- Overall cancellation rate: {overall_cancel_rate:.2f}%")

# ---------------------------------------------------------------------------
# 7. Delay rate by carrier
# ---------------------------------------------------------------------------
log("\n## 4. Delay rate by carrier\n")
by_carrier = df_num.groupby("carrier_name").agg(
    flights=("arr_flights", "sum"),
    delayed=("arr_del15", "sum"),
    cancelled=("arr_cancelled", "sum"),
)
by_carrier["delay_rate_%"] = (by_carrier["delayed"] / by_carrier["flights"] * 100).round(2)
by_carrier["cancel_rate_%"] = (by_carrier["cancelled"] / by_carrier["flights"] * 100).round(2)
by_carrier = by_carrier.sort_values("delay_rate_%", ascending=False)
log(by_carrier.to_markdown())

# ---------------------------------------------------------------------------
# 8. Causes of delay (share of total delay minutes)
# ---------------------------------------------------------------------------
log("\n## 5. What causes delays (share of total delay minutes)\n")
delay_causes = {
    "Carrier (airline's own fault)": df_num["carrier_delay"].sum(),
    "Weather": df_num["weather_delay"].sum(),
    "NAS (air traffic system)": df_num["nas_delay"].sum(),
    "Security": df_num["security_delay"].sum(),
    "Late aircraft (previous flight ran late)": df_num["late_aircraft_delay"].sum(),
}
total_delay_minutes = sum(delay_causes.values())
for cause, minutes in sorted(delay_causes.items(), key=lambda x: -x[1]):
    pct = minutes / total_delay_minutes * 100
    log(f"- {cause}: {int(minutes):,} minutes ({pct:.1f}%)")

# ---------------------------------------------------------------------------
# 9. Busiest and worst-delay airports
# ---------------------------------------------------------------------------
log("\n## 6. Airports — busiest by volume\n")
by_airport = df_num.groupby(["airport", "airport_name"]).agg(
    flights=("arr_flights", "sum"),
    delayed=("arr_del15", "sum"),
)
by_airport["delay_rate_%"] = (by_airport["delayed"] / by_airport["flights"] * 100).round(2)
busiest = by_airport.sort_values("flights", ascending=False).head(10)
log(busiest.to_markdown())

log("\n## 7. Airports with highest delay rate (min 500 flights/year, to avoid noise)\n")
worst_delay = by_airport[by_airport["flights"] >= 500].sort_values("delay_rate_%", ascending=False).head(10)
log(worst_delay.to_markdown())

# ---------------------------------------------------------------------------
# 10. Seasonality — delay rate by month
# ---------------------------------------------------------------------------
log("\n## 8. Delay rate by month\n")
by_month = df_num.groupby("date").agg(
    flights=("arr_flights", "sum"),
    delayed=("arr_del15", "sum"),
)
by_month["delay_rate_%"] = (by_month["delayed"] / by_month["flights"] * 100).round(2)
log(by_month.to_markdown())

# ---------------------------------------------------------------------------
# 11. Hypothesis check: are summer months worse for delays?
# ---------------------------------------------------------------------------
log("\n## 9. Hypothesis: summer months (Jun-Aug) have higher delay rates\n")
df_num["month_num"] = df_num["date"].str.split("-").str[1].astype(int)
summer = df_num[df_num["month_num"].isin([6, 7, 8])]
rest = df_num[~df_num["month_num"].isin([6, 7, 8])]
summer_rate = summer["arr_del15"].sum() / summer["arr_flights"].sum() * 100
rest_rate = rest["arr_del15"].sum() / rest["arr_flights"].sum() * 100
log(f"- Summer (Jun-Aug) delay rate: {summer_rate:.2f}%")
log(f"- Rest of year delay rate: {rest_rate:.2f}%")
log("- Hypothesis confirmed: summer delay rates are higher." if summer_rate > rest_rate
    else "- Hypothesis not confirmed by this data.")

# ---------------------------------------------------------------------------
# 12. Data quality issues found
# ---------------------------------------------------------------------------
log("\n## 10. Data quality issues identified\n")
log(f"- {len(missing_rows)} rows have missing values across all numeric flight-count "
    "columns simultaneously — likely carrier-airport pairs with zero reported activity "
    "that month. Dropped from numeric analysis.")
log(f"- Duplicate (date, carrier, airport) combinations: {dupes} "
    + ("(none found — data is clean on this front)." if dupes == 0 else "(should be reviewed/dropped)."))
log("- `arr_del15`, delay-cause counts, and delay-cause minutes are aggregated at the "
    "carrier-airport-month level, not per-flight — so no individual flight records exist "
    "to drill into further.")
log("- Airport and carrier volumes are highly uneven (major hubs vs small regional "
    "airports), so raw counts can be misleading without normalizing by flight volume "
    "(handled above via delay_rate_%).")

# ---------------------------------------------------------------------------
# 13. Save cleaned dataset for later tasks
# ---------------------------------------------------------------------------
df_clean = df_num.drop(columns=["month_num"])
df_clean.to_csv("../data/delays_2019_clean.csv", index=False)
log(f"\nSaved cleaned dataset -> data/delays_2019_clean.csv ({df_clean.shape[0]} rows)")

# ---------------------------------------------------------------------------
# Write report to file
# ---------------------------------------------------------------------------
with open("../outputs/EDA_report.md", "w") as f:
    f.write("\n".join(report_lines))

print("\n\nReport saved to outputs/EDA_report.md")
