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
	Game class.
	"""

	mongoclient = MongoClient('mongodb://localhost:27017') # Creates aa connection to MongoDB
	db = client.search_results #Selects a database
	
	collTweets = db['#ski']
	collStates = db.States #Selects a collection
	tweets_with_places = collTweets.find({'place':{"$type":3}}) #query for tweets that have non null place. 
	tweet = twets_with_places[0] # Get the first tweet. This is a dictionary
	place = tweet['place']# also a dictionary
	name = place['full_name']
	state = name[-2:]
	state = collStates.find_one({u'_id':u'New York'}) #Query MongoDB
	StatePoints = state['points'] #extract points
	StatelastUpdate = date(state['lastUpdate'][0],state['lastUpdate'][1],state['lastUpdate'][2]) #extract last update date
	StateName = state['_id']
	StateTotalTweets = state['totalTweets']
	
	coll.update({'_id':state['_id']},state,True) #mongodb update
