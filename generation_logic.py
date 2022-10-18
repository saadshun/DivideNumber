import random


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,93,97]


def get_num_factors():
	p = random.randint(1, 4)
	return p

def get_primes(n_factors, nums):
	pfs = []

	for i in range(n_factors):
		idx = 100
		while idx >= len(primes):
			p = random.uniform (0, 1)
			idx = int(1/p)-1
		
		pfs.append(primes[idx])

	return pfs

def get_random_number(nums):
	while 1:	
		n = get_num_factors()
		ps = get_primes(n, nums)
		# print(ps)

		num = 1

		for i in ps:
			num *= i

		# print(num)

		if num<=100:
			return num