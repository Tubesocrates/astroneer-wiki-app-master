__author__ = 'Tubesocrates'
import tkinter as tk
from functools import partial
from PIL import ImageTk,Image

josh = 'soil/josh/soil_interface - Josh'
def calljosh():
    call(['python', josh])

def call_result1(label_result, canister_total, result1):
    cannister_total = int((josh.get()))
    compound = canister_total / 0.25

    label_result.config(text="# of compound is %d" % compound)

    return
call_result1 = partial(call_result1, labelResult, number1)

root = tk.Tk()
icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)
root.geometry('400x100')
root.title('Soil Centrifuge Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Compound Soil Calculator").grid(row=0, column=2)
labelcompound= tk.Label(root, text="# of soil cannisters: ").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=2, column=2)
entrycannisters = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

call_result1 = partial(call_result1, labelResult, number1, number2)

b1 = tk.Button(root, text="Calculate Compound", command=call_result1).grid(row=3, column=0)

root.mainloop()
