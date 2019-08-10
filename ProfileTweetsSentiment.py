from textblob import TextBlob
import tweepy





def prof(name):
    s="none"
    max_count=200
    customer_key=''
    customer_code=''
    acess_token=''
    acess_secret=''
    aces=tweepy.OAuthHandler(customer_key,customer_code)
    aces.set_access_token(acess_token,acess_secret)
    api=tweepy.API(aces)
    tweets = api.user_timeline(screen_name=name,count=200)
    sum=0
    sum1=0
    for tweet in tweets:
        s=TextBlob(tweet.text)
        print(s.sentiment)
        if(s.sentiment.polarity >0):
            sum=sum+((s.sentiment.polarity)*(s.sentiment.subjectivity))
            sum1=sum1+((s.sentiment.polarity)*(s.sentiment.subjectivity))
        else:
            sum1=sum1-((s.sentiment.polarity)*(s.sentiment.subjectivity))
        



        
    return ((sum/sum1)*100)



    

    


    
