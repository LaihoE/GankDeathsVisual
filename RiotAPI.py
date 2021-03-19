import requests
import pandas as pd
import json
import csv
import random
import time
import matplotlib.pyplot as plt
import os



def API(creds):
    df=pd.read_csv(os.path.join(os.path.dirname(__file__),"data","CSV","recentgames.csv"))
    counter=0
    api_key=creds.APIKEY

    for ids in df['id']:
        counter += 1
        print((counter / len(df))*100, "%")
        paths = {
            "normal": os.path.join(os.path.dirname(__file__), "data", "normaldata", f"game{counter}.json"),
            "timeline": os.path.join(os.path.dirname(__file__), "data", "timelinedata", f"game{counter}.json")
        }

        # API requests. Limit is 100 requests every 2 min
        timeline=f"https://euw1.api.riotgames.com/lol/match/v4/timelines/by-match/{ids}?api_key={api_key}"
        normal=f"https://euw1.api.riotgames.com/lol/match/v4/matches/{ids}?api_key={api_key}"
        timedata = requests.get(timeline)
        time.sleep(0.1)
        normaldata = requests.get(normal)

        print(timedata)

        x=timedata.json()
        y=normaldata.json()

        out_file = open(paths['timeline'], "w")
        json.dump(x,out_file,indent=8)

        out_file = open(paths['normal'], "w")
        json.dump(y, out_file, indent=8)
