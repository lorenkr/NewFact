
import customtkinter as ctk
import random

#Apperarance
ctk.set_appearance_mode("light")     
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title("Fact Of The Day")
root.geometry("600x300")

#Read the facts file
with open("facts.txt", "r") as f:
    facts = [line.strip() for line in f.readlines()]


# Create a label widget
label = ctk.CTkLabel(root,
                      text="My New Fact Is",
                      font=("MS Serif",20))
label.pack(pady=20) 


# Create a button widget
def on_button_click():
    fact=random.choice(facts)
    label.configure(text=fact)
    button.pack_forget()


button = ctk.CTkButton(root, 
                       text="Click To Learn",
                       font=("MS Serif",20),
                       command=on_button_click,
                       width=200,
                       height=40,
                       corner_radius=15)
button.pack()

# Start the main event loop
root.mainloop()
