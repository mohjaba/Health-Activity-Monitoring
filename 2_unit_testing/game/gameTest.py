# written by: Ioannis Paraskevakos
# tested by: Ioannis Paraskevakos
# debugged by: Ioannis Paraskevakos

from __future__ import division
import flask
import pip
import pymongo
from datetime import date
from game import Game

class gameTest:
    """
    This is the unit test class of the Game class defined in the game.py
    file.
    
    Methods:
        testget : Test that the attributes of the Game object are the same
              as those in the class construction
        
        testPointsIncrease : Test the NewPoints method if it can increase
            the points of the area and return the correct result.

        testPointsDateDecrease : Test if points of an area decrease if the
            area is not updated for more than a week

    """

    lastUpdate = date.today();
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
        self.AreaTest.__set__('tweets',0)
        self.AreaTest.NewPoints()
        if(self.AreaTest.__get__('points') == 594):
            print 'Point Decrease Due to date Success'
        else:
            print 'Point Decrease Due to date Failed'


if __name__ == "__main__":
    Test = gameTest()
    Test.testget()
    Test.testPointsIncrease()
    Test.testPointsDateDecrease()
