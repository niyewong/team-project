# Initiated by Kelsey Kraus
#
# Contributors: Owen Fisher, Kasey La, Nicole Wong 
#
# Description: This file is a replication of the data cleaning method implemented by CTK 2016.

# NOTE: the suggested approaches below are NOT the only way to complete this task! It is merely given as a starting point. You can choose to do this in a different way if you want, but be sure to comment on your process along the way.

# !!! You may need to run in your Shell: pip install pandas !!!

import os
import pandas
import re

allTweets = []
with open('pro-who-tweets.csv') as file:
  allTweets = file.read()
  #print(allTweets)


# -- Preprocessing: -- We don't care about the other data in our .csv. We want to only get the tweet text data in 'content' column.
# -- Suggested approach: -- create a list variable and save the 'content' column of the pro-who-tweets.csv file as your list. Print the length of the list. See here for more: https://www.geeksforgeeks.org/python-read-csv-columns-into-list/

data = pandas.read_csv('pro-who-tweets.csv')
tweets = data['content'].tolist()
print('List length: ' + str(len(tweets)))

#NW setting entire list to lowercase so that it is easier on the regex
for i in range(len(tweets)):
  tweets[i] = tweets[i].lower()

# === Part 1: Filtering ===

# -- First filter: -- Remove duplicates. 
# -- Suggested approach: -- using your list, convert the list into a dictionary, which will automatically remove duplicates. Then convert your dictionary back into a list. Print the length of the list. https://www.w3schools.com/python/python_howto_remove_duplicates.asp

noDups = list(dict.fromkeys(tweets))
print('1st filter list length:', str(len(noDups)))

# -- Second filter: -- Remove tweets where the last non-whitespace character before the word 'who' is not a letter or a comma. See Lecture 3 slides for more explanation of this!
# -- Suggested approach: -- Use the list you created as a result of the previous filter. Save the 10 possible pronouns in a list. Create a loop to run through each entry in your list. Use a conditional statement to construct a regular expression match, and save the list elements matching your condition. Print the length of the list.

alphaWho = []
pronoun = ['he', 'she', 'it', 'him', 'her', 'they', 'them', 'we', 'us', 'you']

for tweet in noDups:
  if re.search(r'[,a-z]\s*who', tweet) is None:
    continue
  else:
    alphaWho.append(tweet)

print('2nd filter list length:', str(len(alphaWho)))

# -- Third filter: -- Remove the pattern 'of PRO who'
# -- Suggested approach: -- Create another loop, and another conditional statement using a regular expression from the list you got from the previous filter. This time, save only those that DO NOT match the conditional statement. Print the length of the list.

noOfWho = []

for tweet in alphaWho:
  count = 0
  for pn in pronoun:
    if re.search(rf'of {pn} who', tweet):
      count += 1
  if count == 0:
    noOfWho.append(tweet)

print('3rd filter list length:', len(noOfWho))

# -- Fourth filter: -- Remove tweets where the pronoun 'it' preceeds the word 'who' by 2-4 words
# -- Suggested approach: -- Write a regular expression that picks out this pattern. Using the list you generated from the previous filter, use create a loop with a conditional statement that removes this pattern. Print the length of the list.

noItWho = []

for tweet in noOfWho:
  if re.search(r'it ([\s]*\b([^\s]+)\b[\s]*){2,4} who', tweet):
    continue
  else:
    noItWho.append(tweet)

print("4th filter list length:",len(noItWho))

# -- Fifth filter: -- Remove tweets where 'PRO who' is preceded by the verbs 'ask', 'tell', 'wonder', 'inform', and 'show'.
# -- Suggested approach: --  Save the verbs above into a list. Create a loop that iterates through your pronoun list from above, and removes examples that contain the pattern '[element-from-verb-list] [element-from-PRO-list]'. Print the length of the list.

noProWho = []

verbsList = ["ask", "tell", "wonder", "inform", "show"]

for tweet in noItWho[::-1]:
  for verb in verbsList:
    for pn in pronoun:
      if re.search(rf'{verb} {pn} who', tweet):
        noItWho.remove(tweet)

noProWho = noItWho

print("5th filter list length:",len(noProWho))

# output your list as a .csv or .tsv file.

something = pandas.DataFrame(noProWho)

something.to_csv('pro-who-tweets2.csv', index=False)




# === Part 2: Uniqueness ===

# -- Instruction: -- You now need to find out whether the tweets you have left are "literary" or "non-literary", according to CTK's classification. I've written a bit of this for you. Modify the block of code below so that it runs with your variable names. You should replace 'tweetList' in the 'for' block with your variable name that holds the final filtered list of 'PRO who' tweets.

# Test variable: contains a short list of test utterances for the pattern "who <word1> <word2>"
tweetList = ['this is a quote: he who shall not be named', 'who among us really', 'jeff is wondering who sings', 'he who shall not be named again', 'but who among us is perfect']

# This evaluates each tweet in TweetList for whether it contains the specified regex search, and whether that regex pattern in a tweet matches exactly to any other tweet in the list. If it does, it is assigned a value True. If it doesn't, it's assigned a value False.
trueFalseList = []
for tweet in noProWho:
  whoPhrase = re.search("who \w+ \w+", tweet)
  if whoPhrase is None:
      trueFalseList.append(False)
  else:
      trueFalseList.append(any(whoPhrase.group(0) in t for t in noProWho))
#print(trueFalseList)

# The following takes our two lists, tweetList and trueFalseList, and zips them together. It then creates a dataframe out of this list, that can then be converted to a .csv file

annotatedTweetList = list(zip(noProWho, trueFalseList))
tweetDataframe = pandas.DataFrame(annotatedTweetList)
tweetDataframe.to_csv('literary-annotated-tweets.csv', header=["Tweets", "isLiterary"], index=False)
