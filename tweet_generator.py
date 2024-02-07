import ollama
import re


class TweetGenerator:

    thread_limit = 19

    def __init__(self, model):
        self.model = model

    def generate_tweets(self, prompt, iteration=1):
        text = self.generate_response(prompt)
        tweets = self.create_tweet_array(text)
        if len(tweets) > self.thread_limit:
            if iteration > 5:
                raise Error("Error: Response is too long")
            new_prompt = f"""Make this body of text shorter:
                             {text}
                          """
            return self.generate_tweets(new_prompt, iteration=iteration + 1)
        return tweets

    def generate_response(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return response["message"]["content"]

    def create_tweet_array(self, text):
        max_length = 140
        words = re.split(r"\s|\n", text)
        tweets = [""]
        index = 0
        for word in words:
            if len(tweets[index]) + len(word) < max_length:
                tweets[index] += f" {word}"
            else:
                index += 1
                tweets.append(word)
        tweets[0] = tweets[0].strip()
        return tweets
