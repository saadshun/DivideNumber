from board import print_board
'''
Board with Options

 _______ _______ _______ 
|       |       |       |
|  100  |   2   |   2   |
|_______|_______|_______|
|       |       |       |
|  100  |   2   |   2   |
|_______|_______|_______|
|       |       |       |
|  100  |   81  |   2   |
|_______|_______|_______|


         OPTIONS

(1) 100    (2) 81     (3) 2

Enter Choice: 1

Enter Row: 2
Enter Col: 3

'''


def print_options(options):
	print('')
	print('         OPTIONS\n')

	i = 1

	for opt in options:
		opt = str(opt)

		if len(opt)==1:
			opt = opt+'  '

		elif len(opt)==2:
			opt = opt+' '

		print(f'({i}) '+str(opt)+'   ',end='')
		i += 1




# options = [12,2,100]
# print_options(options)


def get_response_and_position(arr):

	print()
	choice = ''

	dim = len(arr)

	rc = [str(i+1) for i in range(dim)]

	while choice not in ['1' ,'2' ,'3']:
		choice = input('Enter Choice: ').strip()

		if choice not in ['1', '2', '3']:
			print('Enter a valid option!')

	print()

	while True:
		row = ''
		while row not in rc:
			row = input('Enter Row: ').strip()

			if row not in rc:
				print('Enter a valid row!')	

		col = ''
		while col not in rc:
			col = input('Enter Col: ').strip()

			if col not in rc:
				print('Enter a valid col!')	

		if arr[int(row)-1][int(col)-1]=='':
			break

		else:
			print('Cell is not empty!\n')
			row = ''
			col = ''


	return choice, row, col



# get_response_and_position([[1,2,3],[4,' ', 6],[' ',2,22]])

