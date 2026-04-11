# Global Purchasing Power Parity Analysis  
### Testing the Law of One Price with the Big Mac Index

## Objective  
This project applies the Big Mac Index to empirically test the **Law of One Price** by comparing implied purchasing power parity (PPP) exchange rates across countries relative to the U.S. dollar.

## Methodology  
- Constructed a structured dataset from *The Economist’s* 2015 Big Mac Index using manually defined Python dictionaries  
- Calculated **implied PPP exchange rates** by comparing local Big Mac prices to the U.S. benchmark  
- Computed **currency misalignment percentages** to determine whether each currency was overvalued or undervalued relative to the USD  
- Analyzed deviations from PPP to assess real-world frictions such as trade barriers, non-tradable inputs, and market segmentation  

## Key Findings  
The analysis reveals systematic deviations from purchasing power parity across countries. Several currencies appeared **overvalued**, indicating higher local price levels than predicted by PPP, while others were **undervalued**, suggesting potential arbitrage opportunities in a frictionless market. These deviations highlight the limitations of the Law of One Price in practice and illustrate how transportation costs, wage differences, and local market conditions prevent full price convergence across countries.
