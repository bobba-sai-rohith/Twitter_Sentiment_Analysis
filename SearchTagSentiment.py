from textblob import TextBlob
import tweepy






def senti(name):
    sum2=0
    sum1=0
    customer_key=''
    customer_code=''
    acess_token=''
    acess_secret=''
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
    


    
