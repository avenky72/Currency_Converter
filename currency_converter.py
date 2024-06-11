import tkinter as tk
#import tkFont
from tkinter import ttk

from forex_python.converter import CurrencyRates

# Force the use of decimal
c = CurrencyRates()

#font1 = tkFont.Font(family="Helvetica",size=36,weight="bold")


def enter_data():
    amount = money_entry.get()
    start = curr_start_combobox.get()
    end = curr_end_combobox.get()
    output = c.convert(start, end, amount)
    #print("Starting Amount: ", amount, " Initial Currency: ", start, " End Currency: ", end, "Converted Amount: ", output)
    #print(c.get_rates('USD'))
    converted_field.insert(0, str(output))

def clear_data():
    money_entry.delete(0, tk.END)
    converted_field.delete(0, tk.END)

root = tk.Tk()
root.title("Currency Converter")
root.configure(background='wheat3')


money_label = tk.Label(root, fg="navy", text="Enter the monetary amount to be converted")
money_entry = tk.Entry(root, bg="MistyRose2")
curr_label_start = tk.Label(root, text="Choose your starting currency")
curr_start_combobox = ttk.Combobox(root, font=('Helvetica', 15, 'bold'), values=[" ", "USD", "INR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "EUR", "HKD", "AUD", "CNY", "PHP"])
curr_label_end = tk.Label(root, text="Choose the currency you wish to convert to")
curr_end_combobox = ttk.Combobox(root, font=('Helvetica', 15, 'bold'), values=[" ", "USD", "INR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "EUR", "HKD", "AUD", "CNY", "PHP"])
enter_button = tk.Button(root, font=('arial', 15, 'bold'), text="Convert",  bg="magenta4", fg="OliveDrab4", command= enter_data)
converted_field = tk.Entry(root, bg="SeaGreen1")
clear_button = tk.Button(root, font=('arial', 15, 'bold'), text="Clear",  bg="magenta4", fg="magenta4", command= clear_data)


money_label.pack(padx=5, pady=5, side=tk.LEFT)
money_entry.pack(padx=5, pady=5, side=tk.LEFT)
curr_label_start.pack(padx=5, pady=5, side=tk.LEFT)
curr_start_combobox.pack(padx=5, pady=5, side=tk.LEFT)
curr_label_end.pack(padx=5, pady=5, side=tk.LEFT)
curr_end_combobox.pack(padx=5, pady=5, side=tk.LEFT)
enter_button.pack(padx=5, pady=5, side=tk.LEFT)
converted_field.pack(padx=5, pady=5, side=tk.LEFT)
clear_button.pack(padx=5, pady=5, side=tk.LEFT)

root.mainloop()
