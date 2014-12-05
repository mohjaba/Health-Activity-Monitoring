from pymongo import MongoClient
from datetime import date

def get_name_lead():
	mongoclient = MongoClient('mongodb://localhost:27017')
	CollState = mongoclient.search_results.States.find().sort('points')
	StateLeadName = list()
	for i in range(0,10):
		StateLeadName.append(CollState[50-i]['name'])
	
	return StateLeadName


def get_point_lead():
	mongoclient = MongoClient('mongodb://localhost:27017')
	CollState = mongoclient.search_results.States.find().sort('points')
	StateLeadPoints = list()
	for i in range(0,10):
		StateLeadPoints.append(CollState[50-i]['points'])
	
	return StateLeadPoints

if __name__ == '__main__':
	
	NameLead = get_name_lead()
	PointsLead = get_point_lead()

	for i in range (0,10):	
		print NameLead[i]
	        print PointsLead[i]
