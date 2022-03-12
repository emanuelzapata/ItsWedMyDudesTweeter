# print("workingc")
import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

# token = os.environ.get("API_KEY")
# print(token)
auth = tweepy.OAuthHandler(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_SECRET"))

api = tweepy.API(auth)

image = api.media_upload('./assets/itswednesday.mp4')

api.update_status(status="Its Wednesday My Dudes!", media_ids=[image.media_id_string])