# import tkinter
#
# window = tkinter.Tk()
# window.title("MY First GUI Program")
# window.minsize(width=500, height=300)
#
# #LABEL
#
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
#
# window.mainloop()

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3, multiply=5)

