import twitter
import time

    
api = twitter.Api(consumer_key='Consumer Key',
                      consumer_secret='Consumer Secret',
                      access_token_key='access token Key',
                      access_token_secret='access token secret')
def fav_tweet(tweet):
    try:
        result = api.favorites.create(_id=tweet['id'])
        print("Favorited: %s" % (result['text']))
        return result
    # when you have already favourited a tweet
    # this error is thrown
    except TwitterHTTPError as e:
        print("Error: ", e)
        return None
    #enter phrase to like
results = api.GetSearch(raw_query="f=tweets&vertical=default&q=\"start%20my%20business\"&count=50")
    
for tweet in results:
    encoded = tweet.text.encode("utf-8", errors='ignore')
    print(encoded)
    time.sleep(5)
    try:
        api.CreateFavorite(status_id=tweet.id)
    except:
        print("Error")
        
    





