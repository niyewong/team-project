# CTK Replication

Team Members: Owen Fisher, Kasey La, Nicole Wong

This folder currently contains 7 files and 1 folder:

 1. this **README** file
 2. **scrapeTweets.py**, a script that was used to scrape data from Twitter of the pattern _PRONOUN who_ from tweets posted on 22 September, 2021. 
 3. **pro-who-tweets.csv**, a file containing the tweets that were scraped, gathered on 08 January 2022.
 4. **filter-by-regex.py**, a .py file containing descriptions of the patterns that students should use to filter out irrelevant examples from **pro-who-tweets.csv**
 5. **literary-annotated-tweets.csv**, a file containing valid tweets from (3) and are tagged as literary or non-literary.
 6. **sample-annotated-tweets.csv**, a file containing a sample of 150 tweets from (5), where relative clauses are tagged with RC-type, RC-head, and Role.
 7. **CTK-Replication-Findings.pdf**, a short description of our findings.
 8. **ProjectProposals**, a folder containing a .pdf file with our project proposals.

### Overview of data in _pro-who-tweets.csv_

The following table (made with help of [a markdown table generator](https://www.tablesgenerator.com/markdown_tables)), outlines the count of each search type that was pulled from tweets with that pattern posted on 22 September 2021. The maximum number of tweets collected for each pattern was 1,000, meaning that numbers less than 1,000 represent all the tweets from that day corresponding to that pattern.

| **Search string** | **Tweet Count** |
|-------------------|-----------------|
| "he who"          | 1000            |
| "she who"         | 381             |
| "it who"          | 1000            |
| "him who"         | 1000            |
| "her who"         | 419             |
| "they who"        | 264             |
| "them who"        | 1000            |
| "we who"          | 301             |
| "us who"          | 1000            |
| "you who"         | 1000            |
| **Total**         | 7365            |

Each line in this file is a comma-separated list (csv) of the following information:
  - **date**: The datestamp (date & time) that the tweet was sent 
  - **content**: The unedited text of the tweet
  - **id**: the tweet ID 
  - **url**: the address where this tweet can be publically viewed

Test Text for S1.4 - Owen Fisher
....
