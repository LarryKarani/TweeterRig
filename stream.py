import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    '''sets twitter authentication
       return tweepy.Oauthhandler object
    '''
    
    try:
        consumer_key = os.environ['ckey']
        consumer_secrect = os.environ['csecret']
        access_token = os.environ['atoken']
        access_secrect = os.environ['asecret']
    
    except KeyError:
        sys.stderr.write("Twitter_ environment variable not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key, consumer_secrect)
    auth.set_access_token(access_token, access_secrect)
    return auth
def get_twitter_client():
    ''' Setup twitter API client. 
    Return tweepy.API object
    '''
    auth = get_twitter_auth()
    client = API(auth)
    return client

