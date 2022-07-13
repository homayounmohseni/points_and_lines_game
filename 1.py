class Player:
	uid = 0
	def __init__(self):
		uid += 1
		self.uid = uid - 1
		self.wins_cnt = 0
	def increment_wins(self):
		self.wins_cnt += 1

#TODO make classes of Square and Line and store instances of them in field instead of simple refrences to playes
#TODO extent Player class, let Player have a refrence to field so it could independently play his or her turn
#TODO count_square_sides
class Square:
	pass

class Field:
	def __init__(self, rows, cols, players_cnt):
		self.rows = rows
		self.cols = cols
		self.lines_hor = [[None] * cols] * (rows + 1)
		self.lines_ver = [[None] * (cols + 1)] * rows
		self.squares = [[None] * cols] * rows
		self.players_cnt = players_cnt

	def fill(self, hor_ver_bar, row, col, player):
		if (hor_ver_bar):
			if lines_hor[row][col]:
				return False
			lines_hor[row][col] = player
		else:
			if lines_ver[row][col]:
				return False
			lines_ver[row][col] = player

		eval_new_squares(hor_ver_bar, row, col, player)
		return True
	
	def finished(self):
		for i in range(rows):
			for j in range(cols):
				if (squares[i][j] is None):
					return False
		return True
	
	def eval_new_squares(self, hor_ver_bar, row, col, player):
		if (hor_ver_bar):
			if row > 0:
				if count_square_sides((row - 1, col)) == 3:
					square[row - 1][col] = player
			if row < rows:
				if count_square_sides((row, col)) == 3:
					square[row][col] = player
		else:
			if col > 0:
				if count_square_sides((row, col - 1)) == 3:
					square[row][col - 1] = player
			if col < cols:
				if count_square_sides((row, col)) == 3:
					square[row][col] = player
	
	def evalue_winner(self):
		squares_cnt = [0] * players_cnt
		for i in range(rows):
			for j in range(cols):
				squares_cnt[int(squares[i][j].uid)] += 1
		max_squares = -1		
		winner_index = -1
		for i in range(players_cnt):
			if squares_cnt[i] > max_squares:
				max_squares = squares_cnt[i]
				argmax = i
		return winner_index
	def count_square_sides(self, top_right):
		cnt = 0
		if not (lines_hor[top_right[0]][top_right[1]] is None):
			cnt += 1
		if not (lines_hor[top_right[0] + 1][top_right[1]] is None):
			cnt += 1
		if not (lines_ver[top_right[0]][top_right[1]] is None):
			cnt += 1
		if not (lines_ver[top_right[0]][tor_right[1] + 1] is None):
			cnt += 1
		return cnt



n = int(input()) #players count
m, k = [int(x) for x in input().split()] #rows and columns
players = [Player(x) for x in range(n)]
while True:
	field = Field(n, m)
	turn = 0
	while not field.finished():
		player = players[turn]
		hor_ver_bar, row, col = input("player " + player.uit + "'s turn:").split()
		hor_ver_bar = hor_ver_bar == "True"
		row = int(row)
		col = int(col)

		#get input row col:
		if field.fill(hor_ver_bar, row, col, player):
			turn += 1
			turn %= n
		else:
			print("already filled")

	winner_index = field.evaluate_winner()
	palyers[winner_index].increment_wins()