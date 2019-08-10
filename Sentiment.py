from textblob import TextBlob
import tweepy






def senti(name):
    sum2=0
    sum1=0
    customer_key='bFKZ6t8sVOWGwHWc36D2BdJau'
    customer_code='c9dhsfHJWW9UerMFlRlTdeJJxg7Ccx9KikQzfsofN27SxCkJ0H'
    acess_token='1031035056695828481-22eefQQtOLRWtyGZmHJtknDQsd6rgn'
    acess_secret='iVa7DZnxrMTeyxjwkOI8wrDYCffk9ptpumFoutK6GlK9y'
    aces=tweepy.OAuthHandler(customer_key,customer_code)
    aces.set_access_token(acess_token,acess_secret)
    api=tweepy.API(aces)
    
    tweet=api.search(name,count=200)
    for tweets in tweet:
        s=TextBlob(tweets.text)
        
        if(s.sentiment.polarity >0):
            sum2=sum2+((s.sentiment.polarity)*(s.sentiment.subjectivity))
            sum1=sum1+((s.sentiment.polarity)*(s.sentiment.subjectivity))
        else:
            sum1=sum1-((s.sentiment.polarity)*(s.sentiment.subjectivity))
    return ((sum2/sum1)*100)
    


    
