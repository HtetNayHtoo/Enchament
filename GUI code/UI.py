import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound


def text_to_speech(a, b, c):
    try:

        tts = gTTS(text=a, lang=b, slow=c)
        tts.save('yel.mp3')
        playsound('yel.mp3')
        os.remove("yel.mp3")
        print("deleted")
        exit()

    except:
        print("nothing")

class NewprojectApp:
    def __init__(self, master=None):
        # build ui

        frame_1 = ttk.Frame(master)
        entry_1 = ttk.Entry(frame_1)
        entry_1.config(cursor='xterm', exportselection='true', font='TkTextFont', justify='left')
        entry_1.config(state='normal', takefocus=True)
        _text_ = '''Hello'''
        entry_1.delete('0', 'end')
        entry_1.insert('0', _text_)
        entry_1.place(anchor='nw', height='50', relx='0.29', rely='0.37', width='150', x='0', y='0')
        label_1 = ttk.Label(frame_1)
        label_1.config(anchor='w', compound='top', cursor='arrow', font='TkDefaultFont')
        label_1.config(takefocus=False, text='Enter Text')
        label_1.place(anchor='nw', relx='0.06', rely='0.37', x='0', y='0')
        button_1 = ttk.Button(frame_1)
        button_1.config(text='Text To Speech')
        button_1.place(anchor='nw', height='50', relx='0.29', rely='0.64', width='100', x='0', y='0')
        button_1.configure(command=lambda: text_to_speech(entry_1.get(), combobox_1.get(), combobox_2.get()))
        label_2 = ttk.Label(frame_1)
        label_2.config(text='Speed')
        label_2.place(anchor='nw', relx='0.06', rely='0.21', x='0', y='0')
        combobox_1 = ttk.Combobox(frame_1)
        combobox_1.config(values=["en-uk", "en-us", "ja", "fr", "my", "zh-cn", "zh-tw"])
        combobox_1.place(anchor='nw', relx='0.29', rely='0.21', x='0', y='0')
        combobox_1.current(0)
        label_1_2 = tk.Label(frame_1)
        label_1_2.config(text='Speed')
        label_1_2.place(anchor='nw', relx='0.62', rely='0.21', x='0', y='0')
        combobox_2 = ttk.Combobox(frame_1)
        combobox_2.config(values=["True", "False"])
        combobox_2.place(anchor='nw', relx='0.7', rely='0.21', width='70', x='0', y='0')
        combobox_2.current(1)
        button_2 = ttk.Button(frame_1)
        button_2.config(text='About')
        button_2.place(anchor='nw', height='50', relx='0.67', rely='0.64', width='100', x='0', y='0')
        button_2.configure(command=self.on_button1_clicked)
        frame_1.config(cursor='arrow', height='300', takefocus=False, width='500')
        frame_1.pack(fill='both', side='top')

        # Main widget
        self.mainwindow = frame_1