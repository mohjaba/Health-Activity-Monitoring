import pymongo
from datetime import datetime
from __future__ import division

class Game:
	def __init__(self,area='State',name=None,points=0,tweets=None,lastTweetVal=None,lastIncrease=None,lastUpdate=None,totalTweets=None,motherState=None):
		self.area         = area
		self.name         = name
		self.points       = points
		self.tweets       = tweets
		self.lastTweetVal = lastTweetVal
		self.lastUpdate   = lastUpdate
		self.totalTweets  = totalTweets
		self.motherState  = motherState

	def __get__(self, attr='name'):
		if attr == 'area':
			return self.area
  		elif attr == 'name':
			return self.name
  		elif attr == 'points':
			return self.points
  		elif attr == 'tweets':
			return self.tweets
  		elif attr == 'lastTweetVal':
			return self.lastTweetVal
  		elif attr == 'lastUpdate':
			return self.lastUpdate
  		elif attr == 'totalTweets':
			return self.totalTweets
  		elif attr == 'motherState':
			return self.motherState
		else:	
			return 0

	def __set__(self, attr,val):
		if attr == 'area':
			self.area = val
			return 1
  		elif attr == 'name':
			self.name = val
			return 1
  		elif attr == 'points':
			self.points = val
			return 1
  		elif attr == 'tweets':
			self.tweets = val
			return 1
  		elif attr == 'lastTweetVal':
			self.lastTweetVal = val
			return 1
  		elif attr == 'lastUpdate':
			self.lastUpdate = val
			return 1
  		elif attr == 'totalTweets':
			self.totalTweets = val
			return 1
  		elif attr == 'motherState':
			self.motherState = val
			return 1
		else:	
			return 0
		

	def NewPoints(self):
		
		TimeNow = datetime.now()
		TimeDelta = TimeNow - lastUpdate
		LastTweetCount = self.lastTweetVal
		NewTweetCount = self.tweets
		Update = 0
		if (TimeDelta.days > 7 && self.tweets == 0 && self.totalTweets != 0):
			NewPoints = self.points - 10
			Update = 1
			self.set('lastUpdate',TImeNow)
		else:
			NewPoints = NewTweetCount - LastTweetCount
			if(NewPoints > 0 && NewTweetCount/LastTweetCount >= 1.5 && NewTweetCount/self.totalTweets > 0.1):
				NewPoints = NewPoints + 10
				Update = 1
			elif (NewPoints > 0 && NewTweetCount/LastTweetCount >= 1.5 && NewTweetCount/self.totalTweets =< 0.1):
				NewPoints = NewPoints + 5
				Update = 1
			elif (NewPoints > 0 && NewTweetCount/LastTweetCount < 1.5 && NewTweetCount/self.totalTweets > 0.1):
				NewPoints = NewPoints + 5
				Update = 1
			elif (NewPoints > 0 && NewTweetCount/LastTweetCount < 1.5 && NewTweetCount/self.totalTweets =< 0.1):
				Update = 1
			elif (NewPoints < 0 && NewTweetCount/LastTweetCount >= 0.5 && NewTweetCount/self.totalTweets > 0.1):
				
				

	
		self.set('points',NewPoints)
