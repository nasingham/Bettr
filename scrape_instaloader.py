import instaloader
import csv
import pandas as pd

bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'bettr.academy')

bot.login(user="justusxpeccator",passwd="nictheman3")

followers = [follower.username for follower in profile.get_followers()]

mydict = {'followers':followers}
df = pd.DataFrame(mydict)
df.to_csv('bettr.academy_followers.csv')

