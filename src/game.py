from __future__ import division
import pymongo
from datetime import datetime

class Game:
	"""
	  This is the class that updates the points of an area. Add more comments
	"""
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
		TimeDelta = TimeNow - self.lastUpdate
		LastTweetCount = self.lastTweetVal
		NewTweetCount = self.tweets
		Update = 0
		if (TimeDelta.days > 7 and self.tweets == 0 and self.totalTweets != 0):
			EarnedPoints = -10
			Update = 1
			self.set('lastUpdate',TimeNow)
		else:
			EarnedPoints = NewTweetCount - LastTweetCount
			if(EarnedPoints > 0 and NewTweetCount/LastTweetCount >= 1.5 and NewTweetCount/self.totalTweets > 0.1):
				EarnedPoints = EarnedPoints + 10
				Update = 1
			elif (EarnedPoints > 0 and NewTweetCount/LastTweetCount >= 1.5 and NewTweetCount/self.totalTweets <= 0.1):
				EarnedPoints = EarnedPoints + 5
				Update = 1
			elif (EarnedPoints > 0 and NewTweetCount/LastTweetCount < 1.5 and NewTweetCount/self.totalTweets > 0.1):
				EarnedPoints = EarnedPoints + 5
				Update = 1
			elif (EarnedPoints > 0 and NewTweetCount/LastTweetCount < 1.5 and NewTweetCount/self.totalTweets <= 0.1):
				Update = 1
			elif (EarnedPoints < 0 and NewTweetCount/LastTweetCount >= 0.5 and NewTweetCount/self.totalTweets > 0.1):
				EarnedPoints = 0.5*EarnedPoints
				Update = 1
			elif (EarnedPoints < 0 and NewTweetCount/LastTweetCount < 0.5 and NewTweetCount/self.totalTweets > 0.1):
				EarnedPoints = 0.75*EarnedPoints
				Update = 1
			else:
				Update = 1

		if (Update):
			self.points = self.points+EarnedPoints
			self.lastTweetVal = NewTweetCount
			self.totalTweets = self.totalTweets + NewTweetCount
			self.lastUpdate = TimeNow

		
