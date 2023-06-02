import scrapgmaps
import pandas as pd

# Import the CSV file
df = pd.read_csv("latlong_jakarta.csv") #ini adalah file 39 titik yang tersebar di jakarta
for i in range(39):
    lat = df["lat"][i]
    long = df["long"][i]
    scrapgmaps.scrapGmaps("restoran","restaurants_jakarta.csv",lat,long) #keyword,file_output,lat,long
    print(f"percobaan {i+1} berhasil dengan latlong {lat},{long}")