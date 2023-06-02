import time
import scrapulasan as ul
import pandas as pd

data = "restaurants_jakarta_clean.csv" #ganti sama data restoran yang udh di clean
data = pd.read_csv(data)

limit = 300
resto = data["nama"]
datalink = data["link"]


for i,j in zip(resto,datalink):
    ul.detailulasan(i,j,limit,"review.csv") #resto, link, limit(restoran yang reviewnya yg lebih dari brp yg mau di scrap),output

