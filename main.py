from tweet_generator import TweetGenerator
from twitter_api import TwitterAPI
import sys


def main():

    model = sys.argv[1]
    prompt = sys.argv[2]
    main_tweet = sys.argv[3]

    generator = TweetGenerator(model=model)
    tweets = generator.generate_tweets(prompt)

    twitterAPI = TwitterAPI()
    twitterAPI.tweet_thread(main_tweet, tweets)


if __name__ == "__main__":
    main()
