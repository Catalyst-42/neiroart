import tkinter as tk
from tkinter import ttk
from pprint import pprint
from colors import RGB, WHITE, BLACK
from setup import inputs

window = tk.Tk()
window.title("Neiroart")

def setup():
    for i, field in enumerate(inputs[current_script].keys()):
        inputs[current_script][field][2] = ttk.Label(window, text=field)
        inputs[current_script][field][3] = ttk.Entry(window, width=35)
        
        inputs[current_script][field][2].grid(row=i + 1, column=0, padx=(4, 0), pady=(4, 0))
        inputs[current_script][field][3].grid(row=i + 1, column=1, padx=(0, 4), pady=(4, 0))
        
        # Setup values in tkinter fileds
        value = inputs[current_script][field][1]            
        inputs[current_script][field][3].insert(0, str(value))
    
def switch(_):
    global current_script
    
    for field in inputs[current_script].keys():
        inputs[current_script][field][2].grid_forget()
        inputs[current_script][field][3].grid_forget()
    
    current_script = clicked.get()
    
    setup()

def gen():
    # Update input settings
    generator = __import__(current_script)
    
    for i, field in enumerate(inputs[current_script].keys()):
        if inputs[current_script][field][0] != 'str':
            inputs[current_script][field][1] = eval(inputs[current_script][field][3].get())  # Argessive
        else:
            inputs[current_script][field][1] = inputs[current_script][field][3].get()
        
    
    generator.gen()

# Init
current_script = "map_linear"
clicked = tk.StringVar()
clicked.set(current_script)

script_label = ttk.Label(window, text="Script")
script_options = ttk.OptionMenu(window, clicked, "map_linear",*inputs.keys(), command=switch)
script_label.grid(row=0, column=0, padx=(0, 4), pady=(4, 0))
script_options.grid(row=0, column=1, padx=(4, 0), pady=(4, 0))

generate_button = ttk.Button(text="Generate", command=gen)
generate_button.grid(row=100, column=0, columnspan=2, pady=(0, 4))    
setup()

window.mainloop()
