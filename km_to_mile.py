from tkinter import *

window = Tk()
window.title("MY First GUI Program")
window.minsize(width=500, height=300)

#LABEL

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#Button

def button_clicked():
    global my_label
    my_label.config(text=input.get(), font=("Arial", 24, "bold"))

button = Button(text = "Click Me", command = button_clicked)
button.pack()


#Entry

input = Entry(width=10)
input.pack()
print(input.get())







window.mainloop()



