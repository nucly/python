import tweepy
import time

auth = tweepy.OAuthHandler('n3AQztuAr4P2eKp4Fh8Vuhlc4', 'SVB8tttAHkorFSZbzycyNE31tEskGAKtDy7FX7EUBTcFB0ws82')
auth.set_access_token('1059924169830350848-4jkPK3tsMDHhN9J1ET1UxZBiWe6Kpa', '23hLkupPAvBzGxuUEBCt9aKBcbxxCqrD1yO10oFl6nKXR')

api = tweepy.API(auth)
user = api.me()

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print("I like that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
