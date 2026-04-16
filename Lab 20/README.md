## Time Series Diagnostics & Advanced Decomposition

### Objective  
Develop a robust, diagnosis-first framework for analyzing economic time series by combining decomposition methods, stationarity testing, and structural break detection.

### Methodology  
- Diagnosed and corrected a flawed STL decomposition by applying a log transformation to handle multiplicative seasonality  
- Fixed a misspecified Augmented Dickey-Fuller (ADF) test by including the appropriate deterministic components (constant and trend)  
- Applied MSTL to decompose multi-seasonal data, capturing both daily and weekly cycles in simulated electricity demand  
- Implemented a moving block bootstrap to construct confidence bands for GDP trend estimates, preserving autocorrelation structure  
- Detected structural breaks using the PELT algorithm and analyzed regime-specific behavior through stationarity tests  
- Built a reusable Python module (`decompose.py`) with standardized functions for decomposition, stationarity testing, and break detection  

### Key Findings  
- Real GDP is non-stationary in levels (I(1)) and becomes stationary after first differencing  
- Structural breaks are identified around major macroeconomic shocks, particularly near the :contentReference[oaicite:0]{index=0} and the :contentReference[oaicite:1]{index=1}  
- MSTL effectively separates multiple seasonal patterns, improving interpretability over single-period methods  
- Block bootstrap reveals higher trend uncertainty during volatile periods, highlighting the importance of accounting for autocorrelation in time series inference  
