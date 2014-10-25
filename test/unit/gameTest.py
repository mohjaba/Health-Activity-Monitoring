#####################################################################
# file : gameTest.py
# author: Ioannis Paraskevakos
# version : 0.1
# date: October 2014
# description: Unit test of class Game
#####################################################################
from __future__ import division
import pymongo
from datetime import date
from game import Game

class gameTest:
	lastUpdate = date.today(); #Get today's date
	AreaTest = Game('County','Essex',249,500,150,lastUpdate,15000,'NJ')
	AttrVal = ['County','Essex',249,500,150,lastUpdate,15000,'NJ']
	
	def testget(self):
		for i,j in enumerate(['area','name','points','tweets','lastTweetVal','lastUpdate','totalTweets','motherState']):
			if (self.AreaTest.__get__(j) == self.AttrVal[i]):
				print 'Test get',j,'Success'
			else:
				print 'Test get',j,'Success'

	def testPointsIncrease(self):
		self.AreaTest.NewPoints()
		if (self.AreaTest.__get__('points') == 604):
			print 'Point Increase Success'
		else:
			print 'Point Increase Failed'

	def testPointsDateDecrease(self):
		newlastupdate = date(2014,10,16)
		self.AreaTest.__set__('lastUpdate',newlastupdate)
		self.AreaTest.NewPoints()
		if(self.AreaTest.__get__('points') == 594):
			print 'Point Decrease Due to date Success'
		else:
			print 'Point Decrease Due to date Success'


if __name__ == "__main__":
	Test = gameTest()
	Test.testget()
	Test.testPointsIncrease()
	Test.testPointsDateDecrease()
