#a secondary file that opens files and moves them based on what it has read
from tkinter import *
from tkinter import filedialog
import shutil

# opens a directory to the main file folder where a decklist can be selected
filename = filedialog.askopenfilename(initialdir = "../Desktop/FinalProject",
        	title = "Select a Deck", filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
file = open(filename,'r')
form = file.readline()
color = file.readline()
file.close()

#after opening, split the first two lines to create the keywords
formtype = form.split(':')
colortype = color.split(':')
formatorg = formtype[1].strip().capitalize()
colororg = colortype[1].split(',')[0].strip().capitalize()
print(formatorg)
print(colororg)

#shell utility, moves the file based on the keywords which are 
# inserted into the file path			here           here
shutil.move(filename,f'../FinalProject/{formatorg}/{colororg}/')


