import os
import tweepy
from dotenv import load_dotenv

load_dotenv()  # .envを読み込む

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API認証
#認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
client = tweepy.Client(
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET
)

def post_to_twitter(text):
    try:
        response = client.create_tweet(text=text)
        tweet_id = response.data["id"]
        username = client.get_me().data.username
        tweet_url = f"https://twitter.com/{username}/status/{tweet_id}"
        print("Twitter投稿成功")
        print(f"投稿URL: {tweet_url}")
        return tweet_url
    except Exception as e:
        print(f"❌ Twitter投稿失敗: {e}")
        return False

if __name__ == "__main__":
    post_to_twitter("test")
