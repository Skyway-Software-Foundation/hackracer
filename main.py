"""
This is the main application window. It is provided under the MIT License, as follows:

MIT License

Copyright (c) 2021 Skyway-Software-Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#import necessary dependencies
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import json

def enterName():
    fahrenheit = playerName.get()
    print(fahrenheit)

# Set-up the window
window = tkinter.Tk()
window.title("HackRacer")
window.resizable(width=True, height=True)


###############################
#Lobby
###############################
frm_entry = tkinter.Frame(master=window)
lbl_temp = tkinter.Label(master=frm_entry, text="Enter Player Name: ")
playerName = tkinter.Entry(master=frm_entry, width=10)
btn_convert = tkinter.Button(
    master=frm_entry,
    text="Play!",
    command=enterName
)
#Grid Lobby
playerName.grid(row=0, column=1, sticky="e")
lbl_temp.grid(row=0, column=0, sticky="w")
btn_convert.grid(row=1, column=0, pady=10)
#Format Lobby entry
frm_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)





# Run the application
window.mainloop()