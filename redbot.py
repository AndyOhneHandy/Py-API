from pandas.core import series
import praw
import pandas
from praw.models import MoreComments
import configLogin
import msgcheckforRedBot as msgcheck
import time
from pandas.core.reshape import reshape

reddit = praw.Reddit(
    client_id = configLogin.clientid,
    client_secret = configLogin.clientsecret,
    user_agent = configLogin.useragent,
    username = configLogin.username,
    password = configLogin.pw,
)

print(reddit.read_only)
commentcount = 0

df = pandas.DataFrame(columns=['id', 'AfD-Dummy', 'FDP-Dummy', 'Union-Dummy', 'SPD-Dummy', 'Die Grünen-Dummy', 'Die Linke-Dummy', 'mehrfache Parteien-Dummy', 'Trigger-Wörter', 'AfD-Absolut', 'FDP-Absolut', 'CDU-Absolut', 'SPD-Absolut', 'Grüne-Absolut', 'Linke-Absolut', 'Trigger-Wort-Counter', 'Konnotations-Score', 'Unklar', 'Redditor-Karma', 'Account-Erstellung', 'Account-Alter bei BTW (Tage)', 'Subreddit', 'Kommentar-Inhalt',  'Redditor-Name',])

subreddit = reddit.subreddit("polScrape_test")

def timecalc(input):
    return time.ctime(input+7200)

def accagecalc(input):
    btw = 1632643200
    return round((btw -  input) / (60*60*24),1)

for comment in subreddit.stream.comments(skip_existing = True):
    print("Ich sehe einen Kommentar")
    commentcount += 1
    redditor = comment.author
    msgdata = [commentcount] + msgcheck.mainF(comment.body.lower()) + [redditor.link_karma, timecalc(redditor.created_utc), accagecalc(redditor.created_utc), subreddit.display_name, comment.body.lower(), redditor.name,]
    seriesTemp = pandas.Series(msgdata, index = df.columns)
    df = df.append(seriesTemp, ignore_index = True)
    print(df)
