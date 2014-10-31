#####################################################################
# file : Play.py
# author: Ioannis Paraskevakos
# version : 0.1
# date: October 2014
# description:
#####################################################################
from __future__ import division
from pymongo import MongoClient
from datetime import date
from game import Game

class Play:
	
	"""
	This Class is the Class that conects MongoDB with the
	Game class. Contains all the necessary the methods to enable the game.
	
	** *Attributes* **
	   mongoclient   : This is the actual connection with the MongoDB
	   CollState     : This is the connection with the Collection that
                           holds the data for the Game over the States.
           CollTwets     : This is the connection with the Collection that 
                           holds the data from the tweets pulled from Twitter
           TweetedStates : This attribute has a list of the states mentioned
                                in the Tweets

        ** *Methods* **
           __init__ : The constructor of the class must be present for
                            python classes.

           grab_tweets  : This method is to utilize the existing connection
                                 with the database and get the needed data

           update_area : This method is used to call the game class and update
                         the database entry for that specific area.
	"""
	def __init__(self):
		"""
		Class Constructor
		"""
		self.mongoclient = MongoClient('mongodb://localhost:27017') # Creates aa connection to MongoDB
		self.CollState = client.search_results.States #Get State collection from search_results database
		self.CollTweets = client.search_results.raw_data #Get raw_data collection from search_results database
		self.TweetedStates = None

	def grab_tweets(self):
		Tweets = self.CollTweets.find({'place':{"$type":3}}) # Find the tweet that have geo coordinates for the moment.
		for i in range(Tweets.count()):
			tweet = Tweets[i] # Get tweet. This is a dictionary
			place = tweet['place']# also a dictionary
			name = place['full_name']
			state = name[-2:]
			#If the states is already found increment the number of tweets
			#for this state else put 1 since this is the first tweet
			if (self.TweetedStates.__contains__(state) and name['country_code']=='US'):
				self.TweetedStates[state] = self.TweetedStates[state]+1
			else:
				self.TweetedStates[state] = 1


	def update_area(self,tweets,area,name,motherstate=None):
		if (area == 'state'):
                        # Query the database for the state with id its name.
			AreaEntry = self.CollState.find_one({'_id':name})
		elif (area == 'county'):
                        # Query the database for the state with id the motherstate
                        # By taking the name field the proper collection for the
			# the county leaderboard is selected.
			state = self.CollState.find_one({'_id':,motherstate})
			CollCounty = db[state['name']]
			AreaEntry = collCounty.find_one('name':name)

		#Grad the date of the last update, create an object of the Game
		#class and call the method for the new points
		lastdate = date(AreaEntry['lastUpdate'][0],AreaEntry['lastUpdate'][1],AreaEntry['lastUpdate'][2]) #extract last update date
		GamingArea = Game(area,AreaEntry['name'],AreaEntry['points'],tweets,AreaEntry['lastTweettVal'],lastdate,AreaEntry['totalTweets'])
		GamingArea.NewPoints()

		#Change the values of the database entry based on the decisions
		#made by the Game class object
		AreaEntry['points']=GamingArea.__get__('points')
		AreaEntry['lastTweetVal'] = GamingArea.__get__('lastTweetVal')
		AreaEntry['lastUpdate'] = GamingArea.__get__('lastUpdate')
		AreaEntry['totalTweets'] = GamingArea.__get__('totalTweets')

		#Update the entry in the correct collection for the state or the county.
		if area == 'state':
			CollState.update({'_id':AreaEntry['_id']},AreaEntry,True)
		elif area == 'county':
			CollCounty.update({'_id':AreaEntry['_id']},AreaENtry,True)

	

