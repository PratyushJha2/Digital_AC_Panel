import tkinter as tk
from tkmacosx import Button
import tkmacosx as tkm
import pygame

pygame.mixer.init()

audioPlaying = False
currentVol = .5

def start_ac():
    global audioPlaying
    if not audioPlaying:
        pygame.mixer.music.load('ac_1.mp3')
        pygame.mixer.music.set_volume(currentVol)
        pygame.mixer.music.play()
        audioPlaying=True
    else:
        pygame.mixer_music.fadeout(1000)
        audioPlaying=False

def volIncr():
    global currentVol
    currentVol=min(currentVol+0.1,3)
    if audioPlaying:
        pygame.mixer.music.set_volume(currentVol)

def volDecr():
    global currentVol
    currentVol=max(currentVol-.1,0)
    if audioPlaying:
        pygame.mixer.music.set_volume(currentVol)

def closure():
    pygame.mixer.music.stop()
    window.destroy()

def powerclick():
    start_ac()


window = tk.Tk()
window.geometry("500x600")
window.config(bg="#0000FF")
window.title("ACU Control")

label = tk.Label(text="ACU CONTROL", font=("IrisUPC", 17, "bold"), foreground="#FFFFFF", background="#696563", width=1000, height=4)
label.pack()

powerButton = tkm.Button(window, text="⚡", font=('Arial',26,'bold'),width=70, height=63,bg='#f5a700',borderless=1, relief=tk.GROOVE)
powerButton.place(x=220,y=300)
powerButton.config(command=powerclick)

ifsButton = tkm.Button(window, text="✇✇✇",font=('Helventica',26),width=70,height=63,bg='#898380',borderless=1)
ifsButton.place(x=310,y=300)
ifsButton.config(command=volIncr)


dfsButton = tkm.Button(window, text="✇",font=('Arial',26),width=70,height=63,bg='#898380',borderless=1)
dfsButton.place(x=125,y=300)
dfsButton.config(command = volDecr)

def sliderChange(val):
    temp = int(val)
    update_temp(temp)

def update_temp(temp):
    
    blue_value = max(0, min(255, int((temp - 30) * 6)))  # Adjusted calculation
    color = f'#{18:02X}{blue_value:02X}{208:02x}'  # Keep red and green components fixed
    window.config(bg=color)
    tempLabel.config(text=f"Temperature: {temp}°F")


tempSlider = tk.Scale(window, from_=30,to=70, orient=tk.HORIZONTAL,length=300,command=sliderChange)
tempSlider.place(x=107,y=500)

tempLabel = tk.Label(window, text="Temperature: ",font=("Helvetica",12))
tempLabel.pack()



 






window.mainloop()