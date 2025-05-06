from tkinter import *
from datetime import datetime 
window = Tk()
window.geometry("400x400")
window.title("Age Calculator App")

def calculate_age():
    name = name_entry.get()
    birth_date = date_entry.get()
    birth_day = datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.now()
    age = today.year - birth_day.year
    result_label.config(text=f"Hello {name}! You are {age} years old.")
    
name_label = Label(window, text="Name: ", bg='Light Blue')
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

date_label = Label(window, text="Birth Date (DD/MM/YYYY):", bg='Light Blue')
date_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
date_entry = Entry(window)
date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

calculate_button = Button(window, text="Calculate", command=calculate_age, bg='Beige')
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label = Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.columnconfigure(1, weight=1)
window.mainloop()