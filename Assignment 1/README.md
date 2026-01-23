# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem: Why the “Average” CPI Fails Students

Official inflation statistics, such as the U.S. Consumer Price Index (CPI), are designed to measure the average cost of living for a typical household. However, students face a very different spending reality. Tuition and rent make up a much larger share of a student’s budget, while categories that matter less to students receive relatively high weights in the official CPI.

As a result, national inflation measures can understate the real cost pressures experienced by students, especially those living in high-cost cities like Boston. This project asks a simple question:

**Does the official CPI hide the true inflation faced by students?**

---

## Methodology: Python, APIs, and Index Theory

This project uses Python and the Federal Reserve Economic Data (FRED) API to collect inflation data for student-relevant spending categories, including tuition, rent, food away from home, and streaming services.

To ensure meaningful comparisons, all series are normalized to a common base year (2016 = 100). This step is critical because CPI components are reported using different base years. Without normalization, comparisons across categories are misleading.

I then construct a custom **Student Spending Price Index (Student SPI)** using a weighted average approach inspired by the Laspeyres index framework. The weights reflect a realistic student budget, where tuition and rent account for the majority of expenses. The Student SPI is compared against both the national CPI and the Boston-area CPI.

---

## Key Findings

The analysis reveals a clear divergence between student inflation and official inflation measures. Since 2016, the Student SPI has increased faster than the national CPI, indicating that students experience higher effective inflation than what the national average suggests.

When regional prices are considered, the gap becomes even more pronounced. The Boston-Cambridge-Newton CPI rises faster than the national CPI, reinforcing the idea that local cost pressures amplify the financial burden faced by students in major urban areas.

Overall, the results show that **national averages and standard CPI weights can mask significant inflation experienced by specific groups**, particularly students.

---

## Why Comparing Raw Indices with Different Base Years Is a “Data Crime”

Comparing raw indices with different base years is a data crime because it mixes numbers that are on different scales, leading to misleading visual comparisons and incorrect conclusions.

In the raw CPI chart, tuition appears much larger than streaming services because the tuition index is based on an older base period (such as 1982–1984), while streaming uses a much later base year (such as 2002). In this case, the value “100” does not represent the same starting point for the two series.

As a result, tuition looks “huge” and streaming looks “tiny,” even though this difference mostly reflects how the indices are constructed rather than real inflation dynamics. Normalization fixes this problem by placing all series on a common base year, allowing fair and meaningful comparisons.

---

## Tools and Skills Demonstrated

- Python (pandas, matplotlib)
- API-based data collection (FRED)
- Inflation index construction and normalization
- Data visualization and interpretation
- Translating economic theory into applied data analysis
