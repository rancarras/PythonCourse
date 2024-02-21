class Fish:
	def __init__(self):
		# Some fishies
		self.members = ['Goldfish', 'Tuna', 'Sardine']

	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print('\t%s ' % member)