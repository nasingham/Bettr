import instaloader
import csv
import pandas as pd
import os

bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
bot.login(user="<username>",passwd="<password>")

with open('bettr.academy_followers.csv','r') as infile:
    data = pd.read_csv(infile)

counter = 0
mydict = {}
for user in data['followers']:
    try:
        counter +=1
        print(counter)
        profile = instaloader.Profile.from_username(bot.context, user)
        followers = [follower.username for follower in profile.get_followers()]
        mydict[user] = followers
        if os.path.exists('break.txt'):
            break
        else:
            continue
    except Exception as e:
        print('Error occured, breaking out of loop to write data to csv file')
        break
    else:
        continue

df = pd.DataFrame(mydict)
df.to_csv('relations.csv')