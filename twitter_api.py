import tweepy
import os
import time
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

class twitter_api():
   
    def __init__(self, user_name:str, hashtags_in:list):
        self.user_name = user_name
        self.hashtags_in = hashtags_in
        self.api = None
        self.tweets = None
        self.hashtags = None
        self.connect()
        self.hashtags = self.twitter_hashtags_requests()
        self.tweets = self.twitter_user_requests()
        
    def connect(self) -> object:
        try:
            auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SECRET'))
            auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
            self.api = tweepy.API(auth)
            
        except tweepy.TweepError as e:
            print(e)
            
    def twitter_hashtags_requests(self) -> object:
        try:
            return self.api.search(q=self.hashtags_in, result_type='recent', tweet_mode='extended')

        except tweepy.TweepError as e:
            if e.message[0]['code'] == '429': 
                time.sleep(900)
                twitter_hashtags_requests()
            else:
                print(e)
            
    def twitter_user_requests(self) -> object:
        try:
            return self.api.user_timeline(id=self.user_name, result_type='recent', tweet_mode='extended')
                    
        except tweepy.TweepError as e:
            if e.message[0]['code'] == '429': 
                time.sleep(900)
                twitter_user_requests()
            else:
                print(e)

