from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry('600x250')
window.title('Igbo Dictionary')

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

igbo_dict = {'Kedu': 'Hello',
             'Biko': 'Please',
             'Agu': 'Lion',
             'Nne': 'Mother',
             'Bia': 'Come',
             'Nwanne': 'Sister',
             'Dalu': 'Goodbye',
             'Ndewo': 'Welcoome',
             'Ego': 'Money',
             'Ehi':'Cow',
             'Nna': 'Father',
             'Egusi': 'Melon seed',
             'Ji': 'Yam',
             'Nkita': 'Dog',
             'Udo': 'Peace',
             'Ozo': 'Respect',
             'Ulo': 'House',
             'Di': 'Husband',
             'Okuko': 'Chicken',
             'Akara':'Bean cake'
             }

def search(word):
    if word in igbo_dict:
        result.set(igbo_dict[word])
        print(igbo_dict[word])
    else:
        result.set('invalid')
        print('invalid')

search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()
