<p align="center">
  <img src="images/banner.png" alt="Trading on Trials Banner" width="100%" />
</p>

### Overview

This project explores whether biotech press releases—such as clinical trial updates or regulatory decisions—can provide insights into stock price behavior. By leveraging large language models (LLMs) for feature extraction and annotation, combined with machine learning and event-based backtesting, the goal is to uncover patterns in market reactions that can inform trading strategies and help predict stock movements.

### Introduction
Having worked in biotech for several years, I have often been puzzled by the seemingly counterintuitive market reactions to clinical trial results and FDA decisions. Positive trial outcomes would sometimes lead to stock price drops, while negative news occasionally resulted in gains. This paradox sparked my curiosity to explore whether there were underlying patterns driving these reactions. 

In the past, investigating this phenomenon would be extremely difficult due to the time and effort required to manually download and annotate press releases. Advances in large language models (LLMs) have made this process much more efficient, enabling automated parsing, feature extraction, and annotation. This has allowed for a structured and scalable analysis of market reactions, uncovering patterns that could inform trading strategies.

### Repository Contents

- **analysis**: This directory contains Jupyter notebooks and Python scripts used for data analysis, machine learning modeling, and event-based backtesting. These tools are designed to uncover patterns in market reactions and evaluate the effectiveness of potential trading strategies.

- **data**: Includes all the resources and scripts necessary for processing and analyzing press releases and stock price data.
  - **data_processing_scripts**: A collection of Python scripts for parsing raw press releases, extracting key features (e.g., publication date, classifications, and drug details), and linking them with corresponding stock price data.
  - **press_releases**: A directory containing the raw press release files (in HTML or XML format) that were manually collected from company websites. These files serve as the foundation for the analysis.
  - **csv_files**: Contains processed datasets in CSV format, including positive clinical trial result press releases and negative press releases, which are key subsets of the analysis.
  - **prompts**: Contains templates and configurations for large language models (LLMs) used to extract and annotate features from the press releases, enabling automated and scalable data processing.

- **images**: This folder contains visual assets, including the project banner, charts, and figures used in the documentation or analysis to illustrate key findings and insights.

### Data
We analyzed approximately 30,000 press releases from around 100 biotechnology and pharmaceutical companies, spanning the years 2014 to 2025. These press releases were manually collected from each company's website as raw HTML files and then processed using the scripts provided in the `data/data_processing_scripts/` directory. Stock price data corresponding to these press releases was downloaded using the `yfinance` library, enabling us to link market reactions to specific events.

Manually extracting key information from each press release—such as the date of publication, title, text, and classifications like "Financial Announcement" or "Change in Board of Directors," as well as details like whether the drug was a small molecule or biologic—would have been extremely time-intensive. To address this, we leveraged large language models (LLMs) to efficiently parse and annotate key features from each article. This approach allowed for the creation of a structured and detailed dataset while significantly reducing the time and effort required.

In addition to the raw press release files, some processed data is available in the form of CSV files. These include datasets of positive clinical trial result press releases and negative press releases, which are some of the most closely investigated parts of this analysis.

The full dataset is not included in this repository due to its size (approximately 3GB). However, you can reconstruct the database using the scripts provided in the `data/data_processing_scripts/` directory, along with the source files located in the `data/press_releases/` directory.

If you'd prefer to access the pre-processed database directly, feel free to reach out to me at **hansenrjhan@gmail.com**, and I’d be happy to share it with you.

### Results


### Future Work
- **RSS Feeds**: each publicly traded company has an RSS feed which sends live updates of articles that would fit into this analysis pipeline



### Disclaimer
The information provided in this article is for educational and informational purposes only and should not be construed as financial or investment advice. The author and the publisher are not financial advisors or professionals and do not claim to be providing personalized financial advice. The article is based on the author's research and analysis, and the results reported may not be applicable to individual circumstances. Before making any financial decisions or investments, readers should consult with a financial advisor or professional to consider their specific situation, goals, and risk tolerance. Past performance is not indicative of future results, and no representation or warranty is made regarding the accuracy or completeness of the information provided.