from tkinter import *
from tkinter import ttk
from tkinter import Menu


#  окно

window = Tk()
window.title("Добро пожаловать в приложение БДН")
window.geometry("500x500")


#  вкладки

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

style = ttk.Style(window)
style.configure('TNotebook.Tab', width=window.winfo_screenwidth())

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

tab1.pack(fill=NONE, expand=True)
tab2.pack(fill=BOTH, expand=True)
tab3.pack(fill=BOTH, expand=True)

notebook.add(tab1, text='калькулятор')
notebook.add(tab2, text="чекбоксы", )
notebook.add(tab3, text="текст")


#  калькулятор

def calculate():
    number1 = int(num1.get())
    number2 = int(num2.get())
    operation = combobox.get()
    if operation == '+':
        result = number1 + number2
        label = Label(tab1, text=result)
        label.grid(row=3, column=2)
    elif operation == '-':
        result = number1 - number2
        label = Label(tab1, text=result)
        label.grid(row=3, column=2)
    elif operation == '*':
        result = number1 * number2
        label = Label(tab1, text=result)
        label.grid(row=3, column=2)
    elif operation == '/':
        if number2 == 0:
            label = Label(tab1, text='деление на 0')
            label.grid(row=3, column=2)
        else:
            result = number1 - number2
            label = Label(tab1, text=result)
            label.grid(row=3, column=2)
    else:
        label = Label(tab1, text='это не сработает')
        label.grid(row=3, column=2)


num1 = Entry(tab1)
num1.grid(row=0, column=1)

num2 = Entry(tab1)
num2.grid(row=0, column=3)

operations = ['+', '-', '*', '/']
combobox = ttk.Combobox(tab1, values=operations)
combobox.grid(row=0, column=2)

button = Button(tab1, text='=', command=calculate)
button.grid(row=2, column=2)


# чекбоксы

def clicked():
    if selected.get() == 1:
        lbl.configure(text='Вы выбрали первый вариант')
    elif selected.get() == 2:
        lbl.configure(text='Вы выбрали второй вариант')
    else:
        lbl.configure(text='Вы выбрали третий вариант')


selected = IntVar()
btn = Button(tab2, text="выбор", command=clicked)
lbl = Label(tab2)

rad1 = Radiobutton(tab2, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(tab2, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(tab2, text='Третий', value=3, variable=selected)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=1)


# текст

def text():
    txt = open('текст0.txt', encoding="utf-8")
    lbl1 = Label(tab3, text=txt.read())
    lbl1.grid(column=0, row=2)


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='вывести', command=text)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)

task = Label(tab3, text='выведите текст с помощью меню - файл')
task.grid(row=1, column=0)

window.mainloop()
