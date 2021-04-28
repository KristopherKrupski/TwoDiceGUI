from breezypythongui import EasyFrame
import random
from playsound import playsound

# Requires a PIP install of playsound and the breezypythongui.py file found in this projects folder


class TwoDice(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Two Dice", background="#33c43a", width=225, height=200, resizable=False)
        self.addLabel(text="Two Dice", row=0, column=0, sticky="NSEW", background="#33c43a", foreground="white",
                      columnspan=2).config(font=("Helvetica", 20, "bold"))

        self.addLabel(text="Player roll: ", sticky="E", row=1, column=0, background="#33c43a").config(font=("helvetica", 16))
        self.user_roll = self.addLabel(text="", row=1, column=1, sticky="W", background="#33c43a")
        self.user_roll.config(font=("helvetica", 16))

        self.addLabel(text="Dealer roll: ", sticky="E", row=2, column=0, background="#33c43a").config(font=("helvetica", 16))
        self.dealer_roll = self.addLabel(text="", row=2, column=1, sticky="W", background="#33c43a")
        self.dealer_roll.config(font=("helvetica", 16))

        self.button = self.addButton(text="Roll", row=3, column=0, command=self.roll, columnspan=2)
        self.button.grid(sticky="NSEW")
        self.button.config(width=10)
        self.result = self.addTextField(text="", row=4, column=0, columnspan=2, sticky="NSEW")
        self.result.config(justify="center", font=("helvetica", 16))
        self.result["background"] = "#33c43a"

    def roll(self):
        playsound("diceroll.mp3")
        self.button["state"] = "disabled"
        user_num = random.randint(1, 6)
        dealer_num = random.randint(1, 6)
        if user_num > dealer_num:
            self.user_roll["background"] = "green"
            self.user_roll["foreground"] = "white"
            self.dealer_roll["background"] = "red"
            self.dealer_roll["foreground"] = "black"
            self.result["background"] = "green"
            self.result["foreground"] = "white"
            self.result.setText("Player Win!")
            playsound("WinSound.wav", False)
            self.button.after(200, self.enable)
        elif user_num < dealer_num:
            self.user_roll["background"] = "red"
            self.user_roll["foreground"] = "black"
            self.dealer_roll["background"] = "green"
            self.dealer_roll["foreground"] = "white"
            self.result["background"] = "red"
            self.result["foreground"] = "black"
            self.result.setText("Dealer Win!")
            playsound("LoseSound.mp3", False)
            self.button.after(3800, self.enable)
        else:
            self.result.setText("Push!")
            self.result["background"] = "white"
            self.result["foreground"] = "black"
            self.user_roll["background"] = "white"
            self.user_roll["foreground"] = "black"
            self.dealer_roll["background"] = "white"
            self.dealer_roll["foreground"] = "black"
            playsound("DrawSound.mp3", False)
            self.button.after(2000, self.enable)
        self.user_roll["text"] = (str(user_num))
        self.dealer_roll["text"] = (str(dealer_num))

    def enable(self):
        self.button["state"] = "normal"


def main():
    TwoDice().mainloop()


if __name__ == "__main__":
    main()
