import tkinter as tk
from openAI import *
count = 0

def process_input():
    user_input = input_text.get("1.0", "end-1c")  # Get text from the input text box
    print("User: " + user_input)
    gptResp = openAIBot(user_input)
    print("GPT: " + gptResp)

    output_text.delete("1.0", "end")  # Clear the existing text in the output text box
    output_text.insert("1.0", gptResp)  # Display the string



# Create the main application window
app = tk.Tk()
app.title("Input and Output Text Boxes")

# Create the input text box
input_text = tk.Text(app, height=20, width=100)
input_text.pack()

# Create the output text box
output_text = tk.Text(app, height=20, width=100)
output_text.pack()

# Create a button to process the input
process_button = tk.Button(app, text="Process Input", command=process_input)
process_button.pack()

# Start the Tkinter main loop
app.mainloop()