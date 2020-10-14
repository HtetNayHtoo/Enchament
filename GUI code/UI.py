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