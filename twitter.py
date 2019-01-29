import tweepy 
from tweepy import OAuthHandler
import json
import re
from textblob import TextBlob
import matplotlib.pyplot as plt



class Main_Class(object):

    ###  slef call function ####

    def __init__(self):

        #consumer key, consumer secret, access token, access secret.
        ckey="EeRgV2xxeH2aRfbfIyNMDDTI3"
        csecret="640ipwD1kHJiwUMHnVEDBLNdH5Tg4JiSJ2aM4INTs42GGiSX6P"
        atoken="767312780705861632-6jgCz79gVNUtnCdosI0OnPfGAIKzu9O"
        asecret="hYlQdvzW5Gda6CeWx2SZGOUENsqY2Aud7ph24tTiRnYxR"

        ### try to make authenticate connection ####
        try:
            self.authenticate= OAuthHandler(ckey, csecret)
            self.authenticate.set_access_token(atoken, asecret)
            self.connect = tweepy.API(self.authenticate)

        ### for invalid credential
        except:
            print("invalid credential")


    def sentiment_of_tweet(self,tweet):

        tweets= TextBlob(tweet)

        ## analyse the tweeet
        if tweets.sentiment.polarity ==0:
            return 'neutral'
        elif tweets.sentiment.polarity>0:
            return 'positive'
        else:
            return 'negative'

    def get_tweet(self, name):
        tweet =[]

        try:
            fetched = self.connect.search(q=name,count=10)

            for tweets in fetched:
                 check = {}

                 
                 check['text']=tweets.text

                 check['sentiment'] = self.sentiment_of_tweet(tweets.text)
                 
                 # appending parsed tweet to tweets list

                 tweet.append(check)
                 
            return tweet
        except tweepy.TweepError as e:

            print("Error")

def Plot(positive,negative,neutral):
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive, negative,neutral]
    explode = (0, 0.1, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()

def main():
    

    api = Main_Class()
    print("enter keyword to search for tweet")
    names=input()
    tweets = api.get_tweet(name = names)

    positive_tweet=[]
    negative_tweet=[]
    neutral_tweet=[]

    for tweet in  tweets:
        if tweet['sentiment'] =='positive':
            positive_tweet.append(tweet)
        elif tweet['sentiment'] =='negative':
            negative_tweet.append(tweet)
        else:
            neutral_tweet.append(tweet)
    all_tweet= len(tweets)
    pt= len(positive_tweet)
    nt=len(negative_tweet)
    neutral= len(neutral_tweet)

    print("Positive tweet percentage : {} ", format(100*(pt/all_tweet)))

    print("Negative tweet percentage : {} ", format(100*(nt/all_tweet)))

    print("Neutral tweet percentage : {} ", format(100*(neutral/all_tweet)))

    Plot(pt,nt,neutral)

if __name__ == "__main__":

    main()




