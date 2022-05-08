# This project was created by me. Reach out to me directly on GitHub for any inquiries; please do not use without my expressed consent.

# SpotifyAnalyzer
While it is one of the most important events of the year, receiving your Spotify Wrapped playlist requires waiting until the end of the year, and it doesn’t consider the entirety of your liked songs – only the songs you listened to in the past 365 days. While we can technically use the Spotify API (and spotipy library) to analyze all of our music data,  I wanted to create my own. So, this is a very simple spotify analysis app that analyzes your playlist metrics for Python 3+.

#You will need:
1. Your Spotify playlist of choice:
For your liked songs: Go to your “liked songs” playlist, click on the first song and press ctrl + a to select all, and ctrl + c to copy. Create a new playlist, and ctrl + v to paste.
For any other playlist: see the next step.

2. The .csv file for your playlist: 
go to https://exportify.net/ and download the playlist you wish to analyze.
--- to get the file location:
go to wherever you downloaded the file and right click, select “properties”
your file location is the location + \(yourfilename).csv. For example, mine is C:\Users\ferri\Downloads\y2kelsey.csv

3. The following libraries (if they aren’t already installed):
from tkinter import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

4. For visuals, you will also need a background image, saved as "background" and the logo file saved as "logo2" -- included in the repository. 


#The Execution

The only thing you will need to change for this code is the .csv file:

> df = pd.read_csv(r'YOURFILE.CSV', usecols=["Track Name", "Artist Name(s)",
                                                                   "Release Date", "Genres"]) 
                                                                   


#Identified issues
1. It’s not very pretty, but it’s mine. Graphs can be made prettier with more advanced design concepts, but I was more focused on the functionality.
2. Certain playlists will display the year with a decimal, for example, 2018.0 –  it is something I'm working on.

