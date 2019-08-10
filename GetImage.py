
from textblob import TextBlob
import tweepy



def imag(name):
    s="none"
    l=0
    r=0
    customer_key=''
    customer_code=''
    acess_token=''
    acess_secret=''
    aces=tweepy.OAuthHandler(customer_key,customer_code)
    aces.set_access_token(acess_token,acess_secret)
    api=tweepy.API(aces)
    tweet=api.search(name,count=200)
    for tweets in tweet:
        if(tweets.retweet_count>r or tweets.favorite_count>l):
            if 'media' in tweets.entities:
                for image in tweets.entities['media']:
                    s=image['media_url']
                    l=tweets.favorite_count
                    r=tweets.retweet_count
    print(l,r)

    return s




def profimag(name):
    customer_key=''
    customer_code=''
    acess_token=''
    acess_secret=''
    aces=tweepy.OAuthHandler(customer_key,customer_code)
    aces.set_access_token(acess_token,acess_secret)
    api=tweepy.API(aces)
    tweet=api.get_user(name)
    #p=tweet.profile_banner_url
    p=tweet.profile_image_url
    p = (tweet.profile_image_url[:p.rfind('_')]
			+ tweet.profile_image_url[p.rfind('.'):])
    return p
