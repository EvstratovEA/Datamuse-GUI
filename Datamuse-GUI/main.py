# import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import connection_to_wordbase
from write_to_file_new import write_to_file
from update_content_table import update_content_table
# import requests

window = Tk()
window.title("Datamuse")
window.geometry("800x600")

options_input = Frame(window)  # Окно/рамка для выбора фунцкии и ввода слов
words_board = Frame(window)  # Для окна с выводом списка слов
buttons_element = Frame(window)  # Для кпопок

'''Секция выбора функции'''
options_input.configure()
selected_opt_main = StringVar()
selected_opt_hint = StringVar()
choose_option = Combobox(options_input, values=list(connection_to_wordbase.constraint_dict.keys()), state='readonly', textvariable=selected_opt_main)  # Выбор опции для работы со словом
choose_option.bind('<<ComboboxSelected>>', lambda event: label_selected.configure(text=connection_to_wordbase.constraint_dict[selected_opt_main.get()]))

label_selected = Label(options_input, text="Not Selected")
label_selected.grid(row=0, column=2)

choose_option.current(0)
choose_option.grid(column=0, row=0)
hint = Combobox(options_input, values=list(connection_to_wordbase.optional_hint.keys()), state='readonly', textvariable=selected_opt_hint)  # Выбор опции подсказки
hint.bind('<<ComboboxSelected>>', lambda event: label_selected_hint.configure(text=connection_to_wordbase.optional_hint[selected_opt_hint.get()]))
hint.grid(column=0, row=1)
label_selected_hint = Label(options_input, text="Not Selected topics")
hint.current(0)
label_selected_hint.grid(row=1, column=2)

'''Секция ввода основного и дополнительно слов'''
main_word_input_strvar = StringVar()
main_word_input = Entry(options_input, width=20, textvariable=main_word_input_strvar)  # , state = "disable") # Поле ввода слова
main_word_input.grid(column=1, row=0)
hint_input_strvar = StringVar()
hint_input = Entry(options_input, width=20, textvariable= hint_input_strvar)  # Выбор доп.опции/подсказки main_word_input
hint_input.grid(column=1, row=1)

options_input.pack()  # Запаковка блока слов

# main_word_input.focus()

# def search_word():
#     words_list = requests.get("https://api.datamuse.com/words?ml=box&topics=crate").json()
#     words_list_full = []
#     for info in words_list:
#         words_list_full.append(info)
#         list_of_words.insert(INSERT, str(info) + '\n')
#         # print(info)
#
# def search_word_2():
#     words_list = requests.get("https://api.datamuse.com/words?ml=box&topics=grave").json()
#     words_list_full = []
#     for info in words_list:
#         words_list_full.append(info)
#         list_of_words.insert(INSERT, str(info) + '\n')

list_of_words = scrolledtext.ScrolledText(words_board)
# search_word()
list_of_words.configure ()# (state="disable")
list_of_words.pack()  # Запаковка блока списка слов

# params = connection_to_wordbase.search_word(connection_to_wordbase.constraint_dict[selected_opt_main.get()], main_word_input_strvar.get(), connection_to_wordbase.optional_hint[selected_opt_hint.get()], hint_input_strvar.get())
# print(params)
def to_button():
    list_of_words.delete(1.0, constants.END)
    for info in connection_to_wordbase.search_word(connection_to_wordbase.constraint_dict[selected_opt_main.get()], main_word_input_strvar.get(), connection_to_wordbase.optional_hint[selected_opt_hint.get()], hint_input_strvar.get()):
        list_of_words.insert(constants.INSERT, str(info) + '\n')

def to_write():
    write_to_file(connection_to_wordbase.search_word(connection_to_wordbase.constraint_dict[selected_opt_main.get()],
                                                     main_word_input_strvar.get(),
                                                     connection_to_wordbase.optional_hint[selected_opt_hint.get()],
                                                     hint_input_strvar.get()), main_word_input_strvar.get())

def to_update():
    update_content_table()

# print(main_word_input)
words_board.pack(expand=True)

# from tkinter import messagebox
# def worked():
#     messagebox.showinfo('Поиск/Запись работают', 'Поиск/Запись работают')

'''Секция кнопок'''
search_button = Button(buttons_element, text="Поиск")
search_button['command'] = to_button
search_button.grid(column=0, row=0)
write_button = Button(buttons_element, text="Запись") # , command=search_word_2)
write_button.grid(column=1, row=0)
write_button['command'] = to_write
update_button = Button(buttons_element, text='Обновить реестр слов')
update_button['command'] = to_update
update_button.grid(column=2, row=0)

buttons_element.pack()  # Запаковка блока кнопок


# print(os.getcwd())
window.mainloop()
