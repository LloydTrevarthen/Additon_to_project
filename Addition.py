""" This script is for an additional menu that can be added into
the main menu, that allows the easy entry of data into the main database
for use in the simulation.

The 'Add' button commits the data in the entry fields to the database.
The 'Suggestion' button pulls a suggestion from a dataset that is...
'Input', allows a dataset of items to be entered.
"""

import sys
from tkinter import *
import tkinter.ttk as ttk
import Database
import os
import random

root = Tk()

def main():
    root.resizable(width=FALSE, height=FALSE)
    gui = ItemAdd(root)
    root.geometry('{}x{}'.format(700, 500))
    BackgroundColour = '#E0EBFF'
    root.configure(bg=BackgroundColour)
    root.wm_title("Virtual Robot Bargain Hunt")
    root.mainloop()
    

class ItemAdd():
    def __init__(self, root):
        #global datasetData
        #global addData
        self.root = root
        addData = Button(root, text='Add', font=("Helvetica", 16), bg='white', height=1, width=13, command = adddata)
        canvas.create_window(100, 340, window = addData)

def Close():
    root.destroy()


ItemAddText = Label(root, text='Item Addition', font=("Helvetica", 28), bg='#E0EBFF')
ItemAddText.pack(pady=20)
canvas = Canvas(root, width=650, height= 350, bg='#E0EBFF', bd=0, highlightthickness=0, relief='ridge')
canvas.pack()
#Entry fields
itemName= Entry()
itemNameText = Label(root, text='Name', bg='#E0EBFF', font=("Helvetica", 20))
canvas.create_window(200,40, window = itemName)
canvas.create_window(80,40, window = itemNameText)
itemType= Entry()
itemTypeText = Label(root, text='Type', bg='#E0EBFF', font=("Helvetica", 20))
canvas.create_window(500,40, window = itemType)
canvas.create_window(380,40, window = itemTypeText)
itemPrice= Entry()
itemPriceText = Label(root, text='Price', bg='#E0EBFF', font=("Helvetica", 20))
canvas.create_window(200,140, window = itemPrice)
canvas.create_window(80,140, window = itemPriceText)
itemWeight= Entry()
itemWeightText = Label(root, text='Weight', bg='#E0EBFF', font=("Helvetica", 20))
canvas.create_window(500,140, window = itemWeight)
canvas.create_window(380,140, window = itemWeightText)
#Entry fields end

exampText = Label(root, text='EG: Bread, Food, 2, 0.1', font=("Helvetica", 16), bg='#E0EBFF')
exampTextDraw = canvas.create_window(325,240, window = exampText)

mainMenu = Button(root, text='Main Menu', command = Close, font=("Helvetica", 16), bg='white', height=1, width=13)
canvas.create_window(550, 235, window = mainMenu)

#progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
#canvas.create_window(250,240, window = progressbar)

def adddata():
    itemN = itemName.get()
    itemT = itemType.get()
    itemP = itemPrice.get()
    itemW = itemWeight.get()
    write = 0
    if itemN:
        write += 1
    if itemT:
        write += 1
    if itemP:
        write += 1
    if itemW:
        write += 1

    if write == 4:

        lines_in_database = set()
        
        for line in open('itemsraw.txt', "r"):
            lines_in_database.add(line.split(', ', 1)[0])
        
        if line == itemN:
            print(itemN,"is already in the database.")
            itemName.delete(0, 'end')
            itemType.delete(0, 'end')
            itemPrice.delete(0, 'end')
            itemWeight.delete(0, 'end')
        else:
            #Commit to database
            #progressbar.start()
            f = open("test.txt", "a")
            text = ("\n",itemN,", ",itemT,", ",itemP,", ",itemW)
            for t in text:
                f.write(''.join(str(s) for s in t))
            f.close
            itemName.delete(0, 'end')
            itemType.delete(0, 'end')
            itemPrice.delete(0, 'end')
            itemWeight.delete(0, 'end')
            Database.init()

            
            for line in open('dataset.txt', "r"):
                x = line.split((', ', 1)[0])
                if x == itemN:
                    print("Removing suggestion from dataset.")
                    line.write(" ")
            
            #progressbar.stop()
        
    else:
        print("Only",write,"of 4 entries filled.")
    
def datasetData():
    #Check data is present and remove duplicates
    statinfo = os.stat('datasetInput.txt')
    isdata = statinfo.st_size
    if isdata > 0:
        print("New dataset found, duplicates being removed.")
        lines_seen = set()
        lines_in_database = set()
        
        for line in open('itemsraw.txt', "r"):
            lines_in_database.add(line.split(', ', 1)[0])
        #print(lines_in_database)
        
        outfile = open('dataset.txt', "w")
        for line in open('datasetInput.txt', "r"):
            if line not in lines_in_database:
                if line not in lines_seen:
                    outfile.write(line)
                    lines_seen.add(line)
                    print("Added:",line)
                    #seems to miss end of list
                
        outfile.close()
        open('datasetInput.txt', 'w').close()
               
    else:
        print("No new data set detected; pulling suggestion...")
        itemName.delete(0, 'end')
        with open('dataset.txt') as f:
            items = [line.rstrip() for line in f]
        itemName.insert(END,(random.choice(items)))
        
        
datasetData = Button(root, text='Suggestion', font=("Helvetica", 16), bg='white', height=1, width=13, command = datasetData)
canvas.create_window(325, 340, window = datasetData)

def opendatawindow():
    os.startfile('datasetInput.txt')

datasetData = Button(root, text='Input', font=("Helvetica", 16), bg='white', height=1, width=13, command = opendatawindow)
canvas.create_window(550, 340, window = datasetData)

main()
