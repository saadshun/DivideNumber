'''
Board

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


'''

def print_board(arr):
	'''
	arr : contains contents of the matrix ; data type: 2d string list
	'''
	dim = len(arr)
	print()

	print(" " + "_______ "*dim)

	for i in range(dim):

		print('|' + '       |'*dim)

		print('|', end='')
		for j in range(dim):
			if arr[i][j]==1:
				arr[i][j] = ''

			num = str(arr[i][j])

			if len(num)==1:
				num = ' '+num+' '

			elif len(num)==2:
				num = ' '+num

			elif len(num)==0:
				num = '   '

			print(f'  {num}  |', end='')
		
		print()
		print('|' + '_______|'*dim)



	print()


# arr = [[1,2,3],[81,'',6],[7,100,'']]
# print_board(arr)