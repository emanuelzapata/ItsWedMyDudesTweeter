# print("workingc")
import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

def send_tweet(api):
    image = api.media_upload('./assets/itswednesday.mp4')
    api.update_status(status="Its Wednesday My Dudes!", media_ids=[image.media_id_string])

def authenticate(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def main():
    api = authenticate(os.environ.get("API_KEY"), os.environ.get("API_SECRET"), os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_SECRET"))
    send_tweet(api)

if __name__ == "__main__":
    main()