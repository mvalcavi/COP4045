import tkinter as tk
from tkinter import ttk


class SCFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        ttk.Label(self, text="Items:").grid(column=0, row=0)
        ttk.Entry(self, width=25, state="readonly").grid(column=1, row=0)
        ttk.Label(self, text="Pick an Item:").grid(column=0, row=1)
        ttk.Entry(self, width=25).grid(column=1, row=1)

        ttk.Button(self, text="Add to Cart").grid(column=0, row=2)
        #ttk.Button(self, text="Add to Cart", command = self.add_item).grid(column=0, row=2)

        ttk.Button(self, text="Remove from Cart").grid(column=2, row=2)
        #ttk.Button(self, text="Remove from Cart", command = self.remove_item).grid(column=2, row=2)

        ttk.Button(self, text="Go to Cart").grid(column=1, row=3)
        #ttk.Button(self, text="Go to Cart", command = self.show_cart).grid(column=1, row=3)

        for child in self.winfo_children():
            child.grid_configure(padx=9, pady=7)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Welcome to the Store")
    SCFrame(root)
    root.mainloop()