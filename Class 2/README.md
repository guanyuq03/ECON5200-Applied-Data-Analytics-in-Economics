# The Illusion of Growth & the Composition Effect  
*Deflating History with FRED*

## Objective
This project investigates long-run wage growth in the United States by separating **nominal increases** from **real purchasing power**. Using live data from the Federal Reserve, the goal is to demonstrate how inflation and labor-market composition effects can create the *illusion* of wage growth—particularly during periods of economic shock such as the COVID-19 pandemic.

## Methodology
- **Data Ingestion (API-driven):**  
  I built a Python data pipeline using the Federal Reserve Economic Data (FRED) API (`fredapi`) to pull authoritative macroeconomic time series directly from the Federal Reserve Bank of St. Louis.

- **Real Wage Construction:**  
  - Fetched nominal wage data (**AHETPI – Average Hourly Earnings of Production Employees**).  
  - Fetched inflation data (**CPIAUCSL – Consumer Price Index**).  
  - Deflated nominal wages using CPI to compute inflation-adjusted *Real Wages*.

- **Anomaly Detection (2020 Pandemic Spike):**  
  Visual inspection revealed a sharp spike in real wages during 2020—counterintuitive during a major recession.

- **Bias Correction via ECI (Advanced Analysis):**  
  To address the **Composition Effect** (low-wage workers disproportionately exiting employment), I fetched the **Employment Cost Index for Wages and Salaries (ECIWAG)**.  
  Unlike average wages, the ECI tracks a fixed “basket of jobs,” allowing for a cleaner comparison of true wage growth without workforce composition bias.

## Key Findings
- **The Money Illusion:**  
  Over the past 50+ years, nominal wages rise steadily, but real wages remain relatively flat—demonstrating that much of observed wage “growth” is driven by inflation rather than increased purchasing power.

- **The Pandemic Paradox:**  
  The apparent wage boom in 2020 was not a real improvement in worker compensation.  
  - Standard average wages (AHETPI) show a sharp spike due to low-wage job losses.
  - The ECI remains comparatively stable, proving the spike was a **statistical artifact**, not genuine labor-market strength.

## Takeaway
This lab highlights why **methodology matters** in economic analysis. Without correcting for inflation and composition bias, headline wage statistics can be deeply misleading—especially during periods of economic disruption.
