"""
theLottery.py

Lottery Number Generator
Create a Python GUI-based application that acts as a lottery number generator.
This app should contain a title WITHIN the GUI which reads "Lottery Number Generator" or SOMETHING of that sort.
You will need components for the winning numbers to be placed once the function that generates them is triggered.  You will also of course need a command button to trigger the function that generates and displays the numbers.
Base the numbers on the NY PowerBall lottery which is FIVE individual numbers with the range from 1 to 69. And then a PowerBall number which is only from 1 to 26.  Each click of the command button should generate a new series of numbers.

Mike Norrito 
5/1/2020
"""
from breezypythongui import EasyFrame 
import random


class TheLottery(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title = "Mushroom Kingdom PowerUp Lottery", width = 424, height = 234, background = "royalblue" )
		self.power = self.addLabel(text = "PowerUp! Mushroom Kingdom Lottery", row = 0, column = 0, columnspan = 1, background = 'red', sticky = "NEWS", foreground = "white")
		self.dothis = self.addLabel(text = "Welcome to the Mushroom Kingdom Lottery!\n To get a Jackpot, you MUST match ALL 6 numbers to the Winning numbers!\n Click below to spend gold coins to generate your ticket!:", row = 1, column = 0, foreground = "goldenrod", background = "royalblue")
		self.outputLabel = self.addLabel(text = "", row = 2, column = 0, background = "royalblue", foreground = "white", sticky = "NEWS")
		self.comOutput = self.addLabel(text = "", row = 3, column = 0, foreground = "red", background = "black", sticky = "S")
		self.WinLoose = self.addLabel(text = "", row = 5, column = 0, foreground = "white", background = "red", sticky = "NEWS")
		self.spendCoins = self.addButton(text = "Spend 200 Gold Coins", row = 4, column = 0, command = self.spendCoins)
		
		self.spendCoins["bg"] = "goldenrod"

	def spendCoins(self):
		""" generates user lottery numbers AND display winning numbers """
		
		#User
		num1 = random.randint(1,69)
		num2 = random.randint(1,69)
		num3 = random.randint(1,69)
		num4 = random.randint(1,69)
		num5 = random.randint(1,69)
		powerUP = random.randint(1,26)
		self.outputLabel["text"] = "Your Numbers:", num1, num2, num3 , num4, num5, powerUP
		#ComLotto
		num1c = random.randint(1,69)
		num2c = random.randint(1,69)
		num3c = random.randint(1,69)
		num4c = random.randint(1,69)
		num5c = random.randint(1,69)
		powerUPc = random.randint(1,26)
		self.comOutput["text"] = "Winning Numbers:", num1c, num2c, num3c , num4c, num5c, powerUPc

			
		if num1 == num1c and num2 == num2c and num3 == num3c and num4 == num4c and num5 == num5c and powerUP == powerUPc:
				
			self.WinLoose["text"] = "POWERUP JACKPOT!!!\n YOU STOLE ALL OF BOWSERS GOLD COINS!!!\n 20000000000 GOLD COINS!!!"
			self.outputLabel["fg"] = "goldenrod"
			self.WinLoose["fg"] = "white"
			self.comOutput["fg"] = "lightgreen"

		

		else:
			self.WinLoose["text"] = "LOSERRRRRRRR You died trying to defeat Bowser!"
			self.outputLabel["fg"] = "white"
			self.comOutput["fg"] = "red"
		





#goldenrod



def main():
	TheLottery().mainloop()


main()