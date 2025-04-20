# Introduction
Having worked in biotech for several years, I have often been puzzled by the seemingly counterintuitive market reactions to clinical trial results and FDA decisions. Positive trial outcomes would sometimes lead to stock price drops, while negative news occasionally resulted in gains. This paradox sparked my curiosity to explore whether there were underlying patterns driving these reactions. 

In the past, investigating this phenomenon would be extremely difficult due to the time and effort required to manually download and annotate press releases. Advances in large language models (LLMs) have made this process much more efficient, enabling automated parsing, feature extraction, and annotation. This has allowed for a structured and scalable analysis of market reactions, uncovering patterns that could inform trading strategies.


# Data
We analyzed approximately 30,000 press releases from around 100 biotechnology and pharmaceutical companies, spanning the years 2014 to 2025. These press releases were manually collected from each company's website as raw HTML files and then processed using the scripts provided in the `data/data_processing_scripts/` directory. Stock price data corresponding to these press releases was downloaded using the `yfinance` library, enabling us to link market reactions to specific events.

Manually extracting key information from each press release—such as the date of publication, title, text, and classifications like "Financial Announcement" or "Change in Board of Directors," as well as details like whether the drug was a small molecule or biologic—would have been extremely time-intensive. To address this, we leveraged large language models (LLMs) to efficiently parse and annotate key features from each article. This approach allowed for the creation of a structured and detailed dataset while significantly reducing the time and effort required.

In addition to the raw press release files, some processed data is available in the form of CSV files. These include datasets of positive clinical trial result press releases and negative press releases, which are some of the most closely investigated parts of this analysis.

The full dataset is not included in this repository due to its size (approximately 3GB). However, you can reconstruct the database using the scripts provided in the `data/data_processing_scripts/` directory, along with the source files located in the `data/press_releases/` directory.

If you'd prefer to access the pre-processed database directly, feel free to reach out to me at **hansenrjhan@gmail.com**, and I’d be happy to share it with you.

**Note:**  
This analysis excludes companies that were merged, acquired, or went bankrupt during the study period. As a result, the dataset is inherently biased toward companies that did not experience these events. This limitation may have particular significance for interpreting the results of **Positive Events**, which could lead to a buyout, or **Negative Events**, which might result in company collapse. These excluded scenarios could represent extreme outcomes that are not captured in the current analysis.

# Results

## Press Release Types and Their Impact on Stock Price Volatility

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


## Counterintuitive Market Reactions to Clinical Trial Results: Positive Outcomes Aren't Always Positive

For the "Clinical Trial Update or Regulatory Update" category, we further classified the results into **Positive**, **Negative**, **Mixed**, or **Null** outcomes. The chart below illustrates the distribution of stock price changes from the average of two days before the event to one day after the event, based on these classifications.

Interestingly, the data reveals some counterintuitive trends:
- For **Positive Results**, 1583 samples led to positive stock price changes, but 1413 resulted in negative changes. This surprising finding aligns with the initial motivation for this work—that nearly half of the "positive results" led to negative stock price changes.
- **Mixed Results** also showed a roughly 50/50 split between positive and negative stock price changes, possibly reflecting market uncertainty.
- Even for **Negative Results**, 25 out of 95 press releases surprisingly led to positive stock price changes, further highlighting the complexity of market reactions.

Additionally, the table below provides a statistical summary of the returns for each result type:

**Table 2. Statistical Summary of Returns by Result Type**  
This updated table includes additional metrics such as the count of positive and negative outcomes and their ratio. It highlights that **Positive Results** not only exhibit an almost even split between positive and negative outcomes, but their mean return is only 1.6%. This suggests that the returns are effectively random, and even the outliers do not heavily skew the results toward being positive. In contrast, **Negative Results** typically lead to negative returns most of the time, with a mean return of -12%, indicating a more consistent and heavily negative market reaction.

| Result Type       | Mean Return | Median Return | Std Dev  | 25th Percentile | 75th Percentile | Positive Count | Negative Count | Positive-to-Negative Ratio |
|-------------------|-------------|---------------|----------|-----------------|-----------------|----------------|----------------|----------------------------|
| Positive Results  | 0.016827    | 0.002125      | 0.171329 | -0.022216       | 0.026125        | 1583           | 1413           | 1.123317                   |
| Mixed Results     | -0.077735   | -0.008186     | 0.175897 | -0.085165       | 0.011723        | 35             | 39             | 0.897436                   |
| Negative Results  | -0.120127   | -0.018451     | 0.233041 | -0.149855       | 0.000612        | 25             | 70             | 0.357143                   |

**Figure 1. Distribution of Stock Price Changes 1 Day After Press Release by Clinical Trial Result Type**  
This box plot shows the price change distribution for Positive, Mixed, and Negative results. Positive results generally exhibit higher variability and larger positive price changes, while Negative results tend to show a more consistent downward trend. Mixed results show minimal price movement, reflecting market uncertainty.

![Distribution of Price Change by Event Type](images/result_type_distribution.png)



### Exploring Heuristic Trading Rules Based on Event Trends

One of the ideas explored in this project was to identify potential trends in stock price movements following specific types of press releases. The goal was to determine whether heuristic rules could be developed to capitalize on these trends. For example:
- Do **Positive Results** that lead to a 5%+ drop in price on Day 1 tend to recover and show price increases over the next 30 days?
- Do **Negative Results** with a 5%+ drop on Day 1 continue to decline over the next 30 days?

To test these ideas, we simulated various trading strategies based on heuristic rules and compared their performance to a control portfolio (S&P 500). The chart below illustrates the cumulative portfolio balance for each strategy over time.

**Figure 2. Portfolio Performance of Heuristic Trading Strategies**  
This figure compares the performance of different heuristic trading strategies such as going long on positive results with Day 1 price increases, while also demonstrating the risks of other strategies, such as going long on positive results with Day 1 price drops.

![Comparing Heuristic Trading Strategies](images/comparing_heuristic_strategies.png)



# Future Work
I am not actively working on this project or planning to pursue further development in the future. However, there are several potential directions I've thought of for anyone interested in expanding this work:

- **RSS Feeds**: each publicly traded company has an RSS feed which sends live updates of articles that would fit into this analysis pipeline
- **Deeper Analysis of Other Press Release Types**: I only closely examined the "Clinical Trial Update or Regulatory Update" press release type - it would be very interesting to look at some of the other ones, especially "Press Related to Stock Offerings, Inclusion in Indexes" and "Partnership, Collaboration, or Licensing Agreement" press releases which also had high volatility around the events
- **Applying to Other Sectors**: it would be interesting to apply this framework to other sectors besides biotech / pharma - close cousins could be medtech devices, but virtually any sector that is publicly listed and has investor relations sites with press releases would be interesting candidates for similar analysis
