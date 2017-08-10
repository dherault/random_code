#!/usr/bin/python3.5

# Solves the magic hexagon problem for n = 3 by brute force
# https://en.wikipedia.org/wiki/Magic_hexagon

line_jumps = [3, 4, 5, 4, 3]
lines = [
	[0, 1, 2],
	[3, 4, 5, 6],
	[7, 8, 9, 10, 11],
	[12, 13, 14, 15],
	[16, 17, 18],
	[7, 3, 0],
	[12, 8, 4, 1],
	[16, 13, 9, 5, 2],
	[17, 14, 10, 6],
	[18, 15, 11],
	# [2, 6, 11],
	# [1, 5, 10, 15],
	# [0, 4, 9, 14, 18],
	# [3, 8, 13, 17],
	# [7, 12, 16]
]

def print_board(board):
	c = 0
	s = ''
	for jump in line_jumps:
		for x in board[c:jump + c]:
			s += str(x) + ' '
		s += '\n'
		c += jump
	print(s)

def validate(board):
	for indexes in lines:
		line = [board[i] for i in indexes]
		if 0 not in line and sum(line) != 38:
			return False

	return True

r = range(1, 20)
board = [0] * 19
current_slot = 0
remaining_pieces = { x for x in r }
slot_incorrect_pieces = [ set() for x in r ]

while current_slot < 19:
	incorrect_pieces = slot_incorrect_pieces[current_slot]
	available_pieces = remaining_pieces - incorrect_pieces

	# print(current_slot)
	# print('current_slot:', current_slot)
	# print('available_pieces:', available_pieces)

    # Try available pieces
	if len(available_pieces):
		piece = available_pieces.pop()
		board[current_slot] = piece

		if validate(board):
			current_slot += 1
			remaining_pieces.remove(piece)
		else:
			board[current_slot] = 0
			incorrect_pieces.add(piece)
    # Or backtrack
	else:
		slot_incorrect_pieces[current_slot] = set()
		current_slot -= 1
		previous_piece = board[current_slot]
		board[current_slot] = 0
		slot_incorrect_pieces[current_slot].add(previous_piece)
		remaining_pieces.add(previous_piece)

	# print_board(board)
	# print('incorrect_pieces:', incorrect_pieces)
	# print('remaining_pieces:', remaining_pieces)
	# input()

print('Solution:\n')
print_board(board)
