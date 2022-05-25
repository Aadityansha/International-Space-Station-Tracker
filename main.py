# importing modules
from tkinter import *
import tkintermapview
import requests
import json
import time

# functions
def fetchAPI(): # fetch location of ISS from external API
    api = "http://api.open-notify.org/iss-now.json"
    response = requests.get(api)
    data = json.loads(response.text)
    return data

# getting latitude and longitude
data = fetchAPI()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# creating GUI
win = Tk() # creates GUI
win.title("International Space Station Tracker") # set GUI title
win.geometry("800x600") # specify window height and width
win.minsize(800, 600) # specifies minimum window of GUI

# GUI widgets
heading = Label(win, text = "International Space Station Tracker", font=("Arial", 25)) # create title
heading.pack(pady=(5, 0))

map = tkintermapview.TkinterMapView(win, width=750, height=500, corner_radius=0) # widget creates map
map.place(relx=0.5, rely=0.5, anchor=CENTER)
map.set_zoom(2)
iss = map.set_marker(iss_latitude, iss_longitude, text="International Space Station") # marks ISS location on map

win.mainloop() # runs app