from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

def convert():
    miles = int(num_entry.get())
    km = miles * 1.6
    res_label.config(text=km)

num_entry = Entry()
num_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

res_label = Label(text="0")
res_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)



window.mainloop()
