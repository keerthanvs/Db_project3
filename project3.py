from pymongo import ReturnDocument
from pymongo import MongoClient
from bson import json_util
import datetime
import pymongo
from nltk.tokenize import word_tokenize
from collections import Counter

from datetime import *
import matplotlib.pyplot as plt
plt.rcdefaults()
from textblob import TextBlob
import array as arr
import numpy as np
from scipy.stats import skew
import statistics




MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'database1'
COLLECTION_NAME = 'got2'
COLLECTION_NAME1 = 'critics'


def weeklysentimentanlysis(collection):
    d3 = datetime(2019, 4, 14)
    d4 = datetime(2019, 4, 20)
    d5 = datetime(2019, 4, 21)
    d6 = datetime(2019, 4, 27)
    d7 = datetime(2019, 4, 28)
    d8 = datetime(2019, 5, 4)
    d9 = datetime(2019, 5, 5)
    d10 = datetime(2019, 5, 11)
    d11 = datetime(2019, 5, 12)
    d12 = datetime(2019, 5, 18)
    d13 = datetime(2019, 5, 19)
    d14 = datetime(2019, 5, 26)


    week1 = arr.array('f', [])
    week2 = arr.array('f', [])
    week3 = arr.array('f', [])
    week4 = arr.array('f', [])
    week5 = arr.array('f', [])
    week6 = arr.array('f', [])

    week7 = arr.array('f', [])


    for x in collection.find():
        gfg = TextBlob(x["text"])
        gfg = gfg.sentiment.polarity

        date_object = datetime.strptime(x["created_at"], '%Y-%m-%dT%H:%M:%S')

        if ((date_object >= d3) and (date_object <= d4)):
            week1.append(gfg)
        if ((date_object >= d5) and (date_object <= d6)):
            week2.append(gfg)
        if ((date_object >= d7) and (date_object <= d8)):
            week3.append(gfg)
        if ((date_object >= d9) and (date_object <= d10)):
            week4.append(gfg)
        if ((date_object >= d11) and (date_object <= d12)):
            week5.append(gfg)
        if ((date_object >= d13) and (date_object <= d14)):
            week6.append(gfg)

        if ((date_object > d14)):
            week7.append(gfg)

    print("******************WEEK 1******************")
    len_1= len(week1)
    S1 = sum(week1) / len_1
    SD1 = (statistics.stdev(week1))
    print("Mean Sentiment Score: ", S1)
    print("Number of Tweets: ",len_1)
    print("Standard Deviation of Sentiment Scores is: ",SD1)

    print("******************WEEK 2******************")
    len_2= len(week2)
    S2 = sum(week2) / len_2
    SD2 = (statistics.stdev(week2))
    print("Mean Sentiment Score: ", S2)
    print("Number of Tweets: ",len_2)
    print("Standard Deviation of Sentiment Scores is: ",SD2)

    print("******************WEEK 3******************")
    len_3=len(week3)
    S3 = sum(week3) / len_3
    SD3 = (statistics.stdev(week3))
    print("Mean Sentiment Score: ", S3)
    print("Number of Tweets: ",len_3)
    print("Standard Deviation of Sentiment Scores is: ",SD3)

    print("******************WEEK 4******************")
    len_4=len(week4)
    S4 = sum(week4) / len_4
    SD4 = (statistics.stdev(week4))
    print("Mean Sentiment Score: ", S4)
    print("Number of Tweets: ",len_4)
    print("Standard Deviation of Sentiment Scores is: ",SD4)

    print("******************WEEK 5******************")
    len_5=len(week5)
    S5 = sum(week5) / len_5
    SD5 = (statistics.stdev(week5))
    print("Mean Sentiment Score: ", S5)
    print("Number of Tweets: ",len_5)
    print("Standard Deviation of Sentiment Scores is: ",SD5)

    print("******************WEEK 6******************")
    len_6=len(week6)
    S6 = sum(week6) / len_6
    SD6 = (statistics.stdev(week6))
    print("Mean Sentiment Score: ", S6)
    print("Number of Tweets: ",len_6)
    print("Standard Deviation of Sentiment Scores is: ",SD6)

    print("******************AFTER WEEK 6******************")
    len_7=len(week7)
    S7 = sum(week7) / len_7
    SD7 = (statistics.stdev(week7))
    print("Mean Sentiment Score: ", S7)
    print("Number of Tweets: ",len_7)
    print("Standard Deviation of Sentiment Scores is: ",SD7)

    display_option= input("Do you want to see the plot(Type yes)\n")

    if(display_option == "yes"):
        objects = ('episode1', 'episode2', 'episode3', 'episode4', 'episode5', 'episode6', 'after_episode6')

        performance = [S1, S2, S3, S4, S5, S6, S7]
        #SDS = [SD1, SD2, SD3, SD4, SD5, SD6, SD7]

        y_pos = np.arange(len(objects))
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('score')
        plt.title('mean score of all episodes')
        plt.show()


def correlate(collection):
    d3 = datetime(2019, 4, 14)
    d4 = datetime(2019, 4, 20)
    d5 = datetime(2019, 4, 21)
    d6 = datetime(2019, 4, 27)
    d7 = datetime(2019, 4, 28)
    d8 = datetime(2019, 5, 4)
    d9 = datetime(2019, 5, 5)
    d10 = datetime(2019, 5, 11)
    d11 = datetime(2019, 5, 12)
    d12 = datetime(2019, 5, 18)
    d13 = datetime(2019, 5, 19)
    d14 = datetime(2019, 5, 26)

    week1 = arr.array('f', [])
    week2 = arr.array('f', [])
    week3 = arr.array('f', [])
    week4 = arr.array('f', [])
    week5 = arr.array('f', [])
    week6 = arr.array('f', [])

    for x in collection.find():
        gfg = TextBlob(x["text"])
        gfg = gfg.sentiment.polarity
        ##print(gfg)
        sentiment_dict = {}
        date_object = datetime.strptime(x["created_at"], '%Y-%m-%dT%H:%M:%S')
        if ((date_object >= d3) and (date_object <= d4)):
            week1.append(gfg)
        if ((date_object >= d5) and (date_object <= d6)):
            week2.append(gfg)
        if ((date_object >= d7) and (date_object <= d8)):
            week3.append(gfg)
        if ((date_object >= d9) and (date_object <= d10)):
            week4.append(gfg)
        if ((date_object >= d11) and (date_object <= d12)):
            week5.append(gfg)
        if ((date_object >= d13) and (date_object <= d14)):
            week6.append(gfg)


    S1 = sum(week1) / len(week1)
    SD1 = (statistics.stdev(week1))


    S2 = sum(week2) / len(week2)
    SD2 = (statistics.stdev(week2))


    S3 = sum(week3) / len(week3)
    SD3 = (statistics.stdev(week3))


    S4 = sum(week4) / len(week4)
    SD4 = (statistics.stdev(week4))


    S5 = sum(week5) / len(week5)
    SD5 = (statistics.stdev(week5))


    S6 = sum(week6) / len(week6)
    SD6 = (statistics.stdev(week6))

    objects = ('episode1', 'episode2', 'episode3', 'episode4', 'episode5', 'episode6')

    performance = [S1, S2, S3, S4, S5, S6]
    SDS = [SD1, SD2, SD3, SD4, SD5, SD6]


    week1c = arr.array('f', [])
    week2c = arr.array('f', [])
    week3c = arr.array('f', [])
    week4c = arr.array('f', [])
    week5c = arr.array('f', [])
    week6c = arr.array('f', [])

    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)

    collection1 = connection[DB_NAME][COLLECTION_NAME1]
    for x in collection1.find():

        gfg1 = TextBlob(x["review"])
        gfg1 = gfg1.sentiment.polarity
        ##print(x["review"])
        if (x["Epidose"] == 'E1'):
            week1c.append(gfg1)
        if (x["Epidose"] == 'E2'):
            week2c.append(gfg1)
        if (x["Epidose"] == 'E3'):
            week3c.append(gfg1)
        if (x["Epidose"] == 'E4'):
            week4c.append(gfg1)
        if (x["Epidose"] == 'E5'):
            week5c.append(gfg1)
        if (x["Epidose"] == 'E6'):
            week6c.append(gfg1)

    #print("mean score of critics in week 1")
    SC1 = sum(week1c) / len(week1c)
    #print(SC1)

    #print("mean score of critics in week 2")
    SC2 = sum(week2c) / len(week2c)
    #print(SC2)

    #print("mean score of critics in week 3")
    SC3 = sum(week3c) / len(week3c)
    #print(SC3)

    #print("mean score of critics in week 4")
    SC4 = sum(week4c) / len(week4c)
    #print(SC4)

    #print("mean score of critics in week 5")
    SC5 = sum(week5c) / len(week5c)
    #print(SC5)

    #print("mean score of critics in week 6")
    SC6 = sum(week6c) / len(week6c)
    #print(SC6)

    criticsscore = [SC1, SC2, SC3, SC4, SC5, SC6]

    corr = np.correlate(criticsscore, performance)
    print("CORRELATION Between Critics and Audience: ",corr)



def skewnessofdata(collection):
    d3 = datetime(2019, 4, 14)
    d4 = datetime(2019, 4, 20)
    d5 = datetime(2019, 4, 21)
    d6 = datetime(2019, 4, 27)
    d7 = datetime(2019, 4, 28)
    d8 = datetime(2019, 5, 4)
    d9 = datetime(2019, 5, 5)
    d10 = datetime(2019, 5, 11)
    d11 = datetime(2019, 5, 12)
    d12 = datetime(2019, 5, 18)
    d13 = datetime(2019, 5, 19)
    d14 = datetime(2019, 5, 26)

    week1 = arr.array('f', [])
    week2 = arr.array('f', [])
    week3 = arr.array('f', [])
    week4 = arr.array('f', [])
    week5 = arr.array('f', [])
    week6 = arr.array('f', [])

    week7 = arr.array('f', [])



    for x in collection.find():
        gfg = TextBlob(x["text"])
        gfg = gfg.sentiment.polarity
        ##print(gfg)
        sentiment_dict = {}
        date_object = datetime.strptime(x["created_at"], '%Y-%m-%dT%H:%M:%S')
        if ((date_object >= d3) and (date_object <= d4)):
            week1.append(gfg)
        if ((date_object >= d5) and (date_object <= d6)):
            week2.append(gfg)
        if ((date_object >= d7) and (date_object <= d8)):
            week3.append(gfg)
        if ((date_object >= d9) and (date_object <= d10)):
            week4.append(gfg)
        if ((date_object >= d11) and (date_object <= d12)):
            week5.append(gfg)
        if ((date_object >= d13) and (date_object <= d14)):
            week6.append(gfg)

        if (date_object > d14):
            week7.append(gfg)

    S1 = sum(week1) / len(week1)
    SD1 = (statistics.stdev(week1))

    S2 = sum(week2) / len(week2)
    SD2 = (statistics.stdev(week2))

    S3 = sum(week3) / len(week3)
    SD3 = (statistics.stdev(week3))

    S4 = sum(week4) / len(week4)
    SD4 = (statistics.stdev(week4))

    S5 = sum(week5) / len(week5)
    SD5 = (statistics.stdev(week5))

    S6 = sum(week6) / len(week6)
    SD6 = (statistics.stdev(week6))


    S7 = sum(week7) / len(week7)
    SD7 = (statistics.stdev(week7))

    objects = ('episode1', 'episode2', 'episode3', 'episode4', 'episode5', 'episode6', 'after_episode6')

    performance = [S1, S2, S3, S4, S5, S6, S7]
    print("Skewness of All the Audience Emotions: ",skew(performance))

def deviationofmeans(collection):
    d3 = datetime(2019, 4, 14)
    d4 = datetime(2019, 4, 20)
    d5 = datetime(2019, 4, 21)
    d6 = datetime(2019, 4, 27)
    d7 = datetime(2019, 4, 28)
    d8 = datetime(2019, 5, 4)
    d9 = datetime(2019, 5, 5)
    d10 = datetime(2019, 5, 11)
    d11 = datetime(2019, 5, 12)
    d12 = datetime(2019, 5, 18)
    d13 = datetime(2019, 5, 19)
    d14 = datetime(2019, 5, 26)



    week1 = arr.array('f', [])
    week2 = arr.array('f', [])
    week3 = arr.array('f', [])
    week4 = arr.array('f', [])
    week5 = arr.array('f', [])
    week6 = arr.array('f', [])

    week7 = arr.array('f', [])


    for x in collection.find():
        gfg = TextBlob(x["text"])
        gfg = gfg.sentiment.polarity
        ##print(gfg)
        sentiment_dict = {}
        date_object = datetime.strptime(x["created_at"], '%Y-%m-%dT%H:%M:%S')
        if ((date_object >= d3) and (date_object <= d4)):
            week1.append(gfg)
        if ((date_object >= d5) and (date_object <= d6)):
            week2.append(gfg)
        if ((date_object >= d7) and (date_object <= d8)):
            week3.append(gfg)
        if ((date_object >= d9) and (date_object <= d10)):
            week4.append(gfg)
        if ((date_object >= d11) and (date_object <= d12)):
            week5.append(gfg)
        if ((date_object >= d13) and (date_object <= d14)):
            week6.append(gfg)

        if ((date_object > d14)):
            week7.append(gfg)

    S1 = sum(week1) / len(week1)
    SD1 = (statistics.stdev(week1))

    S2 = sum(week2) / len(week2)
    SD2 = (statistics.stdev(week2))

    S3 = sum(week3) / len(week3)
    SD3 = (statistics.stdev(week3))

    S4 = sum(week4) / len(week4)
    SD4 = (statistics.stdev(week4))

    S5 = sum(week5) / len(week5)
    SD5 = (statistics.stdev(week5))

    S6 = sum(week6) / len(week6)
    SD6 = (statistics.stdev(week6))

    S7 = sum(week7) / len(week7)
    SD7 = (statistics.stdev(week7))



    performance = [S1, S2, S3, S4, S5, S6, S7]
    print("Standard Deviation of all the Audience Sentiments: ",statistics.stdev(performance))

    print("Do you want to see the weekly Standard Deviation Plot? (type yes)")

    std_plot=input()

    if(std_plot == "yes"):
        SDS = [SD1, SD2, SD3, SD4, SD5, SD6, SD7]
        objects = ('episode1', 'episode2', 'episode3', 'episode4', 'episode5', 'episode6', 'after_episode6')
        y_pos = np.arange(len(objects))
        plt.bar(y_pos, SDS, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('standard deviation')
        plt.title('standard deviation score in week')
        plt.show()




def frequent_positive(res):
    positive_words=[]
    with open("positive_words.txt") as fileobject:
        for line in fileobject:
            positive_words.append(line.strip())

    arr=[]
    positive_array=[]
    for i in res:
        arr=word_tokenize(i["text"])
        for j in arr:
            if j in positive_words:
                positive_array.append(j)
    counter_output=Counter(positive_array)
    frequent_positive_list=counter_output.most_common(5)
    #print("The 5 Most Frequently Used Positive Words Are: ")
    for i in frequent_positive_list:
        print(i[0]," : ",i[1]," times")


def frequent_negative(res):
    negative_words=[]
    with open("negative_words.txt") as fileobject:
        for line in fileobject:
            negative_words.append(line.strip())

    arr=[]
    negative_array=[]
    for i in res:
        arr=word_tokenize(i["text"])
        for j in arr:
            if j in negative_words:
                negative_array.append(j)
    counter_output=Counter(negative_array)
    frequent_negative_list=counter_output.most_common(5)
    #print("The 5 Most Frequently Used Negative Words Are: ")
    for i in frequent_negative_list:
        print(i[0]," : ",i[1]," times")

def frequent_characters(res):
    characters=["sansa","arya","bran","jon","aegon","daenerys","euron","theon","cersei","jaime",
    "tyrion","gendry","nightking","night","missandei","samwell","brienne","varys",
    "clegane","hound","tormund","worm","melisandre","gregor","mountain"]


    arr=[]
    character_array=[]
    for i in res:
        arr=word_tokenize(i["text"])
        for j in arr:
            if j in characters:
                character_array.append(j)
    counter_output=Counter(character_array)
    frequent_character_list=counter_output.most_common(5)
    #print("The 5 Most Frequently Mentioned Characters Are: ")
    for i in frequent_character_list:
        print(i[0]," : ",i[1]," times")

def recent_tweets(connection):
        collection = connection[DB_NAME][COLLECTION_NAME]
        cur=collection.find().sort("created_at",pymongo.DESCENDING).limit(5)
        #print("The 5 Most Recent tweets are\n")
        for i in cur:
            print(i["text"])

            print("\n")
            #print(cur[i]["created_at"])




def insert(collection):

    user_id=input("Enter your userid\n")
    print("\n")

    status_id=input("Enter your status_id\n")
    print("\n")

    now=datetime.now().replace(second=0,microsecond=0)
    created_at=now.isoformat()
    print(created_at)

    screen_name=input("Enter your Twitter username\n")
    print("\n")

    text= input("Enter the Tweet\n")
    print("\n")
    entry={"user_id": user_id , "status_id": status_id , "created_at": created_at,
           "screen_name": screen_name, "text": text}

    collection.insert_one(entry)
    print("Inserted\n")



def update(connection):
    collection = connection[DB_NAME][COLLECTION_NAME]


    screen_name = input("Enter your Twitter username\n")
    print("\n")

    print("latest Tweet of ",screen_name,"is: ")
    store=collection.find_one({"screen_name": screen_name}, sort=[('created_at', pymongo.DESCENDING)])
    idof=store["_id"]
    print(store["_id"])
    print(store["text"])
    text=input("enter text to update the tweet")
    doc = collection.find_one_and_update(
        {"_id": idof},
        {"$set":
             {"text": text}
         }, return_document=ReturnDocument.AFTER
    )


    print("updated Tweet")
    print(doc["_id"])
    print(doc["text"])



def delete(collection):
    cur=collection.find().sort("created_at",pymongo.DESCENDING).limit(1)
    for i in cur:
        collection.delete_one({"text" : i["text"]})
    print('deleted')





if __name__ == "__main__":
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][COLLECTION_NAME]
    res=list(collection.find({},{"text":1, "_id":0}))

    print("Welcome to Game of Thrones (Season 8) Tweet Analyser\n")

    while(True):

            print("\nMenu\n")
            print("1. Top 5 Recent Tweets\n")
            print("2. Top 5 Frequently Used Positive Words in the Tweets\n")
            print("3. Top 5 Frequently Used Negative Words in the Tweets\n")
            print("4. Top 5 Popular GOT Characters\n")
            print("5. Episode wise(Week wise) Sentiment Analysis\n")
            print("6. Skewness Analysis of Audience Emotions\n")
            print("7. Episode wise(Week wise) Deviation of Mean in the Emotions\n")
            print("8. Comparision of Critics and Audience Opinion\n")
            print("9. Insert/Delete/Edit a Tweet\n")
            print("10. EXIT\n")

            option= int(input())

            if(option == 1):
                recent_tweets(connection)
            if(option == 2):
                frequent_positive(res)
            if(option == 3):
                frequent_negative(res)
            if(option == 4):
                frequent_characters(res)
            if(option == 5):
                weeklysentimentanlysis(collection)
            if(option == 6):
                skewnessofdata(collection)
            if(option == 7):
                deviationofmeans(collection)
            if(option == 8):
                correlate(collection)
            if(option == 9):

                print("1. Insert a Tweet\n")
                print("2. Delete the Most Recent Tweet\n")
                print("3. Edit a Tweet\n")

                option2=int(input())

                if(option2 == 1):
                    insert(collection)
                if(option2 == 2):
                    delete(collection)
                if(option2 == 3):
                    update(connection)

            if(option == 10):
                break
