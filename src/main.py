import json
import ollama
import tkinter as tk
from tkinter import ttk, scrolledtext


def load_conversation_data():
    with open('./assets/conversation.json') as f:
        data = json.load(f)
        def extraction(x): return f"{x['speaker']}: {x['text']}"
        conversation = list(map(extraction, data))
        conversation_string = "\n".join(conversation)
    return conversation_string

def submit():
    user = user_choice.get()
    message = message_entry.get()
    conversation = f"{user}: {message}\n"
    conversation_text.insert(tk.END, conversation)
    print(f"{user}: {message}")
    conversation_json = {"speaker": user, "text": message}
    
    # Append the conversation to the JSON file
    with open('./assets/conversation.json', 'r+') as file:
        data = json.load(file)
        data.append(conversation_json)
        file.seek(0)
        json.dump(data, file)

def generate_summary():
    conversation_string = load_conversation_data()
    response = ollama.chat(model='gemma:2b', messages=[
        {
            'role': 'system',
            'content': 'Your goal is to summarize the text that is given to you in roughly 300 words. It is from a meeting between one or more people. Only output the summary without any additional text. Focus on providing a summary in freeform text with a summary of what people said and the action items coming out of it.'
        },
        {
            'role': 'user',
            'content': conversation_string,
        },
    ])
    summary = response['message']['content']
    summary_text.insert(tk.END, summary)
    print(summary)

root = tk.Tk()

# Set window size
root.geometry("600x400")

# Set window title
root.title("Ollama-Gemma-Summarizer")

# Create a label for the user selection
user_label = tk.Label(root, text="User :")
user_label.grid(column=0, row=0, padx=10, pady=10)

# Create a label for the user selection
user_label = tk.Label(root, text="Message :")
user_label.grid(column=0, row=1, padx=10, pady=10)

# Create a dropdown menu for user selection
user_choice = tk.StringVar()
user_dropdown = ttk.Combobox(root, textvariable=user_choice)
user_dropdown['values'] = ('Dhruti', 'Singam', 'Anshuprem', 'Subham')
user_dropdown.grid(column=1, row=0, padx=0, pady=0)

# Create a text entry field for the message
message_entry = tk.Entry(root, width=40)
message_entry.grid(column=1, row=1, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(column=0, row=2, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Generate Summary", command=generate_summary)
submit_button.grid(column=1, row=2, padx=10, pady=10)

# Create a text box for the conversation
conversation_text = scrolledtext.ScrolledText(root, width=30, height=15)
conversation_text.grid(column=0, row=3, padx=20, pady=10)

# Create a text box for the conversation
summary_text = scrolledtext.ScrolledText(root, width=30, height=15)
summary_text.grid(column=1, row=3, padx=20, pady=10)

root.mainloop()
