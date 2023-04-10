import tkinter as tk
from tkinter import scrolledtext

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Formatted Text Example")
        
        # Create a scrolled text widget
        self.text_box = scrolledtext.ScrolledText(self.root, width=50, height=10, font=("Helvetica", 12), state='disabled')
        self.text_box.pack(padx=10, pady=10)
        
        # Insert some text with formatting
        self.text_box.configure(state='normal')
        self.text_box.insert(tk.END, "This is some ")
        self.text_box.insert(tk.END, "red", ("red",))
        self.text_box.insert(tk.END, " text.\n")
        self.text_box.insert(tk.END, "This is some ")
        self.text_box.insert(tk.END, "blue", ("blue",))
        self.text_box.insert(tk.END, " text.\n")
        self.text_box.insert(tk.END, "This is some ")
        self.text_box.insert(tk.END, "bold", ("bold",))
        self.text_box.insert(tk.END, " text.\n")
        self.text_box.insert(tk.END, "This is some ")
        self.text_box.insert(tk.END, "underlined", ("underline",))
        self.text_box.insert(tk.END, " text.\n")
        self.text_box.configure(state='disabled')
        
        # Define the text tag configurations
        self.text_box.tag_config("red", foreground="red")
        self.text_box.tag_config("blue", foreground="blue")
        self.text_box.tag_config("bold", font=("Helvetica", 12, "bold"))
        self.text_box.tag_config("underline", underline=True)
        
        self.root.mainloop()

# Create an instance of the GUI
gui = GUI()
