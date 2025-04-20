# Introduction
Having worked in biotech for several years, I have often been puzzled by the seemingly counterintuitive market reactions to clinical trial results and FDA decisions. Positive trial outcomes would sometimes lead to stock price drops, while negative news occasionally resulted in gains. This paradox sparked my curiosity to explore whether there were underlying patterns driving these reactions. 

In the past, investigating this phenomenon would be extremely difficult due to the time and effort required to manually download and annotate press releases. Advances in large language models (LLMs) have made this process much more efficient, enabling automated parsing, feature extraction, and annotation. This has allowed for a structured and scalable analysis of market reactions, uncovering patterns that could inform trading strategies.


# Data
I analyzed approximately 30,000 press releases from around 100 biotechnology and pharmaceutical companies, spanning the years 2014 to 2025. These press releases were manually collected from each company's website as raw HTML files and then processed using the scripts provided in the `data/data_processing_scripts/` directory. Stock price data corresponding to these press releases was downloaded using the `yfinance` library, enabling us to link market reactions to specific events.

Manually extracting key information from each press release—such as the date of publication, title, text, and classifications like "Financial Announcement" or "Change in Board of Directors," as well as details like whether the drug was a small molecule or biologic—would have been extremely time-intensive. To address this, I leveraged large language models (LLMs) to efficiently parse and annotate key features from each article. This approach allowed for the creation of a structured and detailed dataset while significantly reducing the time and effort required.

In addition to the raw press release files, some processed data is available in the form of CSV files. These include datasets of positive clinical trial result press releases and negative press releases, which are some of the most closely investigated parts of this analysis.

The full dataset is not included in this repository due to its size (approximately 3GB). However, you can reconstruct the database using the scripts provided in the `data/data_processing_scripts/` directory, along with the source files located in the `data/press_releases/` directory.

If you'd prefer to access the pre-processed database directly, feel free to reach out to me at **hansenrjhan@gmail.com**, and I’d be happy to share it with you.

**Note:**  
This analysis excludes companies that were merged, acquired, or went bankrupt during the study period. As a result, the dataset is inherently biased toward companies that did not experience these events. This limitation may have particular significance for interpreting the results of **Positive Events**, which could lead to a buyout, or **Negative Events**, which might result in company collapse. These excluded scenarios could represent extreme outcomes that are not captured in the current analysis.

# Results

## Press Release Types and Their Impact on Stock Price Volatility

I identified approximately 9 distinct types of press releases, including **Clinical Trial Updates or Regulatory Updates**, **Press Related to Stock Offerings**, **Partnerships, Collaborations, or Licensing Agreements**, **Quarterly or Annual Financial Updates**, **Changes in Executive Management or Board of Directors**, **Company Attendance at Conferences**, **Legal Disputes**, **Other**, and **Press Releases Related to Index Inclusions**. These categories exhibit varying levels of stock price volatility, with some showing much higher variability in market reactions than others. For example, **Clinical Trial Updates or Regulatory Updates** and **Press Related to Stock Offerings** tend to have higher volatility, reflecting the market's sensitivity to these announcements.

To estimate the immediate effect of the event on stock price, I calculated the change in stock price from the average of the two days before the event to the price one day after the event. This approach accounts for potential information leakage, as press releases may be issued either before or after trading hours on the day of the event. By using this buffer, we ensure a more accurate assessment of the event's impact on stock price.

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

For the "Clinical Trial Update or Regulatory Update" category, I further classified the results into **Positive**, **Negative**, **Mixed**, or **Null** outcomes. The chart below illustrates the distribution of stock price changes from the average of two days before the event to one day after the event, based on these classifications.

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

We conducted additional analyses to determine whether certain factors, such as **Phase**, **Combination vs. Monotherapy**, or **Regulatory Action Types**, could help explain the observed trends in positive and negative market reactions. 

### Key Findings:
1. **Phase and Combination vs. Monotherapy**:  
   We observed no significant difference in the ratio of positive to negative results when comparing clinical trial phases (e.g., Phase 1, 2, or 3) or whether the treatment was a combination therapy or monotherapy. These factors did not appear to strongly influence the likelihood of positive or negative market reactions.

2. **Market Cap**:  
   Small-cap stocks were more likely to have negative responses to news overall, with a **positive-to-negative ratio of 0.80**, indicating that negative reactions outweighed positive ones. In contrast, mid-cap and large-cap stocks had ratios of **1.26** and **1.19**, respectively, suggesting that larger companies tend to experience more favorable market reactions.

3. **Timing of Press Releases**:  
   Press releases indicating **future events** (e.g., "Company X to announce Phase 2 results at AACR next Fall") had a **positive-to-negative ratio of 1.21**, compared to a ratio of **1.07** for press releases focused on **present events**. This suggests that forward-looking announcements may generate slightly more positive market sentiment.

4. **Regulatory Action Types**:  
   We also examined the regulatory action types associated with positive results to see if any patterns emerged. The table below summarizes the results:

**Table 4. Statistical Summary of Returns by Regulatory Action Type**  
This table highlights the mean, median, and standard deviation of returns, along with the count of positive and negative outcomes and their ratio, for each regulatory action type. Notable findings include:
- **Emergency Use Authorization (EUA)** had the highest positive-to-negative ratio (1.50), suggesting strong market optimism for these announcements.
- **Supplemental New Drug Applications (sNDA)** and **Fast Track, Orphan, or Priority Review Designations** also showed relatively high ratios of 1.36 and 1.24, respectively.
- **New Drug Applications (NDA)** had a ratio of 1.13, indicating a more balanced market reaction.
- **Label Expansions** and **Investigational New Drug (IND) Applications** had ratios close to or below 1, suggesting more neutral or mixed market responses.

| Regulatory Action Type                                           | Mean Return | Median Return | Std Dev  | 25th Percentile | 75th Percentile | Count | Positive Count | Negative Count | Positive-to-Negative Ratio |
|------------------------------------------------------------------|-------------|---------------|----------|-----------------|-----------------|-------|----------------|----------------|----------------------------|
| Emergency Use Authorization (EUA)                               | 0.006542    | 0.014666      | 0.067890 | -0.043302       | 0.022153        | 25    | 15             | 10             | 1.500000                   |
| Supplemental New Drug Application (sNDA)                        | 0.015016    | 0.004358      | 0.113649 | -0.015091       | 0.017297        | 78    | 45             | 33             | 1.363636                   |
| Fast Track, Orphan, Priority Review, or Similar Designation      | 0.009712    | 0.003294      | 0.120511 | -0.024407       | 0.031427        | 94    | 52             | 42             | 1.238095                   |
| New Drug Application (NDA)                                      | 0.054944    | 0.002381      | 0.336181 | -0.017525       | 0.028092        | 331   | 176            | 155            | 1.135484                   |
| Label Expansion                                                 | -0.006008   | 0.001462      | 0.065487 | -0.011474       | 0.021141        | 41    | 21             | 20             | 1.050000                   |
| Investigational New Drug (IND) Application                      | 0.015153    | -0.001144     | 0.110596 | -0.050600       | 0.063692        | 24    | 12             | 12             | 1.000000                   |
| Biologics License Application (BLA)                             | 0.009459    | 0.001439      | 0.085916 | -0.020792       | 0.020627        | 22    | 11             | 11             | 1.000000                   |
| Regulatory Opinion Only                                         | 0.020800    | -0.001306     | 0.192951 | -0.020213       | 0.015773        | 93    | 45             | 48             | 0.937500                   |

These findings suggest that while certain regulatory action types, such as EUA and sNDA, tend to generate more positive market reactions, the overall trends remain nuanced. Factors such as market cap, timing of announcements, and the specific regulatory context all contribute to the complexity of interpreting market responses to press releases.


## Exploring Heuristic Trading Rules Based on Event Trends

One of the ideas explored in this project was to identify potential trends in stock price movements following specific types of press releases. The goal was to determine whether heuristic rules could be developed to capitalize on these trends. For example: Do **Positive Results** that lead to a 5%+ drop in price on Day 1 tend to recover and show price increases over the next 30 days?

To test these ideas, I simulated various trading strategies based on heuristic rules and compared their performance to a control portfolio (S&P 500). The chart below illustrates the cumulative portfolio balance for each strategy over time.

**Figure 2. Portfolio Performance of Heuristic Trading Strategies**  
This figure compares the performance of different heuristic trading strategies such as going long on positive results with Day 1 price increases, while also demonstrating the risks of other strategies, such as going long on positive results with Day 1 price drops.

![Comparing Heuristic Trading Strategies](images/comparing_heuristic_strategies.png)




# Future Work
I am not actively working on this project or planning to pursue further development in the future. However, there are several potential directions I've thought of for anyone interested in expanding this work:

- **RSS Feeds**: each publicly traded company has an RSS feed which sends live updates of articles that would fit into this analysis pipeline
- **Deeper Analysis of Other Press Release Types**: I only closely examined the "Clinical Trial Update or Regulatory Update" press release type - it would be very interesting to look at some of the other ones, especially "Press Related to Stock Offerings, Inclusion in Indexes" and "Partnership, Collaboration, or Licensing Agreement" press releases which also had high volatility around the events
- **Applying to Other Sectors**: it would be interesting to apply this framework to other sectors besides biotech / pharma - close cousins could be medtech devices, but virtually any sector that is publicly listed and has investor relations sites with press releases would be interesting candidates for similar analysis
