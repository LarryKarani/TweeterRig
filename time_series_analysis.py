import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pickle

if __name__ == '__main__':
    fname= sys.argv[1]
    with open(fname, 'r') as f:
        all_dates = []

        for line in f:
            tweet = json.loads(line)
            all_dates.append(tweet.get('created_at'))
        idx = pd.DatetimeIndex(all_dates)
        ones = np.ones(len(all_dates))

        #the actual series (at series of 1s for the momet)
        my_series = pd.Series(ones, index=idx)

        #resampling / bucketing into 1-minute buckets
        per_minute = my_series.resample('1Min').sum().fillna(0)
        #ploting the series

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Tweet frequencies")
        hours = mdates.MinuteLocator(interval=20)
        date_formatter = mdates.DateFormatter('%H:%M')

        datemin = datetime(2018, 6, 27, 5, 0)
        datemax = datetime(2018, 9, 23, 7,0)

        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freg = per_minute.max()
        ax.set_ylim(0, max_freg)
        ax.plot(per_minute.index,per_minute)

        plt.savefig('tweet_time_series.png')