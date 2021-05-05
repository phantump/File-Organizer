from tkinter import *
from tkinter import filedialog



def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "../Desktop/FinalProject",
                                          title = "Select a Deck",
                                          filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
      
    label_file_explorer.configure(text="File Opened: "+filename)
#open any decklist to view
def open_txt():
	filename = filedialog.askopenfilename(initialdir = "../Desktop/FinalProject",
        								 title = "Select a Deck", filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
	deckfile = open(filename,'r')  
	listing = deckfile.read()

	mytext.insert(END,listing)
	deckfile.close()
# function files can be edited and then saved with this function
def save_txt():
	filename = filedialog.askopenfilename(initialdir = "../Desktop/FinalProject",
        								 title = "Select a Deck", filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
	deckfile = open(filename,'w')
	deckfile.write(mytext.get(1.0,END))
#Function that allows a new file to be made
def newdeck():
	deck = mytext.get("1.0",END)
	filename = filedialog.asksaveasfilename(initialdir = "../Desktop/FinalProject",
        								 title = "New Deck", filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
	Ndeck = open(filename,'w')
	Ndeck.write(deck)


                                                                                                  
# Create the root window
window = Tk()
  
window.title('Deck List')
window.geometry("700x500")
window.config(background = "white")
 
label_file_explorer = Label(window,
                            text = "Deck File System",
                            width = 100, height = 4,
                            fg = "blue")
  
 #buttons for use of directory 
button_open = Button(window, text = "open decklist",command = open_txt)
button_save = Button(window, text = "save decklist Edits", command = save_txt)
button_new=Button(window,text="New Deck Name", command=newdeck)
button_exit = Button(window, text = "Exit", command = exit)

#organizes the buttons into a grid  
label_file_explorer.grid(column = 1, row = 1)
mytext = Text(window,width = 50,height = 10, font =("helvetica",16))
mytext.grid(column =1, row = 2)
button_open.grid(column = 1, row = 3)
button_save.grid(column = 1, row = 4)
button_new.grid(column = 1, row = 5)
button_exit.grid(column = 1,row = 6)





window.mainloop()