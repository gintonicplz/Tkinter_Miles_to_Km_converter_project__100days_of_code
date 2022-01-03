from tkinter import *


# todo - design layout
# todo - functionality
# todo - function to convert km to miles
# 1 mile => 1.61km

def conversion():
    entry_var = float(input_to_convert.get())
    conversion_result = entry_var * 1.609
    return round(result.config(text=conversion_result))


window = Tk()
window.title("David's Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# labels
equal_to = Label(text="is equal to", font=("Arial", 20, "normal"))
equal_to.grid(column=0, row=1)

result = Label(text=0, font=("Arial", 20, "normal"))
result.grid(column=1, row=1)

miles = Label(text="Miles", font=("Arial", 20, "normal"))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Arial", 20, "normal"))
km.grid(column=2, row=1)

# entry
input_to_convert = Entry(width=10, font=("Arial", 20, "normal"))
input_to_convert.grid(column=1, row=0)

# button
button = Button(text="Calculate", font=("Arial", 20, "normal"), command=conversion)
button.grid(column=1, row=2)

window.mainloop()
