from pythonFiles.handlers import *
import tkinter as tk
from tkinter import *
#from PIL import ImageTk,Image


def getInfo():
    artist, album, albumURL, ranked = spotifyHandler()
    if albumURL==0:
        #if this is true, the artist variable will contain an error message that will be displayed
        reviewFinal = "Cannot display information due to error..."
        reviewSubTitle.configure(text="")
    else:
        reviewFinal = webscrapeHandler(artist, album)

    reviewText.configure(state=NORMAL)
    reviewTitle.configure(text=f"{artist} | {album}")
    reviewText.insert(INSERT, reviewFinal)
    reviewText.configure(state=DISABLED)
    #return albumURL, reviewFinal, artist, album

window = tk.Tk()

window.title("Music Teacher")
window.minsize(1300, 750)

albumFrame = tk.Frame(window, bg="#1a1a1a", width=300)
albumFrame.pack(side=RIGHT, fill="y")

reviewCanvas = tk.Canvas(window, bg="#222A35", bd=0, highlightthickness=0, relief='ridge')
reviewCanvas.pack(side=RIGHT, fill=BOTH, expand=True)

reviewTitle = tk.Label(reviewCanvas, text="error", bg="#222A35", fg="light grey", font=("verdana", 21, "bold"))
reviewTitle.place(relwidth=.9, relheight=0.05, relx=.05, rely=0.025)

reviewSubTitle = tk.Label(reviewCanvas, text="ALBUM REVIEW", bg="#222A35", fg="light grey", font=("verdana", 10, "bold"))
reviewSubTitle.place(relwidth=.5, relheight=0.025, relx=.25, rely=0.075)

reviewText = tk.Text(reviewCanvas)
reviewText.place(relwidth=0.9, relheight=0.85, relx=.05, rely=.125)
reviewText.configure(bg="#222A35", fg="#b3b3b3", font=("verdana", 12), bd=0, wrap = WORD)

#canvas = Canvas(root, width = 300, height = 300)
#canvas.pack()
#img = ImageTk.PhotoImage(Image.open("ball.png"))
#canvas.create_image(20, 20, anchor=NW, image=img)

getInfo()
window.mainloop()


