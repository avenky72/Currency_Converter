import tkinter as tk
from tkinter import ttk

from forex_python.converter import CurrencyRates

# Force the use of decimal
c = CurrencyRates(force_decimal=True)

root = tk.Tk()
root.title("Currency Converter")

money_label = tk.Label(root, text="Enter the monetary amount to be converted")
money_entry = tk.Entry(root)
curr_label_start = tk.Label(root, text="Choose your starting currency")
curr_start_combobox = ttk.Combobox(root, values=[" ", "USD", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "EUR", "HKD", "AUD", "CNY", "PHP"])
curr_label_end = tk.Label(root, text="Choose the currency you wish to convert to")
curr_end_combobox = ttk.Combobox(root, values=[" ", "USD", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "EUR", "HKD", "AUD", "CNY", "PHP"])


money_label.pack(padx=7, pady=7, side=tk.LEFT)
money_entry.pack(padx=5, pady=5, side=tk.LEFT)
curr_label_start.pack(padx=5, pady=5, side=tk.LEFT)
curr_start_combobox.pack(padx=5, pady=5, side=tk.LEFT)
curr_label_end.pack(padx=5, pady=5, side=tk.LEFT)
curr_end_combobox.pack(padx=5, pady=5, side=tk.LEFT)

root.mainloop()
