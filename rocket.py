import time
from tkinter import *
from tkinter import messagebox
import webbrowser

 
 
# creating Tk window
root = Tk()
  
# setting geometry of tk window
root.geometry("300x250")
  
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Rocket Launch Countdown")
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")
  
# Use of Entry class to take input from the user
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=100,y=70)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=150,y=70)
  
def play_video(url):
    webbrowser.open(url)
  
def countdown():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Enter valid value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            launch_rocket()
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
 # ====================== DO NOT EDIT THE CODE ABOVE ===========================

def launch_rocket():
    #Show a pop up with a launch message
   
    #use the play_video function to play a video of a rocket launching
   
    pass

# ====================== DO NOT EDIT THE CODE BELOW ===========================

if __name__ == '__main__':

    # button widget
    btn = Button(root, text='Start Countdown', bd='5',command= countdown)
    btn.place(x = 70,y = 120)

    root.mainloop()