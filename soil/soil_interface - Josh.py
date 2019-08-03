#Calculator for soil centrifuge
#1. Enter Amount of Cannisters
#2. Outputs the amount of items you can get
import tkinter as tk
from functools import partial
from subprocess import call
from PIL import ImageTk,Image

compound = 'soil/josh/compound.py'
resin = 'soil/josh/resin.py'
ammonium = 'soil/josh/ammonium.py'
clay = 'soil/josh/clay.py'
organic = 'soil/josh/organic.py'
quartz = 'soil/josh/quartz.py'
graphite = 'soil/josh/graphite.py'




root = tk.Tk()
#this is a proper dictionary


icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

root.geometry('240x525')
root.title('Soil Centrifuge - Enter Number of Cannisters')
#entrybox
number1 = tk.StringVar()

varcompound = tk.StringVar()
resource = [
    #associating the label with the ratio, rather than a string with a ratio.
    [varcompound, .25]
    #"resin": .25,
    #"ammonium": .5,
    #"graphite": 1.5,
    #"organic": .25,
    #"quartz": .5,
    #"clay": .33
]

def call_result1(result1):
    try:
        cannister_total = int((number1.get()))
    except:
        return

    #looping through the key value pairs
    #for var, val in resource:
        #var.set(str(cannister_total//val))
    return
call_result1 = partial(call_result1, number1)

labelcannisters= tk.Label(root, text="# of Cannisters: ").grid(row=0, column=0)
#labelResult = tk.Label(root)
#putthisinbutton?
#labelResult.grid(row=2, column=2)
entrycannisters = tk.Entry(root, textvariable=number1, validate='key', vcmd=call_result1).grid(row=0, column=1)

#call_result1 = partial(call_result1, labelResult, number1)

#b1 = tk.Button(root, text="Calculate Resources Earned", command=call_result1).grid(row=3, column=0)
#call images
img_comound = "images/resources/compound.png"
img_resin = "images/resources/resin.png"
img_organic = "images/resources/organic.png"
img_clay = "images/resources/clay.png"
img_graphite = "images/resources/graphite.png"
img_quartz = "images/resources/quartz.png"
img_ammonium = "images/resources/ammonium.png"

compound_icon = ImageTk.PhotoImage(Image.open(img_comound))
resin_icon = ImageTk.PhotoImage(Image.open(img_resin))
organic_icon = ImageTk.PhotoImage(Image.open(img_organic))
clay_icon = ImageTk.PhotoImage(Image.open(img_clay))
graphite_icon = ImageTk.PhotoImage(Image.open(img_graphite))
quartz_icon = ImageTk.PhotoImage(Image.open(img_quartz))
ammonium_icon = ImageTk.PhotoImage(Image.open(img_ammonium))

#def callcompound():
    #call(['python', compound])


#def callresin():
    #call(['python', resin])

#def callammonium():
    #call(['python', ammonium])

#def callclay():
    #call(['python', clay])

#def callorganic():
    #call(['python', organic])

#def callquartz():
    #call(['python', quartz])

#def callgraphite():
    #call(['python', graphite])


tk.Label(root, text="       ").grid(row=3,column=0)
tk.Button(root, image=compound_icon, width=115, height=115).grid(row=4, column=0)
lblcompound = tk.Label(root, text=varcompound.get(), textvariable=varcompound).grid(row=5, column=0)
tk.Button(root, image=resin_icon,  width=115, height=115).grid(row=4, column=1)
#tk.Button(root, image=organic_icon, command=callorganic, width=115, height=115).grid(row=5, column=0)
tk.Button(root, image=clay_icon,  width=115, height=115).grid(row=5, column=1)
tk.Button(root, image=quartz_icon, width=115, height=115).grid(row=6, column=0)
tk.Button(root, image=graphite_icon, width=115, height=115).grid(row=6, column=1)
tk.Button(root, image=ammonium_icon, width=115, height=115).grid(row=7, column=0)
def compound_callback(*args):
    lblcompound.config(text=self.get())
varcompound.trace("w", compound_callback)

root.mainloop()
