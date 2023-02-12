# snscrape is used to get twitter data we can use twitter api for good speed but in neet permision
import snscrape.modules.twitter as sntwitter
import pandas as pd
# googletrans is used to translate the tweets to english from any language
from googletrans import Translator
# it is self coded module which perform sentmental analysis using NLP(Natural language processing) 
import sentment

def tw_data(query,limit,filename):
    translator = Translator()

    tweets = []
    
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
        if len(tweets) == limit:
            break
        else:

            # collecting list of data
            tweets.append([tweet.date,tweet.username,tweet.url,translator.translate(tweet.content).text,tweet.likeCount,
            tweet.retweetCount,tweet.hashtags,(sentment.analyse_text(translator.translate(tweet.content).text))['pos'],
            (sentment.analyse_text(translator.translate(tweet.content).text))['neg'],
            (sentment.analyse_text(translator.translate(tweet.content).text))['neu']])

    # df is the dataset of the tweet we created
    df = pd.DataFrame(tweets, columns=['Date', 'User','Url','Tweet','likeCount','retweetCount','hashtags','positive','negative','neutral'])
    # converting pandas dataframe to csv file
    df.to_csv(filename,index=False)

#calling the function
tw_data(query="(#SayNoToValentines)",limit=100,filename="data.csv")
