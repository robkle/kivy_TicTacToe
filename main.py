import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from math import inf
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

Builder.load_file('TttApp.kv')

class TttLayout(BoxLayout):
	tic = NumericProperty(1)
	symbol = StringProperty('')
	tictactoe = ObjectProperty([inf for i in range(9)])
	
	def selectCell(self):
		if self.tic:
			self.tic = 0
		else:
			self.tic = 1
	
	def symbolCell(self):
		if self.tic:
			self.symbol = 'O'
		else:
			self.symbol = 'X'

	def win(self):
		row1 = self.tictactoe[0] + self.tictactoe[1] + self.tictactoe[2]
		row2 = self.tictactoe[3] + self.tictactoe[4] + self.tictactoe[5]
		row3 = self.tictactoe[6] + self.tictactoe[7] + self.tictactoe[8]
		col1 = self.tictactoe[0] + self.tictactoe[3] + self.tictactoe[6]
		col2 = self.tictactoe[1] + self.tictactoe[4] + self.tictactoe[7]
		col3 = self.tictactoe[2] + self.tictactoe[5] + self.tictactoe[8]
		dgn1 = self.tictactoe[0] + self.tictactoe[4] + self.tictactoe[8]
		dgn2 = self.tictactoe[2] + self.tictactoe[4] + self.tictactoe[6]
		
		winsum = [row1, row2, row3, col1, col2, col3, dgn1, dgn2]

		if 0 in winsum:
			return 'X wins'
		if 3 in winsum:
			return 'O wins'
		if inf not in winsum:
			return 'Draw'
		return False
		
	def win_display(self):
		if self.win():
			self.ids.win.text = self.win();
		else:
			self.ids.win.text = 'Tic-tac-toe'

class TttApp(App):
	def build(self):
		self.title = 'Tic-Tac-Toe'
		#self.icon = '' logo file
		return TttLayout()

if __name__ == "__main__":
	Config.set('graphics', 'width', '400')
	Config.set('graphics', 'height', '500')
	TttApp().run()
