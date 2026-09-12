# EDA Report — US Airline Arrival Delays (2019)

Rows: 20946, Columns: 20

## 1. Column overview

| Column | Dtype | Non-null | Missing % |
|---|---|---|---|
| date | str | 20946 | 0.0% |
| carrier | str | 20946 | 0.0% |
| carrier_name | str | 20946 | 0.0% |
| airport | str | 20946 | 0.0% |
| airport_name | str | 20946 | 0.0% |
| arr_flights | float64 | 20932 | 0.07% |
| arr_del15 | float64 | 20927 | 0.09% |
| carrier_ct | float64 | 20932 | 0.07% |
| weather_ct | float64 | 20932 | 0.07% |
| nas_ct | float64 | 20932 | 0.07% |
| security_ct | float64 | 20932 | 0.07% |
| late_aircraft_ct | float64 | 20932 | 0.07% |
| arr_cancelled | float64 | 20932 | 0.07% |
| arr_diverted | float64 | 20932 | 0.07% |
| arr_delay | float64 | 20932 | 0.07% |
| carrier_delay | float64 | 20932 | 0.07% |
| weather_delay | float64 | 20932 | 0.07% |
| nas_delay | float64 | 20932 | 0.07% |
| security_delay | float64 | 20932 | 0.07% |
| late_aircraft_delay | float64 | 20932 | 0.07% |

**Duplicate (date, carrier, airport) rows:** 0

**Rows missing core flight-count data:** 14 (dropped for numeric analysis — no usable data in those rows).

## 2. Overall scale

- Total scheduled arrivals recorded: 7,422,037
- Total delayed arrivals (15+ min): 1,389,253
- Total cancelled arrivals: 134,925
- Total diverted arrivals: 18,880
- Carriers covered: 18
- Airports covered: 360
- Months covered: ['2019-1', '2019-10', '2019-11', '2019-12', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6', '2019-7', '2019-8', '2019-9']

## 3. Delay and cancellation rates

- Overall delay rate (15+ min late): 18.72%
- Overall cancellation rate: 1.82%

## 4. Delay rate by carrier

| carrier_name             |          flights |   delayed |   cancelled |   delay_rate_% |   cancel_rate_% |
|:-------------------------|-----------------:|----------:|------------:|---------------:|----------------:|
| ExpressJet Airlines LLC  |  97099           |     24357 |        4163 |          25.08 |            4.29 |
| Frontier Airlines Inc.   | 135543           |     33921 |        2281 |          25.03 |            1.68 |
| JetBlue Airways          | 297411           |     74133 |        3764 |          24.93 |            1.27 |
| ExpressJet Airlines Inc. |  37584           |      8682 |        1923 |          23.1  |            5.12 |
| United Air Lines Inc.    | 625910           |    132136 |        5384 |          21.11 |            0.86 |
| American Airlines Inc.   | 946776           |    195097 |       20151 |          20.61 |            2.13 |
| Mesa Airlines Inc.       | 227888           |     46688 |        6709 |          20.49 |            2.94 |
| Allegiant Air            | 105305           |     21541 |         624 |          20.46 |            0.59 |
| Envoy Air                | 327007           |     65843 |       11430 |          20.14 |            3.5  |
| PSA Airlines Inc.        | 289304           |     55727 |        6826 |          19.26 |            2.36 |
| Republic Airline         | 329149           |     61705 |        7692 |          18.75 |            2.34 |
| Spirit Air Lines         | 204845           |     37992 |        3590 |          18.55 |            1.75 |
| SkyWest Airlines Inc.    | 836445           |    153115 |       17453 |          18.31 |            2.09 |
| Alaska Airlines Inc.     | 264816           |     48359 |        3077 |          18.26 |            1.16 |
| Endeavor Air Inc.        | 257132           |     44250 |        4257 |          17.21 |            1.66 |
| Southwest Airlines Co.   |      1.36395e+06 |    233109 |       33622 |          17.09 |            2.47 |
| Delta Air Lines Inc.     | 991986           |    143021 |        1842 |          14.42 |            0.19 |
| Hawaiian Airlines Inc.   |  83891           |      9577 |         137 |          11.42 |            0.16 |

## 5. What causes delays (share of total delay minutes)

- Late aircraft (previous flight ran late): 38,075,922 minutes (39.7%)
- Carrier (airline's own fault): 29,352,960 minutes (30.6%)
- NAS (air traffic system): 23,044,854 minutes (24.0%)
- Weather: 5,282,501 minutes (5.5%)
- Security: 133,484 minutes (0.1%)

## 6. Airports — busiest by volume

|                                                                   |   flights |   delayed |   delay_rate_% |
|:------------------------------------------------------------------|----------:|----------:|---------------:|
| ('ATL', 'Atlanta, GA: Hartsfield-Jackson Atlanta International')  |    395026 |     55657 |          14.09 |
| ('ORD', "Chicago, IL: Chicago O'Hare International")              |    339569 |     74056 |          21.81 |
| ('DFW', 'Dallas/Fort Worth, TX: Dallas/Fort Worth International') |    304346 |     60257 |          19.8  |
| ('DEN', 'Denver, CO: Denver International')                       |    252064 |     48783 |          19.35 |
| ('CLT', 'Charlotte, NC: Charlotte Douglas International')         |    235490 |     37378 |          15.87 |
| ('LAX', 'Los Angeles, CA: Los Angeles International')             |    219996 |     40516 |          18.42 |
| ('IAH', 'Houston, TX: George Bush Intercontinental/Houston')      |    179682 |     36267 |          20.18 |
| ('PHX', 'Phoenix, AZ: Phoenix Sky Harbor International')          |    175343 |     29959 |          17.09 |
| ('LGA', 'New York, NY: LaGuardia')                                |    171665 |     44856 |          26.13 |
| ('SFO', 'San Francisco, CA: San Francisco International')         |    170966 |     43313 |          25.33 |

## 7. Airports with highest delay rate (min 500 flights/year, to avoid noise)

|                                                                |   flights |   delayed |   delay_rate_% |
|:---------------------------------------------------------------|----------:|----------:|---------------:|
| ('PSE', 'Ponce, PR: Mercedita')                                |       826 |       266 |          32.2  |
| ('EWR', 'Newark, NJ: Newark Liberty International')            |    136124 |     39809 |          29.24 |
| ('BQN', 'Aguadilla, PR: Rafael Hernandez')                     |      2305 |       659 |          28.59 |
| ('MKG', 'Muskegon, MI: Muskegon County')                       |       727 |       204 |          28.06 |
| ('LWB', 'Lewisburg, WV: Greenbrier Valley')                    |       665 |       184 |          27.67 |
| ('PIB', 'Hattiesburg/Laurel, MS: Hattiesburg-Laurel Regional') |       709 |       196 |          27.64 |
| ('AZA', 'Phoenix, AZ: Phoenix - Mesa Gateway')                 |      5721 |      1526 |          26.67 |
| ('MEI', 'Meridian, MS: Key Field')                             |       976 |       257 |          26.33 |
| ('LGA', 'New York, NY: LaGuardia')                             |    171665 |     44856 |          26.13 |
| ('CMX', 'Hancock/Houghton, MI: Houghton County Memorial')      |       728 |       185 |          25.41 |

## 8. Delay rate by month

| date    |   flights |   delayed |   delay_rate_% |
|:--------|----------:|----------:|---------------:|
| 2019-1  |    583985 |    105222 |          18.02 |
| 2019-10 |    636014 |    105046 |          16.52 |
| 2019-11 |    602453 |     85651 |          14.22 |
| 2019-12 |    625763 |    126945 |          20.29 |
| 2019-2  |    533175 |    119477 |          22.41 |
| 2019-3  |    632074 |    106277 |          16.81 |
| 2019-4  |    612023 |    108518 |          17.73 |
| 2019-5  |    636390 |    126283 |          19.84 |
| 2019-6  |    636691 |    153358 |          24.09 |
| 2019-7  |    659029 |    135630 |          20.58 |
| 2019-8  |    658461 |    133278 |          20.24 |
| 2019-9  |    605979 |     83568 |          13.79 |

## 9. Hypothesis: summer months (Jun-Aug) have higher delay rates

- Summer (Jun-Aug) delay rate: 21.61%
- Rest of year delay rate: 17.68%
- Hypothesis confirmed: summer delay rates are higher.

## 10. Data quality issues identified

- 14 rows have missing values across all numeric flight-count columns simultaneously — likely carrier-airport pairs with zero reported activity that month. Dropped from numeric analysis.
- Duplicate (date, carrier, airport) combinations: 0 (none found — data is clean on this front).
- `arr_del15`, delay-cause counts, and delay-cause minutes are aggregated at the carrier-airport-month level, not per-flight — so no individual flight records exist to drill into further.
- Airport and carrier volumes are highly uneven (major hubs vs small regional airports), so raw counts can be misleading without normalizing by flight volume (handled above via delay_rate_%).

Saved cleaned dataset -> data/delays_2019_clean.csv (20932 rows)