import tkinter as tk

screen = tk.Tk()
screen.geometry("500x500")
screen.title("YORUBA DICTION")
window = tk.Tk()
window.geometry("600x400")
window.title("YORUBA DICTIONARY")

entry_text = tk.Entry(screen)
entry_text = tk.Entry(window)
entry_text.pack()

outcome = tk.StringVar()
outcome_label = tk.Label(screen,textvariable=outcome)
outcome_label.pack()
result = tk.StringVar()
result_label = tk.Label(window,textvariable=result)
result_label.pack()
yoruba_dictionary = {
    "God":'Oluwa',
    "Rest":'Simi',
    "Enjoyment":'igbadun',
    "Obirin":'woman',
    "woman":'Obirin',
    "Come":'Wa',
    "Child":'Omo',
    "Man":'Okurin',
    "Cap":'Fila',
    "House":'Ile',
    "Beans":'Ewa',
    "Friend":'Ore',
    "Festival":'Odun',
    "Crown":'Ade',
    "Clock":'Ago',
}

def check(word):
    if word in yoruba_dictionary:
        yoruba_dictionary.set(yoruba_dictionary[word])
        print(yoruba_dictionary[word])

    else:
        yoruba_dictionary.set("Not found")
        print("Not found")

search_btn = tk.Button(screen, text="Yoruba", command = lambda: check(entry_text.get()))
search_btn = tk.Button(window, text="Yoruba", command = lambda: check(entry_text.get()))
search_btn.pack()


screen.mainloop()
window.mainloop()