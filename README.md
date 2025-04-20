<p align="center">
  <img src="images/banner.png" alt="Trading on Trials Banner" width="100%" />
</p>

## Overview

This project explores whether biotech press releases—such as clinical trial updates or regulatory decisions—can provide insights into stock price behavior. By leveraging large language models (LLMs) for feature extraction and annotation, combined with machine learning and event-based backtesting, the goal is to uncover patterns in market reactions that can inform trading strategies and help predict stock movements.

## Introduction
Having worked in biotech for several years, I have often been puzzled by the seemingly counterintuitive market reactions to clinical trial results and FDA decisions. Positive trial outcomes would sometimes lead to stock price drops, while negative news occasionally resulted in gains. This paradox sparked my curiosity to explore whether there were underlying patterns driving these reactions. 

In the past, investigating this phenomenon would be extremely difficult due to the time and effort required to manually download and annotate press releases. Advances in large language models (LLMs) have made this process much more efficient, enabling automated parsing, feature extraction, and annotation. This has allowed for a structured and scalable analysis of market reactions, uncovering patterns that could inform trading strategies.

## Repository Contents

- **analysis**: This directory contains Jupyter notebooks and Python scripts used for data analysis, machine learning modeling, and event-based backtesting. These tools are designed to uncover patterns in market reactions and evaluate the effectiveness of potential trading strategies.

- **data**: Includes all the resources and scripts necessary for processing and analyzing press releases and stock price data.
  - **data_processing_scripts**: A collection of Python scripts for parsing raw press releases, extracting key features (e.g., publication date, classifications, and drug details), and linking them with corresponding stock price data.
  - **press_releases**: A directory containing the raw press release files (in HTML or XML format) that were manually collected from company websites. These files serve as the foundation for the analysis.
  - **csv_files**: Contains processed datasets in CSV format, including positive clinical trial result press releases and negative press releases, which are key subsets of the analysis.
  - **prompts**: Contains templates and configurations for large language models (LLMs) used to extract and annotate features from the press releases, enabling automated and scalable data processing.

- **images**: This folder contains visual assets, including the project banner, charts, and figures used in the documentation or analysis to illustrate key findings and insights.

## Data
We analyzed approximately 30,000 press releases from around 100 biotechnology and pharmaceutical companies, spanning the years 2014 to 2025. These press releases were manually collected from each company's website as raw HTML files and then processed using the scripts provided in the `data/data_processing_scripts/` directory. Stock price data corresponding to these press releases was downloaded using the `yfinance` library, enabling us to link market reactions to specific events.

Manually extracting key information from each press release—such as the date of publication, title, text, and classifications like "Financial Announcement" or "Change in Board of Directors," as well as details like whether the drug was a small molecule or biologic—would have been extremely time-intensive. To address this, we leveraged large language models (LLMs) to efficiently parse and annotate key features from each article. This approach allowed for the creation of a structured and detailed dataset while significantly reducing the time and effort required.

In addition to the raw press release files, some processed data is available in the form of CSV files. These include datasets of positive clinical trial result press releases and negative press releases, which are some of the most closely investigated parts of this analysis.

The full dataset is not included in this repository due to its size (approximately 3GB). However, you can reconstruct the database using the scripts provided in the `data/data_processing_scripts/` directory, along with the source files located in the `data/press_releases/` directory.

If you'd prefer to access the pre-processed database directly, feel free to reach out to me at **hansenrjhan@gmail.com**, and I’d be happy to share it with you.

## Results

### Press Release Types and Their Impact on Stock Price Volatility

We identified approximately 9 distinct types of press releases, including **Clinical Trial Updates or Regulatory Updates**, **Press Related to Stock Offerings**, **Partnerships, Collaborations, or Licensing Agreements**, **Quarterly or Annual Financial Updates**, **Changes in Executive Management or Board of Directors**, **Company Attendance at Conferences**, **Legal Disputes**, **Other**, and **Press Releases Related to Index Inclusions**. These categories exhibit varying levels of stock price volatility, with some showing much higher variability in market reactions than others. For example, **Clinical Trial Updates or Regulatory Updates** and **Press Related to Stock Offerings** tend to have higher volatility, reflecting the market's sensitivity to these announcements.

To estimate the immediate effect of the event on stock price, we calculated the change in stock price from the average of the two days before the event to the price one day after the event. This approach accounts for potential information leakage, as press releases may be issued either before or after trading hours on the day of the event. By using this buffer, we ensure a more accurate assessment of the event's impact on stock price.

**Table 1. Stock Price Change 1 Day After Press Release by Release Type (Sorted by Volatility)**  
The table below summarizes the standard deviation (volatility) of stock price changes, along with other statistics such as mean, median, and percentiles, for each press release type. The data is sorted in descending order of volatility.

| Press Release Type                                      | Std Dev | Mean Change | Median Change | Min Change | Max Change | 25th Percentile | 75th Percentile | Count |
|---------------------------------------------------------|---------|-------------|---------------|------------|------------|-----------------|-----------------|-------|
| Press Related to Stock Offerings, Inclusion in Indexes | 0.16331 | 0.017534    | -0.001441     | -0.673332  | 3.065537   | -0.036009       | 0.035415        | 2402  |
| Clinical Trial Update or Regulatory Update             | 0.14796 | 0.006826    | -0.000266     | -0.849870  | 3.423897   | -0.022527       | 0.023950        | 7247  |
| Partnership, Collaboration, or Licensing Agreement     | 0.13076 | 0.017683    | 0.003043      | -0.616836  | 1.928587   | -0.017324       | 0.028662        | 1306  |
| Quarterly or Annual Financial Update                   | 0.10273 | 0.002964    | -0.001812     | -0.715528  | 2.633242   | -0.036001       | 0.033297        | 4276  |
| Change in Executive Management or Board of Directors   | 0.07304 | -0.001377   | -0.005778     | -0.310005  | 0.847846   | -0.035288       | 0.020359        | 1196  |
| Other                                                  | 0.07156 | 0.006649    | 0.000593      | -0.681751  | 0.979390   | -0.016893       | 0.021230        | 3017  |
| Company to Attend Conference                           | 0.07032 | 0.005604    | 0.001650      | -0.656182  | 1.171123   | -0.025438       | 0.029169        | 4777  |
| Legal Dispute                                          | 0.06202 | 0.017984    | 0.007050      | -0.065337  | 0.315043   | -0.007444       | 0.020771        | 90    |

- **Press Related to Stock Offerings** and **Clinical Trial Updates** exhibit the highest volatility, with standard deviations of 0.16331 and 0.14796, respectively.
- **Quarterly or Annual Financial Updates** and **Partnership Announcements** show moderate volatility, reflecting their routine but impactful nature.
- **Legal Disputes** and **Changes in Executive Management** have the lowest volatility, suggesting more stable market reactions to these events.
- **Clinical Trial Update or Regulatory Update** was the most common type of press release. 



### Counterintuitive Market Reactions to Clinical Trial Results: Positive Outcomes Aren't Always Positive

For the "Clinical Trial Update or Regulatory Update" category, we further classified the results into **Positive**, **Negative**, **Mixed**, or **Null** outcomes. The chart below illustrates the distribution of stock price changes from the average of two days before the event to one day after the event, based on these classifications.

Interestingly, the data reveals some counterintuitive trends:
- For **Positive Results**, 1583 samples led to positive stock price changes, but 1413 resulted in negative changes. This surprising finding aligns with the initial motivation for this work—that nearly half of the "positive results" led to negative stock price changes.
- **Mixed Results** also showed a roughly 50/50 split between positive and negative stock price changes, possibly reflecting market uncertainty? 
- Even for **Negative Results**, 25 out of 95 press releases surprisingly led to positive stock price changes, further highlighting the complexity of market reactions.

**Figure 1. Distribution of Stock Price Changes 1 Day After Press Release by Clinical Trial Result Type**  
This box plot shows the price change distribution for Positive, Mixed, and Negative results. Positive results generally exhibit higher variability and larger positive price changes, while Negative results tend to show a more consistent downward trend. Mixed results show minimal price movement, reflecting market uncertainty.

![Distribution of Price Change by Event Type](images/result_type_distribution.png)


## Future Work
I am not actively working on this project or planning to pursue further development in the future. However, there are several potential directions I've thought of for anyone interested in expanding this work:

- **RSS Feeds**: each publicly traded company has an RSS feed which sends live updates of articles that would fit into this analysis pipeline
- **Deeper Analysis of Other Press Release Types**: I only closely examined the "Clinical Trial Update or Regulatory Update" press release type - it would be very interesting to look at some of the other ones, especially "Press Related to Stock Offerings, Inclusion in Indexes" and "Partnership, Collaboration, or Licensing Agreement" press releases which also had high volatility around the events
- **Applying to Other Sectors**: it would be interesting to apply this framework to other sectors besides biotech / pharma - close cousins could be medtech devices, but virtually any sector that is publicly listed and has investor relations sites with press releases would be interesting candidates for similar analysis



## Disclaimer
The information provided in this article is for educational and informational purposes only and should not be construed as financial or investment advice. The author and the publisher are not financial advisors or professionals and do not claim to be providing personalized financial advice. The article is based on the author's research and analysis, and the results reported may not be applicable to individual circumstances. Before making any financial decisions or investments, readers should consult with a financial advisor or professional to consider their specific situation, goals, and risk tolerance. Past performance is not indicative of future results, and no representation or warranty is made regarding the accuracy or completeness of the information provided.
