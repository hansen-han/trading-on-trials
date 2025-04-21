<p align="center">
  <img src="images/banner.png" alt="Trading on Trials Banner" width="100%" />
</p>

## Overview

This project explores whether biotech press releases—such as clinical trial updates or regulatory decisions—can provide insights into stock price behavior. By leveraging large language models (LLMs) for feature extraction and annotation, combined with machine learning and event-based backtesting, the goal is to uncover patterns in market reactions that can inform trading strategies and help predict stock movements.

## Summary

- Parsed and structured ~30,000 biotech press releases using large language models (LLMs)  
- Identified high-volatility event types like clinical trial results and stock offerings  
- Found that "positive" trial results often led to negative stock reactions  
- Explored contextual drivers: market cap, trial design, regulatory details, and more  
- Trained an ensemble of machine learning models to forecast 30-day price moves after key trial announcements — including a shorting strategy on negative outcomes that significantly outperformed the S&P 500 on held-out test data  



See [analysis.md](analysis.md) for full results, tables, and modeling insights.


## Repository Contents

- [**analysis.md**](analysis.md): A detailed writeup report of the findings from the analysis, summarizing key insights and results.
- [**scripts**](scripts/): This directory contains Jupyter notebooks and Python scripts used for data analysis, machine learning modeling, and event-based backtesting. These tools are designed to uncover patterns in market reactions and evaluate the effectiveness of potential trading strategies.
- [**data**](data/): Includes all the resources and scripts necessary for processing and analyzing press releases and stock price data.
  - [**data_processing_scripts**](data/data_processing_scripts/): A collection of Python scripts for parsing raw press releases, extracting key features (e.g., publication date, classifications, and drug details), and linking them with corresponding stock price data.
  - [**press_releases**](data/press_releases/): A directory containing the raw press release files (in HTML or XML format) that were manually collected from company websites. These files serve as the foundation for the analysis.
  - [**csv_files**](data/csv_files/): Contains processed datasets in CSV format, including positive clinical trial result press releases and negative press releases, which are key subsets of the analysis.
  - [**prompts**](data/prompts/): Contains templates and configurations for large language models (LLMs) used to extract and annotate features from the press releases, enabling automated and scalable data processing.
- [**images**](images/): This folder contains visual assets, including the project banner, charts, and figures used in the documentation or analysis to illustrate key findings and insights.

## Contact
Reach out: **hansenrjhan@gmail.com**


## Disclaimer
The information provided in this article is for educational and informational purposes only and should not be construed as financial or investment advice. The author and the publisher are not financial advisors or professionals and do not claim to be providing personalized financial advice. The article is based on the author's research and analysis, and the results reported may not be applicable to individual circumstances. Before making any financial decisions or investments, readers should consult with a financial advisor or professional to consider their specific situation, goals, and risk tolerance. Past performance is not indicative of future results, and no representation or warranty is made regarding the accuracy or completeness of the information provided.
