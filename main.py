from tkinter import *
import pandas
import random
import math
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0)
img_title = PhotoImage(file="images/card_front.png")
img2_title = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=img_title)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)

data_dict = {
    "French": [],
    "English": []
}
to_learn = {}

try:
    diction = pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_diction = pandas.read_csv("data/french_words.csv")
    to_learn = original_diction.to_dict(orient="records")
else:
    to_learn = diction.to_dict(orient="records")
# words = diction.French.to_list()
# eng_words = diction.English.to_list()
# for i in range(len(words)):
#     data_dict["French"].append(words[i])
#     data_dict["English"].append(eng_words[i])

def counter(count = 3):
    global timer
    window.after_cancel(timer)
    count_sec = count % 60
    if count > 0:
        timer = window.after(3000, counter, count - 1)

        print(count_sec)
    else:
        canvas.create_image(400, 263, image=img2_title)
        canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), fill="white")
        canvas.create_text(400, 263, text=f"{b}", font=("Ariel", 50, "bold"), fill="white")

def is_known():
    to_learn.remove(ran)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)

    randomize()


def randomize():
    canvas.create_image(400, 263, image=img_title)
    title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
    global ran
    ran = random.choice(to_learn)
    global a
    a = ran["French"]
    global b
    b = ran["English"]
    canvas.itemconfig(title, text= "French")
    canvas.itemconfig(word, text=f"{a}")
    counter(count=3)

    # canvas.itemconfig(title, text="English")
    # canvas.itemconfig(word, text=f"{b}")


my_correct = PhotoImage(file="images/right.png")
right_button = Button(image=my_correct, highlightthickness=0,bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1,row=1)
my_wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_wrong, highlightthickness=0,bg=BACKGROUND_COLOR, command=randomize)
wrong_button.grid(column=0,row=1)
timer = window.after(3000, counter)


randomize()

window.mainloop()





