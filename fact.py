import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Fact Of The Day")
root.geometry("400x300")

#Create the facts list
with open("facts.txt", "r") as f:
    facts = [line.strip() for line in f.readlines()]

# Create a label widget
label = tk.Label(root, text="My New Fact Is")
label.pack(pady=20) # Pack the label into the window


# Create a button widget
def on_button_click():
    fact=random.choice(facts)
    label.config(text=fact)
    button.pack_forget()


button = tk.Button(root, text="Click To Learn", command=on_button_click)
button.pack()

# Start the main event loop
root.mainloop()
