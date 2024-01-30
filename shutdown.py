# Description:  Do a delayed shutdown + kill/start Windows Explorer
# Dependencies: click
# OS: Windows

import subprocess
import tkinter as tk

from click import command

ver = '1.21'
rel = '18-05-2023'

def shutdown(delay):
    command = 'shutdown -s -t ' + str(delay)
    proc = subprocess.Popen(command)

def killprocess(process):
    command = 'Taskkill /IM ' + process + ' /F'
    proc = subprocess.Popen(command)

def startprocess(process):
    proc = subprocess.Popen(process)
    
def abort():
    proc = subprocess.Popen('shutdown -a')

def init_gui():
    gui = tk.Tk()
    gui.geometry('240x195')
    gui.title('Shutdown ' + ver)

    frame = tk.Frame(gui)
    frame.pack(side='top')

    button_shutdown_1 = tk.Button(frame, width=30, text='Shutdown in 1 Minute', command=lambda:shutdown(60))
    button_shutdown_2 = tk.Button(frame, width=30, text='Shutdown in 3 Minutes', command=lambda:shutdown(180))
    button_shutdown_3 = tk.Button(frame, width=30, text='Shutdown in 5 Minutes', command=lambda:shutdown(300))
    button_killprocess = tk.Button(frame, width=30, bg='blue', fg='white', text='Kill Windows Explorer', command=lambda:killprocess('explorer.exe'))
    button_startprocess = tk.Button(frame, width=30, bg='blue', fg='white', text='Start Windows Explorer', command=lambda:startprocess('explorer.exe'))
    button_abort = tk.Button(frame, width=30, bg='red', fg='white', text='Abort Shutdown', command=abort)

    button_shutdown_1.grid(row=0, column=0, pady=3)
    button_shutdown_2.grid(row=1, column=0, pady=3)
    button_shutdown_3.grid(row=2, column=0, pady=3)
    button_killprocess.grid(row=3, column=0, pady=3)
    button_startprocess.grid(row=4, column=0, pady=3)
    button_abort.grid(row=5, column=0, pady=3)

    gui.mainloop()

init_gui()