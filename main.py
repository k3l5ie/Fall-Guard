import tkinter as tk
import fall

def retrieve_input():
    input_value = input_field.get()  # Get the text from input_field
    print(input_value)  # Print the input to the console

# Create the main window
root = tk.Tk()
root.title("Fall Guard Emergency Setup")

# Create a label widget
label = tk.Label(root, text="Enter User's Name")
label.pack(padx=20, pady=20)

# Create a text entry widget
input_field = tk.Entry(root, width=50)
input_field.pack(padx=20, pady=20)

# Create a button that retrieves the input
submit_button = tk.Button(root, text="Submit", command=retrieve_input)
submit_button.pack(padx=20, pady=20)

# Start the GUI event loop
root.mainloop()