import tkinter as tk

# ----------------- SETTINGS ----------------- #
COUNTDOWN_TIME = 10  # seconds

# ----------------- APP ----------------- #
class BombApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bomb Timer")
        self.root.geometry("500x500")
        self.root.configure(bg="white")

        # Label
        self.label = tk.Label(root, text="You know what time it is", font=("Arial", 20, "bold"), bg="white")
        self.label.pack(pady=20)

        # Bomb Image (GIF or PNG supported by Tkinter)
        self.bomb_photo = tk.PhotoImage(file="bomb.png")   # <-- put a bomb.png file in same folder
        self.image_label = tk.Label(root, image=self.bomb_photo, bg="white")
        self.image_label.pack(expand=True)

        # Timer Label
        self.timer_label = tk.Label(root, text=str(COUNTDOWN_TIME), font=("Arial", 24, "bold"), bg="white")
        self.timer_label.pack(pady=10)

        self.time_left = COUNTDOWN_TIME
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=str(self.time_left))
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.boom()

    def boom(self):
        # Change label
        self.label.config(text="💥 It's BOOM time! 💥", fg="red", bg="black")

        # Change background to fire
        self.fire_photo = tk.PhotoImage(file="fire.png")  # <-- put fire.png in same folder
        self.image_label.config(image=self.fire_photo, bg="black")
        self.image_label.image = self.fire_photo  # keep reference


# ----------------- RUN ----------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = BombApp(root)
    root.mainloop()
