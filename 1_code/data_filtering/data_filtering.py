from pymongo import MongoClient


def data_filter2 (keywords, Tweets):
  '''
    This function searches through all the Tweets for each word in the keyword
    list. If a keyword exists in the tweet's text and the tweet has not been
    added to the final list by a previous keyword success it is added to the
    tweets that will be returned.

    Arguments:
      keywords: A list of keywords that will be used for the selection

      Tweets: The list with the tweets that need to be filtered.

    Output:
      good_tweets: A list with all the tweets that contained at least one 
                  keyword
  '''
  good_tweets=list()
  # For every tweet
  for tweet in Tweets:
    #Get the text of the tweet
    text = tweet['text']
    #For every keyword
    for keyword in keywords:
       # If the keyword exists and the tweet has not been selected insert it in
       # the good tweets list
       if keyword in text and tweet not in good_tweets:
          good_tweets.append(tweet)
  
  # Return the Filtered tweets.
  return good_tweets

def data_filter3(keywords,Tweets):
  '''
  This function searches through all the Tweets for each word in the keyword
  list. If a keyword exists in the tweet's text and the tweet has not been
  discarded from the final list by a previous keyword success it is discarded
  from the tweets that will be returned.

  Arguments:
    keywords: A list of keywords that will be used for the selection

    Tweets: The list with the tweets that need to be filtered.

  Output:
    good_tweets: A list with all the tweets that contained at least one 
                keyword
  '''
  final_tweets = list()
  final_tweets = Tweets

  # For every tweet
  for tweet in Tweets:
    # Get the text of the tweet
    text = tweet['text']
    # For every keyword
    for keyword in keywords:
      # If the keyword exists and the tweet has not been discarded, remove it
      # from the final tweets
      if keyword in text and tweet in final_tweets:
        final_tweets.remove(tweet)

  return final_tweets

def data_filtering():
  '''
  '''

  fpK1 = open('keywords1.txt','r')
  fpK2 = open('keywords2.txt','r')
  fpK3 = open('keywords3.txt','r')

  keywords1 = [line.strip() for line in fpK1]
  keywords2 = [line.strip() for line in fpK2]
  keywords3 = [line.strip() for line in fpK3]
  fpK1.close()
  fpK2.close()
  fpK3.close()

  # Change the Mongo Client argument to the URL of your Mongo DB. If using two
  # databases replicate the following line, change the URL to target database
  # and change to the proper Client the line with the comment "Target" as a
  # suffix
  client = MongoClient('mongodb://localhost:27017')

  RawTweets = client.twiter_data.twitter_coll.find({'place':{"$type":3}})

  usable_tweet = list()
  for tweet in RawTweets:
    if tweet['place']['country_code']=='US':
      usable_tweet.append(tweet)

  tweets_f1 = data_filter2 (keywords2, usable_tweet)
  tweets_final = data_filter3(keywords3,tweets_f1)

  for tweets in tweets_final:
    Tweets2 = {'_id':tweets['_id'],'coordinates':tweets['coordinates'],
               'lang':tweets['lang'],'text':tweets['text'],'place':tweets['place'],
               'user':tweets['user']}
    client.twiter_data.clean_tweets.update({'_id':Tweets2['_id']},Tweets2,True) #Target

  client.close()
  return True
