from tkinter import *

window = Tk()
window.minsize(300, 100)
window.title("Miles to Kms Converter")
window.configure(padx=30, pady=20)

# todo _entry to take input miles -- label = miles
# todo _output of entry which is also a label but changed using button
#       and two labels to the left and right
#todo - a button named calculate
input = Entry(window)
input.grid(row=0, column=1)

label_miles = Label(window, text="Miles")
label_miles.grid(row=0, column=2)


label_equal = Label(window, text="is equal to")
label_equal.grid(row=1, column=0)

label_km = Label(window, text="0")
label_km.grid(row=1, column=1)

label_kms = Label(window, text="Kms")
label_kms.grid(row=1, column=2)

def calculate():
    input_miles = float(input.get())
    output_kms = round(input_miles * 1.60934,2)
    label_km.config(text=output_kms)


button_miles = Button(window, text="Calculate", command = calculate)
button_miles.grid(row=2, column=1)












window.mainloop()