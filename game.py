from Project import *

window = Tk()
window.title("Turtle Game")
window.geometry("800x400")
window.config(bg="forestgreen")

Label(window, text="The Turtle Game", fg="white", bg="forestgreen", font=("century", 40)).pack(pady=(0, 60))

Button(window, text="Enter the Game", fg="forestgreen", bg="lightgreen", font=("century", 20), command=startgame).pack(ipadx=150, ipady=10)

window.mainloop()