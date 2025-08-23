from tkinter import *

window = Tk()
window.title("MY First GUI Program")
window.minsize(width=500, height=300)

#LABEL

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    global my_label
    my_label.config(text="I got clicked", font=("Arial", 24, "bold"))

button = Button(text = "Click Me", command = button_clicked)
button.pack()







window.mainloop()



