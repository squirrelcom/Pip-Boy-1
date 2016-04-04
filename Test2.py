import matplotlib
import numpy
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter as ttk
from tkinter import *
import spotipy
import sys
import webbrowser

PIP_FONT = ("Verdana", 12)
photo = "mrPip.gif"

uri_ID = 'spotify:artist:1Xylc3o4UrD53lo9CvFvVg'

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(uri_ID)

#getting the track and audio link to top song
for track in results['tracks'][:1]:
   text = 'Track    : ' + track['name']
   text2 = track['preview_url']


def callback(event):
    webbrowser.open_new(text2)


class SetUp(tk.Tk):  #inheriting
    def __init__(self, *args, **kwargs):  #method, initialisng

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_iconbitmap(self, default="favicon.ico")

        container = tk.Frame(self) #container for holding everything
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}  #dictionary of frames

        for F in (StartPage, RadioPage, MapPage, DataPage, InvPage, StatsPage): #loop through the number of pages

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew") #alignment plus stretch

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() #raised to the front

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        label = tk.Label(self, text = "photo will appear here", bg = "black", fg = "white")
        label.pack(side = BOTTOM)

        #to make width for now
        label = tk.Label(self, width = 60, bg = "black")
        label.pack(side = BOTTOM)


class RadioPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        var = tk.StringVar()
        var.set(text)

        var2 = tk.StringVar()
        var2.set(text2)

        label = tk.Label(self, textvariable = var, bg = "black", fg = "white")
        label.pack(side = BOTTOM)

        label2 = tk.Button(self, text = "Play", bg = "black", fg = "white", cursor = "hand2")
        label2.bind("<Button-1>", callback)
        label2.pack(side = BOTTOM)



class MapPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        label = tk.Label(self, text = "map functionality", bg = "black", fg = "white")
        label.pack(side = BOTTOM)


class DataPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        label = tk.Label(self, text = "data functionality", bg = "black", fg = "white")
        label.pack(side = BOTTOM)


class InvPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        label = tk.Label(self, text = "inv functionality", bg = "black", fg = "white")
        label.pack(side = BOTTOM)


class StatsPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.place(x = 15, y = 0)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.place(x = 95, y = 0)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.place(x = 175, y = 0)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.place(x = 255, y = 0)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.place(x = 335, y = 0)

        f = Figure(figsize = (7,5), dpi = 50)
        a = f.add_subplot(111) #onexone chart number 1

        data = (1, 2, 3, 4, 5)
        ind = numpy.arange(5) #the x plots
        width = 0.4

        a.barh(ind + width, data, width, color = 'g')

        a.set_axis_bgcolor('black')
        a.set_title('Stats')
        a.set_xticks(ind + width)
        a.set_xticklabels(('Strength', 'Perception', 'Endurance', 'Charisma', 'Agility'))

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = BOTTOM)



app = SetUp()
app.mainloop()