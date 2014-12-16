1) Open the file mongodb.py and fill lines 14 to 17 with your credentials from
   Twitter. In a linux terminal write "python mongodb.py". Make sure you have
   Mongodb installed in your machine
2) Part of our Data stored online. If you wat to access our online MongoDB write this command via your command line:
   mongo ds047020.mongolab.com:47020/twitter_data -u t_db_user -p t_db_pass
3) Set the MongoDB database for the Game feature by running
	mongoimport --host localhost --db search_results --collection States < states.json
	mongoimport --host localhost --db twiter_data --collection clean_tweets < clean_tweets.json
