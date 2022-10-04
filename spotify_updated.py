from tkinter import *
from tkinter import filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dateutil import parser
import plotly
import plotly.express as px

#Window stuff
window = Tk()
window.title('Your Spotify Library!')
window.geometry("500x450")
window.resizable(0,0) #it cannot be resized
frame = Frame(window) #create a frame to take background img and transparent logo
frame.pack()
canvas = Canvas(frame, bg="black", width=500, height=700) #canvas stores complex imgs, like transparent ones
canvas.pack()
background = PhotoImage(file="background.png")
canvas.create_image(500,500,image=background)
logo = PhotoImage(file="logo2.png")
canvas.create_image(250,50,image=logo) #position the logo


def getcsv():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path, usecols=["Track Name", 'Artist Name(s)',
                                                                    "Release Date", "Genres", "Popularity"])
importing = Button(window, text="Import CSV", bg='lightgreen', fg='Black', font="helvetica 16 bold", width="25",
                    command=getcsv).place(x=90, y=100)  # the button, calling back to the command


#Commands and buttons
def artists():

    count = df.groupby('Artist Name(s)').count().nlargest(10, columns=['Track Name']).head(10) #group by artist name, then count occurences and
    #display the most frequent 10 values
    sns.barplot(x=count.index, y='Track Name', data=count, palette=("viridis")) #barplot using the count as the x axis, and number of tracks for y
    plt.ylabel("Frequency", fontsize=20, weight='bold')
    plt.xlabel("Artist Name", fontsize=20, weight='bold')
    plt.title('Top 10 Artists', fontname='Helvetica', fontsize=40, color='yellowgreen', weight='bold')
    plt.show()

topten = Button(window, text="Top 10 Artists", bg='Black', fg='lightgreen', font="helvetica 16 bold", width="25",
                    command=artists).place(x=90, y=150) #the button, calling back to the command


def years():
    df['Release Year'] = pd.DatetimeIndex(df['Release Date']).year #same concept as above, but convert release date to just year
    count = df.groupby('Release Year').count().nlargest(5, columns=['Track Name']).head(5) #use that year to count occurences, take the
    #most frequent 5 values by counting the number of tracks in the playlist released that year
    sns.barplot(x=count.index, y='Track Name', data=count, palette=("viridis")) #count mesauring track name again
    plt.ylabel("Frequency", fontsize=20, weight='bold')
    plt.xlabel("Years", fontsize=20, weight='bold')
    plt.title('Songs liked by release year', fontname='Helvetica', fontsize=30, color='yellowgreen', weight='bold')
    plt.show()

years = Button(window, text ="Songs ♥ by release year", bg="black", fg='lightgreen', font= "helvetica 16 bold", width="25", command=years).place(x=90,y=200)
#command button

def genres():
    sums = df.groupby(df["Genres"])["Track Name"].count().nlargest(5).head(5) #same concept, using genre!
    plt.title('Top 5 Genres', fontname='Helvetica', fontsize=40, color='yellowgreen', weight='bold')
    plt.axis('equal')
    plt.pie(sums, labels=sums.index, autopct='%.1f%%', labeldistance=1.15, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },
            colors = ['#925acf', '#435a82', '#2e8b7e', '#88c35b','#b2c83b']) #displays labels on pie chart, also, some white lines
    #to separate the data and make it prettier
    plt.show()
genres = Button(window, text ="Top 5 Genres", bg="black", fg='lightgreen', font= "helvetica 16 bold", width="25", command=genres).place(x=90,y=250)
#the button

def popularity():
    artistpop = df.groupby('Artist Name(s)').sum().sort_values('Popularity', ascending=False)[:10]
    artistpop = artistpop.reset_index()
    fig = px.bar(x='Artist Name(s)', y='Popularity', data_frame=artistpop, color='Artist Name(s)')
    fig.update_layout(title_text='Global popularity of your artists', title_x=0.5, title_font_size=40, title_font_color='lightgreen')
    fig.show()

pop = Button(window, text ="Artist Popularity Ranking", bg="black", fg='lightgreen', font= "helvetica 16 bold", width="25", command=popularity).place(x=90,y=300)

window.mainloop()