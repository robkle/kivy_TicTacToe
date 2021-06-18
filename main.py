import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from math import inf
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

Builder.load_file('TttApp.kv')

class TttLayout(BoxLayout):
	count = 1
	tic = NumericProperty(1)
	symbol = StringProperty('')
	score_O = NumericProperty(0)
	score_X = NumericProperty(0)
	tictactoe = ObjectProperty([inf for i in range(9)])

	def click(self, bt):
		if self.tictactoe[bt] == inf and self.win() == False:
			self.symbolCell();
			self.ids[f'bt{bt}'].text = self.symbol
			self.tictactoe[bt] = self.tic; 
			self.selectCell(); 
			self.win_display();
	
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
		win = self.win()
		if win:
			self.ids.win.text = win;
			if win[0] == 'O':
				self.score_O += 1
			elif win[0] == 'X':
				self.score_X += 1
			self.ids.so.text = f'[color=008080]O: {self.score_O}[/color]'
			self.ids.sx.text = f'[color=008080]X: {self.score_X}[/color]'
		else:
			if self.tic == 1:
				self.ids.win.text = 'O to play'
			else:
				self.ids.win.text = 'X to play'
	
	def refresh(self):
		self.tictactoe = [inf for i in range(9)]
		self.count += 1
		if self.count % 2:
			self.tic = 1
			self.ids.win.text = 'O starts'
		else:
			self.tic = 0 
			self.ids.win.text = 'X starts'
		for i in range(9):
			self.ids[f'bt{i}'].text = ''

class TttApp(App):
	def build(self):
		self.title = 'Tic-Tac-Toe'
		#self.icon = '' logo file
		return TttLayout()

if __name__ == "__main__":
	Config.set('graphics', 'width', '400')
	Config.set('graphics', 'height', '500')
	TttApp().run()
