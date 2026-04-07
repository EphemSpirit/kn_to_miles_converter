from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

def convert():
    initial_value = float(num_entry.get())
    res = initial_value * 1.6 if radio_state.get() == 1 else initial_value / 1.6
    res_label.config(text=res)


num_entry = Entry(width=10)
num_entry.grid(column=1, row=0)

from_label = Label(text="Miles")
from_label.grid(column=2, row=0)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

res_label = Label(text="0")
res_label.grid(column=1, row=1)

to_label = Label(text="km")
to_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

def radio_used():
    from_label_text = "Miles" if radio_state.get() == 1 else "Km"
    to_label_text = "Km" if radio_state.get() == 1 else "Miles"
    from_label.config(text=from_label_text)
    to_label.config(text=to_label_text)


radio_state = IntVar()
miles_radio = Radiobutton(text="Miles", value=1, variable=radio_state, command=radio_used)
miles_radio.grid(column=1, row=3)

km_radio = Radiobutton(text="Km", value=2, variable=radio_state, command=radio_used)
km_radio.grid(column=0, row=3)

miles_radio.select()


window.mainloop()
