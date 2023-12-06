import requests
import json
from tkinter import *

window = Tk()
window.title("практика 12")
window.geometry("500x400")


def get_data():
    name = name_rep.get()
    user_data = requests.get(f'https://api.github.com/users/{name}').json()
    json_string = json.dumps(user_data).split(', ')
    list_of_data = []
    for i in json_string:
        if (
            i.startswith('"company": ') or i.startswith('"created_at": ') or
            i.startswith('"email": ') or i.startswith('"id":') or
            i.startswith('"name": ') or i.startswith('"url": ')
        ):
            list_of_data.append(i)
    with open('result_app.json', 'w') as file:
        json.dump(list_of_data, file, indent=4)
    notification = Label(text='результат записан в файл "result_app"')
    notification.pack()

lbl = Label(text='введите название репозитория')
lbl.pack(pady=10)

name_rep = Entry(window, width=40)
name_rep.pack()
name_rep.focus()

button = Button(window, text='результат', command=get_data)
button.pack(pady=10)

window.mainloop()
