import json
import sys
from tweepy import Cursor
from stream import get_twitter_client

if __name__ == '__main__':
    user = sys.argv[1]
    client = get_twitter_client()

    fname = 'user_timeline_{}.json1'.format(user)

    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline,screen_name=user, counter=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+ "\n")
