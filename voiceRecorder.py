import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory

folder = ""

def file_folder():
    global folder
    folder = askdirectory()
    print(folder)

def save_file():
    global folder

    try:
        time = int(timeInbox.get())
        file_name = input("Enter file name: ")
        file_path = (f"{folder}/{file_name}.wav")
        showinfo(title="Start", message="Start Recording")
        Record = sounddevice.rec((time * 44100), samplerate=44100, channels=2)
        sounddevice.wait()
        write(file_path, 44100, Record)
        showinfo(title="end", message="Recording Completed")

    except:
        showwarning(title="timeError", message="Invalid time format. Please enter time in seconds.")

def mainInterface():
    global timeInbox

    interface = Tk()
    interface.geometry("350x500")
    interface.resizable(False, False)
    interface.title("Bidisha's Voice Recorder")
    interface.config(bg="grey")
    
    signalImg = PhotoImage(file="signal.png")
    label1 = Label(interface, image=signalImg, bg="grey")
    label1.place(x=78, y=430, height=80, width=200)

    timeInbox = Entry(interface, font=(20))
    timeInbox.place(x=125, y=300, height=50, width=100)

    label2 = Label(interface, text="Enter time (in Sec) :", font=("Time New Roman", 12), bg="grey")
    label2.place(x=105, y=270)

    location = Button(interface, text="Select Folder", font=("Time New Roman", 12), command=file_folder)
    location.place(x=75, y=370, height=40, width=200)

    micImg = PhotoImage(file="mic.png")
    startButton = Button(interface, image=micImg, command=save_file)
    startButton.place(x=80 ,y=50)

    interface.mainloop()
    
mainInterface()