__author__ = 'chrismelnyk'
import tkinter as tk
from functools import partial
from PIL import ImageTk,Image

def call_result1(label_result, graphite, result1):
    graphite = int((graphite.get()))
    canister_total = graphite * 0.66

    label_result.config(text="# of canisters is %d" % canister_total)

    return

root = tk.Tk()
icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)
root.geometry('400x100')
root.title('Soil Centrifuge Calculator')
number1 = tk.StringVar()
#number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Graphite Soil Calculator").grid(row=0, column=2)
labelgraphite= tk.Label(root, text="# of graphite desired: ").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=2, column=2)
entrygraphite = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

call_result1 = partial(call_result1, labelResult, number1)

b1 = tk.Button(root, text="Calculate Soil Canisters", command=call_result1).grid(row=3, column=0)

root.mainloop()
