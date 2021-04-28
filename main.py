from twitter_api import twitter_api
from dotenv import load_dotenv

load_dotenv()

def main(user:str, hashtag:str):
    twitter_data = twitter_api(user,'#AmericasComebackTour')
    tweets = twitter_data.tweets
    hashtags = twitter_data.hashtags
    for i in tweets:
        print(i._json)
        break

if __name__ == '__main__':
    main('Nigel_Farage', '#AmericasComebackTour')


