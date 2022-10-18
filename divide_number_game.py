import os
import sys
import numpy as np
from options import print_options, get_response_and_position 
from board import print_board
from generation_logic import get_random_number


def form_matrix(dim):
	arr = []
	for i in range(dim):
		tmp = []

		for j in range(dim):
			tmp.append('')

		arr.append(tmp)

	return arr


def inside(x,y,dim):
	return x>=0 and y>=0 and x<dim and y<dim


def reduce(arr):
	score = 0
	dim = len(arr)
	pos = dict()

	for i in range(dim):
		for j in range(dim):
			if arr[i][j]!='':
				if arr[i][j] in pos.keys():
					pos[arr[i][j]].append((i,j))
				else:
					pos[arr[i][j]] = [(i,j)]

	sorted_keys = sorted(pos.keys())

	prev_score = -1

	while score != prev_score:

		prev_score = score

		for k in sorted_keys:
			check = 0
			dx = [1,0,-1,0]
			dy = [0,1,0,-1]

			for p in pos[k]:
				i,j = p
				# check = 0

				for w in range(4):
					x = i+dx[w]
					y = j+dy[w]

					if inside(x,y,dim) and isinstance(arr[x][y], int) and arr[x][y]%arr[i][j]==0:
						score += arr[x][y]//arr[i][j]
						arr[x][y] = arr[x][y]//arr[i][j]
						check = 1

				if check:
					arr[i][j] = ''
					break

			if check:
				break

		pos.clear()

		for i in range(dim):
			for j in range(dim):
				if arr[i][j]!='':
					if arr[i][j] in pos.keys():
						pos[arr[i][j]].append((i,j))
					else:
						pos[arr[i][j]] = [(i,j)]

		sorted_keys.clear()
		sorted_keys = sorted(pos.keys())

	return score


def game(dim):

	arr = form_matrix(dim)

	score = 0

	while True:
		nums = []
		cnt = 0
		for l in arr:
			nums += l
			if '' not in l:
				cnt += 1
		
		if cnt == dim:
			os.system('cls')
			print_board(arr)
			print('Score:', score)
			print('\nGAME OVER!\n')
			break

		
		def_row = np.random.randint(0,dim)
		def_col = np.random.randint(0,dim)

		while arr[def_row][def_col] != '':
			def_row = np.random.randint(0,dim)
			def_col = np.random.randint(0,dim)


		def_val = 0
		ok = 0
		while not ok:
			def_val = get_random_number(nums)
			# print('ok')
			ok = 1
			for num in nums:
				if isinstance(num,int) and (num%def_val==0 or def_val%num==0):
					ok = 0
					break
		
		arr[def_row][def_col] = def_val

		reduce(arr)

		cnt = 0
		for l in arr:
			if '' not in l:
				cnt += 1
		
		if cnt == dim:
			os.system('cls')
			print_board(arr)
			print('Score:', score)
			print('\nGAME OVER!\n')
			break

		print_board(arr)

		opt1 = get_random_number(nums)
		opt2 = get_random_number(nums)
		while opt2 == opt1:
			opt2 = get_random_number(nums)

		opt3 = get_random_number(nums)
		while opt3 == opt1 or opt2 == opt3:
			opt3 = get_random_number(nums)


		options = [opt1, opt2, opt3]

		print_options(options)

		print('\n')
		print('Score:', score)

		choice, row, col = get_response_and_position(arr)

		arr[int(row)-1][int(col)-1] = options[int(choice)-1]

		score += reduce(arr)

		os.system('cls')


game(int(sys.argv[1]))