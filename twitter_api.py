import tweepy
import os


class TwitterAPI:

    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.environ["TWITTER_API_KEY"],
            consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )
    
    def tweet_thread(self, first_tweet_text, replies):
        last_tweet_id = ''
        first_tweet = self.client.create_tweet(text=first_tweet_text)
        last_tweet_id = first_tweet.data['id']
        for reply in replies:
            reply_tweet = self.client.create_tweet(text=reply, in_reply_to_tweet_id=last_tweet_id)
            last_tweet_id = reply_tweet.data['id']
