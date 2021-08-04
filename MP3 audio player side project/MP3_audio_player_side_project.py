import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system


# Create the user interface.
player = tkr.Tk()
player.title("Life in Music")

player.geometry("450x350")

# The directory prompts user to enter in the folder which is mp3 file is located.
directory = askdirectory()
os.chdir(directory)
list_songs = os.listdir()

# Display interface to the user. While pushing the program to select each item from 
# The songlist to insert them into item box.
playlist = tkr.Listbox(player, font="Helvetica 12 bold",
bg="yellow", selectmode=tkr.SINGLE)

for item in list_songs:
    position = 0
    playlist.insert(position, item)
    position += 1

# Loading and sound function within pygame.
pygame.init()
pygame.mixer.init()

# Defining the play, stop, pause, and unpause functions with the help of the tkinter module to create the interface buttons.
def play_function():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play_function()

def stop_function():
    pygame.mixer.music.stop_function()

def pause_function():
    pygame.mixer.music.pause_function()

def unpause_function():
    pygame.mixer.music.unpause_function()

# Font and text for the onscreen buttons.
Button1 = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play_function, bg="blue", fg="white")
Button2 = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop_function, bg="red", fg="white")
Button3 = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause_function, bg="purple", fg="white")
Button4 = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause_function, bg="orange", fg="white")

# Above onscreen display to indicate what song is currently playing.
var = tkr.StringVar()
song_title = tkr.Label(player, font="Helvetica 12 bold", textvaribale=var)

# Rearrange button in horizontal format and mainloop function to run appilcation.
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")
player.mainloop()

