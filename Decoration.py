import tkinter as tk

def on_enter(e):
    e.widget['background'] = 'green'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'