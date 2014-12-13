from pymongo import MongoClient
from datetime import date
import sys

def get_name_lead(name):
	mongoclient = MongoClient('mongodb://localhost:27017')
	CollCounty = mongoclient.search_results[name].find().sort('points') #Get County collection from search_results database
	CountyLeadName = list()
	NumOfCounties = CollCounty.count()-1
	if NumOfCounties >= 9:
		for i in range(0,10):
			CountyLeadName.append(CollCounty[NumOfCounties-i]['name'])
	else:
		for i in range(0,NumOfCounties+1):
			CountyLeadName.append(CollCounty[NumOfCounties-i]['name'])
	
	return CountyLeadName


def get_point_lead(name):
	mongoclient = MongoClient('mongodb://localhost:27017')
	CollCounty = mongoclient.search_results[name].find().sort('points') #Get County collection from search_results database
	CountyLeadName = list()
	NumOfCounties = CollCounty.count()-1
	if NumOfCounties >= 9:
		for i in range(0,10):
			CountyLeadName.append(CollCounty[NumOfCounties-i]['points'])
	else:
		for i in range(0,NumOfCounties+1):
			CountyLeadName.append(CollCounty[NumOfCounties-i]['points'])
	
	return CountyLeadName

if __name__ == '__main__':
	
	name = sys.argv[1]
	NameLead = get_name_lead(name)
	PointsLead = get_point_lead(name)

	Num = NameLead.__len__()
	if Num >= 10:
		for i in range(0,10):
			print NameLead[i]
        		print PointsLead[i]
	else:
		for i in range(0,Num):
			print NameLead[i]
        		print PointsLead[i]
		for i in range(0,10-Num):
			print ''
			print ''

