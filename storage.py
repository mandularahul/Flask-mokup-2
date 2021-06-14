import csv
import pandas as pd

all_movies=[]
data=pd.read_csv('final4.csv')
all_movies=data[1:]

liked_movies=[]
not_liked_movies=[]
did_not_watch=[]
