import tkinter as tk

# Create the main window
screen = tk.Tk()
screen.geometry("500x500")
screen.title("FRENCH DICTIONARY")

# Entry widget
entry_text = tk.Entry(screen)
entry_text.pack()

# StringVar for the output
outcome = tk.StringVar()
outcome_label = tk.Label(screen, textvariable=outcome)
outcome_label.pack()

# FRENCH dictionary
FRENCH_dictionary = {
    "HELLO": 'BONJOR',
    "THANK YOU": 'MERCI',
    "APPLE": 'POMME',
    "CAT": 'CHAT',
    "LOVE": 'AMOUR',
    "HOUSE": 'MAISON',
    "WATER": 'EAU',
    "BOOK": 'LIVRE',
    "DOG": 'CHIEN',
    "ECOLE": 'SCHOOL',
    "FLOWER": 'FLEUR',
    "LIGHT": 'LUMIERE',
    "CIEL": 'SKY',
    "SUN": 'SOLERIL',
    "BLACK": 'NOIR',
    "WHITE": 'BLANC',
    "RED":'ROUGE',
    "TIME":'TEMPS',
    "LIFE":'VIE',
    "FOREST":'FORET'
}

# Function to check the dictionary
def check(word):
    if word in FRENCH_dictionary:
        outcome.set(FRENCH_dictionary[word])
    else:
        outcome.set("Not found")

# Button to search
search_btn = tk.Button(screen, text="Translate to FRENCH", command=lambda: check(entry_text.get()))
search_btn.pack()

# Start the application
screen.mainloop()







