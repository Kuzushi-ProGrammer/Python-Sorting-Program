
from tkinter import *
from tkinter import ttk
import random
import time
import BinarySearch
import Bubblesort
import SelectionSort
#import InsertionSort

def Ball():
    print("balling")

def SwapModes():
    print("clicked")
    global sortType

    if sortType == "Custom Array":
        modeButton.config(text="Random Array")
        sortType = "Random Array"

        elementLabel.grid(column=2, row=2, sticky=(W, E))
        rangeLabel.grid(column=2, row=3, sticky=(W, E))
        elementEntry.grid(column=3, row=2, sticky=(W, E))
        rangeEntry.grid(column=3, row=3, sticky=(W, E))

        customLabel.grid_remove()
        customEntry.grid_remove()
        customInstructions.grid_remove()
        generateButton.configure(text="Generate List")
        generateButton.grid_configure(column=4, row=3, sticky=(W, E))

    elif sortType == "Random Array":
        modeButton.config(text="Custom Array")
        sortType = "Custom Array"

        customLabel.grid(column=2, row=2, sticky=(W, E))
        customEntry.grid(column=3, row=2, sticky=(W, E))
        customInstructions.grid(column=3, row=3, sticky=W, columnspan=2)
        customLabel.grid_configure(padx=5, pady=2.5)
        customEntry.grid_configure(padx=5, pady=2.5)

        elementLabel.grid_remove()
        rangeLabel.grid_remove()
        elementEntry.grid_remove()
        rangeEntry.grid_remove()
        generateButton.configure(text="Confirm")
        generateButton.grid_configure(column=4, row=2, sticky=(W, E))

def Binary():
    pass

def Bubble():
    pass

def Insertion():
    pass

def Selection():
    pass

sortType = "Random Array"

root = Tk()
root.title("Sorting Algorithms")
root.geometry("500x500+0+0")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# columnspan and rowspan make the things go across more than one column or row
# columnspan horizontal, rowspan vertical

#constants
inputSpan = IntVar()
inputRange = DoubleVar()
inputList = StringVar()

# top bar configuration
bubbleButton = ttk.Button(mainframe, text="Bubble Sort", command=Ball)
insertionButton = ttk.Button(mainframe, text="Insertion Sort", command=Ball)
selectionButton = ttk.Button(mainframe, text="Selection Sort", command=Ball)
binaryButton = ttk.Button(mainframe, text="Binary Search", command=Ball)
modeButton = ttk.Button(mainframe, text="Custom Array", command=SwapModes)

bubbleButton.grid(column=2, row=1, sticky=W)
insertionButton.grid(column=3, row=1, sticky=W)
selectionButton.grid(column=4, row=1, sticky=W)
binaryButton.grid(column=5, row=1, sticky=W)
modeButton.grid(column=1, row=1, sticky=W)

bubbleButton.grid_configure(padx=5, pady=2.5)
insertionButton.grid_configure(padx=5, pady=2.5)
selectionButton.grid_configure(padx=5, pady=2.5)
binaryButton.grid_configure(padx=5, pady=2.5)
modeButton.grid_configure(padx=5, pady=2.5)

# assigning references (grid isnt called yet)
# random array
elementLabel = ttk.Label(mainframe, text="# of elements:")
rangeLabel = ttk.Label(mainframe, text="Range:")
elementEntry = ttk.Entry(mainframe, width=5, textvariable=inputSpan)
rangeEntry = ttk.Entry(mainframe, width=5, textvariable=inputRange)
generateButton = ttk.Button(mainframe, text="Generate List", command=Ball)

# custom array
customLabel = ttk.Label(mainframe, text="Input Array:")
customInstructions = ttk.Label(mainframe, text="Format: 1, 4, 5, 6, etc.")
customEntry = ttk.Entry(mainframe, width=5, textvariable=inputList)

# output statements
inputLabel = ttk.Label(mainframe, text="Unsorted List:")
outputLabel = ttk.Label(mainframe, text="Sorted List:")
timeLabel = ttk.Label(mainframe, text="Time Taken:")
emptySpace = ttk.Label(mainframe, text="-")


# default state
elementLabel.grid(column=2, row=2, sticky=(W, E))
rangeLabel.grid(column=2, row=3, sticky=(W, E))
elementEntry.grid(column=3, row=2, sticky=(W, E))
rangeEntry.grid(column=3, row=3, sticky=(W, E))
customLabel.grid(column=2, row=3, sticky=(W, E))
customEntry.grid(column=3, row=3, sticky=(W, E))
generateButton.grid(column=4, row=3, sticky=(W, E))
emptySpace.grid(column=3, row=4)
inputLabel.grid(column=2, row=5, columnspan=3)
outputLabel.grid(column=2, row=6, columnspan=3)
timeLabel.grid(column=2, row=7, columnspan=3)

elementLabel.grid_configure(padx=5, pady=2.5)
rangeLabel.grid_configure(padx=5, pady=2.5)
elementEntry.grid_configure(padx=5, pady=2.5)
rangeEntry.grid_configure(padx=5, pady=2.5)

customLabel.grid_remove()
customEntry.grid_remove()
'''
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=2.5)
 '''
root.mainloop()
'''
array = []
for x in range(100): #user define this bitch (number of values)
    array.append(random.randrange(0,1000))
length = len(array)

sortedArray = SelectionSort(array, length)
print(sortedArray)
'''