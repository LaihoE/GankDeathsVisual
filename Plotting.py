import pandas as pd
import matplotlib.pyplot as plt
import os

def plot():
    df1=pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "CSV", "wardtimers.csv"))
    df2=pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "CSV", "killtimers.csv"))
    print(df1)
    plt.hlines(y=df1['game'], xmin=df1['placed'], xmax=df1['died'], linewidth=2, color='r')
    plt.scatter(x=df2['kill'], y=df2['game'])
    plt.legend(['ward placed','died to a gank'])
    plt.xlabel('time (min)')
    plt.ylabel('games from newest to oldest')
    plt.show()