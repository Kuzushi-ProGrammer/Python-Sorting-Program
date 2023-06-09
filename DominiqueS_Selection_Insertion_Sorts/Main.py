
from sqlite3 import Timestamp
from tkinter import *
from tkinter import ttk
import random
import time
import BinarySearch #change menu to a number selector to search
import Bubblesort
import SelectionSort
#import InsertionSort (I HAVENT MADE THIS YET)

def Ball():
    print("balling")

def Confirm():
    global generatedList
    generatedList = inputList.get()

    print(generatedList)
    generatedList = generatedList.split(",")
    for x in generatedList:
         generatedList[generatedList.index(x)] = x.strip(" ")

    generatedList = list(map(int, generatedList))
    inputLabel.configure(text=f"Unsorted List:\n{generatedList}\n")


def GenerateList():
    minimum = minInputRange.get()
    maximum = maxInputRange.get()
    length = inputLength.get()

    global generatedList
    generatedList = []

    for x in range(length):
        generatedList.append(random.randint(minimum, maximum))

    inputLabel.configure(text=f"Unsorted List:\n{generatedList}\n")

def SwapModes():
    print("clicked")
    global sortType

    if sortType == "Custom Array":
        modeButton.config(text="Random Array")
        sortType = "Random Array"

        elementLabel.grid(column=2, row=2, sticky=(W, E))
        elementEntry.grid(column=3, row=2, sticky=(W, E))

        minRangeLabel.grid(column=2, row=3, sticky=(W, E))
        minRangeEntry.grid(column=3, row=3, sticky=(W, E))

        maxRangeLabel.grid(column=2, row=4, sticky=(W, E))
        maxRangeEntry.grid(column=3, row=4, sticky=(W, E))

        generateButton.grid(column=4, row=4, sticky=(W, E))

        customLabel.grid_remove()
        customEntry.grid_remove()
        customInstructions.grid_remove()
        confirmButton.grid_remove()

    elif sortType == "Random Array":
        modeButton.config(text="Custom Array")
        sortType = "Custom Array"

        customLabel.grid(column=2, row=2, sticky=(W, E))
        customEntry.grid(column=3, row=2, sticky=(W, E))
        customInstructions.grid(column=3, row=3, sticky=W, columnspan=2)
        confirmButton.grid(column=4, row=2, sticky=(W, E))

        customLabel.grid_configure(padx=5, pady=2.5)
        customEntry.grid_configure(padx=5, pady=2.5)

        elementLabel.grid_remove()
        elementEntry.grid_remove()
        minRangeLabel.grid_remove()
        minRangeEntry.grid_remove()
        maxRangeLabel.grid_remove()
        maxRangeEntry.grid_remove()
        generateButton.grid_remove()

def Binary():
    #something something do the mario
    pass

def Bubble():
    timeStamp = time.time_ns()
    sortedList = Bubblesort.Sort(generatedList)
    timeStamp = time.time_ns() - timeStamp
    outputLabel.configure(text=f"Sorted List:\n{sortedList}\n")

    if timeStamp <=0:
        timeLabel.configure(text=f"Time Taken: {round(timeStamp*0.000000001, 6)} Seconds")
    else:
        timeLabel.configure(text=f"Time Taken: {round(timeStamp, 6)} Nanoseconds")

def Insertion():
    #sortedList = Insertionsort(text=f"Sorted List:\n{sortedList}\n")
    #outputLabel.configure(text=f"Sorted List:\n{sortedList}\n")
    pass

def Selection():
    length = inputLength.get()

    timeStamp = time.time_ns()
    sortedList = SelectionSort.Sort(generatedList, length)
    timeStamp = time.time_ns() - timeStamp
    outputLabel.configure(text=f"Sorted List:\n{sortedList}\n")

    print(timeStamp)
    if timeStamp <=0:
        timeLabel.configure(text=f"Time Taken: {round(timeStamp*0.000000001, 6)} Seconds")
    else:
        timeLabel.configure(text=f"Time Taken: {round(timeStamp, 6)} Nanoseconds")
    
def AdjustScrollbar(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

sortType = "Random Array"

root = Tk()
root.title("Sorting Algorithms")
root.geometry("460x500+0+0")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = Frame(mainframe, width=250)
frame.grid(column=2, row=6, columnspan=3, sticky=(N,S))
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.grid_propagate(True)

canvas = Canvas(frame, width=250)
canvas.grid(column=2, row=6, columnspan=3)

scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.grid(column=6, row=6, sticky=(N,S))

output_frame = Frame(canvas)

canvas.create_window(0,0, window=output_frame, anchor="n")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.configure(scrollregion=canvas.bbox("all"))

output_frame.bind("<Configure>", AdjustScrollbar)

#

# columnspan and rowspan make the things go across more than one column or row
# columnspan horizontal, rowspan vertical

#constants
inputLength = IntVar()
minInputRange = IntVar()
maxInputRange = IntVar()
inputList = StringVar()

# top bar configuration
bubbleButton = ttk.Button(mainframe, text="Bubble Sort", command=Bubble)
insertionButton = ttk.Button(mainframe, text="Insertion Sort", command=Insertion)
selectionButton = ttk.Button(mainframe, text="Selection Sort", command=Selection)
binaryButton = ttk.Button(mainframe, text="Binary Search", command=Binary)
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
elementEntry = ttk.Entry(mainframe, width=5, textvariable=inputLength)
minRangeLabel = ttk.Label(mainframe, text="Min. range:")
minRangeEntry = ttk.Entry(mainframe, width=5, textvariable=minInputRange)
maxRangeLabel = ttk.Label(mainframe, text="Max. Range:")
maxRangeEntry = ttk.Entry(mainframe, width=5, textvariable=maxInputRange)
generateButton = ttk.Button(mainframe, text="Generate List", command=GenerateList)
confirmButton = ttk.Button(mainframe, text="Confirm", command=Confirm)

# custom array
customLabel = ttk.Label(mainframe, text="Input Array:")
customInstructions = ttk.Label(mainframe, text="Format: 1, 4, 5, 6, etc.")
customEntry = ttk.Entry(mainframe, width=5, textvariable=inputList)

# output statements (experimenting with frames)
inputLabel = ttk.Label(output_frame, text="Unsorted List:", wraplength=250, anchor="n")
outputLabel = ttk.Label(output_frame, text="Sorted List:", wraplength=250, anchor="n")
timeLabel = ttk.Label(mainframe, text="Time Taken:", wraplength=250, anchor="n", justify="center")

#empty spaces
ttk.Label(mainframe, text="\n").grid(column=3, row=5)
ttk.Label(mainframe, text="\n").grid(column=3, row=8)


# default state
elementLabel.grid(column=2, row=2, sticky=(W, E))
elementEntry.grid(column=3, row=2, sticky=(W, E))
maxRangeLabel.grid(column=2, row=4, sticky=(W, E))
maxRangeEntry.grid(column=3, row=4, sticky=(W, E))
minRangeLabel.grid(column=2, row=3, sticky=(W, E))
minRangeEntry.grid(column=3, row=3, sticky=(W, E))
customLabel.grid(column=2, row=3, sticky=(W, E))
customEntry.grid(column=3, row=3, sticky=(W, E))
generateButton.grid(column=4, row=4, sticky=(W, E))
confirmButton.grid(column=4, row=2, sticky=(W, E))
inputLabel.grid(column=3, row=6, columnspan=3)
outputLabel.grid(column=3, row=7, columnspan=3)
timeLabel.grid(column=2, row=9, columnspan=3)

elementLabel.grid_configure(padx=5, pady=2.5)
elementEntry.grid_configure(padx=5, pady=2.5)

minRangeLabel.grid_configure(padx=5, pady=2.5)
minRangeEntry.grid_configure(padx=5, pady=2.5)

maxRangeLabel.grid_configure(padx=5, pady=2.5)
maxRangeEntry.grid_configure(padx=5, pady=2.5)

customLabel.grid_remove()
customEntry.grid_remove()
confirmButton.grid_remove()

root.mainloop()
