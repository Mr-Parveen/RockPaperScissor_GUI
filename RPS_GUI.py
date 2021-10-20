from random import randint
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("ROCK PAPER SCISSOR")
window.geometry("1300x580")
window.maxsize(1300,580)
window.minsize(1300,580)

window.configure(background="#E400B4")  # #E400B4  == this is for the purple color


# Pictures
rock_img = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor.png"))
rock_img_com = ImageTk.PhotoImage(Image.open("Rock-com.png"))
paper_img_com = ImageTk.PhotoImage(Image.open("Paper-com.png"))
scissor_img_com = ImageTk.PhotoImage(Image.open("Scissor-com.png"))

# insert picture
player_lable = Label(window, image=rock_img, bg="#E400B4")
computer_lable = Label(window, image=rock_img_com, bg="#E400B4")
player_lable.grid(row=1, column=0)
computer_lable.grid(row=1, column=4)

# scores
playerScore = Label(window, text=0, font="airal 25 bold", bg="#E400B4", fg="white")
computerScore = Label(window, text=0, font="airal 25 bold", bg="#E400B4", fg="white")
playerScore.grid(row=1, column=1)
computerScore.grid(row=1, column=3)

# indicator
playerIndicator = Label(window, font="airal 15 bold", text="PLAYER", bg="#E400B4", fg="white")
computerIndicator = Label(window, font="airal 15 bold", text="COMPUTER", bg="#E400B4", fg="white")
playerIndicator.grid(row=0, column=1)
computerIndicator.grid(row=0, column=3)

# message
msg = Label(window, font="airal 15 bold", bg="#E400B4", fg="white")  # text="You Lose!")
msg.grid(row=3, column=2)

# updatemessage
def updateMessage(x):
    msg['text'] = x

# updateplayer score
def updatePlayerScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# updatecomputer score
def updateComputerScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner
def checkWin(player,computer):
    if player== computer:
        updateMessage("It's a TIE!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win")
            updatePlayerScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win")
            updatePlayerScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You WIN")
            updatePlayerScore()
    else:
        pass

# updatechoices
comChoice= ["rock","paper","scissor"]
def updateChoice(x):
    # computer
    comRandChoice= comChoice[randint(0,2)]
    if comRandChoice == "rock":
        computer_lable.configure(image=rock_img_com)
    elif comRandChoice == "paper":
        computer_lable.configure(image=paper_img_com)
    else:
        computer_lable.configure(image=scissor_img_com)

    # player
    if x == "rock":
        player_lable.configure(image=rock_img)
    elif x == "paper":
        player_lable.configure(image=paper_img)
    else:
        player_lable.configure(image=scissor_img)

    checkWin(x,comRandChoice)

# button
rock_btn = Button(window, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command= lambda:updateChoice("rock"))
paper_btn = Button(window, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command= lambda:updateChoice("paper"))
scissor_btn = Button(window, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command= lambda:updateChoice("scissor"))
rock_btn.grid(row=2, column=1)
paper_btn.grid(row=2, column=2)
scissor_btn.grid(row=2, column=3)

window.mainloop()
