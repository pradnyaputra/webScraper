from pythonFiles.handlers import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import shutil

def getInfo():
    artist, album, albumURL, ranked = spotifyHandler()
    if albumURL==0:
        #if this is true, the artist variable will contain an error message that will be displayed
        reviewFinal = "Cannot display information due to error..."
    else:
        reviewFinal = webscrapeHandler(artist, album)

    return albumURL, reviewFinal, artist, album, ranked

albumURL, reviewFinal, artist, album, rankedTracks=getInfo()

window = tk.Tk()

window.title("Music Teacher")
window.minsize(1300, 750)

sidebar = tk.Frame(window, bg="#1a1a1a", width=300)
sidebar.pack(side=RIGHT, fill="y")

reviewCanvas = tk.Canvas(window, bg="#222A35", bd=0, highlightthickness=0, relief='ridge')
reviewCanvas.pack(side=RIGHT, fill=BOTH, expand=True)

reviewTitle = tk.Label(reviewCanvas, text="error", bg="#222A35", fg="light grey", font=("verdana", 21, "bold"))
reviewTitle.place(relwidth=.9, relheight=0.05, relx=.05, rely=0.025)

reviewSubTitle = tk.Label(reviewCanvas, text="ALBUM REVIEW", bg="#222A35", fg="light grey", font=("verdana", 10, "bold"))
reviewSubTitle.place(relwidth=.5, relheight=0.025, relx=.25, rely=0.075)

reviewText = tk.Text(reviewCanvas)
reviewText.place(relwidth=0.9, relheight=0.85, relx=.05, rely=.125)
reviewText.configure(bg="#222A35", fg="#b3b3b3", font=("verdana", 12), bd=0, wrap = WORD)

reviewTitle.configure(text=f"{artist} | {album}")
reviewText.insert(INSERT, reviewFinal)
reviewText.configure(state=DISABLED)

if albumURL!=0:
    albumimage = albumURL
    filename = "artwork.jpg"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(albumimage, stream = True)

    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    img = ImageTk.PhotoImage(Image.open("artwork.jpg"))
else:
    img = ImageTk.PhotoImage(Image.open("errorImage.jpg"))

albumLabel = Label(sidebar, image = img, bd=0)
albumLabel.pack()

rankedListTitle = tk.Label(sidebar, text="Album Songs Ranked In Popularity", bg="#1a1a1a", fg="light grey", pady=10, font=("verdana", 10, "bold"))
rankedListTitle.pack(side=TOP, fill="x")

rankedTracksList = Listbox(sidebar, bg="#1a1a1a", fg="#b3b3b3", bd=0, highlightthickness=0, font=("verdana", 10))

for track in rankedTracks:
    rankedTracksList.insert(END, f"{track[1]}")

#rankedTracksList.configure(state=DISABLED)
rankedTracksList.pack(side=TOP, fill="both", expand=True)

window.mainloop()


