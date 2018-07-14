import tweepy
from time import sleep

##CONSUMER_KEY = '#Place Consumer Key here'
##CONSUMER_SECRET = '#Place Consumer Secret here'
##ACCESS_TOKEN = '#Place Access Token here'
##ACCESS_SECRET = '#Place Access Secret here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

class Retweet:
    def koyfin(self):
        for tweet in tweepy.Cursor(api.user_timeline, '@koyfincharts').items(1):
            try:
                print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
                tweet.retweet()
                print('Retweeted Koyfin')
                sleep(300)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(300)

    def eWhispers(self):
        for tweet in tweepy.Cursor(api.user_timeline, '@eWhispers').items(1):
            try:
                print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
                tweet.retweet()
                print('Retweeted eWhispers')
                sleep(300)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(300)

    def Rubicon(self):
        for tweet in tweepy.Cursor(api.user_timeline, '@TeamRubicon').items(1):
            try:
                print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
                tweet.retweet()
                print('Retweeted Rubicon')
                sleep(300)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(300)

def RT():
    bot = Retweet()
    bot.koyfin()
    bot.eWhispers()
    bot.Rubicon

import time

while True:
    RT()
