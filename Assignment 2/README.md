## Audit 02: Deconstructing Statistical Lies

This audit examines how commonly reported metrics can mislead decision-making when data is skewed, rare events dominate outcomes, or failures are silently removed. Using a mix of manual statistical checks and AI-assisted simulation, I deconstruct three recurring statistical “lies” in modern tech and financial systems.

### 1. Latency Skew and the Mean Illusion
In a simulated cloud system, 98% of requests had normal latency (20–50ms), while 2% experienced extreme spikes (1–5 seconds). Although the mean latency appeared acceptable, the distribution was heavily right-skewed. A comparison between Standard Deviation (SD) and Median Absolute Deviation (MAD) showed that SD was dominated by rare tail events, while MAD remained stable and representative of typical user experience. This demonstrates why mean-based metrics are unreliable in heavy-tailed systems and why robust statistics are necessary for performance audits.

### 2. The False Positive Paradox in AI Detection
Using Bayes’ Rule, I audited a plagiarism detector claiming 98% accuracy. When the base rate of cheating was high, flagged cases were usually correct. However, in low-prevalence environments (e.g., an honors seminar with a 0.1% cheating rate), most flagged students were innocent despite high sensitivity and specificity. This analysis shows that accuracy alone is insufficient and that AI systems can produce systematically misleading outcomes when base rates are ignored.

### 3. Survivorship Bias in Crypto Markets
To study survivorship bias, I simulated 10,000 crypto token launches using a power-law (Pareto) distribution. Over 99% of tokens peaked near zero market cap, while a tiny fraction achieved large successes. By comparing the full dataset (“the graveyard”) with only the top 1% of tokens (“survivors”), I showed that the mean market cap increases by over an order of magnitude when failures are removed. This demonstrates how platforms that highlight only listed or successful assets create a false narrative of profitability.

### Key Takeaway
Across systems performance, AI decision-making, and financial markets, statistical summaries can lie when distributions are skewed, events are rare, or data is selectively filtered. Robust auditing requires understanding data-generating processes, base rates, and what has been excluded—not just what is reported.
